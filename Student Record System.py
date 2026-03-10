record ={
     
}
def doAll(op):

     if op == 'addnew':
          name = input('Please Enter The Name of the Student You want to add:\n ')
          marks = int(input('Also Enter His Marks: \n'))
          record[name] = marks
          print(f'{name} With Marks {marks} is added..')
     elif op == 'remove':
          name = input('Please Enter the name of the Student You want to remove:\n')
          if record[name]:
              del record[name]
              print(f'{name} removed from the record.')
          else:
              print('The {name} was not found')
     elif op == 'showall':
          for i in record.items():
               print(i)
     elif op == 'seeperson':
          name = input('Please Enter the name of the Student You want to Display:\n')
          if name in record:
              print(record[name])
          else:
               print('This name not fount in the record')
     elif op == 'clearall':
          if record == {}:
               print('Database is already empty')
          else:     
               record.clear()
               print('All data in the record have deleted..')


print('')
operation = '''Operations List:
addnew: for adding new member
remove: for removing a student from the database
showall: for displaying all record
seeperson: for searching a student
clearall: for making database empty'''

print(operation)
while True:
     op = input('Please Enter any opteration You Want To Perform or type exit:\n')
     if op == 'exit':
          break
     doAll(op)
     