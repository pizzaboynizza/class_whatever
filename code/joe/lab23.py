# Lab 23
# Author : Joe

def printContact(con, key): #Print a single contact
    print(f"[{key[0]}]: {con[key[0]]}")
    for i in range(1, len(key)):
        print(f"\t[{key[i]}]: {con.get(key[i], '')}", end="," if i < len(key) - 1 else "\n")

def find(contacts, name): #Find and return a contact within a list of contacts
    for item in contacts:
        if item["name"] == name:
            return item
    return None


filename = "data/contacts.csv"

# Open file and get contacts
with open(filename, "r") as file:
    lines = file.read().split("\n")

keys = lines.pop(0).split(",") #The list of attributes
contacts = [] #The list of contacts

while len(lines) > 0:
    temp = lines.pop(0).split(",")
    contact = dict()
    for i in range(min(len(keys), len(temp))):
        contact[keys[i]] = temp[i]
    contacts.append(contact)


# CRUD REPL loop (Version 2)
print("\nWelcome to Contact List!")
print("(C)reate, (R)etrieve, (U)pdate, (D)elete, (S)how all, (N)ew Attribute, (A)bolish Attribute, (M)ass Update, or (Q)uit\n")
user_in = ""

while True:
    user_in = input("What would you like to do? ")

    if user_in == "": #Prevent index errors
        print("Invalid command, please try again.\n")

    #Create
    elif user_in[0].lower() == "c":
        add = dict()
        for i in range(len(keys)):
            temp = input(f"Enter {keys[i]}: ")
            add[keys[i]] = temp
        contacts.append(add)
        print("Contact added!\n")
    
    #Retrieve
    elif user_in[0].lower() == "r":
        to_get = input("Enter name of contact you want to retrieve: ")
        to_get = find(contacts, to_get)
        if to_get is None: #Exit if can't find contact
            print("Could not find that contact.\n")
            continue
        printContact(to_get, keys)
        print("")

    #Update
    elif user_in[0].lower() == "u":
        to_edit = input("Enter name of contact you want to update: ") #Find contact to update
        to_edit = find(contacts, to_edit)
        if to_edit is None: #Exit if can't find contact
            print("Could not find that contact.\n")
            continue
        edit_attr = input("Which attribute would you like to edit: ")
        if edit_attr not in keys:
            print("Invalid attribute.\n")
            continue
        to_edit[edit_attr] = input(f"Enter new value for {edit_attr}: ")
        print("Contact updated!\n")
    
    #Delete
    elif user_in[0].lower() == "d":
        to_del = input("Enter name of contact to delete: ")
        to_del = find(contacts, to_del)
        if to_del is None: #Exit if can't find contact
            print("Could not find that contact.\n")
            continue
        contacts.remove(to_del)
        print("Contact deleted!\n")

    #Show all
    elif user_in[0].lower() == "s":
        for item in contacts:
            printContact(item, keys)
        print("")
    
    #Quit
    elif user_in[0].lower() == "q":
        print("Goodbye!")
        break
    
    #New Attribute
    elif user_in[0].lower() == "n":
        new_attr = input("Enter name of new attribute: ").lower()
        if new_attr in keys:
            print("That attribute already exists!\n")
            continue
        keys.append(new_attr)
        print("Attribute added!\n")

    #Abolish (Remove) Attribute
    elif user_in[0].lower() == "a":
        del_attr = input("Enter name of attribute to abolish: ").lower()
        if del_attr == "name":
            print("Cannot remove the 'name' attribute!\n")
            continue
        elif del_attr not in keys:
            print("That attribute does not exist!\n")
            continue
        keys.remove(del_attr)
        print("Attribute removed!\n")

    #Mass Update (update one attribute for every contact)
    elif user_in[0].lower() == "m":
        to_edit = input("Enter attribute to update: ")
        if to_edit not in keys:
            print("That attribute does not exist!\n")
            continue
        for con in contacts:
            con[to_edit] = input(f"Enter {to_edit} for {con['name']} (previously '{con.get(to_edit, '')}'): ")
        print("Contacts updated!\n")

    else:
        print("Invalid command, please try again.\n")


# Save changes to file (Version 3)
to_save = ""

for i in range(len(keys)): #Add keys
    to_save += keys[i]
    if i < len(keys) - 1:
        to_save += ","
to_save += "\n"

for con in contacts: #Add contacts
    for i in range(len(keys)):
        to_save += con.get(keys[i], "")
        if i < len(keys) - 1:
            to_save += ","
    to_save += "\n"

to_save = to_save.strip() #Get rid of an extra "\n" at the end

with open(filename, "w") as file:
    file.write(to_save)