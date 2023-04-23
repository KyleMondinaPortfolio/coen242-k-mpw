# Find k most common word using a max heap of tuples where the first element is the negative count of each word
import heapq
from collections import Counter

def k_most_common_word(word_generator, k):
    word_count = Counter(word_generator)
    k_most_common = heapq.nlargest(k, word_count.items(), key=lambda x: x[1])
    print(f"{k}th most common word: {k_most_common}")

    return k_most_common