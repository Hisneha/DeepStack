import json
import os

# Define your story files
story_files = [
    "C:/Users/Snehal Suryawanshi/OneDrive/Documents/my_project/langchain_character_extraction/data/a-mother.txt",
    "C:/Users/Snehal Suryawanshi/OneDrive/Documents/my_project/langchain_character_extraction/data/sorrow.txt",
    "C:/Users/Snehal Suryawanshi/OneDrive/Documents/my_project/langchain_character_extraction/data/the-lantern-keepers.txt",
    "C:/Users/Snehal Suryawanshi/OneDrive/Documents/my_project/langchain_character_extraction/data/the-poor-relations-story.txt",
    "C:/Users/Snehal Suryawanshi/OneDrive/Documents/my_project/langchain_character_extraction/data/the-schoolmistress.txt"
]

# Create a function to read the text of a story
def read_story(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Generate metadata for each story
def generate_metadata(story_files):
    metadata = []
    for file_path in story_files:
        story_text = read_story(file_path)
        
        # Extract metadata (You can expand the metadata extraction logic as needed)
        story_metadata = {
            "storyTitle": os.path.basename(file_path).replace(".txt", ""),
            "summary": "A brief summary of the story.",  # Placeholder for story summary
            "relations": [],  # Placeholder for character relationships
            "characterType": "Protagonist"  # Placeholder for character type (example: Protagonist)
        }

        # Add metadata for this story to the list
        metadata.append(story_metadata)
        print("added metadat")

    return metadata

# Function to update the metadata.json file
def update_metadata(metadata):
    # Check if metadata.json exists
    if os.path.exists("metadata.json"):
        # Load the existing metadata
        with open("metadata.json", "r", encoding="utf-8") as file:
            try:
                existing_metadata = json.load(file)
                
                # Ensure the existing data is a list
                if not isinstance(existing_metadata, list):
                    existing_metadata = []
            except json.JSONDecodeError:
                # In case the file is empty or corrupted, initialize an empty list
                existing_metadata = []

        # Merge new metadata without duplicates
        for new_data in metadata:
            # Check if storyTitle already exists in existing metadata
            if not any(item["storyTitle"] == new_data["storyTitle"] for item in existing_metadata):
                existing_metadata.append(new_data)
                print("appended new data")
        
        # Write updated metadata back to the file
        with open("metadata.json", "w", encoding="utf-8") as file:
            json.dump(existing_metadata, file, indent=4)
    else:
        # If the file doesn't exist, create it and write the metadata
        with open("metadata.json", "w", encoding="utf-8") as file:
            json.dump(metadata, file, indent=4)

# Main function to generate and update metadata
def main():
    metadata = generate_metadata(story_files)
    update_metadata(metadata)
    print(metadata)
    print("File updated succesfully")

# Run the script
if __name__ == "__main__":
    main()
