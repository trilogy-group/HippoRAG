DATA=worksmart_20104_2024-06-04
LLM=gpt-3.5-turbo-1106
SYNONYM_THRESH=0.8
GPUS=0,1,2,3
LLM_API=openai

bash src/setup_hipporag_colbert.sh $DATA $LLM $GPUS $SYNONYM_THRESH $LLM_API