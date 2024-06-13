import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import pandas as pd
from loguru import logger
import re
import argparse

def evaluate_reasoning_steps(question, predicted_reasoning_steps, ground_truth_reasoning_steps, llama_model, llama_tokenizer):
    messages = [
        {"role": "system", "content": "You are an AI assistant that evaluates if the predicted reasoning steps match the ground truth reasoning steps."},
        {"role": "user", "content": f"Question: {question}\n\nPredicted Reasoning Steps:\n{predicted_reasoning_steps}\n\nGround Truth Reasoning Steps:\n{ground_truth_reasoning_steps}\n\nDo the predicted reasoning steps follow the same approach as the ground truth reasoning steps and lead to the correct solution? Respond with 'yes' if they match, or 'no' if they differ significantly or lead to an incorrect solution."}
    ]
    
    input_ids = llama_tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to('cuda')
    
    with torch.no_grad():
        output = llama_model.generate(
            input_ids,
            max_new_tokens=32,
            num_return_sequences=1,
            pad_token_id=llama_tokenizer.eos_token_id
        )
    
    response = output[0][input_ids.shape[-1]:]
    evaluation = llama_tokenizer.decode(response, skip_special_tokens=True).strip()
    return evaluation

def main(args):
    # Load the llama3-8b model and tokenizer
    model_name = "meta-llama/Meta-Llama-3-70B-Instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    config = BitsAndBytesConfig(
        load_in_4it=True,
        llm_int8_enable_fp32_cpu_offload=True,
        bnb_4bit_compute_dtype = torch.float16
    ) 
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="cuda",
        quantization_config=config,
    )

    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(args.csv_file)

    question_column = "question"
    ground_truth_answer_column = "answer"
    ground_truth_reasoning_column = "solution"
    predicted_reasoning_column = args.reasoning_column

     # Filter out rows with empty ground truth reasoning steps
    # df = df[df[ground_truth_reasoning_column].notna() & (df[ground_truth_reasoning_column] != '')]
    # df = df.astype({ground_truth_reasoning_column: 'str'})

    # Filter the DataFrame to include only the rows with the specified indices
    # indices_to_process = [259, 274, 2346]
    # df = df[df.index.isin(indices_to_process)]
    
    answers = []
    answer_verifications = []
    reasoning_evaluations = []
    for i, row in df.iterrows():
        logger.info('Index: {}', i)
        # if row[ground_truth_reasoning_column]) == 0:
        #     logger.info('test')
        #     reasoning_evaluations.append('unknown')
        # else:
        question = row[question_column]
        predicted_reasoning_steps = row[predicted_reasoning_column]
        ground_truth_reasoning_steps = row[ground_truth_reasoning_column]
        reasoning_evaluation = evaluate_reasoning_steps(question, predicted_reasoning_steps, ground_truth_reasoning_steps, model, tokenizer)
        reasoning_evaluations.append(reasoning_evaluation)

        logger.info('result = {}', reasoning_evaluation)

        # logger.info('R: {}', reasoning_evaluations)

    # Add the reasoning evaluations as a new column in the DataFrame
    df["solution_verification"] = reasoning_evaluations
    
    pattern = re.compile(r'\b(yes|no)\b', re.IGNORECASE)
    df['solution_verification_match'] = df['solution_verification'].apply(lambda x: x.lower())

    df.to_csv(args.output_file, index=False)
    
    # valid_evaluations = df['solution_verification_match'].isin(['yes', 'no'])
    # accuracy = (df.loc[valid_evaluations, 'solution_verification_match'] == 'yes').mean()
    
    # logger.info("Accuracy: {:%}", accuracy)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify evaluation steps of model.")
    parser.add_argument("--csv_file", type=str, required=True, help="Path to the input CSV file")
    parser.add_argument("--reasoning_column", type=str, required=True, help="Column name for reasoning steps")
    parser.add_argument("--output_file", type=str, required=True, help="Path to the output CSV file")
    args = parser.parse_args()

    main(args)
