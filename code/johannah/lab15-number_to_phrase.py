'''
1. Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99. (Hint: you can use modulus to extract the ones and tens digit.)
x = 67
tens_digit = x//10
ones_digit = x%10
(Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.)

2. Handle numbers from 100-999
'''

#user_input = []
user_input = int(input('Enter a whole number to determine if it is a number 0 to 99: '))
tens_digit = user_input // 10
ones_digit = user_input % 10
print(tens_digit)
print(ones_digit)

if ones_digit == '1':
  print('one')
if ones_digit == '2':
  print('two')
if ones_digit == '3':
  print('three')
if ones_digit == '4':
  print('four')
if ones_digit == '5':
  print('five')
if ones_digit == '6':
  print('six')
if ones_digit == '7':
  print('seven')
if ones_digit == '8':
  print('eight')
if ones_digit == '9':
  print('nine')
else:
  print('')
'''
if tens_digit == '0':
  #do not print 'zero'
if tens_digit == '1':
  print('ten')
if tens_digit == '2':
  print('twenty')
if tens_digit == '3':
  print('thirty')
if tens_digit == '4':
  print('forty')
if tens_digit == '5':
  print('fifty')
if tens_digit == '6':
  print('sixty')
if tens_digit == '7':
  print('seventy')
if tens_digit == '8':
  print('eighty')
if tens_digit == '9':
  print('ninety')
'''
11 eleven
12 twelve
13 thirteen
14 fourteen
15 fifteen
16 sixteen
17 seventeen
18 eighteen
19 nineteen

CREATE A FUNCTION