import sys
from extract_words import extract_words
from kalgo1 import kalgo1
from kalgo2 import kalgo2
from performance_test import performance_test

# Get the file path from the command line argument
if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    print("Please provide a file path as an argument.")
    sys.exit()

words = extract_words(file_path)

print("algorithm 1 performance:")
performance_test(kalgo1,words,1)

print("algorithm 2 performance:")
performance_test(kalgo2,words,1)
