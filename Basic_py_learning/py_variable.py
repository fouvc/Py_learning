'''
Variables do not need to be declared with any specific type,
and their type can even be changed after setting
'''

x=5 # x is of type int
x='adb' # x is now of type str

#str use '' or "" to declare
y='Bill'
# is the same
y="Bill"
print('-----------------------------')


'''
Variables name rules:
1.Variable names must to begin with a letter or underscore character
2.Variable names can't start with a number
3.Variable names are case-sensitive'''

#Assign values to multiple variables
x,y,z='Banana','apple',5
print(x,y,z)

#Assign the same values to multiple variable in a single row
x=y=z='Orange'
print(x,y,z)

#To combine text and variable,Python uses the + character
x='easy'
print('Python is '+x)

#Use the + character to add a variable to another variable
x='Python is '
y='easy'
print(x+y)
print('-----------------------------')


'''Global variables
1.A variable created outside the function are called global variable
2.Global variables can be used by everyone inside and outside the function
3.If you create a variable with the same name inside the function,the variable will be local
and only be used inside the function.Global variable with the same name are left as is and have the original vaule'''

x='awesome'
def function(): # Create a variable with the same name as the global variable inside the function
    x='happy'
    print('Python is '+x)
function()
print('Python is '+x)
print('-----------------------------')


'''keyword:global
If you want to create a global variable inside the function,use the keyword global'''
def function():
    global x    # You use keyword global,so the variable is in global scope
    x='easy'
function()
print('Python is '+x)

'''If you want to change the global variable inside the function,use global keyword'''
x='awesome'
def function():
    global x    #   Change the global variable inside the function
    x='happy'
function()
print('Python is '+x)

