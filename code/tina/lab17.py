import string
print("This is a palindrome and Anagram checker")
word1 = input("Give me a word: ")
word2 = input("Give me a word: ")


def ang(word1, word2):
    a = sorted(list(word1.lower()))
    b = sorted(list(word2.lower()))
    if a == b:
        return print("This is anagram")
    else:
        return print("This is not an anagram")

    

ang(word1, word2)


def reverse_string1(word2):
    # H is storage word2 in rev order by use index system
    h = word2[::-1]
    # now h and word2 work togeather. 
    if h == word2:
        print("This is a palindrome")
    else:
        print("this is not a palindrome")
    
    
print(reverse_string1(word2))