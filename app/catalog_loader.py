import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/shl_catalog.json", "r") as f:
    data = json.load(f)

texts = []

for item in data:

    text = item["name"]

    texts.append(text)

embeddings = model.encode(texts)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

faiss.write_index(index, "vectorstore/shl.index")

print("Vector database created successfully")