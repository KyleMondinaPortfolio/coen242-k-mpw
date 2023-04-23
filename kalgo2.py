# Find k most common word using a max heap of tuples where the first element is the negative count of each word

import heapq
from collections import Counter

def kalgo2(words,k):
    counter = Counter(word for word in words)
    heap = [(-count, word) for word, count in counter.items()]
    heapq.heapify(heap)

    try:
        k_most_common = [heapq.heappop(heap)[1] for _ in range(k)]
    except IndexError:
        print("There are not enough unique words in the generator to extract k most common words")
        k_most_common = []

    print(f"{k}th most common word: {k_most_common}")

    return k_most_common