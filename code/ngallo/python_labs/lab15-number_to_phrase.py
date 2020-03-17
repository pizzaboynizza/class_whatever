# dictionary of words
number_to_words = {0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Fourty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninty', 1000:"Thousand"}

 #input of user   
user_input = int(input("Enter a number to 999! "))

# function to display results 
def result_of_number(user_input):
    modul = user_input % 10
    tens_digit = user_input - modul
    hundreth_digit = user_input % 100
    anything_really = (user_input % 100) // 10 * 10
    remaining_digit = (user_input - hundreth_digit) // 100

    # print(modul)
    # print(tens_digit)
    # print(anything_really)
    # print(remaining_digit)

    if user_input <= 19:
        print(number_to_words[user_input])
    elif user_input <= 99:NotADirectoryError
        print(number_to_words[tens_digit] + ' ' + number_to_words[modul])
    elif user_input > 99:
        print(number_to_words[remaining_digit] + ' hundred ' + number_to_words[anything_really] + ' ' + number_to_words[modul])
    else: 
        print("That's not a number")
        user_input = int(input("Enter a number to 100! "))

# if statement for if you want to play again
    user_yes_no = input("Would you like to try again? ")
    if user_yes_no == "yes":
        user_input = int(input("Enter a number to 100! "))
        result_of_number(user_input)
    else:
        print("Goodbye!")


# function call
result_of_number(user_input)




'''
Lab 15: Number to Phrase
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10
Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

Version 2
Handle numbers from 100-999.

Version 3 (optional)
Convert a number to roman numerals.

Version 4 (optional)
Convert a time given in hours and minutes to a phrase.

'''