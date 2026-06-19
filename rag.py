from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# ==========================================
# Cargar documentos
# ==========================================
loader = DirectoryLoader(
    "documentos/",
    glob="*.txt",
    loader_cls=lambda path: TextLoader(path, encoding="utf-8")
)

documents = loader.load()

# ==========================================
# Crear embeddings
# ==========================================
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ==========================================
# Crear base vectorial ChromaDB
# ==========================================
db = Chroma.from_documents(
    documents,
    embeddings,
    persist_directory="./chroma_db"
)

# ==========================================
# Crear retriever
# ==========================================
retriever = db.as_retriever(
    search_kwargs={"k": 1}
)

print("\n===== SISTEMA RAG CON CHROMADB =====")

while True:

    query = input("\nHaz una pregunta (o escribe salir): ")

    if query.lower() == "salir":
        print("\nHasta luego.")
        break

    docs = retriever.invoke(query)

    print("\n==============================")
    print("Pregunta:")
    print(query)

    print("\nRespuesta encontrada:\n")

    for doc in docs:
        print(doc.page_content)

    print("\n==============================")