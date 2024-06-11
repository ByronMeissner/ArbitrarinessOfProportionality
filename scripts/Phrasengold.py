import json
import os
import re
import csv
from word2number import w2n

def extract_vote_ratio(json_data):
    def words_to_numbers(words):
        try:
            return w2n.word_to_num(words)
        except:
            return None

    def extract_majority_patterns(content):
        patterns = [
            r'by (\w+) votes? to (\w+)\b.*?violation',
            r'by (\w+) votes? to (\w+)\b.*?no violation',
            r'holds by (\w+) votes? to (\w+)\b.*?violation',
            r'holds by (\w+) votes? to (\w+)\b.*?no violation',
            r'by (\w+) votes? to (\w+)\b.*?no breach',
            r'holds by (\w+) votes? to (\w+)\b.*?breach',
            r'Holds by (\w+) votes? to (\w+)'
        ]

        majority_votes = []
        minority_votes = []

        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                major = words_to_numbers(match[0])
                minor = words_to_numbers(match[1])
                if major is not None and minor is not None:
                    majority_votes.append(major)
                    minority_votes.append(minor)
        
        return majority_votes, minority_votes

    vote_ratio = 0
    majority_votes = []
    minority_votes = []

    content_sections = json_data.get("content", {}).values()
    for sections in content_sections:
        for section in sections:
            if isinstance(section, dict):
                elements = section.get("elements", [])
                for element in elements:
                    text = element.get("content", "")
                    major_votes, minor_votes = extract_majority_patterns(text)
                    if major_votes and minor_votes:
                        majority_votes.extend(major_votes)
                        minority_votes.extend(minor_votes)

    if majority_votes and minority_votes:
        ratios = [minor/major for minor, major in zip(minority_votes, majority_votes) if major != 0]
        vote_ratio = sum(ratios) / len(ratios) if ratios else 0

    return vote_ratio

def process_files(input_directory, output_file):
    results = []

    for filename in os.listdir(input_directory):
        if filename.endswith(".json"):
            filepath = os.path.join(input_directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
                vote_ratio = extract_vote_ratio(json_data)
                results.append({
                    'filename': filename,
                    'vote_ratio': vote_ratio
                })

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['filename', 'vote_ratio']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

input_directory = ""
output_file = ""
process_files(input_directory, output_file)
print(f"CSV file has been created successfully at {output_file}.")














