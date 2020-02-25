
def check_palindrome(word):
    print("Let's see if a word is a palindrome!")
    word = input("Give me a word: ")
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else: 
        return False

# print(check_palindrome())

def check_anagram():
    print("Welcome to Anagram Checker!")
    word_1 = input("Give me your first word or words: ").casefold()
    word_2 = input("Give me your second word or words: ").casefold()
    word_1 = sorted(word_1.strip())
    word_2 = sorted(word_2.strip())
    if word_1 == word_2:
        return True
    else:
        return False

print(check_anagram())