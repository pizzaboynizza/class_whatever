##  Gaming Companion List ##

from pprint import pprint

players=[]

with open('contactinfo.csv','r') as csv:
    lines=csv.read().split('\n')

top = lines[0]
top = top.split(',')

for i in range(1, len(lines)):
    contacts = lines[i]
    contacts = contacts.split(',')
    contacts = dict(zip(top, contacts))
    players.append(contacts)

# for i, player in enumerate(players, 1):
#     print(i, player)   



# #I wanna make this pretty and nerdy
print('****<(^w^)>*******+*+*+*+*+(>^-^)> GAMING CONTACTS <(^-^<)*+*+*+*+*+********<(^w^)>****')
while True:
    print('[1] VIEW ALL    [2] SEARCH    [3] ADD    [3]UPDATE    [4]DELETE    [0] FINISH AND CLOSE')
    call=input('>>>>>>'  )

    #Searches for an entry
    if call == '1':
        for i, player in enumerate(players, 1):
            print(i, player)
    #Add new names to the list
    elif call == '2':
        keyline=print(f'{top}'  + 'ALL' +' '+ 'NONE')
        entry=input('Input Query:  ').lower()
        if entry == 'ALL':
            for i, player in enumerate(players, 1):
                print(i, player)
        elif entry == 'NONE':
            print('No Search Paramerters Given')
        para = []
        # for contact in data:
        #     if contact[entry] == keyline:
                #print results here
# Update Entry Information
    if call == '3':
        new_contact = {}
        for key in top:
            new_contact[key]=input(f'Input new contact: {key} ')
#Delete Contact
    if call == '4':
        remove = {}
        
#Save Contact List and Terminate Program
    if call == '0':
        print('Thank You!  Goodbye!')
    else:
        print('Invalid Entry')