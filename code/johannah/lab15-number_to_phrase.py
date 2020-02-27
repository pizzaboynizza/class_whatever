'''
1. Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99. (Hint: you can use modulus to extract the ones and tens digit.)
x = 67
tens_digit = x//10
ones_digit = x%10
(Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.)

2. Handle numbers from 100-999
'''


user_input = int(input('Enter a whole number to determine if it is a number 0 to 999: '))
hundreds_digit = user_input // 100
#tens_digit = user_input // 10
ones_digit = user_input % 10

under_twenty = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundreds = ['', 'one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred']

if user_input < 20:
  tens_digit = user_input // 10
  print(under_twenty[user_input])
elif 20 <= user_input <= 99:
  tens_digit = user_input // 10
  print(tens[tens_digit] + ' ' + under_twenty[ones_digit])
elif 100 <= user_input <= 119:
  tens_digit = user_input // 10
  print(hundreds[hundreds_digit] + ' ' + under_twenty[user_input - (hundreds_digit * 100)])
else:
  tens_digit = (user_input - (hundreds_digit * 100)) // 10
  print(hundreds[hundreds_digit] + ' ' + tens[tens_digit] + ' ' + under_twenty[ones_digit])
#   print(under_twenty[ones_digit])
# print(type(tens[tens_digit]))
# print(type(under_twenty[ones_digit]))