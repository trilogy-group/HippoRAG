Use `qa_reader.py` to leverage retrieved documents to answer the questions, e.g.,

```shell
python qa_reader.py --dataset hotpotqa --retriever bm25 --data output/hippo_hotpotqa_bm25_.json
```

where `--data` is the retrieval result file.

python qa/qa_reader.py --dataset worksmart_20104_2024-06-04 --retriever colbertv2 --data output/hippo_worksmart_20104_2024-06-04_colbertv2_.json