# In Python,string literals are enclosed in single or double quotes
# 'hello world'="hello world"
# You can use three quotes(single or double) marks to aissgn a multiline string to a variable

a='''Python is not easy,
    nothing is easy'''
print(a)
print('----------------------------------')


# Get the character at position 1(Remember that the position of the first character is 0)
b='hello world'
print(b[1])

# Truncate:
# Specifies the start and end indexs(not included),separated by colons,to return part of a string
b='hello,world'
print(b[2:5])   # start index:2     end index:5(not included)


# Index from the front:0,1,2,3....n-1
# Index form the behind:-n,-n-1....-2,-1
# Use negative index to crop from the end of the string
b='hello,world!'
print(b[-5:-2])
print('--------------------------------')

# Python string updates
# You can intercept part of the string and concatenate it other fields
var='hello,world'
print(var[:6]+'Python')
print('-------------------------------')

#Python eascape characters
print("line1\
...line2\
...line3...")   # is line1...line2...line3...

print("\\")     # is \

print('\'')     # is '

print("\"")     # is "

print("Hello \b World!")    # (backspace)is Hello World!

print("\000")       # is NULL

print("a\nb")       # line break is a
                    #               b

print("Hello \v World!")    # Portrait tabs  is Hello
                            #                               World!

print("Hello \t World!")    # Horizontal tabs Hello 	 World!

print('google\rruby')         # is ruby

print('hello \f world')
print('----------------------------------')

#Python string operators
a='hello'
b='world'
# + :
print(a+b)  # is helloworld
# * :
print(a*2)  # is hellohello
# [] :
print(a[1]) # is e
# [x:y] :
print(a[2:3])   # is l
# in :
print('h' in a) # is True
# not in :
print('h'not in a)# is False
# r :
print(r'\n')    # is \n
print('-----------------------------')

#Python format
print('My name is %s and I am %d years old !'%('fouvc',20))
# is the same
print('My name is {} and I am {} years old !'.format('fouvc',20))
# following is the same
print('My name is {1} and I am {0} years old !'.format(20,'fouvc'))
#and
name='fouvc'
age=20
print(f'My name is {name} and I am {age} years old !')
print('-----------------------------------')

#Python string method
x='**Hello,World!**'
# Get string length
print(len(x))
# Remove specific characters from beginning and end
print(x.strip('*'))
# Return a lowercase string
print(x.lower())
# Return an uppercase string
print(x.upper())
# Replace the string with another string
print(x.replace('World','Python'))
# Splits the string into substrings when an instance of the delimiter is found  ->split(str,nums)   nums:split nums
print(x.split(','))





