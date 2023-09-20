"""
Iterator objects are accessed from the first element of the collection until all elements have been accessed.
Iterators can only go forward, not backwards
"""

# Iterator:
# Use iter()
lst=['apple','orange','banana']
# Create an iterator object
it=iter(lst)
# Output next element of the iterator
print(next(it))         # is apple
print(next(it))         # is orange
"""
If you use for a statement,only banana will be output in the end,
because iterator only go forward."""

# Use for
lst=[1,2,3,4]
x=iter(lst)
for i in x:
    print(i,end=' ')
print('\n',end='')
print('---------------------')

# Create an iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
#The StopIteration exception is used to identify the completion of an iteration and prevent an infinite loop
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)
print('--------------------------')


# Generators:
# Functions that use yield are called generators
"""
When you use the yield statement in a generator function, 
the execution of the function is paused and the expression after yield 
is returned as the value of the current iteration"""
def countdown_i(n):
    while n>0:
        yield n
        n-=1
a=countdown_i(5)
print(next(a))  # Output 5
print(next(a))  # Output 4
print(next(a))  # Output 3
print('--------------------')
for value in a:
    print(value)# Output 1 and 2


