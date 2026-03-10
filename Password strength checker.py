password=input('Please Enter Your Password: ')
upch, loch, spch, digit = 0, 0, 0, 0
while len(password)<8:
        password=input('The Password must be atleast 8 characters, renter please: ')
for i in range(0, len(password)):
        if password[i].isupper():
                upch+=1
        elif password[i].islower():
                loch+=1
        elif password[i].isdigit():
                digit+=1
        else:
              spch+=1
if upch!=0 and loch!=0 and digit!=0 and spch!=0:
        print('Your password strength is strong')
elif upch>0 and loch>0 or digit>0 and spch>0 or loch>0 and digit>0 or upch>0 and spch>0 or upch>0 and digit>0 or loch>0 and spch>0:
        print('Your password strength is medium')
else:
        print('Your password is weak') 
if upch==0:
        print('You must need an upper case character')
if loch==0:
        print('You must need an lower case character')
if digit==0:
        print('You must need a digit')
if spch==0:
        print('You need at least one special character.')