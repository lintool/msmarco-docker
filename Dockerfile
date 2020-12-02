FROM openkbs/jdk11-mvn-py3

RUN pip install pyserini==0.10.0.1 fastapi uvicorn

RUN python3 -c "from pyserini.search import SimpleSearcher; SimpleSearcher.from_prebuilt_index('msmarco-doc-slim')"

COPY main.py /home/developer/

CMD [".local/bin/uvicorn", "main:app", "--host", "0.0.0.0"]
