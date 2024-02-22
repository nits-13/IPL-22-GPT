import datefinder

def find_dates_in_sentence(sentence):
    dates = []
    matches = datefinder.find_dates(sentence)
    for match in matches:
        dates.append(str(match.date()))
    return dates

# Example usage:
sentence = "The event will take place on 15th June, 2023 and June 18, 2023."
dates = find_dates_in_sentence(sentence)
print(dates)
