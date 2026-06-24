from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# ======================================
# Cargar documentos
# ======================================
loader = DirectoryLoader(
    "S2-D2-BusquedaSemantica/documentos/",
    glob="*.txt",
    loader_cls=lambda path: TextLoader(path, encoding="utf-8")
)

documents = loader.load()

# ======================================
# Crear embeddings
# ======================================
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ======================================
# Crear base vectorial
# ======================================
db = Chroma.from_documents(
    documents,
    embeddings,
    persist_directory="S2-D2-BusquedaSemantica/chroma_db"
)

# ======================================
# Demo de búsqueda semántica
# ======================================
print("\n===== DEMO DE BÚSQUEDA SEMÁNTICA =====")

while True:

    pregunta = input("\nHaz una pregunta (o escribe salir): ")

    if pregunta.lower() == "salir":
        print("\nHasta luego.")
        break

    resultados = db.similarity_search(
        pregunta,
        k=1
    )

    print("\nDocumento más similar:\n")

    for doc in resultados:
        print(doc.page_content)