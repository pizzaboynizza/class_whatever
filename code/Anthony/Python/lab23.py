# buidling a program to mange a list of contacts
# \n for new line/row

'''name,age,gender,race,nationality
Anthony,37,ale,black,US
Anita,24,female,white,Nigeria
Alma,22,female,white,Nigeria
Alex,55,male,black,UK
Andrew,23,male,indian,Ghana
Justin,50,male,white,France
Obama,60,male,black,Canada
Michelle,60,female,black,Grenada
Jiu,22,female,asian,China
Sin,45,male,asian,Japan'''




with open('contacts.csv', 'r') as file:
    lines = file.read()
    # print(lines)
lines = lines.split( '\n') #spliting into a list of lines
# print(lines)

keys = lines[0].split(',')
# print(keys)

# values = lines[1].split(',')
# print(values)
# print(keys,values)
# print(keys)

contact_dict= []
for i in lines[1:len(lines)]: # from the second(value list)item in lines to the lenght of lines
    values = i.split(',')
    dict_list = dict(zip(keys, values)) #makes the dictionary
    contact_dict.append(dict_list) #puts the dictionary into a list called contact_dict
# print(f" THIS IS A LIST OF FULL CONTACT IN DICT: {contact_dict}")
#TAKE IN CONTACT INFO


'''Version 2
Implement a CRUD REPL

Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.'''



'''Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.'''

attributes = []
def add_new():
    while True:
        user_input = input("Enter user attributes name,age,gender,race,nationality or done: ")
        if user_input == 'done':
            break
        attributes.append(user_input)
        # contact_dict.update(contact_dict:attributes)
    new_contacts = dict(zip(keys,attributes))
    contact_dict.append(new_contacts)
    return contact_dict
print("CREATE:" )
print(add_new())
#                  OR OR BELOW!!!!!!!!!!!!!!!!!!!
# new_values = [input('name: '), input('age: '),input('gender: '),input('race: '),input('nationality: ')]
# new_values2 = dict(zip(keys,new_values))
# contact_dict.append(new_values2)
# print(contact_dict)



def retrieve_contact():
    user = input("Enter name: ")
    for i in contact_dict:
        if i['name'] == user:
            return i
print("RERTRIEVE:")
print(retrieve_contact())



def update_record():  #VERSION ONE
    contact = retrieve_contact() #USES VALUES FROM RETRIEVE CONTACT and aks for user's name in retrieve
    user_input = input("Enter key(attribute) to change or done") #then asks for what what key to change
    new_value = input("Enter new value") #and then what value in that keey to change to
    contact[user_input] = new_value #puts the new value into the key for the list(contact)
print("UPDATE")
print(update_record())


#OR RUN  WITHOUT USING THE RECORD UPDATE VALUE 
    

# def record_update(): #VERSION 2
#     name_search = input("Enter name to search")
#     key_input = input("Enter values\s key(attribute)to change")
#     new_value = input("Enter the new value of the key seeached ")
#     for i in range (len(contact_dict)): # TAKENOTE THAT I CANT JUST USE SAME METHOD AS VERSION 1. I HAVE TO USE A LOOP TO LOOK THROUGH ALL THE LIST COS ITS IN A LIST. SO THE LOOP HERE
#         contact_dict[i][key_input] = new_value
#     print(contact_dict)
# record_update()

        #THIS IS TO DELETE
def delete_record():
    user = input("Enter name to delete: ")
    for i in range(len(contact_dict)):
        if contact_dict[i]['name'] == user:
            del contact_dict[i]
            
            return contact_dict
print(delete_record())

# VERSION 3

while True:
    user_input = input("(c)reate, (r)ead, (u)pdate, (d)elete, (q)uit? ")
    if user_input == 'q':
        break
    elif user_input == 'c':
        add_new()
    elif user_input == 'r':
        retrieve_contact()
    elif user_input == 'u':
        update_record()
    elif user_input == 'd':
        delete_record()


with open("contacts.csv", 'w') as file:
    key_value_list = []
    new_join = []
    punctuation_join = []
    new_contact_dict = []

    key_value_list.append(list(contact_dict[0].keys()))

    for x in contact_dict:
        key_value_list.append(list(x.values()))

    for puncts in key_value_list:
        punctuation_join = ','.join(puncts)
        new_join.append(punctuation_join)

    new_contact_dict = '\n'.join(new_join)
    print(new_contact_dict)

    file.write(new_contact_dict)
