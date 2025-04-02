# app/vector_store.py
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.schema import Document
import os

persist_dir = "./chroma_db"
embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# 벡터 저장소 생성
db = Chroma(
    persist_directory=persist_dir,
    embedding_function=embedding
)

def add_memory(user_id: int, memory_text: str):
    doc = Document(page_content=memory_text, metadata={"user_id": user_id})
    db.add_documents([doc])
    db.persist()

def search_similar_memory(user_input: str, user_id: int, top_k: int = 1):
    # 같은 유저의 기억 중에서만 검색
    results = db.similarity_search_with_score(user_input, k=top_k)
    # user_id 필터링
    user_results = [r for r in results if r[0].metadata.get("user_id") == user_id]
    return user_results[0][0].page_content if user_results else ""
