import re
def extract_words(file_path):
    # Open the text file
    with open(file_path, 'r') as file:
        data = file.read()

    # Remove non-alphabetic characters
    data = re.sub(r'[^a-zA-Z\s-]', '', data)

    # Extract only words
    words = data.split()
    # Remove empty words
    words = [word for word in data.split() if word]
    # Remove standalone hyphens
    words = [re.sub(r'(?<![a-zA-Z])-|-(?![a-zA-Z])', '', word) for word in words]

    # Read in the stopwords
    with open('stopwords.txt', 'r') as f:
        stopwords = set(f.read().splitlines())

    # Filter out the stop words
    filtered_words = [word for word in words if word.lower() not in stopwords]

    return filtered_words
