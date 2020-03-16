"""
Lab 21: Count Words
Let's write a python module to analyze a given text file containing a book for its vocabulary 
frequency and display the most frequent words to the user in the terminal.
To get more relevant words, remove stop words from your text.

Print the most frequent top 10 out with their counts.

Version 2 (optional)
Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.

Version 3 (optional)
Let the user enter a word, then show the words which most frequently follow it.
"""
# # Version 1
# import string

# words = {}
# STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

# with open('faith.txt') as worddoc:
#     contents = worddoc.read()

# before_strip = contents.lower()
# translator = str.maketrans("", "", string.punctuation)
# noPunct = before_strip.translate(translator)

# story = noPunct.split(" ")

# while('' in story) :
#     story.remove('')

# for word in STOPWORDS:
#     while(word in story) :
#         story.remove(word)

# for word in story:
#     if word in words:
#         words[word] += 1
#     if word not in words:
#         words[word] = 1

# word_count = list(words.items()) # .items() returns a list of tuples
# word_count.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(word_count))):  # print the top 10 words, or all of them, whichever is smaller
#     print(word_count[i])


# Version 2 

import string

words = {}
STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

with open('faith.txt') as worddoc:
    contents = worddoc.read()

before_strip = contents.lower()
translator = str.maketrans("", "", string.punctuation)
noPunct = before_strip.translate(translator)

story = noPunct.split(" ")

while('' in story) :
    story.remove('')

for word in STOPWORDS:
    while(word in story) :
        story.remove(word)

for word in story:
    if (word, word+1) in words:
        words[(word, word[+1])] += 1
    if word not in words:
        words[(word, word+1)] = 1

word_count = list(words.items()) # .items() returns a list of tuples
word_count.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(word_count))):  # print the top 10 words, or all of them, whichever is smaller
    print(word_count[i])


# # 
# # Version 3 (optional)
# # Let the user enter a word, then show the words which most frequently follow it.

# # Version 3
# user =  input("blah blah blah")
# word_count.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(word_count))):  # print the top 10 words, or all of them, whichever is smaller
#     user_sort = word_count[i]
# for user in dict{}:
#   