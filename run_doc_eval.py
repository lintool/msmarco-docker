import argparse
import requests

from tqdm import tqdm

query_file = 'msmarco-docdev-queries.tsv'

parser = argparse.ArgumentParser(description='Generates a run.')
parser.add_argument('--output', required=True, type=str, help='Output run file.')
parser.add_argument('--k', required=True, type=int, help='Number of hits.')

args = parser.parse_args()

queries = []
with open(query_file, 'r') as f:
    for line in f:
        qid, query = line.rstrip().split('\t')
        queries.append([qid, query])

with open(args.output, 'w') as out:
    for entry in tqdm(queries):
        qid = entry[0]
        query = entry[1]
        #print(f'{qid}----{query}')
        response = requests.get('http://127.0.0.1:8000/search/', params={'q': query, 'k': args.k})
        hits = response.json()

        rank = 1
        for h in hits['results']:
            out.write(f'{qid} Q0 {h["docid"]} {rank} {h["score"]:.6f} Anserini\n')
            rank = rank + 1
