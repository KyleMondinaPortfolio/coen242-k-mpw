# Find k most common word using a dictionary with the word as the key and its occurence as the value

def kalgo1(words,k):

    # Create a dictionary of all unique words in the dataset with their frequency count
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Find the K-most common word:
    print(f'number of unique words: {len(word_count)}')
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    k_most_common = sorted_words[:k]
    print(f"{k}th most common word: {k_most_common}")

    return k_most_common

    

