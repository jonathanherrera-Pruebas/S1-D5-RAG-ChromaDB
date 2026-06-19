# Sistema RAG con ChromaDB

## Descripción

Este proyecto implementa un sistema RAG (Retrieval-Augmented Generation) utilizando LangChain y ChromaDB. El sistema carga documentos de texto, genera embeddings y permite responder preguntas recuperando la información más relevante.

## Tecnologías utilizadas

- Python 3.11
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Sentence Transformers

## Estructura del proyecto

```
S1-D5-RAG-ChromaDB
│
├── documentos
│   ├── documento1.txt
│   ├── documento2.txt
│   └── documento3.txt
│
├── chroma_db
├── venv
├── rag.py
└── README.md
```

## Instalación

Instalar las dependencias:

```bash
pip install langchain
pip install langchain-community
pip install langchain-huggingface
pip install chromadb
pip install sentence-transformers
```

## Ejecución

Ejecutar:

```bash
python rag.py
```

## Ejemplos de preguntas

### ¿Qué es ChromaDB?

Respuesta:

```
ChromaDB es una base de datos vectorial utilizada en sistemas RAG.
```

### ¿Quién creó Python?

Respuesta:

```
Python es un lenguaje de programación creado por Guido van Rossum.
```

### ¿Qué es MongoDB?

Respuesta:

```
MongoDB es una base de datos NoSQL orientada a documentos.
```

## Funcionamiento

1. Se cargan los documentos de texto.
2. Se generan embeddings utilizando HuggingFace.
3. Los embeddings se almacenan en ChromaDB.
4. El usuario realiza una pregunta.
5. El Retriever recupera el documento más relevante.
6. Se muestra la respuesta encontrada.

## Autor

Jonathan David Herrera García