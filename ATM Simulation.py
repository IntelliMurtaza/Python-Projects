print('That is Your ATM machine...')
print('-_'*20)
account = {}
def atm(op):
     if op==1:
          name = input('Enter Your name To register : ')
          password = input('Enter password : ')
          deposit = int(input('Please Enter Deposit some money : '))
          account[name] = [password, deposit]
          print(f'You have been registerd with name {name}, password {password} and amount {deposit}')
     elif op==2:
          name = input('Enter your name to login : ')
          password = input('Enter password : ')
          if name in account and password==account[name][0]:
               deposit = int(input('Enter amount to deposit : '))
               account[name][1]=account[name][1]+deposit
               print(f'Your new balance is {account[name][1]} ')
          else:
               print('You are not registerd or incorrect password. please register or try again ')
     elif op==3:
          name = input('Enter your name to login : ')
          password = input('Enter password : ')
          if name in account and password==account[name][0]:
               withdraw = int(input('Enter amount to withdraw : '))
               if withdraw<account[name][1]:
                    account[name][1]=account[name][1]-withdraw
                    print(f'Your new balance is {account[name][1]} ')
               else:
                    print(f'Your entered amount is greater than your current balance {account[name][1]} please input less.')
          else:
               print('You are not registerd or incorrect password. please register or try again ')
     elif op==4:
          name = input('Enter your name to login : ')
          password = input('Enter password : ')
          if name in account and password==account[name][0]:
               print(f'{name} balance is {account[name][1]}')
          else:          
               print('You are not registerd or incorrect password. please register or try again ')
     else:
          print('Invalide Operation.')

oper = '''
1 : Create Accout
2 : Deposite
3 : Withdraw
4 : Check balance
5 : Exit
'''
print('Press or Enter Operation Number : \n', oper)
while True:
     op = int(input('Press 1,2,3,4 or 5 Accordingly : '))
     if op==5:
          print('Thanks You! Lefting Bank ...')
          break
     else:
          atm(op)
