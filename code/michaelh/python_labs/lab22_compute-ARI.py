'''
# Lab 22: Compute Automated Readability Index

Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. The general formula to compute the ARI is as follows:

![ARI Formula](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/878d1640d23781351133cad73bdf27bdf8bfe2fd)

The score is computed by multiplying the number of characters divided by the number of words by 4.17, adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. **If the result is a decimal, always round up.** Scores greater than 14 should be presented as having the same age and grade level as scores of 14.

Scores correspond to the following ages and grad levels:

```
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
```

Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level.

```python
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
```

The output should look something like the following:

    --------------------------------------------------------

    The ARI for gettysburg-address.txt is 12
    This corresponds to a 11th Grade level of difficulty
    that is suitable for an average person 16-17 years old.

    --------------------------------------------------------
'''
import string
filename = 'moby_dick.txt'
with open('/home/michael/Desktop/'+filename, 'r') as f:
    contents = f.read()
contents = ' '.join(contents.split('\n')) #Making it one line
contents = contents.lower() #Making lowercase

#Removing punctuation except '.', '?' and '!'
# print(string.punctuation)
punc_no_sentence_sep = string.punctuation
punc_no_sentence_sep = punc_no_sentence_sep.replace('.', '')
punc_no_sentence_sep = punc_no_sentence_sep.replace('?', '')
punc_no_sentence_sep = punc_no_sentence_sep.replace('!', '')
# print(punc_no_sentence_sep)
translator = str.maketrans('', '', punc_no_sentence_sep)
contents = contents.translate(translator) 
contents = ' '.join(contents.split('—'))
# contents = ' '.join(contents.split(','))
# print(contents)
contents = contents.strip()

#Counting the number of sentences
contents.replace('?', '.')
contents.replace('!', '.')
split_between_periods = contents.split('. ')
# print(split_between_periods)
sentences = len(split_between_periods)
print(sentences)

#Counting the number of words
contents = ' '.join(contents.split('.'))
split_between_spaces = contents.split(' ')
while split_between_spaces.count('') > 0:
    split_between_spaces.remove('')
# print(split_between_spaces)
words = len(split_between_spaces)
print(words)

for char in string.whitespace:
    contents = ''.join(contents.split(char))
# print(contents)
chars = len(contents)
print(chars)
ARI = math.ceil(4.71*(chars/words) + 0.5*(words/sentences) - 21.43)
if ARI > 14:
    ARI = 14
print(ARI)

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

ARI_dict = ari_scale[ARI]
grade_level = ARI_dict['grade_level']
ages = ARI_dict['ages']

print(f'The ARI for {filename} is {ARI}')
print(f'This corresponds to a {grade_level} level of difficulty')
print(f'that is suitable for an average person {ages} years old.')