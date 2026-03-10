quiz = [
     {'que': 'Father of computer is : 1) charless 2) alone 3) pascal', 'ans' : '1'},
     {'que' : 'Father of computer science is : 1)charless 2) alone 3) pascal', 'ans' : '2'},
     {'que' : 'RAM is same to ROM : 1) yes 2) no 3) sometime', 'ans' : '2'},
     {'que' : 'Http is related topice to : 1)architecture 2) compiler 3) networking', 'ans' : '3'},
     {'que' : '34+2 = 1) 36 2) 34 3) 38', 'ans' : '1'}
             ]
score = 0
for each in quiz:
     print(each['que'])
     ans = input('Please enter your answer : 1,2,3 : ')
     if ans == each['ans']:
          score +=1 
          print('Correct')   
     else:
          print('False')
    
          
print(f'Your score is {score} out of five')
    