import string

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


file = open("thegettysburgaddress.txt")
new = file.read()


# remove = dict.fromkeys(map(ord, '\n' + string.punctuation))
with open("thegettysburgaddress.txt", 'r') as inputfile:
    f = inputfile.read()
    f = f.lower()
    sentences = new.split('.')
    # removeing punctuation with maketrans
    trans = str.maketrans('','', string.punctuation)
    # my text doc without punctuation
    newinput = f.translate(trans)
    word = newinput.split()
    charac = newinput.replace(" ","")

    char1 = int(len(charac))
    word1 = int(len(word))
    sen1 = int(len(sentences))


math = 4.71 * (char1/word1) + 0.5 * (word1/sen1) - 21.43

a = round(math)


# how to pull a dic out of a dic by peice. 
ari = (
    f"The ARI for the thegettysburgaddress.text is {a}, The correspounds to a {ari_scale[a]['grade_level']} Grade level of difficulty, that is suitable for an average person {ari_scale[a]['ages']} years old.")


    
    
# print(len(sentences))
# print(len(word))
# print(len(charac))
print(ari)



 
   

