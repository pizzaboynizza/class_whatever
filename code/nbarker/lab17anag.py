'''
nick barker
anagram checker
2/24/2020
'''
#user input
word1 = input("Please enter your first word: ")
word2 = input("Please enter your second word: ")

#make it lowercase
word1 = word1.lower()
word2 = word2.lower()

#see where I'm at!
#print(word1)
#print(word2)

#remove all spaces
word1 = word1.replace(" ", "")
#print(word1)
word2 = word2.replace(" ", "")
#print(word2)

#sort those puppies!  Now they're lists?! okay!
word1 = sorted(word1)
word2 = sorted(word2)
#print(word1)
#print(word2)

#check if equal
def anagram_checker(word1, word2):
    if word1 == word2:
        print("We have a match!!")
        return(True)
    else:
        print("Not a match")
        return(False)

#anagram_checker(word1)
anagram_checker(word1,word2)
