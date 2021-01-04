import sys

# Only for debugging purposes, using a Pyserini local installation.
# sys.path.insert(0, '../pyserini/')

from fastapi import FastAPI
from pyserini.search import SimpleSearcher
from typing import Optional


searcher = SimpleSearcher.from_prebuilt_index('msmarco-doc-slim')
app = FastAPI()


@app.get("/search/")
def search(q: str, k: Optional[int] = 1000):
    hits = searcher.search(q, k=k)

    results = []
    for i in range(0, len(hits)):
        results.append({'docid': hits[i].docid, 'score': hits[i].score})

    return {'results': results}
