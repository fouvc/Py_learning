"""
Loop statements in python only have for and while
There is no do...while loop in python
"""

# Using a while loop,we can execute a set of statements as long as the condition is true
"""
while <condition>:
      <statement...>
"""
# While loop is used to calculate the sum of 1 to 100
sum=0
x=1
while x<=100:
    sum+=x
    x+=1
print('The sum of 1 to 100:',sum)

# Set the condition to always is true--->infinite loop
"""var=1
while var==1:
    print('Infinite !')
print('Good bye !')
"""

# If the conditional statement following while is false,the statement block of else is executed
count=0
while count<=5:
    print(count,'<',5)
    count+=1
else:
    print(count,'>',5)

# Similar to the syntax of the if statement,
# if you have only one statement in the body of your while loop,
# you can write that statement on the same line as the while


# For loop can traverse any iterate objects,such as a list or a string
"""
for <variable> in <sequence>:
    <statement>
else:
    <statement>"""

color=['red','blue','green','white']
for i in color:
    print(i,end=' ')
print('\n',end='')      # For line breaks

words='abcdefg'
for i in words:
    print(i,end=' ')
print('\n',end='')

# Print the numbers from 1 to 5
for i in range(1,6):
    print(i,end=' ')
print('\n',end='')

"""
After traversing the sequence,
if a break statement is encountered during the loop,
the loop is interrupted and a else statement is not executed
"""

for i in range(6):
    print(i,end=' ')
else:
    print("FINISHED !")

# A break statement is encountered during the loop
for i in color:
    if i =='green':
        print('BREAK !')
        break
    print(i)
else:
    print('FINISHED !')
print('-------------------------------')

# If you need to iterate through a sequence of numbers,
# you can use the built-in range() function. It generates the series--->range(start,stop,step) (stop does not include)

# range(x)---> 0~x-1
for x in range(6):
    print(x,end=' ')
print('\n',end='')

# range(x,y)---> x~y-1
for x in range(1,10):
    print(x,end=' ')
print('\n',end='')

# range(x,y,z)---> x~y-1(difference z)
for x in range(1,10,4):
    print(x,end=' ')
print('\n',end='')

for x in range(-10,-100,-30):
    print(x,end=' ')
print('\n',end='')

# Create a list by range()
a=list(range(6))
print(a)


"""
BREAK:
The break statement can jump out of the loop body of for and while. 
If you terminate from a for or while loop, any corresponding loop else blocks will not be executed.

CONTINUE:
The continue statement is used to tell Python to skip the remaining statements 
in the current loop block and continue with the next loop.

PASS:
pass is an empty statement to maintain the integrity of the program structure.
pass does nothing and is generally used as a placeholder statement.
"""

