try:
    from langchain_community.vectorstores import FAISS
    print("Successfully imported FAISS from langchain_community")
    from langchain.embeddings.openai import OpenAIEmbeddings
    print("Successfully imported OpenAIEmbeddings")
except ImportError as e:
    print(f"Import error: {e}")