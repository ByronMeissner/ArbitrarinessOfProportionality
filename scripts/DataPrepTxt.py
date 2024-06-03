from datasets import Dataset

import pandas as pd

import os

# Set the directory containing the text files
DIR = ""#"FINALFALSE"

INSTRUCTION = "For the given data from the court decision, determine whether the principle of proportionality strictu sensu was applied or not."


df_instructions = pd.DataFrame(columns=['text'])
df_stories = pd.DataFrame(columns=['text'])
df_summaries = pd.DataFrame(columns=['text'])

def combine_texts(instruction, story, summary):
  return {
      "text": f"""
{instruction}

### Story
{story}

### Summary
{summary}
"""}


# Loop through the first 173 files in the directory
for i, filename in enumerate(sorted(os.listdir(DIR))[:160]):
    file_path = os.path.join(DIR, filename)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    with open(file_path, "r") as file:
        story = "".join(file.readlines())
        summary = vector[i] 
    
    df_instructions = pd.concat(
    [df_instructions, pd.DataFrame([{'text': INSTRUCTION}])],
    ignore_index=True
    )
    df_stories = pd.concat(
    [df_stories, pd.DataFrame([{'text': story}])],
    ignore_index=True
    )
    df_summaries = pd.concat(
    [df_summaries, pd.DataFrame([{'text': summary}])],
    ignore_index=True
    )

combined_texts = [combine_texts(instruction, story, summary) for instruction, story, summary in zip(df_instructions["text"], df_stories["text"], df_summaries["text"])]

finetuning_dataset = Dataset.from_dict({"text": [ct["text"] for ct in combined_texts]})
# finetuning_dataset[15]['text']
