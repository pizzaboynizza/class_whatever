'''Lab 15: Number to Phrase
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10
Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.'''

input_numbers = int(input("Enter a number: "))
def numbers(input_numbers):
    # print(input_numbers)
    tens_digit = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
    10: "ten", 20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty', 70:'seventy', 80: 'eighty', 90:'ninety', 11:'eleven', 12: 'twelve', 13: 'thirteen', 14:'fourteen', 15: 'fifteen', 16: 'sixteen', 18: 'eighteen', 19:'nineteen'}
    hundreds_digit = {00: 'hundred', 100: 'one-hundred', 200: 'two hundred', 300: 'three-hundred', 400: 'four-hundred', 500: 'five-hundred', 600: 'six-hundred'}
    # input_numbers = int(input("Enter number: "))
    
    # tens_conversion = input_numbers // 10
    # ones_conversion = input_numbers%10
    
    if input_numbers < 20:
        return tens_digit[input_numbers]
        print(tens_digit[input_numbers])
    if input_numbers > 20 and input_numbers <= 99:
        ones_conversion = input_numbers // 10
        tens_conversion = input_numbers%10
        a =  ones_conversion * 10
        return tens_digit[a] + ' ' + tens_digit[tens_conversion]
    if input_numbers >= 100 and input_numbers<= 999:
        hundreds_conversion = input_numbers%10
       
        ones_conversion = input_numbers//10 * 10
        tens_conversion = input_numbers%10
        b = hundreds_conversion * 100
        return hundreds_digit[b] + ' ' + hundreds_digit[ones_conversion] + ' ' + hundreds_digit[tens_conversion]

    
        
    



    #     return ones_digit[input_numbers]
    # if input_numbers == 14:
    #     return ones_digit[input_numbers]
    # if input_numbers == 85:
    #     ones_conversion = ones_digit%10
    #     tens = tens_digit[tens_conversion]
    #     return ones_digit[tens_conversion]
       
    
        
    
print(numbers(input_numbers))

# teens = {'11':'eleven', '12':'twelve', '13': 'thirteen', '14':'fourteen', '15':'fifteen', '16': 'sixteen', '17':'seventeen', '18':'eighteen', '19': 'nineteen'}

#     if input_numbers == 1:
#         return input_numbers[numbers]

# print(main())
    