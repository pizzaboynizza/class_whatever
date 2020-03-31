## Let's Play Fraud Dectector! ##

ccn=[]
print('Input 16 digit card number.')
print('Example: 1234 5678 9876 5432')
card=input('CC#  ')
ccn.append(card)
print(ccn)
card=list(map(int,card))

print(card)


chk=len(card)
print(chk) 
chk2=card.pop(-1)
print(card)
print(chk2)
card.reverse()
print(card)

dcd = [card[i]*2 if i % 2 == 0 else card[i] for i in range (len(card))]
print(dcd)

for i in range (len(dcd)):
    if dcd[i] > 9:
        dcd[i]-=9
print(dcd)
total=0
for n in range(len(dcd)):
    total+=dcd[n]
print(total)

secd=total%10
print(secd)

if secd == chk2:
    print('Validated')
if secd != chk2:
    print('Fraud')
