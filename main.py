import sys
from extract_words import extract_words

# Get the file path from the command line argument
if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    print("Please provide a file path as an argument.")
    sys.exit()

filtered_words = extract_words(file_path)
print(filtered_words)

with open('filtered_words.txt', 'w') as f:
    # Write each word to a new line in the file
    f.write('\n'.join(filtered_words))