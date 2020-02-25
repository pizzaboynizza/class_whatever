'''
Nick Barker
Lab 15
2/21/2020
'''

#I'm definitely not worried about writing functions anymore!

print("Good Morning Welcome to the number writer 5000")

variable = (input("Please enter a number between 1 and 99 no spaces"))

print(variable)

tens = (variable[0])
ones = (variable[1])
words = ones

#this is my practice function, alot of work to make sure you entered the correct number of digits :-)
def funkynum( str ):
    #this should tell you that you have entered too many digits
    # I needed some confidence and wrote a simple function with at least 3 outcomes :-)
    if len(variable) == 3:
        print("please enter a 2 digit number That was 3")
        return
    elif len(variable) == 1:
        print("Broski 2 digits that was one")
        return
    elif len(variable) == 2:
        print((variable) + " great work You have the correct number of digits")
        return

#after separating the variables, I had to convert the numerator to an alpha character
def extractor (ones):
    #prints ones digit as alphastring
    if ones == "1":
        return("one")
    if ones == "2":
        return("two")
    if ones == "3":
        return("three")
    if ones == "4":
        return("four")
    if ones == "5":
        return("five")
    if ones == "6":
        return("six")
    if ones == "7":
        return("seven")
    if ones == "8":
        return("eight")
    if ones == "9":
        return("nine")
    else: ("shibby shibby nah nah")

words = extractor(ones)
print(words)

#this was more difficult than it needed to be.  I imagine writing the same function to extract the 'name' of the number would be the best way to go, then concantenate
def numnamer( str ):
    if tens == '0' and ones == '1':
        print("one")    
        return("one")
    if tens == '0' and ones == '2':
        print("two") 
        return("two")
    if tens == '0' and ones == '3':
        print("three") 
        return("three")
    if tens == '0' and ones == '4':
        print("four") 
        return("four")
    if tens == '0' and ones == '5':
        print("five") 
        return("five")
    if tens == '0' and ones == '6':
        print("six") 
        return("six")
    if tens == '0' and ones == '7':
        print("seven") 
        return("seven")
    if tens == '0' and ones == '8':
        print("eight") 
        return("eight")
    if tens == '0' and ones == '9':
        print("nine") 
        return("nine")
    if tens == '1' and ones == '0':
        print("Ten") 
        return("ten")
    if tens == '1' and ones == '1':
        print("Eleven") 
        return("Eleven")
    if tens == '1' and ones == '2':
        print("Twelve") 
        return("Twelve")
    if tens == '1' and ones == '3':
        print("Thirteen") 
        return("Thirteen")
    if tens == '1' and ones == '4':
        print("Forteen") 
        return("Forteen")
    if tens == '1' and ones == '5':
        print("Fifeteen") 
        return("Fifeteen")
    if tens == '1' and ones == '6':
        print("Sixteen") 
        return("Sixteen")
    if tens == '1' and ones == '7':
        print("Seventeen") 
        return("Seventeen")
    if tens == '1' and ones == '8':
        print("Eighteen") 
        return("Eighteen")
    if tens == '1' and ones == '9':
        print("Nineteen") 
        return("Nineteen")
    
    if tens == '2':
        print("Twenty" + words)
        return("twenty")
    
    if tens == '3':
        print("thirty" + words)
        return("thirty")
    
    if tens == '4':
        print("forty" + words)
        return("forty")
    
    if tens == '5':
        print("fifety" + words)
        return("fifety")
    
    if tens == '6':
        print("sixty" + words)
        return("sixty")
    
    if tens == '7':
        print("seventy" + words)
        return("seventy")
    
    if tens == '8':
        print("eighty" + words)
        return("eighty")
    
    if tens == '9':
        print("ninety" + words)
        return("ninety")
    
    else:
        print("how did you do that?")


funkynum(variable)
words = extractor(ones)
numnamer(variable)
