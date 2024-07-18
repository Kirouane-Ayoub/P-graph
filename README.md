# Custom Property Graph Retriever with Advanced Reranking

This repository showcases a custom **property graph retriever** tailored for detailed retrieval tasks using techniques like vector search and text-to-Cypher queries. It integrates the `Meta-Llama-3-8B` language model and `BAAI/bge-small-en-v1.5` embeddings for enhanced performance. Additionally, it features the **CohereRerank** module for post-processing retrieval results.

## Features
- **Custom Retrieval:** Combines vector context retrieval and text-to-Cypher queries.
- **Advanced Reranking:** Enhances results using CohereRerank for improved relevance.
- **Friendly UI:** Built using the Mesop framework for a user-friendly experience.

## Usage

### Installation
1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Data Setup
2. Move your data source files (PDFs, TXT, MD, etc.) into the `data` folder.

### Configuration
3. Edit `settings.py` to include:
   - `NEO4J_URL`: URL for your Neo4j database.
   - `NEO4J_USERNAME`: Username for Neo4j authentication.
   - `NEO4J_PASSWORD`: Password for Neo4j authentication.
   - `COHERE_API_KEY`: API key for CohereRerank integration.

### Customization
4. Customize `retriever.py` to implement advanced features or modify retrieval logic as needed.

### Running the UI
5. Start the UI application:
   ```bash
   python app.py
   ```
