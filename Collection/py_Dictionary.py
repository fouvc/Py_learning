'''
List: List is an ordered and changeable collection.Duplicate members are allowed.
Tuple: Tuple is an ordered and immutable collection.Duplicate members are allowed.
Set :Set is an unordered and unindexs collection.There are no duplicate members.
Dictionary: Dictionary is an unordered ,mutable and indexs collection.There are no duplicate members.
'''


# Create a dictionary  (key=>value)
d={'key1':1,'key2':2,'key3':3}
print('d:',d,'\n''length:',len(d),'\n''id:',id(d))

# Access the values in the dictionary.Put the appropriate key in square brackets
print('d[key1]:',d['key1'])
print('d[key2]:',d['key2'])
# is the same
print('d[key1:',d.get('key1'))

# Modify the dictionary

# Add:
d['key5']=5
print(d)            # is {'key1': 1, 'key2': 2, 'key3': 3, 'key5': 5}
# Update
d['key1']=100
print(d)            # is {'key1': 100, 'key2': 2, 'key3': 3, 'key5': 5}
# Delete
del d['key1']
print(d)            # is {'key2': 2, 'key3': 3, 'key5': 5}
# Empty
d.clear()
print(d)            # is {}
# Delete entire dictionary
del d
#print(d)             is name 'd' is not defined
print('------------------------------------------')


''' The characteristics of the key:
 The keys must be unique,but the values do not.
 The keys must be immutable,such as strings , numbers and tuple,but the values can take any data type.
 The same key is not allowed to appear twice.If the same key is assigned at creation time,the later value will be remembered.
'''

#dic1={'name':'jack','age':20,'name':'Tom'}
#print(dic1['name'])     # is Tom


# Dictionary methods:
dic={'apple':1,'banana':2,'orange':3}
print('Original the dictionary :',dic)
print('Original id :',id(dic))

# Return a copy of the dictionary--->dict.copy()
print('After copying :',dic.copy())
print('After copying id :',id(dic.copy()))

# Return a dictionary of specified the key and value----dict.fromkeys()
print(dic.fromkeys('abcd',0))

# Return a specified key---->dict.get()
print(dic.get('apple'))

# Return a list of tuples that certain each key-value pair---->dict.items()
print(dic.items())

# Return a list of dictionary keys---->dict.keys()
print(dic.keys())

# Delete an element that owns the specified key--->dict.pop()
dic.pop('apple')
print(dic)

# Delete the last inserted key-value pair---->dict.popitem()
dic.popitem()
print(dic)

# Return the value of the specified key,if the key does not exist,the key of the specified value is inserted--->dict.setdefault()
print(dic.setdefault('apple',0))
print(dic)

# Updates the dictionary with specified the key and value---->dict.update()
dic.update({'orange':1})
print(dic)

# Return a list of dictionary values---->dict.values()
print(dic.values())

# Delete all elements in the dictionary
dic.clear()
print(dic)

'''Similarly, operating on elements 
in a dictionary requires a separate operation 
on the dictionary'''