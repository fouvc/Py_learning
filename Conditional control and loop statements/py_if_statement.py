'''
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
'''
a=200
b=60
if a>b:
    print('a is greater than b')
elif a==b:
    print('a and b are equal')
else:
    print('b is greater than a')

# If there are only two statements to execute,one for if and one for else,you can put them all on thea same lines
a=200
b=60
print('A') if a>b else print('B')

# Nested if
x=int(input('Enter a number'))
if x%2==0:
    if x%3==0:
        print('The number you enter is divisible by 2 and 3')
    else:
        print('The number you enter is divisible by 2, but not by 3')
else:
    if x%3==0:
        print('The number you enter is divisible by 3, but not by 2')
    else:
        print('The numbers you enter are not divisible by 2 and 3')
#The if statement cannot be empty,
# but if for some reason you wrote an if statement with no content,
# use the pass statement to avoid errors