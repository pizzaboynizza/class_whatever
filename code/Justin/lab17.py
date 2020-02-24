def palindrome_checker(user_input):
    return [char for char in user_input]

user_input = input("enter a word:")

list1 = palindrome_checker(user_input)

list2 = list1.copy()

list2.reverse()

if list1 == list2:
    print("Palindrome")
else:
    print("Not Palindrome")

def anagram_checker(str1, str2):
    str1.lower()
    list_str1 = list(str1)
    list_str1.sort()
    str2.lower
    list_str2 = list(str2)
    list_str2.sort()

    if list_str1 == list_str2:
        print("Anagram!")

    else:
        print("Not anagram!")

anagram_checker("d2d3d4", "1d5dd7")








