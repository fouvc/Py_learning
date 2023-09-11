'''
List: List is an ordered and changeable collection.Duplicate members are allowed.
Tuple: Tuple is an ordered and immutable collection.Duplicate members are allowed.
Set: Set is an unordered and unindexed collection.There are no duplicate members.
Dictionary: Dictionary is an unordered ,mutable and indexed collection.There are no duplicate members.
'''
from typing import List

# Create a list
lst=['apple','banana','orange']

# You can access list values by referencing the index numbers
print(list[1])  # is banana

# A negative index indicates a starting end ,-1 indicates the last item,-2 indicates the penultimate ,and so on.
print(list[-1])     # is orange
print('----------------------------')

# Truncate characters:Specify the start and end point of the range to specify the index range
#                      The return values will be a new list
thislist=[1,2,3,4,5,6,7,8,9]
print(thislist,id(thislist))        # is [1, 2, 3, 4, 5, 6, 7, 8, 9] 1274920923264
print(thislist[2:5],id(thislist[2:5]))  #is [3, 4, 5] 1274921229824
print(thislist[-4:-1],id(thislist[-4:-1]))  # is [6, 7, 8] 1274921229824

# Change the item values
# To change the values of the specify item,reference the index
thislist[8]=100
print(thislist)     # is [1, 2, 3, 4, 5, 6, 7, 8, 100]
print('-----------------------------------')

# Delete the list element
list=['google','runoob',1977,1996]
print('Original list:',list)
del list[1]
print('After deleting seceond element:',list)

# List script operators
list1=[1,2,3,4]
list2=[5,6,7,8]
print(len(list1))       # is 4
print(list1+list2)      # is [1, 2, 3, 4, 5, 6, 7, 8]
print(list1*2)          # is [1, 2, 3, 4, 1, 2, 3, 4]
print(100 in list1)     # False
for i in list1:
    print(i,end=' ')    # is 1 2 3 4
print('\n',end='')
list3=[list1,list2]
print(list3)

# List comparison
import operator
list1=[1,2]
list2=[2,3]
list3=[2,3]
print(operator.eq(list1,list2))
print(operator.eq(list2,list3))
print('------------------------------')


# List method#
# (Here are all kinds of methods about list)
new_list =[1,2,3,4,5,6,7,8,9,10]
print('Original list :',new_list)
print('Original id :',id(new_list))

# Add an element at the end of the list--->list.append()
new_list.append(100)
print('list.append(100): ',new_list)

# Return a copy of the list---->list.copy()
print('list.copy(): ',new_list.copy(),'\n''the id of copy:',id(new_list.copy()))

# Return the number of elements with specified value---->list.count()
print('list.count(100): ',new_list.count(100))

# Adds a list element (or any iterable element) to the end of the current list--->list.extend()
slst=[200,300]
new_list.extend(slst)
print('list.extend(slst): ',new_list)

# Return the index of the first element with specified value---->list.index()
print('list.index(2): ',new_list.index(2))

# Add an element at the specified location---->list.insert()
new_list.insert(2,66)
print('list.insert(2,66): ',new_list)

# Delete an element at the specified location-----list.pop()
new_list.pop(2)
print('list.pop(2): ',new_list)

# Delete an item with the specified value-------->list.remove()
new_list.remove(100)
print('list.remove(100):',new_list)

# Reverse the order of the list------>list.reverse()
new_list.reverse()
print('list.reverse(): ',new_list)

# Sort the list------->list.sort()
new_list.sort(reverse=False)
print('list.sort(reverse=False): ',new_list)
new_list.sort(reverse=True)
print('list.sort(reverse=True): ',new_list)

# Clear the entire list---->list.clear()
new_list.clear()
print('list.clear(): ',new_list)

'''
In my opinion, if the data in the list is manipulated, 
such as adding, deleting, or sorting, then it needs to be used separately and then printed, 
and if it is copied and the data is not manipulated, it is not required
'''

