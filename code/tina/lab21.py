import string



# remove = dict.fromkeys(map(ord, '\n' + string.punctuation))
with open("faith.txt", 'r') as inputfile:
    f = inputfile.read()
count = {}
f = f.lower()
# removeing punctuation with maketrans
trans = str.maketrans('','', string.punctuation)
# my text doc without punctuation
newinput = f.translate(trans)
word1 = newinput.split()
# this stopwords to remove from a list
stopwords = ['terms','know','see','like','ship','looked','said','cant','works','im','work','well','back','this','he','you','a','the','i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
# this is a comprehensions to go thought the list and remove stop words and make a new list
new_words = [word for word in word1 if word not in stopwords]


# adding words to a dic with a key being the word and a value being +1 each time it seen
for word in new_words:
    if word in count:
        count[word]+=1  
    else:  
        count[word] = 1


words = list(count.items()) 
words.sort(key=lambda tup: tup[1], reverse=True) 
for i in range(min(10, len(words))): 
    print(words[i])

# print(count)
# print('the'in count)
# count['the'] +=1
# print(count['the'])