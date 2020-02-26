

print("ROT Cipher")

rot = ['a','b','c','d','e','f','g','h','i,','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
user = input("Give me a word: ")

card = list(user)

print("this is list", card)

code = []
# Looping thought each input in the list
for x in card:
    #adding to list with the index as numbers to code from the list
    code.append(rot.index(x))
print("this is number each letter", code)

print("This is store in code", code)

co2 = []
for g in code:
    # This take g in code plus the index by 13 and then % div it by 26 giving it the other rot number
    new = (g + 13)%26
    # add all the letter/number to the list to be printed out
    co2.append(new)


print(co2)

done = []
for x in co2:
    done.append(rot[x])
    
print(done)


# print(other)






















# while x < card:
#     rot.index(card)
#     [(x + 13)%26]
#     print(x)


# x = rot.index(card)
# rip =  [(x + 13)%26]

# print(card)

# # Index is taking the letter in the list and giving it a number
# a = rot.index(card)

# print(a)

# # compre, is take a + 13 and if it over 26 is - 13 with the %
# cip = [(a + 13)%26]

# print(cip)



    


















    
















