import sys
from extract_words import extract_words
from kalgo1 import kalgo1
from kalgo2 import kalgo2
from performance_test import performance_test

# Extract word list from dataset file
#words_2gb = extract_words("./dataset/data_2.5GB.txt")
#words_16gb = extract_words("./dataset/data_16GB.txt")
#words_300mb = extract_words("./dataset/small_50MB_dataset.txt")


words_2gb = extract_words("./dataset/data_2.5GB.txt")
performance_test(kalgo1,words_2gb,10)

words_2gb = extract_words("./dataset/data_2.5GB.txt")
performance_test(kalgo2,words_2gb,10)











