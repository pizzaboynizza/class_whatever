'''
# Lab 21: Count Words

Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on [Project Gutenberg](http://www.gutenberg.org).
Download it as a UTF-8 text file.

1. Open the file.
2. Make everything lowercase, strip punctuation, split into a list of words.

To strip punctuation:
```py
import string
s = 'I $am a !string with punc&^%*tuation!'
translator = str.maketrans('', '', string.punctuation)
string_without_punct = s.translate(translator) # I am a string with punctuation
```

3. Your dictionary will have words as `keys` and counts as `values`. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
4. Print the most frequent top 10 out with their counts. You can do that with the code below.

```python
# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
```

You'll find that the most common words aren't particularly interesting (lots of 'I's, 'the', 'and', 'he', 'she', and 'but's). To get more relevant words, remove *stop words* from your text.

```py
STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
```

## Version 2 (optional)

Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.

## Version 3 (optional)

Let the user enter a word, then show the words which most frequently follow it.
'''
user_word = input('Enter a word: ')
import string
filename = 'moby_dick.txt'
with open('/home/michael/Desktop/'+filename, 'r') as f:
    contents = f.read()
#Removing punctuation
translator = str.maketrans('', '', string.punctuation)
contents = contents.translate(translator) 
contents = ' '.join(contents.split('—'))
contents = contents.strip()

#Counting the number of words
split_between_spaces = contents.split(' ')
while split_between_spaces.count('') > 0:
    split_between_spaces.remove('')

double_word_dict = {}
for i in range(len(split_between_spaces) - 2):
    double_word = split_between_spaces[i] + ' ' + split_between_spaces[i+1]
    double_word_keys = list(double_word_dict.keys())
    if double_word_keys.count(double_word) > 0:
        double_word_dict[double_word] += 1
    else:
        double_word_dict[double_word] = 1

double_words = list(double_word_dict.items())
double_words.sort(key=lambda tup: tup[1], reverse=True)

word_after_user = {}
i = 0
# print(double_words)
while len(word_after_user) < 10 and i < len(double_words):
    double_word_list = double_words[i][0].split()
    first_word = double_word_list[0]
    second_word = double_word_list[1]
    if first_word == user_word:
        word_after_user[second_word] = double_words[i][1]
    i = i + 1

print(word_after_user)
# while len(interesting_words) < 10:
#     if STOPWORDS.count(words[i][0]) == 0:
#         interesting_words.append(words[i])
#         print(words[i])
#     i = i + 1

# # for i in range(min(10, len(double_words))):
# #     print(double_words[i])

# STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", "would"]

# double_STOPWORDS = []
# for i in range(len(STOPWORDS)):
#     for j in range(len(STOPWORDS)):
#         double_STOPWORDS.append(STOPWORDS[i] + ' ' + STOPWORDS[j])

# interesting_double_words = []
# i = 0
# while len(interesting_double_words) < 10:
#     if double_STOPWORDS.count(double_words[i][0]) == 0:
#         interesting_double_words.append(double_words[i])
#         print(double_words[i])
#     i = i + 1

# word_dict = {}
# for word in split_between_spaces:
#     word_keys = list(word_dict.keys())
#     if word_keys.count(word) > 0:
#         word_dict[word] += 1
#     else:
#         word_dict[word] = 1

# words = list(word_dict.items())
# words.sort(key=lambda tup: tup[1], reverse=True)

# interesting_words = []
# i = 0
# while len(interesting_words) < 10:
#     if STOPWORDS.count(words[i][0]) == 0:
#         interesting_words.append(words[i])
#         print(words[i])
#     i = i + 1
# print(STOPWORDS.count('that'))
# for i in range(min(10, len(words))):
#     print(words[i])