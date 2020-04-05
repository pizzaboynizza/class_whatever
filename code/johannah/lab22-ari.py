'''
length
length of string
break things into spaces
sentences: split by period space
If the result is a decimal, always round up.
Scores greater than 14 should be presented as having the same age and grade level as scores of 14.
'''

# book_dir = os.path.join(os.getcwd(), 'count_words')
# for file in os.listdir(book_dir):
#     if file.endswith('.txt'):
#         file_name = file.split('.')[0]
#         with open(os.path.join(book_dir, file), 'r') as f:
#             text = f.read()


with open('phonebook.txt') as phone_book_file:
    phone_book_data = phone_book_file.read().split('\n')

phone_book = {}
for line in phone_book_data:
    name, number = line.split()
    phone_book[name] = number

johannah-pdxcode/class_whatever/code/johannah/gettysburg.txt


ari = 4.71*(characters/words) + 0.5*(words/sentences)-21.43

#Characters are the number of letters and numbers.
characters = len(gettysburg.txt)
words = index
sentences = period space

ari_scale = {
     1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages': '6-7', 'grade_level': '1st Grade'},
     3: {'ages': '7-8', 'grade_level': '2nd Grade'},
     4: {'ages': '8-9', 'grade_level': '3rd Grade'},
     5: {'ages': '9-10', 'grade_level': '4th Grade'},
     6: {'ages': '10-11', 'grade_level': '5th Grade'},
     7: {'ages': '11-12', 'grade_level': '6th Grade'},
     8: {'ages': '12-13', 'grade_level': '7th Grade'},
     9: {'ages': '13-14', 'grade_level': '8th Grade'},
    10: {'ages': '14-15', 'grade_level': '9th Grade'},
    11: {'ages': '15-16', 'grade_level': '10th Grade'},
    12: {'ages': '16-17', 'grade_level': '11th Grade'},
    13: {'ages': '17-18', 'grade_level': '12th Grade'},
    14: {'ages': '18-22', 'grade_level': 'College'}
}

'''
OUTPUT:
The ARI for gettysburg-address.txt is 12
This corresponds to a 11th Grade level of difficulty
that is suitable for an average person 16-17 years old.
'''