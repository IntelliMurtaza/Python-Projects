name = input('Enter your name:')
num = input('Enter your contact no:')
email = input('Enter your email:')
contact = {name: {"phone": num, 'email': email}}
ope = input('Please input an operation add, search, delete, display, exit :')
while True:
    if ope == 'add':
        print("Please enter name, no. and email:")
        name = input('Name:')
        num = input('Number:')
        email = input('Email:')
        contact[name] = {'phone': num, 'Email': email}
    elif ope == 'search':
        name = input('Please enter a name to search for:')
        print(contact.get(name))
    elif ope == 'delete':
        name = input('Please enter a name to delete:')
        per = contact.pop(name)
        print(f'{per} has been removed.')
    elif ope == 'display':
        print(contact.items())
    elif ope == 'exit':
        print('We are exit contact app.')
        break
    ope = input('Please input an operation name:')
print('You are out of the app.')    
