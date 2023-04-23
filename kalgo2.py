# Find k most common word using a max heap of tuples where the first element is the negative count of each word

import heapq
from collections import Counter

def kalgo2(words,k):

    counter = Counter(word for word in words)
    heap = [(-count, word) for word, count in counter.items()]
    heapq.heapify(heap)

    k_most_common = [heapq.heappop(heap)[1] for _ in range(k)]
    print(f"{k}th most common word: {k_most_common}")

    return k_most_common