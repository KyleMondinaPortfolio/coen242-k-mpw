import sys
from extract_words import extract_words
from kalgo1 import kalgo1
from kalgo2 import kalgo2

# Get the file path from the command line argument
if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    print("Please provide a file path as an argument.")
    sys.exit()

words = extract_words(file_path)

algo1_most_common = kalgo1(words,1)
algo2_most_common = kalgo2(words,1)

print(algo1_most_common)
print(algo2_most_common)

