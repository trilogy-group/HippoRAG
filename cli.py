import argparse
from src.hipporag import HippoRAG

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str)
    parser.add_argument('--extraction_model', type=str, default='openai')
    parser.add_argument('--extraction_model_name', type=str, default='gpt-3.5-turbo-1106')
    parser.add_argument('--retrieval_model', type=str, choices=['facebook/contriever', 'colbertv2'])
    parser.add_argument('--doc_ensemble', action='store_true')
    args = parser.parse_args()

    hipporag = HippoRAG(args.dataset, args.extraction_model, args.extraction_model_name, args.retrieval_model, doc_ensemble=args.doc_ensemble)

    queries = ["Who is present in the Google meet on 2024-06-04 ?"]
    for query in queries:
        ranks, scores, logs = hipporag.rank_docs(query, top_k=10)

        print(ranks)
        print(scores)

# python cli.py --dataset worksmart_20104_2024-06-04 --retrieval_model facebook/contriever