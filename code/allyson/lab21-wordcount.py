import string

with open ("frank.txt") as f:
    words=f.read().split()
# print(words)

def cleaner(word):
    line=''
    word=word.lower()
    for char in word:
        if char not in string.punctuation:
            results += char
    line=line.split()
    return line    



def contents():
    db={}
    for word in words:
        if word not in db:
            db[word] = 0
        db[word] += 1
    return db
db=contents()


def topten(db):
    words = list(db.items())
    words.sort(key=lambda tup:tup[1], reverse=True)
    for i in range(min(10,len(words))):
        print(words[i])
topten(db)



