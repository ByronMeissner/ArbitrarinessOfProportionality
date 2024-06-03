import os
import json
import pandas as pd
import re

def extract_information(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    info = {}
    
    # Extract country
    country_data = data.get("country", {}).get("name", "")
    info['country'] = country_data
    
    # Extract docname
    docname_data = data.get("docname", "")
    if "v." in docname_data:
        info['docname'] = docname_data.split(" v.")[0]
    else:
        info['docname'] = docname_data
    
    # Extract judgementdate
    judgementdate_data = data.get("judgementdate", "")
    if judgementdate_data:
        info['judgementdate'] = judgementdate_data.split()[0]
    
    # Extract separateopinion
    separateopinion_data = data.get("separateopinion", "false")
    info['separateopinion'] = separateopinion_data.lower() == "true"
    
    # Extract conclusion
    conclusions = data.get("conclusion", [])
    conclusion_articles = []
    conclusion_types = []
    for conclusion in conclusions:
        article = conclusion.get("base_article", "")
        if article.isdigit():  # Check if the article is a number
            conclusion_articles.append(article)
        
        # Check for types "violation" or "no-violation"
        ctype = conclusion.get("type", "").lower()
        if ctype in ["violation", "no-violation"]:
            conclusion_types.append(ctype)
    
    info['conclusion_articles'] = conclusion_articles
    info['conclusion_types'] = conclusion_types
    
    # Search content for majority patterns
    content_sections = data.get("content", {})
    majority_patterns = [
        r'(Holds|Rejects|Finds|Declares|Decides) by (\w+) votes? to (\w+) that (there has been a violation of Article|there has been no violation of Article)',
        r'by (\w+) votes? to (\w+),? that (there has been a violation of Article|there has been no violation of Article)',
        r'Holds by (\w+) votes? to (\w+) that (there has been a violation of Article|there has been no violation of Article)',
        r'(Holds|Rejects|Finds|Declares|Decides) by (\w+) votes? to (\w+) (that|there has been|there has been no)',
        r'by (\w+) votes? to (\w+),? (that|there has been|there has been no)',
        r'Holds by (\w+) votes? to (\w+) (that|there has been|there has been no)'
    ]
    
    content_text = json.dumps(content_sections)
    dissenting = False
    vote_ratio = 0
    matched_sentences = []
    
    for pattern in majority_patterns:
        matches = re.findall(pattern, content_text, re.IGNORECASE)
        for match in matches:
            if len(match) >= 3:
                matched_sentences.append(match)
    
    if matched_sentences:
        dissenting = True
        # Using the first match for demonstration; this can be adjusted as needed
        first_match = matched_sentences[0]
        major_votes_str = first_match[1].lower()
        minor_votes_str = first_match[2].lower()
        
        num_dict = {
            'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
            'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
            'seventeen': 17
        }
        
        major_votes = num_dict.get(major_votes_str)
        minor_votes = num_dict.get(minor_votes_str)
        
        if major_votes is not None and minor_votes is not None:
            vote_ratio = minor_votes / (major_votes + minor_votes)
    
    info['dissenting'] = dissenting
    info['vote_ratio'] = vote_ratio
    
    return info

def main():
    folder_path = ''
    data_list = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            file_path = os.path.join(folder_path, file_name)
            data = extract_information(file_path)
            if data is not None:  # Only add if data is not None
                data['file_name'] = file_name  # Add the file name to the data dictionary
                data_list.append(data)
    
    df = pd.DataFrame(data_list)
    df.to_csv('', index=False)

if __name__ == "__main__":
    main()
