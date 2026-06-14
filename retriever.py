import numpy as np

from embedding import create_embedding
from vector_db import search


def retrieve(query):

    q=create_embedding(
        query
    )

    q=np.array(
        [q]
    )

    return search(q)