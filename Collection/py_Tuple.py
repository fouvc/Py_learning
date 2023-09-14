'''
List: List is an ordered and changeable collection.Duplicate members are allowed.
Tuple: Tuple is an ordered and immutable collection.Duplicate members are allowed.
Set: Set is an unordered and immutable collection.There are no duplicate members.
Dictionary: Dictionary is an unordered,mutable and indexed collection.There are no duplicate members.
'''

# Create a tuple(It cannot be deleted, updated, or modified)
tup1=('google','runoob',1,2)
print(tup1,type(tup1))

# If the tuple contains only a element ,you need add to a comma after the element,otherwise
# the parentheses is used as operator
tup1=(50)
print(type(tup1))   # is int
tup2=(50,)
print(type(tup2))   # is tuple

# Access tuple
tup=('apple','banana',1,2,3,4)
print(tup[0])
print(tup[0:3],id(tup)) # Return values isn't new tuple
print('---------------------------------')


# Modify tuple
# Although the elements is immutable in the tuple ,we can make concatenated combination of tuple
tup1=(1,2,3,4)
tup2=('apple','banana')
print(tup1+tup2)

# Delete tuple1
# Elements values aren't allowed to be deleted,but we can use the del statement to delete the entire tuple
tup=('apple','banana')
print('Before deletion:',tup)
del tup
#print('After deletion:',tup)   name 'tup' is not defined.
tup=(1,2,3,4,5,6)
print(max(tup))

# Tuple operator
tup1=(1,2,3)
tup2=('apple','banana','orange')
print(len(tup1))
print(tup1+tup2)
print(tup1*2)

# List->Tuple
list=[1,2,3,4,5,6]
print(tuple(list))

# Tuple method
tup=(1,2,3,45,6)
print(tup.count(3))
print(tup.index(45))

# Again,the values in the tuple cannot be changed !