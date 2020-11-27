import sys

sys.path.insert(0, '../pyserini/')

from fastapi import FastAPI
from pyserini.search import SimpleSearcher
from typing import Optional


searcher = SimpleSearcher.from_prebuilt_index('ms-marco-doc')
app = FastAPI()


@app.get("/search/")
def search(q: str, k: Optional[int] = 1000):
    hits = searcher.search(q, k=k)

    results = []
    # Print the first 10 hits:
    for i in range(0, len(hits)):
        #print(f'{i + 1:2} {hits[i].docid:15} {hits[i].score:.5f}')
        results.append({'docid': hits[i].docid, 'score': hits[i].score})

    return {'results': results}
