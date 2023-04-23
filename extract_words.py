# Preprocess dataset file into a list of words without stop words
import re
import os

def extract_words(file_path):
    # Open the text file
    with open(file_path, 'r') as file:
        print("Extracting words from txt file started:")
        while True:
            # Read 1 MB of data at a time
            data = file.read(1024 * 1024)
            if not data:
                break

            # Remove non-alphabetic characters
            data = re.sub(r'[^a-zA-Z\s-]', '', data)

            # Extract only words
            words = data.split()

            # Remove empty words
            words = [word for word in words if word]

            # Remove standalone hyphens
            words = [re.sub(r'(?<![a-zA-Z])-|-(?![a-zA-Z])', '', word) for word in words]

            # Read in the stopwords
            with open('stopwords.txt', 'r') as f:
                stopwords = set(f.read().splitlines())

            # Filter out the stop words
            filtered_words = [word for word in words if word.lower() not in stopwords]

            # Yield the filtered words
            yield from filtered_words
        print("Extracting words from txt file completed")
