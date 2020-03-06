# This is from File IO docs. use this and understand it.
# f is whatever im trying to open.

# with open('filename.txt', 'r') as f:
#     contents = f.read()

# Use this from Lab 21
# To strip punctuation:
# import string
# s = 'I $am a !string with punc&^%*tuation!'
# translator = str.maketrans('', '', string.punctuation)
# string_without_punct = s.translate(translator) I am a string with punctuation

# start with sentences
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}


import re, string


with open("words.txt", "r") as words:
    contents = words.read()
    print(contents)



contents = contents.strip()
sentences = contents.split(".")
sentences.remove("")
numberof_sentences = (len(sentences))
print("\nnumber of sentences", numberof_sentences)
print("\nthese are my sentences", sentences)

# removeing punctuation with maketrans
trans = str.maketrans('','', string.punctuation)
newinput = contents.translate(trans)
characters = newinput.replace(" ", "")
while characters is (", ' . ?"):
    characters.remove(", ' . ?")
print("my characters are: ", characters)
num_of_character = (len(characters))
print(num_of_character)


words = str(re.split("[" " .]",contents))
# print("\n these are words", words)
length_ofwords = len(words)
print("number of words", length_ofwords)



a = 4.71 * (num_of_character/length_ofwords) + 0.5 * (length_ofwords/numberof_sentences) - 21.43
math = round(a)

# my math number equaled 23 and to get it to access inside the dictionary
# i needed the exact number. So i made an if statement for anything over 14
# would equal 14 so that I could access my dictionary.
if math > 14:
    math = 14


# how to pull a dictionary out of a dictionary by peice. 


    

print(f"The ARI for the thegettysburgaddress.text is {math}")
print(f"This corresponds to a {ari_scale[math]['grade_level']} level of difficulty")

# to access a value from a dictionary the key must match exactly if you 
# have single quotes in dictionary you must use single quotes to pull
# the value from the dictionary.
print(f"that is suitable for an average person {ari_scale[math]['ages']} years old.")



 
   






'''Lab 22: Compute Automated Readability Index
Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. The general formula to compute the ARI is as follows:

ARI Formula

The score is computed by multiplying the number of characters divided by the number of words by 4.17, adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal, always round up. Scores greater than 14 should be presented as having the same age and grade level as scores of 14.



Scores correspond to the following ages and grad levels:

    Score  Ages     Grade Level
     1       5-6    Kindergarten
     2       6-7    First Grade
     3       7-8    Second Grade
     4       8-9    Third Grade
     5      9-10    Fourth Grade
     6     10-11    Fifth Grade
     7     11-12    Sixth Grade
     8     12-13    Seventh Grade
     9     13-14    Eighth Grade
    10     14-15    Ninth Grade
    11     15-16    Tenth Grade
    12     16-17    Eleventh grade
    13     17-18    Twelfth grade
    14     18-22    College
Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level.

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
The output should look something like the following:

--------------------------------------------------------

The ARI for gettysburg-address.txt is 12
This corresponds to a 11th Grade level of difficulty
that is suitable for an average person 16-17 years old.'''


