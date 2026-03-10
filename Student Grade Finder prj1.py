name = input('Please enter Your Name:')
sub1 = float(input('Enter your first subject marks:'))
sub2 = float(input('Second subject marks:'))
sub3 = float(input('Third subject marks:'))
all = [sub1, sub2, sub3]
results = {name: all}
print(results)
sum = sub1+sub2+sub3
ave = sum/3
print(f'Sum is {sum}')
print(f'Average is {(sum)/3}')
if ave > 80:
    grade = 'A'
elif ave > 60:
    grade = "B"
elif ave > 40:
    grade = 'C'
else:
    grade = 'Fail'
print(f'Your grade is {grade}')
