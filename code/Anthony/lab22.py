#compute ARI of text using the ARI formula
#load text file: with open(filename, "r") as soemthing
# need to find the instances of words
# need to get rid of punctuations in word

# need to find all the instances of characters
# need to get rid of all puncts. in character


# need to find all the instances of sentences
# need to find all instances of puncts at the end of sentence (,?!.)
# .count(".")



import string

with open('gettysburg-address.txt', 'r') as f:
    profile = f.read()
#print(len(profile))

# def  sentence_text():
#need to find all the instances of sentences
# need to find all instances of puncts at the end of sentence (,?!.)
# .count(".")
def sentence_func():
    
    for i in str(len(profile)):
       i = profile.count('.')

       
       return i
print(sentence_func())

#FOR WORD COUNT
def words(): #filtering punctuation
    no_punc = ''
    
    for i in profile:
        if i not in string.punctuation:
            no_punc+= i
    #print(no_punc)
    new_words = no_punc.split()
    #print(new_words)
    return len(new_words)
    # print(new_words)
#print(words())


#FOR CHARACTER COUNT
def char(): #filtering punctuation
    new_char = ''
    no_space = ''
    for i in profile:
        if i not in string.punctuation: #filters puncs and sends then to end of list
            new_char+= i
    #print(new_char)
    no_space = new_char.replace(' ', '')
    #print(no_space)
    return len(no_space) # this returns all char plus spaces
print(char(), 'THIS IS CHAR')


        
# ARI= (char/words)4.17 + (#words/#sentences)0.5
#round up if result decimal
# if scores >14: is == (14)scores of (age and grade) level
ari = (char()/words()) * 4.71 + (words()/sentence_func()) *0.5 - 21.43
print(round(ari))
print(ari, 'THIS IS ARI')
print(int(ari))
ari = int(ari)

# if ari >= 14:
#     ari = 14

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

# # grade_level = ari_scale[ari]
# print(grade_level)
print(f"The ARI for gettysburg-address.txt is {ari}")
print(f"This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty")
print(f"That is suitable for an average person {ari_scale[ari]['ages']} years old.")
# get arilevel , find dict, set age == ? and gage level =?


# The ARI for gettysburg-address.txt is 12
# This corresponds to a 11th Grade level of difficulty
# that is suitable for an average person 16-17 years old.