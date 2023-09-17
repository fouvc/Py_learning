# You can build from one data series to another new data series

"""
List_derivation:
[expression for variable in list]
or
[expression for variable in list if condition]
"""

lst=[i*i for i in range(1,6)]
print(lst)
print([i**3 for i in range(1,6)])
# or
name=['Bob','Jack','Sharks','Mary','Tom']
new_name=[name.upper() for name in name if len(name)<=3]
print(new_name)
print('------------------------')

"""
Dictionary derivation:
{key_expr:value_expr for value in collection}
or
{key_expr:value_expr for value in collection if condition}
"""

lst=['C','C++','Python','Java']
dic={lst[x]:x for x in range(len(lst))}
print(dic)
# or
dic={lst[x]:x for x in range(len(lst)) if len(lst[x])>2}
print(dic)
print('-----------------------')

"""
Set derivation:
{expr for value in sequence}
or
{expr for value in sequence if condition}
"""

st={x for x in 'apple'}
print(st)
# or
st={x*2 for x in range(6) if x<3}
print(st)
print('-------------------------')

"""
Tuple derivation:
(expr for value in sequence)
or
(expr for value in sequence if condition)
"""

tpe=(x*2 for x in range(6))
# The returned result is a generator object
print(tpe)
# Using the tuple() function, you can directly convert generator objects into tuples
print(tuple(tpe))