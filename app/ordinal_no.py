import re

def extract_ordinals(sentence):
    ordinal_pattern = r"\b(\d+)(?:st|nd|rd|th)\b"
    ordinals = []
    
    matches = re.findall(ordinal_pattern, sentence)
    for match in matches:
        ordinal = int(match)
        ordinals.append(ordinal)
    
    return ordinals


