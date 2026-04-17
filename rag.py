from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_info_rag(college_name, text):
    if not text:
        return {}

    chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    embeddings = model.encode(chunks)
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    query = f"{college_name} NAAC NBA NIRF ranking year founded type autonomous university"
    q_emb = model.encode([query])

    _, I = index.search(np.array(q_emb), k=3)

    context = " ".join([chunks[i] for i in I[0]])

    # Simple rule-based extraction (replace with LLM if needed)
    return {
        "location": extract_field(context, ["located", "location"]),
        "naac": extract_field(context, ["NAAC"]),
        "nba": extract_field(context, ["NBA"]),
        "nirf": extract_field(context, ["NIRF"]),
        "year": extract_field(context, ["founded", "established"]),
        "type": extract_field(context, ["private", "government"]),
        "category": extract_field(context, ["autonomous", "university", "VTU"])
    }


def extract_field(text, keywords):
    for line in text.split("."):
        for k in keywords:
            if k.lower() in line.lower():
                return line.strip()
    return "NA"
