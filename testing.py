# Python indentation 
name = 'kabwe'

#test1 : this example willl not work because the code is not following the indentation rule's
def call1():
 if name == 'kabwe':
  print('this is the name')
 else:
  print('this is not the name')
call1()


#test2 : this will work because it is following the indetation rules
def call2():
 if name == 'mwaba':
  print('this is the right name')
 else:
  print('this is not the name')

call2()

names = ['mwaba', 'john','happy']
print(names)



list = ['mwaba','john','mary']
print(list)
#accessing items
print(list[1])

if 'mwaba' in list:
 print('mwaba is in ')
else:
 print('mwaba is not here')

 #//
 
list2 = ['johnny','mable','hope']
for x in list2:
 print(x)
