#This app will check wahtever The is even or odd and prime no or not
a=int(input('Please Enter a Number: '))
b=False
if a%2==0:
    print('The number is even')
else:
    print('The number is Odd')
if a<=1:
    print('The number is not Prime')
else:
    for i in range(2, a):
        if a%i==0:
            b=True
            break
if b:
    print('and not prime')
else:
    print('and also prime')
