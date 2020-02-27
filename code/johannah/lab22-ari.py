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


ari = (4.71*(characters/words))+(0.5*(words/sentences))-21.43
#Characters are the number of letters and numbers.
characters = len(gettysburg.txt)
words = index
sentences = period space

