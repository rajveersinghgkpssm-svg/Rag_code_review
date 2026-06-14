import faiss
import numpy as np


index=None
chunks=[]


def build_vector_db(
embeddings,
texts
):

    global index
    global chunks

    chunks=texts

    dim=len(embeddings[0])

    index=faiss.IndexFlatL2(
        dim
    )

    index.add(
        np.array(
            embeddings
        )
    )


def search(
query_vector
):

    D,I=index.search(
        query_vector,
        5
    )

    return [
        chunks[i]
        for i
        in I[0]
    ]
