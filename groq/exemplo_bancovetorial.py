import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(name="expansao_zapflow")

collection.upsert(
    documents=[
        "A Zapflow vai abrir escritorio no Brasil.",
        "A Zapflow vai abrir escritorio no França.",
        "A Zapflow vai abrir escritorio no Japão.",
        "A Zapflow vai abrir escritorio no Alemanha.",
        "A Zapflow vai abrir escritorio no Canadá.",
        "A Zapflow vai abrir escritorio no Austrália.",
        "A Zapflow vai abrir escritorio no Italia.",
        "A Zapflow vai abrir escritorio no Argentina.",
        "A Zapflow vai abrir escritorio no Espanha.",
        "A Zapflow vai abrir escritorio no Russia.",
    ],
    ids=["país1", "país2", "país3", "país4", "país5", "país6", "país7", "país8", "país9", "país10",]
)

resultado = collection.query(
    query_texts=["O Zapflow vai ter escritório no Rio de Janeiro?"],
    n_results=3
)

print(resultado)