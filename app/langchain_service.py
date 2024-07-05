from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from app.config import OPENAI_API_KEY

# 初始化檔案加載器，嵌入和向量儲存
loader = DirectoryLoader("documents")
documents = loader.load()
embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
vector_store = FAISS.from_documents(documents, embeddings)
retrieval_chain = ConversationalRetrievalChain(vector_store)

def get_answer(query: str, history: list = []):
    return retrieval_chain.run(query=query, chat_history=history)
