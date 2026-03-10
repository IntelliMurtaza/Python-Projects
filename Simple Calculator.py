print('that is your simple calculator')
#that is getting input
a=float(input('Eenter Your First Number: '))
b=float(input('Enter Your Second number: '))

# Below is the program logic
while True:
    op=input('Enter An Operation Opterator(/,*,+,-,%): ')
    if op=='+':
        print(f'The Addition of {a} and {b} is Equal To :\n {a+b}')
        break
    elif op=='/':
        print(f'The Division of {a} and {b} is Equal To :\n {a/b}')
        break
    elif op=='*':
        print(f'The Multiplication of {a} and {b} is Equal To :\n {a*b}')
        break
    elif op=='-':
        print(f'The Subtraction of {a} and {b} is Equal To :\n {a-b}')
        break
    elif op=='%':
        print(f'The Modulas of {a} and {b} is Equal To :\n {a%b}')
        break
    else:
        print('You Entered the wrong operator. Please retry \n')
        continue