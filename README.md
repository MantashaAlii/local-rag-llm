# 📄 Local RAG System with Ollama, Python, and LangChain

## 🚀 Project Overview

This project demonstrates how to build a **Local Retrieval-Augmented Generation (RAG) System** using **Ollama**, **Python**, and **LangChain**. The system allows querying sensitive PDF documents without internet access, ensuring data privacy and security.

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Large Language Model (LLM):** Ollama (`llama3.2` model)
- **Framework:** LangChain
- **Vector Database:** ChromaDB
- **Embedding Model:** Nomic Embed Text

---

## 🌐 Project Workflow

1. **PDF Loading:** Load local PDF files using `PyPDFLoader`.
2. **Text Chunking:** Split text into smaller, manageable chunks.
3. **Embedding Generation:** Convert text chunks into vector embeddings.
4. **Vector Storage:** Store embeddings in **ChromaDB**.
5. **Querying:** Accept user input as a query.
6. **Multi-Query Retrieval:** Generate multiple variations of the question for optimized search.
7. **Response Generation:** Use the Ollama model to generate accurate answers.

---

## ⚙️ Installation

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/local-rag-system.git
cd local-rag-system
```

2. **Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Install Ollama and ChromaDB**

```bash
pip install langchain chromadb ollama unstructured
```

---

## 🏃‍♂️ Running the Project

### 1. **Start Ollama Server**

Run the Ollama model server on a specific port (e.g., 8000):

```bash
ollama serve --port 8000
```

### 2. **Prepare the PDF Files**

Place your PDF files in the `data/` folder.

### 3. **Run the Python Script**

In a new terminal, navigate to the project directory and run the script:

```bash
python src/main.py
```

### 4. **Query the System**

When prompted, enter your question to query the PDF. Example:

```bash
What is this document about?
```

---

## ✨ Features

- **Offline Processing:** Fully functional without internet.
- **Enhanced Privacy:** Keeps sensitive data secure.
- **Efficient Search:** Multi-query retrieval for optimized results.
- **Customizable:** Easily swap models and databases.

---

## 🔮 Future Enhancements

- 🌐 **Streamlit UI:** Add a user-friendly web interface.
- 🤖 **Model Expansion:** Integrate more advanced local models.
- 📊 **Analytics:** Track and visualize query performance.

---

## 🤝 Contributing

1. **Fork** the repository.
2. **Clone** your forked repo.
3. Create a new **branch**: `git checkout -b feature-name`
4. **Commit** your changes: `git commit -m 'Add feature'`
5. **Push** to the branch: `git push origin feature-name`
6. Open a **Pull Request**.

---

## 📝 License

This project is licensed under the MIT License. Feel free to use and modify it.

---

Thank you for checking out this project! ⭐ Feel free to contribute or provide feedback!
