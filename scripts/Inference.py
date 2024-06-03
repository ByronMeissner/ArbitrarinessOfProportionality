import os

FastLanguageModel.for_inference(model)  # Enable native 2x faster inference

# Path to the directory
DIR = ""

# Example file path
filename_now = ""
file_path = os.path.join(DIR, filename_now)

# Skip directories
if os.path.isdir(file_path):
    raise Exception(f"{file_path} is a directory, not a file.")

# Read the story text
with open(file_path, "r") as file:
    story_text2 = "".join(file.readlines())

summary = ""

# Assuming combine_texts is a function that combines instruction, story, and summary into a format
example = combine_texts(INSTRUCTION, story_text2, summary)


inputs = tokenizer(
[
    example["text"]
], return_tensors = "pt").to("cuda")
