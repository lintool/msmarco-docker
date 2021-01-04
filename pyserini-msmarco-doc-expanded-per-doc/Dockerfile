FROM python:3.6-slim

# Install Java first, to better take advantage of layer caching.
#
# Note (1): first mkdir line fixes the following error:
#   E: Sub-process /usr/bin/dpkg returned an error code (1)
# https://stackoverflow.com/questions/58160597/docker-fails-with-sub-process-usr-bin-dpkg-returned-an-error-code-1
#
# Note (2): pyjnius appears to need JDK, JRE doesn't suffice.
#
RUN mkdir -p /usr/share/man/man1 && \
    apt update && \
    apt install -y bash \
                   build-essential \
                   curl \
                   ca-certificates \
	           openjdk-11-jdk-headless && \
    rm -rf /var/lib/apt/lists


RUN pip install pyserini==0.10.0.1 fastapi uvicorn

RUN python -c "from pyserini.search import SimpleSearcher; SimpleSearcher.from_prebuilt_index('msmarco-doc-expanded-per-doc')"

WORKDIR /home
COPY main.py /home/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
