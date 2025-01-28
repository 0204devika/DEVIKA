def count_words(sentence):
    words = sentence.split()            # Split the sentence into words
    word_count = {}                     # Initialize an empty dictionary to store the word count
    for word in words:
        if word in word_count:
            word_count[word] += 1       # If the word is already in the dictionary, increment its count
        else:
            word_count[word]=1          # If the word is not in the dictionary, add it with a count of 1
    return word_count
def main():
    sentence = input("Enter a sentence: ")
    word_count = count_words(sentence)
    for word, count in word_count.items():
        print(f"{word}: {count}")          # Print each word and its count
main()