


card = input("Enter a card number: ")
# spilt a input list, make it so pop will pop out a number
# list put it in to list, map put inside of list and card is the variabel to use. 
card = list(map(int, card))
print(card)

g = card.pop(-1)
print(g)


card.reverse()

# i is index %(moudles is every 2 number) else do nothing with index. enmuetare is giving index to card
double = [x * 2 if i%2==0 else x for i, x in enumerate(card)]
print(double) 

# If number is great then 9 subtrack it - else leave it alone 
nine = [n - 9 if n > 9 else n for n in double]
print(nine)

a = sum(nine)
print(a)

h = nine.pop(1)

print(h)













# cut = slice(15,16)
# print(card[cut])



# change = (list(reversed(card)))
# print(change) 
