# Preprocess dataset file into a list of words without stop words
import re
import os

def extract_words(file_path):
    # Open the text file
    with open(file_path, 'r') as file:
        print("checkpoint 1")
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
        print("checkpoint 7")





"""
import re
def extract_words(file_path):
    # Open the text file
    with open(file_path, 'r') as file:
        data = file.read()

    print("checkpoint 1")
    # Remove non-alphabetic characters
    data = re.sub(r'[^a-zA-Z\s-]', '', data)
    print("checkpoint 2")

    # Extract only words
    words = data.split()
    print("checkpoint 3")


    # Remove empty words
    words = [word for word in data.split() if word]
    print("checkpoint 4")

    # Remove standalone hyphens
    words = [re.sub(r'(?<![a-zA-Z])-|-(?![a-zA-Z])', '', word) for word in words]
    print("checkpoint 5")


    # Read in the stopwords
    with open('stopwords.txt', 'r') as f:
        stopwords = set(f.read().splitlines())
    print("checkpoint 6")


    # Filter out the stop words
    filtered_words = [word for word in words if word.lower() not in stopwords]
    print("checkpoint 7")


    return filtered_words

    import re
def extract_words(file_path, chunk_size=1024*1024):
    # Read in the stopwords
    with open('stopwords.txt', 'r') as f:
        stopwords = set(f.read().splitlines())

    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            # Remove non-alphabetic characters
            chunk = re.sub(r'[^a-zA-Z\s-]', '', chunk)

            # Extract only words
            words = chunk.split()
            # Remove empty words
            words = [word for word in chunk.split() if word]
            # Remove standalone hyphens
            words = [re.sub(r'(?<![a-zA-Z])-|-(?![a-zA-Z])', '', word) for word in words]

            # Filter out the stop words
            filtered_words = [word for word in words if word.lower() not in stopwords]

            for word in filtered_words:
                yield word

    """
