'''
    The data type of Python:
    Text type:str
    Numeric type:   int,float,complex
    Sequence type:  list,tuple,range
    Mapping type:   dict
    Collection type:set,frozenset
    Boolean type:   bool
    '''

#You can use type() function to get any data type of any object
x=10
print(type(x))
print('------------------------------')

#In Python ,when you assign a values to a variable ,you set the data type
x='hello,world'
x=2
x=2.14
x=1j
x=['a','b','c']
x=('a','b','c')
x=range(6)
x={'name':'Bill','age':63}
x={'apple','banana'}
x=frozenset({'apple','banana'})
x=True
# is the same
# If you want to specify a data type,you can use the following constructor
x=str('hello,world')
x=int(2)
x=float(2.14)
x=complex(1j)
x=list(('a','b','c'))
x=tuple(('a','b','c'))
x=range(6)
x=dict(name='Bill',age=63)
x=set(('apple','banana'))
x=frozenset(('apple','banana'))
x=bool(5)
print('---------------------------')


# Python number
x=5 #int
x=2.1   #float
x=7.285e5   #float 7.258*10^5
x=1+2j  #complex

# You can use int(),float() and complex() methods to convert from one data type to another
#int->float     float->int      int->complex    float->complex
# But complex can't convert other


