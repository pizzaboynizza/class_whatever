with open('contacts.csv', 'r') as file:
    # lines = file.read().split('\n')
    data_csv = file.read()
    csv_lines = data_csv.split('\n')
    data_csv = []
    for line in csv_lines:
        data_csv.append(line.split(','))

    keys = data_csv[0]

    data = [dict(zip(keys, row)) for row in data_csv[1::]]

    contacts = []

    for line in range(len(csv_lines)):
        key_value = csv_lines[0]
        key_value = key_value.split(",")
        row = csv_lines[line]
        row = row.split(",")
        row = dict(zip(key_value, row))
        contacts.append(row)
    print(contacts) #this makes your dict

    def export():
        global contacts
        list_w = []
        contacts[0].values()
        list(contacts[0].values()) 
        list(contacts[0].values())
        contacts[0].keys()
        ",".join(contacts[0].keys())
        ",".join(contacts[0].values())


        for contact in range(len(contacts)):
            list_w.append(",".join(contacts[contact].values()))
            '\n'.join(list_w)
            # row = lines[line]
            # key_value = key_value.join(",")
            # key_value = lines[0]
            # contacts.append(row)
            
            

        with open('contacts.csv', 'w') as contacts:
            contacts.write("\n".join(list_w))


    def create_contact():
        user_input = [input("What is your name?"),input("Favorite fruit?"), input("Favorite color?")]
        newcontact = dict(zip(key_value, user_input))
        contacts.append(newcontact)

    def read_contact():

        user_input = input("Which contact?")
        for contact in contacts:
            if contact['name'] == user_input:
                print(contact)
       
    def update_contact():

        user_input = input("Which contact?")
        attribute = input("What do you want to update?")
        user_input_two = input("With what?")
        for contact in contacts:
            if contact['name'] == user_input:
                print(contact)
                if attribute in contact:     
                    contact[attribute] = user_input_two
                    return contact
        print(contact)

    def delete_contact():

        user_input = input("Which contact?")
        for contact in contacts:
            if contact['name'] == user_input:
             contacts.remove(contact)

while True:
    user_input = input("create, read, update, delete, quit?")
    if user_input == 'quit':
        print("done")
        export()
        break
    elif user_input == 'create':
        create_contact()
    elif user_input == 'read':
        read_contact()
    elif user_input == 'update':
        update_contact()
    elif user_input == 'delete':
        delete_contact()

    