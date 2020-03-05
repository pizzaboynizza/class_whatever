def convert_to_english(num):
    if 100 <= num <=999:
        hundreds_digit = (num//100)
        tens_digit = (num//10)  
        tens_digit_two = tens_digit%10
        ones_digit = (num%10)

        c = ''
        if hundreds_digit == 1:
            c = "one hundred" 
            print(c)

        elif hundreds_digit == 2:
            c = "two hundred"
            print(c)

        elif hundreds_digit == 3:
            c = "three hundred"
            print(c)

        elif hundreds_digit == 4:
            c = "four hundred"
            print(c)

        elif hundreds_digit == 5:
            c = "five hundred"
            print(c)

        elif hundreds_digit == 6:
            c = "six hundred"
            print(c)

        elif hundreds_digit == 7:
            c = "seven hundred"
            print(c)

        elif hundreds_digit == 8:
            c = "eight hundred"
            print(c)

        elif hundreds_digit == 9:
            c = "nine hundred"
            print(c)

        b = ''
        if tens_digit_two == 2:
            b = "twenty"
            print(b)

        elif tens_digit_two == 3:
            b = "thirty"
            print(b)

        elif tens_digit_two == 4:
            b = "forty"
            print(b)

        elif tens_digit_two == 5:
            b = "fifty"
            print(b)

        elif tens_digit_two == 6:
            b = "sixty"
            print(b) 

        elif tens_digit_two == 7:
            b = "seventy"
            print(b)

        elif tens_digit_two == 8:
            b = "eighty"
            print(b) 

        elif tens_digit_two == 9:
            b = "ninety"
            print(b) 

        d = ''

        if ones_digit == 0 and tens_digit_two == 1:
            d = "ten"
            print(d)

        elif ones_digit == 1 and tens_digit_two == 1:
            d = "eleven"
            print(d)

        elif ones_digit == 2 and tens_digit_two == 1:
            d = "twelve"
            print(d)

        elif ones_digit == 3 and tens_digit_two == 1:
            d = "thirteen"
            print(d)

        elif ones_digit == 4 and tens_digit_two == 1:
            d = "fourteen"
            print(d)

        elif ones_digit == 5 and tens_digit_two == 1:
            d = "fifteen"
            print(d)

        elif ones_digit == 6 and tens_digit_two == 1:
            d = "sixteen"
            print(d)

        elif ones_digit == 7 and tens_digit_two == 1:
            d = "seventeen"
            print(d)

        elif ones_digit == 8 and tens_digit_two == 1:
            d = "eighteen"
            print(d)

        elif ones_digit == 9 and tens_digit_two == 1:
            d = "nineteen"
            print(d)

        a = ''
        if ones_digit == 1:
            a = "one"
            print(a)

        elif ones_digit == 2:
            a = "two"
            print(a)

        elif ones_digit == 3:
            a = "three"
            print(a)

        elif ones_digit == 4:
            a = "four"
            print(a)

        elif ones_digit == 5:
            a = "five"
            print(a)

        elif ones_digit == 6:
            a = "six"
            print(a)

        elif ones_digit == 7:
            a = "seven"
            print(a)

        elif ones_digit == 8:
            a = "eight"
            print(a)

        elif ones_digit == 9:
            a = "nine"
            print(a)

        elif ones_digit == 0:
            print(" ")

convert_to_english(309)