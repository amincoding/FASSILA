import pandas as pd
import re

path = "C:/Users/amina/OneDrive/Desktop/corpus/FENNEC.csv"
path2 = "C:/Users/amina/OneDrive/Desktop/corpus/hans-wehr.csv"


data = pd.read_csv(path)
data2 = pd.read_csv(path2)

res = []
def count_MSA_words():
    for text in data["text"]:
        for t in text.split(" "):
            for x in data2["text"]:
                if t == x and t not in res:
                    res.append(t)

    return res



def vocabulary_size():
    words = []
    for sentences in data["text"]:
        for word in sentences.split(" "):
            if word not in words:
                words.append(word)
    return words


def is_ascii(s):
    return all(ord(char) < 128 for char in s)

def count_latin_characters(s):
    latin_count = sum(1 for char in s if char.isalpha() and is_ascii(char))
    return latin_count

# Example usage:
index = 0
for text in data["text"]:
    latin_count = count_latin_characters(text)
    index += latin_count

print("number of latin characters : " + str(index))
print("number of MSA words : " + str(len(count_MSA_words())))
print("vocabulay size : " + str(len(vocabulary_size())))
