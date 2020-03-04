with open('contacts copy.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

    contacts = []

    for line in range(len(lines)):
        key_value = lines[0]
        key_value = key_value.split(",")
        row = lines[line]
        row = row.split(",")
        row = dict(zip(key_value, row))
        contacts.append(row)
    print(contacts) #this makes your dict

    def new_contact():
        user_input = [input("What is your name?"),input("Favorote fruit?"), input("Favorite color?")]
        newcontact = dict(zip(key_value, user_input))
        print(newcontact)

    def retrieve_info():

        user_input = input("What is your name?")

        user_input_two = {'Justin': "Pineapple", 'Billy': "Apple", 'James': "Orange", "Pickles": "Peach", "Pinnochio": "Apricot"}

        user_input_three = {"Justin": "Orange", "Billy": "Red", "James": "Blue", "Pickles": "Pink", "Pinnochio": "Green"}

        if user_input in user_input_two:
            print(str(user_input_two[user_input] + (" ") + user_input_three[user_input]))

    def change_info():

        user_input = input("What is the user's name?")

        output = input("What's their favorite fruit?")
        output_two = input("What's their favorite color?")

        fruit = user_input_two = {'Justin': output, 'Billy': output, 'James': output, "Pickles": output, "Pinnochio": output}

        color = user_input_three = {"Justin": output_two, "Billy": output_two, "James": output_two, "Pickles": output_two, "Pinnochio": output_two}

        print(output + (" ") + output_two)

    def remove_user():
        user_input = input("Which user would you like to remove?") 
        del user_input

new_contact()

# def convert_to_list()

# new_contact = {(key_value: user_input), (key_value: user_input), (key_value: user_input)}
# d1.items()
# dict_items([(key_value: user_input), (key_value: user_input), (key_value: user_input)])
# l1 = list(d1.items())
# l1
# [(key_value: user_input), (key_value: user_input), (key_value: user_input)]
# d1.keys()
# dict_keys([key_value, key_value, key_value])
#  l2 = list(d1.keys())
# l2
# [user_input, user_input, user_input]
# l3 = list(d1.values())
# l3
# ['Ravi', 23, 56]

dict_one = contacts.keys()
print(dict_one)

for contact in contacts:
        dict_two= contacts.values()
        row = row.join(",")
        row = lines[line]
        key_value = key_value.join(",")
        key_value = lines[0]
        
        
        
        
        contacts.append(row)
        
        

with open('contacts copy.csv', 'w') as contacts_copy_two:
   contacts_copy_two.close()