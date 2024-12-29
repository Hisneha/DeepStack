
# Character Information Retrieval System

This project provides a two-command CLI system for extracting and managing character information from text stories. The system leverages embeddings to store, query, and retrieve structured information about characters.

## Overview

### CLI Commands

1. **`compute-embeddings`**
   - **Description**: Processes all story files, computes embeddings for them, and stores these embeddings in a vector database.
   - **Input**: Story files (text format).
   - **Output**: Persisted embeddings in a vector database.

2. **`get-character-info`**
   - **Description**: Retrieves structured information about a specified character by querying the vector database.
   - **Input**: Character name.
   - **Output**: JSON object containing the following keys:
     - `name`: Name of the character.
     - `storyTitle`: Title of the character’s story.
     - `summary`: Brief summary of the character’s story.
     - `relations`: Relationships with other characters in the story.
     - `characterType`: The character’s role (e.g., protagonist, antagonist, side character).

## Features
- **Embedding Management**: Computes and stores story embeddings.
- **Character Search**: Allows retrieval of structured character information.
- **Vector Database Integration**: Supports local open-source vector databases (e.g., FAISS).

---

## Installation and Setup

### Prerequisites
- Python 3.8+
- Required Python packages (see `requirements.txt`)
- A local installation of FAISS or another vector database.

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a directory for story files:
   ```bash
   mkdir data
   ```
   Place your story files (in `.txt` format) in the `data` directory.

4. Ensure that the vector database (e.g., FAISS) is installed and configured.

---

## Usage

### Command 1: `compute-embeddings`

#### Description:
This command processes all story files in the `data` directory, computes embeddings, and stores them in a vector database.

#### Run the command:
```bash
python compute_embeddings.py
```

#### Expected Output:
- Embeddings will be stored in the vector database for subsequent queries.

---

### Command 2: `get-character-info`

#### Description:
This command retrieves structured details about a specified character by querying the vector database.

#### Run the command:
```bash
python get_character_info.py --character "<character_name>"
```

#### Example Output:
```json
{
  "name": "Jon Snow",
  "storyTitle": "A Song of Ice and Fire",
  "summary": "Jon Snow is a brave and honorable leader who serves as the Lord Commander of the Night's Watch and later unites the Free Folk and Westeros against the threat of the White Walkers.",
  "relations": [
    { "name": "Arya Stark", "relation": "Sister" },
    { "name": "Eddard Stark", "relation": "Father" }
  ],
  "characterType": "Protagonist"
}
```

---

## Project Structure

```plaintext
project/
├── data/                   # Directory for story text files
├── compute_embeddings.py   # Script to compute and store embeddings
├── get_character_info.py   # Script to query character information
├── requirements.txt        # Dependencies for the project
├── metadata.json           # (Optional) Metadata for stories (if exists)
└── README.md               # Project documentation
```

---

## Additional Notes
- **Error Handling**: Ensure that your story files are correctly formatted to avoid processing errors.
- **Database Management**: If running `compute-embeddings` multiple times, check for duplicates or conflicts in the database.

---

## Future Improvements
- Support for multiple vector database backends.
- Enhancements to story summarization and character relation extraction.
- Integration with a web interface for easier querying.

---

## License
This project is licensed under the MIT License.

---

## Contact
For questions or issues, please contact [Snehal Suryawanshi](mailto:snehal.suryawanshi21@vit.edu).
