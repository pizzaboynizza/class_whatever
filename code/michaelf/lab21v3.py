import string

while True:
    filename = input("give me your filename: ")
    try:
        with open(filename) as f:
            txt = f.read()
        break
    except IOError:
        print("Invalid filename, check your directory and try again!")
txt = txt.lower()
translator = str.maketrans('', '', string.punctuation)
string_without_punct = txt.translate(translator) 
words = txt.split()
# print(words)

STOPWORDS = ['[footnote', 'one', '"', '|',  'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

# words = [word for word in words if word not in STOPWORDS]
# print(good_words)
print(words)
dic = {}

user_word = input("give me a search word: ").lower()
if user_word in words:
    for i in range(len(words)-1):
        if words[i] == user_word:
            if words[i] + ' ' + words[i+1] in dic:
                dic[words[i] + ' ' + words[i+1]] = dic.get(words[i] + ' ' + words[i+1]) + 1
                
            else:
                dic[words[i] + ' ' + words[i+1]] = 1
else:
    print(f"{user_word} not present in {filename}")


freq_words = list(dic.items()) # .items() returns a list of tuples
freq_words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(freq_words))):  # print the top 10 words, or all of them, whichever is smaller
    print(freq_words[i])