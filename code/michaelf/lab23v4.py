with open('contacts.csv') as file:
    lines = file.read().split('\n')

contacts = []

first_key,last_key,email_key = lines[0].split(',')

for line in lines:
    first_name,last_name,email = line.split(',')
    contact = {first_key : first_name, last_key : last_name,email_key : email}
    contacts.append(contact)

def new_contact(first_name,last_name,email):
    contact = {first_key : first_name, last_key : last_name,email_key : email}
    contacts.append(contact)

def retrieve_contact(name):
    for contact in contacts:
        if name == contact.get('first_name') or name == contact.get('last_name'):
            result = list(contact.values())
            print(result)

def update_contact(name, detail, value):
    for contact in contacts:
        if name == contact.get('first_name') or name == contact.get('last_name'):
            contact[detail] = value

def delete_contact(name):
    for contact in contacts:
        if name == contact.get('first_name') or name == contact.get('last_name'):
                contacts.remove(contact)

while True:
    user_choice = input("1. add contact\n2. retrieve contact\n3. update contact\n4. delete contact\n5. quit\n>>> ")

    if user_choice == "1":
        
        first_name = input('first name: ').capitalize()
        last_name = input('last name: ').capitalize()
        email = input('email: ').lower()
        new_contact(first_name,last_name,email)
        print(contacts)

    if user_choice == "2":
        name = input("first or last name: ").capitalize()
        retrieve_contact(name)

    if user_choice == "3":
        name = input("first or last name: ").capitalize()
        retrieve_contact(name)
        details = list(contact.keys())
        detail = input(f"which detail would you like to change?\n{details}\n>>>  ")
        value = input(f"input new {detail}: ")

        update_contact(name, detail, value)
        print(contacts)

    if user_choice == "4":
        name = input("first or last name: ").capitalize()
        retrieve_contact(name)
        confirm = input(f"Are you sure you want to remove {name}?\n1.yes\n2. no\n>>> ")
        if confirm == "1":
            delete_contact(name)
        print(contacts)
    if user_choice == "5":
        break
# print(contacts)
# print(contacts[0])
keys = list(contacts[0].keys())
line0 = ''
for i in range(0, len(keys)-1):
    line0 += keys[i]+','
line0 += keys[-1]


for i in range(1,len(contacts)):
    values = list(contacts[i].values())
    line = ''
    for i in range(0, len(contact)-1):
        line += values[i]+','
    line += values[-1]
    print(line)

with open('contacts.csv', 'w') as contact_csv:
    contact_csv.write(line0)
    for i in range(1,len(contacts)):
        values = list(contacts[i].values())
        line = ''
        for i in range(0, len(contact)-1):
            line += values[i]+','
        line += values[-1]
        contact_csv.write('\n' + line)