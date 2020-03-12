# Lab 23: Contact List
# Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. Headers might consist of name, favorite fruit, favorite color. Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents the keys, the text in the other lines represent the values.

# with open('contacts.csv', 'r') as file:
#     lines = file.read().split('\n')
#     print(lines)

# Once you've processed the file, your list of contacts will look something like this...

# contacts = [
#     {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
#     {'name':'sam', 'favorite fruit':'pineapple' ...}
# ]
# Note: There is a csv library in Python that will do much of this for you. It is what you would use normally in a project, but for this lab you need to write all the logic yourself.



with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    contact = []
    # print("lines", lines)



# lines[0] chooses the first element from the list. Each element is seperated is surrounded by quotation marks and is seperated by a comma. 
# .split() surrounds whatever i use as my seperator by quotation mark and adds square brackets. key = lines[0].split(",") is outside the for loop so that i wont have name:name, season:season, favoritecolor:favoritecolor.
key = lines[0].split(",")
# print("key", key)
for i in range(1, len(lines)):
    values = lines[i]
    values = values.split(",")
    # print("values", values)
    my_dict = dict(zip(key, values))
    contact.append(my_dict)
    # print("dictionary", (my_dict))
# print("contact", contact)


print(contact,"this is contact")








# Version 2
# Implement a CRUD REPL

# Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
# Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.


def new_contact():
    list_stuff = list(key)
    user_input2 = [input('what is your name?: '), input('what is your fav season?: '), input('what is yoru fav color?: ')]
    print(user_input2)
    new2 = dict(zip(list_stuff,user_input2))
    contact.append(new2)
    print(new2)

# getting TypeError: string indices must be integers
def find():
    name = input("who are you looking for?: ")
    for element in contact:
        if element['name'] == name:
            print(element)
            print(element['name'])
find()

# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.

# Each element in a list of dictionairies is each dictionairy. 
# x["name"] == user_input01 x represents the dictionaries, ["name"] represents the key; this will give me the value im looking for. For x in contacts represents my list of dictionaries.
user_input01 = input("who are you looking for?: ")
update_name = input("what do you want to update the name to?: ")
for x in contact:
    x["name"] == user_input01
    x["name"] = update_name
print(x)

user_input02 = input("who are you looking for?: "), input("this person would be deleted. ")
for x in contact:
    x["name"] == user_input02
    del x["name"]
print(x)

    


# Version 3
# When REPL loop finishes, write the updated contact info to the CSV file to be saved. I highly recommend saving a backup contacts.csv because you likely won't write it correctly the first time.

with open('contacts.csv', 'w') as file:
    