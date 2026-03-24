
from langchain_community.document_loaders import PyPDFDirectoryLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


# The PyPDFDirectoryLoader is a specific tool within the Langchain framework that allows you to load PDF documents from a specified directory.

# Step-1: Data Preparation
DATA_PATH = "data"

def load_documents():
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    return document_loader.load()

documents = load_documents()


# Step-2: Splitting the data
def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, 
                                                   chunk_overlap=80,
                                                   length_function=len,
                                                   is_separator_regex=False)
    return text_splitter.split_documents(documents)

chunks = split_documents(documents)

print(f"Total chunks: {len(chunks)}")   # How many total  chunks
             