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

with open('contacts copy.csv', 'w') as contacts_copy_two:
    contacts_copy_two.write('contacts copy.csv'