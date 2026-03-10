To_do ={}
def perform(op):   

    if op == '1':
        title = (input('Please write your task title :\n'))
        discr = (input('Please input your task description:\n '))
        To_do[title] = discr
        print('Your new task added to the list')
    elif op == '2':
        title = input('Please enter the title of the task you want to mark as complete : ') 
        To_do[title] = 'Completed'
    elif op == '3':
        if To_do !={}:
            for i,j in To_do.items():
                print(i,' \n',j)
                print('*'*15)
        else:
            print('The entire list is empty..')
    elif op == '4':
        title = (input('Please enter the title of the task you want to delete: '))
        if title.upper() in To_do:
            del To_do[title]
            print(f' Task with title {title} have been removed')
        else:
            print('Task not found..')
    else:
        print('invalid operation')


print('please input an operation you want to perfom in your to do list:')
do = '''
1 : adding new task
2 : marking a task as complete
3 : Show all tasks
4 : remove a task from the list
5 : exit from the app
'''
print(do)
while True:
    op = input('Please input the operation number:')
    if op == '5':
        break
    else:
        perform(op)
    