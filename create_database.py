from embeddings import get_embedding_function
from langchain_chroma import Chroma
from langchain_core.documents import Document
from main import chunks

CHROMA_PATH = "chroma"

def add_to_chroma(chunks: list[Document]):
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=get_embedding_function())
    
    # Stable unique IDs using source file + page + index
    chunk_ids = [
        f"{chunk.metadata.get('source', 'doc')}:{chunk.metadata.get('page', 0)}:{i}"
        for i, chunk in enumerate(chunks)
    ]

    existing_ids = set(db.get()["ids"])
    new_chunks = [(chunk, cid) for chunk, cid in zip(chunks, chunk_ids) if cid not in existing_ids]

    if new_chunks:
        new_docs, new_ids = zip(*new_chunks)
        db.add_documents(list(new_docs), ids=list(new_ids))
        print(f"Added {len(new_ids)} new chunks to Chroma!")
    else:
        print("No new chunks. DB is already up to date.")

if __name__ == "__main__":
    add_to_chroma(chunks)
    