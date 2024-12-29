import json
import time
import faiss
import numpy as np
from mistralai import Mistral

# Set up the MistralAI client
api_key = "a7lzyH2Q2BtPGWzIGu71rk2GzrSaV8RB"  # Replace with your actual API key
client = Mistral(api_key=api_key)

# Predefined list of story file paths
STORY_FILES = [
    "C:/Users/Snehal Suryawanshi/OneDrive/Documents/my_project/langchain_character_extraction/data/a-mother.txt",
    "C:/Users/Snehal Suryawanshi/OneDrive/Documents/my_project/langchain_character_extraction/data/sorrow.txt",
    "C:/Users/Snehal Suryawanshi/OneDrive/Documents/my_project/langchain_character_extraction/data/the-lantern-keepers.txt",
    "C:/Users/Snehal Suryawanshi/OneDrive/Documents/my_project/langchain_character_extraction/data/the-poor-relations-story.txt",
    "C:/Users/Snehal Suryawanshi/OneDrive/Documents/my_project/langchain_character_extraction/data/the-schoolmistress.txt"
]



def read_story(file_path):
    """Reads and returns the content of a story file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def create_faiss_index(embedding_dimension):
    """Creates a FAISS index for storing embeddings."""
    return faiss.IndexFlatL2(embedding_dimension)

def get_embeddings(text):
    """Generates embeddings for the given text."""
    response = client.embeddings.create(model="mistral-embed", inputs=[text])
    embedding_data = response.data[0].embedding
    return np.array(embedding_data, dtype=np.float32)

def generate_story_embeddings(story_files):
    """Generates embeddings for all stories and creates a FAISS index."""
    embeddings_list = []
    story_titles = []

    sample_text = read_story(story_files[0])
    first_embedding = get_embeddings(sample_text)
    embedding_dimension = first_embedding.shape[0]

    index = create_faiss_index(embedding_dimension)
    time.sleep(10)  # Adjust for API rate limits

    for file_path in story_files:
        story_text = read_story(file_path)
        embedding_data = get_embeddings(story_text)
        embeddings_list.append(embedding_data)
        story_titles.append(file_path)
        time.sleep(10)  # Adjust for API rate limits

    embeddings_array = np.array(embeddings_list, dtype=np.float32)
    index.add(embeddings_array)

    return {"index": index, "story_titles": story_titles}

def query_faiss_index(query_text, embeddings_dict, k=3):
    """Queries the FAISS index for the top-k matches."""
    query_embedding = get_embeddings(query_text)
    index = embeddings_dict["index"]
    D, I = index.search(np.array([query_embedding], dtype=np.float32), k)
    results = [embeddings_dict["story_titles"][idx] for idx in I[0]]
    return results

def load_story_metadata(file_path):
    """Loads story metadata from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_character_info(metadata, query_name):
    """Retrieves character information from the metadata."""
    for story in metadata["stories"]:
        for character in story["characters"]:
            if character["name"].lower() == query_name.lower():
                return {
                    "name": character["name"],
                    "storyTitle": story["storyTitle"],
                    "summary": character["summary"],
                    "relations": character["relations"],
                    "characterType": character["characterType"]
                }
    return None

def query_with_metadata(query_text, embeddings_dict, metadata_file, k=3):
    """Queries the FAISS index and fetches enriched character details."""
    matching_stories = query_faiss_index(query_text, embeddings_dict, k)
    metadata = load_story_metadata(metadata_file)

    character_info = get_character_info(metadata, query_text)
    if character_info:
        return character_info
    else:
        return {"error": f"No metadata found for '{query_text}'"}

# Main Execution
if __name__ == "__main__":
    # Generate FAISS index with story embeddings
    story_embeddings = generate_story_embeddings(STORY_FILES)

    # Path to the metadata file
    metadata_file_path = "metadata.json"

    # Query input
    query_character = "Jon Snow"
    enriched_info = query_with_metadata(query_character, story_embeddings, metadata_file_path)

    # Output the result
    print(json.dumps(enriched_info, indent=4))
