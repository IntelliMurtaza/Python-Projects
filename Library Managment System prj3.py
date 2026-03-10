books = []
while True:
    ope = input("Please input an operation name show, add, borrow, return: ")
    if ope == 'show':
        for book in books:
            print(book) 
    elif ope == 'borrow':
        name = input("please input the name of book you want to borrow: ")
        if name:
            books.remove(name)
            print(f'{name} has been borrowed')
        else:
            print(f"{name} is not available in the library")             
    elif ope == 'add':
        name = input("Please enter the name of book you want to add: ")
        books.append(name)
        print(f'{name} is added to library')
    elif ope == 'return':
        name = input("Please enter the name of book you want to return: ")
        books.append(name)
        print(f'{name} is returned to library')
    elif ope == 'out':
        print('You are going out of the library. thanks you')
        break
    else:
        print('Wrong Input, please input the correct one')