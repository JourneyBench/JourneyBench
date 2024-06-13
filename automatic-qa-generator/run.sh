python blip_gpt_main.py  \
    --max_n_rounds 8 \
    --data_root=/your/dataset/path \
    --exp_tag=xxxx \
    --dataset=xxxx \
    --device_id=0 \
    --prompt_setting=xxx \
    --data_partition=0_10000 \
    --model gpt4 \
    --vqa_model=blip2_t5_xxl  \
    --temp_gpt=0.0  \
    --data_subset=/your/selected/data/subset/path \
    --openai_key=<your_openai_key>