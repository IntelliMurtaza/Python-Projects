book = {}
print('Your Exciting contact book \n', '*'*20)
def perform(op):
     if op=='1':
          name = input('Please Enter the name : ')
          number = input('Please Enter Phone Number : ')
          email = input('Enter Email : ')
          book[name] = [number, email]    
     elif op=='2':
          name = input('Please Enter the name you want to update : ') #second-name for updating name update()
          if name in book:
               number = input('Change number : ') #book.update(name: )
               email = input('Change Email : ')
               book[name] = [number, email]
               print(f'{name} with Number :  {number} and Email : {email} has been succesfully Changed.')
          else:
               print('The person not found ')
     elif op=='3':
          name = input('Please Enter the name to delete : ')
          if name in book:
               del book[name]
               print(f'{name} has been succesfully deleted.')
          else: 
               print(f'{name} not exist in the contacts..')
     elif op=='4':
          name = input('Please Enter name to search : ')
          if name in book:
               print(name, ' : ', book[name][0], book[name][1])
          else:
               print(f'{name} not found..')
     elif op=='5':
          if book:
               for i,j in book.items():
                    print(i,' : ', j[0], j[1])
          else:
               print('Contact is already empty...')

op_list =  '''
Please enter your operation :
1 : for adding new one
2 : for updating contact
3 : for deleting contact
4 : for searching a contact
5 : for showing all contact
6 : for exiting the 
'''
print(op_list)
while True:
     op = input('Please Enter The Operation Number You Want To Do : ')
     if op=='6':
          print('You are exiting now.. Thanks you')
          break
     else:
          perform(op)
