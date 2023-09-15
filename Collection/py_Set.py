'''
List: List is an ordered and changeable collection.Duplicate members are allowed.
Tuple: Tuple is an ordered and immutable collection.Duplicate members are allowed.
Set :Set is an unordered and unindexed collection.There are np duplicate members.
Dictionary: Dictionary is an unordered,mutable and indexs collection.There are no duplicate members.
'''

# Create a set (The set is a dictionary with no values)
this_set={'apple',"banana",'orange'}
print(this_set)
# A set is an unordered,so you cannot determine the order in which items appear

# You cannot access items in a set by referencing an index because the set is unordered and the items do not have index
# But you can use "for" to loop traversal the set or "in" to judge

# Loop traversal
for i in this_set:
    print(i,end=' ')
# judge
print('\n',end='')
print('abc' in this_set)
print('------------------------------')

# Set method:
# Once a set is created,you cannot change  items,but you can add new items

# Use add() method to add  new items to the set---->set.add()
this_set.add('water')
print(this_set)
# Use update() method to add more new items to the set---->set.update()
this_set.update(['aaa','bbb','ccc'])
print(this_set)
# Get the length of a set
print(len(this_set))

# Delete the items
# Use remove() to delete the items,if the items are not exist,error---->set.remove()
this_set.remove('aaa')
print(this_set)
# Use discard() to delete the items,if the items are not exist,no error---->set.discard()
this_set.discard('bbb')
print(this_set)

# Return a copy of the set ---->set.copy()
print('Original set:',this_set,'Original id:',id(this_set))
print('after copy set:',this_set.copy(),'after copy id :',id(this_set.copy()))

# Returns a collection that contains differences between two or more collections---x.difference(y) (only exist in x and not in y)
that_set={'aaa','bbb','ccc'}
print(that_set.difference(this_set))

'''
In addition, there are others, when you need to check, 
you don't have to finish writing here
'''