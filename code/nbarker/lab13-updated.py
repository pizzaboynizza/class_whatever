import string
import time
import random

alphabetsoup = "abcdefghijklmnopqrstuvwxyz" #the alphabet!

#now we need a STRING from the user
string_input = input("Please enter a phrase to encode! ") #get input from user, this is a string
print("Encoding:", string_input) #now we will print back the string from the user
string_length = len(string_input) #checks length of string_input
print("The number of characters in your cypher is:", string_length)

string_output = "" #we leave this blank for now, we need some input, bro! eventually this is where the enccrypted string will go

#time to create a FOR loop, I wrote a SWEET IF IF IF IF loop, I saved it, it was brutal!  Anyways, FOR loop time!
'''
for i in range(string_length): #whatever the length of the string, this will go through each character (iterate :-) )
    print(i)   #oh shit this prints numbers?!
'''
for i in range(string_length): #for i in the range of the length of the string  >>>0 1 2 3 etc.
    character = string_input[i] #pulling individual characters from a string, one at a time! we use 'i' so that everytime it loops, it will check every character, clever!
    #print(character) just making sure it separated them
    location_of_character = alphabetsoup.find(character) #this calls the position in the string in integer form. position of the character in the string, THE NUMBER, NOT THE LETTER! 
    #print(location_of_character) #this prints the numbered positions of the characters in the string
    new_location = location_of_character + 13 #Oh man, 26 letters, 25 indexes, hilarious how long I spent down here, but it works now
    if new_location < 26: #if the location or original + 13 > Z, start back at A!
        new_location = new_location #we can always set it equal to itself! a handy trick
    else:
        new_location = (new_location-26) #how we get back at a!! 

    string_output = string_output + alphabetsoup[new_location]

print("Encrypted text: ", string_output)   
    
    #print(new_location) #this prints the numbered NEW LOCATION REMEBER THIS IS IN A FOR LOOP!!!! IT will print differently than you're expecting!
    #>>>
    #>>> for A, B
    #>>>int of original locationA 1
    #>>>int of new location (A+3) 4   
    #>>>int of original locationB 2 
    #>>>int of new locationB(B+3) 5 

