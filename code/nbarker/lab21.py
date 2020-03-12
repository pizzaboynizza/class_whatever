import string
'''
Nick Barker
Lab21.py
'''


with open('gettyaddy.txt', 'r', encoding='utf-8') as file:
    contents = file.read()
    #print(contents)
    s = contents

#Just for the example, here is the addresss!
#s = "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we can not dedicate—we can not consecrate—we can not hallow—this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom—and that government of the people, by the people, for the people, shall not perish from the earth."

#stopwords! notice the all caps! #all info first!
STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn', 'one', 'gutenbergtm', 'gutenberg']


#make everything lowercase
low_data = s.lower()
#fuck yeah


def replacer(s):
    #this will filter out punctuation without adding blank spaces.
    result = ''
    for x in low_data: #this is our lowercase string
        #If you're not punctuation, move on!
        if x not in string.punctuation:
            result += x #added to result
    return result

#we take a lower case string and remove punctuation
replacer(s)

def splitter(result):
    #splits the lowercase, punctuationless text into a list
    wordslist = result.split()
    bat = wordslist #totally could have left it as wordslist
    return bat

result = replacer(s) #replaced punctuation
bat = splitter(result) #the list of words!

words_we_do_not_want = {}
words_we_count = {}

for item in bat: #OMFG I was using the wrong variable, I forgot that for this to work, I really, really need to use the SPLIT LIST, not the original string.
    if item in STOPWORDS: #if it's a bad word, it goes to the old list!
        words_we_do_not_want[item] = words_we_do_not_want.get(item, 0) + 1
    if item not in STOPWORDS: #if it's a good word, it goes to the new list!
        words_we_count[item] = words_we_count.get(item, 0) + 1


print("These are the words we count!", words_we_count)
print("these are the wrods we do not want to count!", words_we_do_not_want) #I did not bother to sort this one

words = list(words_we_count.items()) #from the punctuationless, spacelss, only good words list
words.sort(key=lambda tup: tup[1], reverse=True) #change those puppies into tupules!
for i in range(min(10, len(words))): #print the top ten words, or all of the words, whichever is smallest
    print(words[i])
