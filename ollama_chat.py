# ------------ Imports ------------ #
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_community.document_loaders import PyPDFLoader
import os

# ------------ PDF Loading ------------ #
pdf_path = "data/Parameter-Efficient Transfer Learning for NLP.pdf"
loader = PyPDFLoader("Parameter-Efficient Transfer Learning for NLP.pdf")
documents = loader.load()

print("✅ PDF loaded successfully!")

# ------------ Splitting the Document into Chunks ------------ #
text_splitter = RecursiveCharacterTextSplitter(chunk_size=7500, chunk_overlap=100)
chunks = text_splitter.split_documents(documents)

print(f"✅ Document split into {len(chunks)} chunks.")

# ------------ Creating the Vector Database ------------ #
vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=OllamaEmbeddings(model="nomic-embed-text", show_progress=True),
    collection_name="local_rag",
    persist_directory="db"  # Save the vector database locally
)

print("✅ Vector database created and populated with document chunks.")

# ------------ Multi-Query Retriever ------------ #
# LLM model from Ollama
local_model = "llama3.2"
llm = ChatOllama(model=local_model)

# Custom prompt for generating diverse queries
QUERY_PROMPT = PromptTemplate(
    input_variables=["question"],
    template="""You are an AI assistant. Generate five different versions of the following user question to retrieve relevant documents from a vector database:
    Original question: {question}"""
)

# Initialize retriever
retriever = MultiQueryRetriever.from_llm(
    vector_db.as_retriever(),
    llm,
    prompt=QUERY_PROMPT
)

print("✅ Retriever set up.")

# ------------ Retrieval-Augmented Generation (RAG) Chain ------------ #
# Define RAG prompt
rag_template = """Answer the question based ONLY on the following context:
{context}
Question: {question}
"""

# Set up the RAG pipeline
prompt = ChatPromptTemplate.from_template(rag_template)

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# ------------ Running the Retrieval Chain ------------ #
# User input for a question
user_question = input("❓ Ask a question: ")

# Generate the answer
response = chain.invoke(user_question)
print("\n📝 **Answer:**\n", response)

# ------------ Cleanup ------------ #
# Delete the vector database after use (optional)
# vector_db.delete_collection()
# print("🗑️ Vector database collection deleted.")