from transformers import AutoTokenizer

import os

# Set the directory containing the text files
DIR = ""#"FINALFALSE"

# Define the instruction
INSTRUCTION = "For the given data from the court decision, determine whether the principle of proportionality strictu sensu was applied or not."

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("unsloth/llama-3-8b-Instruct-bnb-4bit")

# Create the vector list
applied_string = "proportionality principle strictu sensu applied"
not_applied_string = "proportionality principle strictu sensu not applied"
vector = [not_applied_string] * 80 + [applied_string] * (80) #80 each i think


# Loop through the first 173 files in the directory
for i, filename in enumerate(sorted(os.listdir(DIR))[:160]):#Change this for diff. data file size
    file_path = os.path.join(DIR, filename)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    with open(file_path, "r") as file:
        story = "".join(file.readlines())
        summary = vector[i]

    # Count tokens
    instruction_tokens = tokenizer(INSTRUCTION, return_tensors="pt")["input_ids"].shape[1]
    story_tokens = tokenizer(story, return_tensors="pt")["input_ids"].shape[1]
    summary_tokens = tokenizer(summary, return_tensors="pt")["input_ids"].shape[1]
  
    # Print table of tokens
    total_tokens = instruction_tokens + story_tokens + summary_tokens
    # print(f"{total_tokens:<12}{instruction_tokens:<12}{story_tokens:<12}{summary_tokens:<12}")
