# Lab 21
# Author : Joe

import string

def specificDisplay(a, b, num, xtra=""):
    print(f"{a}{' ' if xtra != '' else ''}{xtra}{' '*(num-len(a)-len(xtra))}{b}")

filename = "data/lab21.txt"

with open(filename, encoding="utf-8") as f:
    full = f.read()

print(f"\nFor '{filename}':\n")

full = full.lower()
translator = str.maketrans("","", string.punctuation + "—”“")
full = full.translate(translator)

full = full.split()

words = dict()

for w in full:
    if w not in words:
        words[w] = 1
    else:
        words[w] += 1

sort_words = list(words.items())
sort_words.sort(key=lambda tup: tup[1], reverse=True)

STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

i = 0
top10 = []
while len(top10) < 10 and i < len(sort_words):
    if sort_words[i][0] not in STOPWORDS:
        top10.append(sort_words[i][0])
    i += 1

print(f"Top {len(top10)} most used words (excluding some more common words):")
for n in top10:
    # print(f"{n}:\t\t{words[n]}")
    specificDisplay(n, words[n], 18)

# Version 2:
word_pairs = dict()
for i in range(len(full)-1):
    if (full[i], full[i+1]) not in word_pairs:
        word_pairs[(full[i], full[i+1])] = 1
    else:
        word_pairs[(full[i], full[i+1])] += 1

sort_pairs = list(word_pairs.items())
sort_pairs.sort(key=lambda tup: tup[1], reverse=True)

top10_pair = []
i = 0
while len(top10_pair) < 10 and i < len(sort_pairs):
    if sort_pairs[i][0][0] not in STOPWORDS and sort_pairs[i][0][1] not in STOPWORDS:
        top10_pair.append(sort_pairs[i][0])
    i += 1

print(f"\nTop {len(top10_pair)} most common word pairs (excluding some more common words):")
for n in top10_pair:
    specificDisplay(n[0], word_pairs[n], 24, n[1])
    # print(f"{n[0]} {n[1]}:\t\t{word_pairs[n]}")

# Version 3
user_word = input("\nEnter a word to see which words follow it most: ")

user_pairs = [] # (followup_word, count)
for n in sort_pairs:
    if n[0][0] == user_word:
        user_pairs.append((n[0][1], n[1]))

print(f"\nThe top {min(10, len(user_pairs))} words that follow '{user_word}' are:")
for i in range(min(10, len(user_pairs))):
    specificDisplay(user_pairs[i][0], user_pairs[i][1], 18) #no need to sort user_pairs, the way it was built already sorted it
    