'''
Prompt the user for a string, and encode it with ROT13. For each character, find the corresponding character, add it to an output string
'''


result_output = ''
user_input = input("Enter a word/phrase/sentence (letters only) to find out each character's ROT13 correspondence: ")
input_lowered = user_input.lower()  # lowercase user input
print(input_lowered)

chars = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(input_lowered)):
  index_of_letter = int(chars.find(input_lowered[i]))  # index of letter in input_lowered
  index_for_chars = index_of_letter + 13   #index of chars to be translated back to letters in ROT13
  if (index_for_chars) > 25:
    index_of_chars_thirteen = index_for_chars - 26
    #print(chars[index_of_chars_thirteen])
    result_output += (chars[index_of_chars_thirteen])  # new index of chars to be add to result_output
    #print(result_output)
    #print(result_output.join(chars[index_of_chars_thirteen]))
  else:
    #print(chars[index_for_chars])
    result_output += (chars[index_for_chars])
    #print(result_output)
    #print(result_output.join(chars[index_for_chars]))

print(result_output)
