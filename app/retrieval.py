import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("vectorstore/shl.index")

with open("data/shl_catalog.json", "r") as f:
    catalog = json.load(f)

def search_assessments(query, top_k=5):

    embedding = model.encode([query])

    distances, indices = index.search(
        np.array(embedding),
        top_k
    )

    results = []

    for idx in indices[0]:

        results.append(catalog[idx])

    return results