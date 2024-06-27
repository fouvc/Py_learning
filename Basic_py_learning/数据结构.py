'列表可以修改，而元组和字符串则不能修改。'
# 以列表a为例
a=[1,2,32,4,5]
print('原列表a：',a)
print('-----------------------------------')

#list.append(obj) 向列表末尾添加一个对象obj，相当于a[len(a):] = [obj]
a.append(11)
#输出：[1, 2, 32, 4, 5, 11]
print('使用list.append(obj)添加对象111后：',a)
print('------------------------------------')

#list.extend(iterable) 扩展列表，相当于a[len(a):] = iterable
a.extend([88,99])
print('使用list.extend(iterable)扩展列表[88,99]后：',a)
print('-----------------------------------')
#输出：[1, 2, 32, 4, 5, 11, 88, 99]

#list.insert(index, obj) 在指定位置index处插入对象obj，而a.insert(len(a),obj)等价于a.append(obj)
a.insert(3,90)
print('使用list.insert(index, obj)在位置3插入对象90后：',a)
#输出：[1, 2, 32, 90, 4, 5, 11, 88, 99]
print('----------------------------------')

#list.remove(obj) 从列表中移除第一个出现的对象obj，如果obj不存在，则会引发ValueError异常
#a.remove(100)
#list.remove(x): x not in list

#list.pop([index]) 移除并返回指定位置的对象，如果没有指定位置，则默认移除并返回最后一个对象,[index]表示可选参数
a.pop(2)
print('使用list.pop([i])移除位置2的对象32后：',a)
#输出：[1, 2, 4, 5, 11, 88, 99]
print('-----------------------------------')

#list.index(obj) 返回列表中第一个出现的对象obj的索引，如果obj不存在，则会引发ValueError异常
print('使用list.index(obj)查找对象2的索引：',a.index(2))
print('-----------------------------------')

#list.count(obj) 返回列表中obj出现的次数
print('使用list.count(obj)查找对象2出现的次数：',a.count(2))
print('-----------------------------------')

#list.sort(reverse=False) 对列表进行排序，默认升序，也可以指定reverse=True进行降序排序
a.sort(reverse=True)
print('使用list.sort(reverse=True)对列表进行降序排序后：',a)
a.sort(reverse=False)
print('使用list.sort(reverse=False)对列表进行升序排序后：',a)
print('-----------------------------------')

#list.copy() 返回列表的浅拷贝，即创建一个新的列表，内容与原列表相同，但内存地址不同
b=a.copy()
print('使用list.copy()创建列表b，内容与a相同，但内存地址不同：',b)
print('-----------------------------------')

#list.clear() 清空列表，相当于del a[:]
a.clear()
print('使用list.clear()清空列表a后：',a)
print('-----------------------------------')


"""
将列表当作栈使用，栈是一种后进先出的数据结构
栈操作：
压入(Push): 将一个元素放入栈顶
弹出(Pop): 将栈顶元素弹出
查看栈顶元素(Peek/Top):返回栈顶元素而不移除它
检查栈是否为空(IsEmpty):检查是否为空
获取栈的大小(Size):返回栈中元素的数量"""
print('------------栈的操作------------------')

#1.创建一个空栈
stack=[]

#2.压入(Push)操作,使用append()方法将元素压入栈顶
stack.append(1)
stack.append(2)
stack.append(3)
print('压入:',stack)

#3.弹出(Pop)操作，使用pop()方法返回并弹出栈顶元素
top_element=stack.pop()
print('返回并移除栈顶元素：',top_element)
print(stack)

#4.查看栈顶元素(Peek/Top)操作，使用[-1]索引访问栈顶元素
top_element=stack[-1]
print('栈顶元素：',top_element)

#5.检查是否为空栈(IsEmpty)
print('False') if len(stack)==0 else print('True')
#or
is_empty=len(stack)==0
print(is_empty)

#6.获取栈的大小(Size)
size=len(stack)
print('栈的大小:',size)
print('------------------------------------------')

#以下是一个完整的实例来使用上述方法模拟一个简单的栈
class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise indexError("pop from empty stack")
        else:
            return self.stack.pop(-1)

    def peek(self):
        if self.is_empty():
            raise indexError("peek from empty stack")
        else:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack)==0

    def size(self):
        return len(self.stack)

#实例化一个栈
stack=Stack()
#压入元素
stack.push(1)
stack.push(2)
stack.push(3)

print("栈顶元素:",stack.peek())
print("栈的大小:",stack.size())
print("弹出栈顶元素:",stack.pop())
print("栈是否为空:",stack.is_empty())
print("栈的大小:",stack.size())
print('---------------栈结束---------------------')

print('----------------队列开始--------------------')
"""
将列表当作队列使用，队列是一种先进先出的数据结构"""
print('-----------------使用列表实现队列-----------------------')
#1.创建一个空队列
queue=[]

#2.入队(Enqueue)操作，使用append()方法将元素加入队列的尾部
queue.append('a')
queue.append('b')
queue.append('c')
print('队列状态：',queue)

#3.出队(Dequeue)操作，使用pop(0)方法将队列头部的元素移除并返回
first_element=queue.pop(0)
print('移除的队列元素:',first_element)
print('队列状态:',queue)

#4.查看队列头部元素(Peek/Front)操作不移除
first_elemnt=queue[0]
print('队列头部元素：',first_elemnt)
print('队列状态:',queue)

#5.检查队列是否为空(IsEmpty)
is_empty=len(queue)==0
print(is_empty)

#6.获取队列的大小(Size)
size=len(queue)
print('队列的大小:',size)
print('--------------------------------')

#以下是一个完整的实例用上述方法来实现队列
class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise indexError("dequeue from empty queue")
        else:
            return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise indexError("peek from empty queue")
        else:
            return self.queue[0]

    def is_empty(self):
        return len(self.queue)==0

    def size(self):
        return len(self.queue)

queue=Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')

print("队列头部元素:",queue.peek())
print("队列大小：",queue.size())
print('移除的元素:',queue.dequeue())
print("队列是否为空:",queue.is_empty())
print("队列大小:",queue.size())
print('-------------------------------')

"""使用列表时，如果频繁地在列表的开头插入或删除元素，性能会受到影响，因为这些操作的时间复杂度是 O(n)。
为了解决这个问题，Python 提供了 collections.deque，它是双端队列，可以在两端高效地添加和删除元素"""

print('---------------使用collecitons.deque实现双端队列------------------------')
from collections import deque

#1.创建一个空双端队列
queue=deque()
#2.向队列添加元素
queue.append('a')
queue.append('b')
queue.append('c')
print('队列状态：',queue)

#3.从队首移除元素
first_element=queue.popleft()
print('移除元素：',first_element)
print('队列状态：',queue)

#4.查看队首元素，不移除
first_element=queue[0]
print('队首元素：',first_element)

#5.检查队列是否为空
is_empty=len(queue)==0
print(is_empty)

#6.获取队列大小
size=len(queue)
print('队列大小：',size)

print('----------------------元组---------------------')
#元组是不可变的序列，一旦创建，其内容不能被修改
#创建元组
t=(1,2,3)
print(t,t[0])
u1=t+(4,5,6)
u2=t,(4,5,6)
print(u1,u2)
#元组的操作与列表类似，但元组不能修改，因此不能使用append()、extend()、insert()等方法
#元组的索引操作与列表相同，但不能使用负数索引
#元组的切片操作与列表相同，但不能使用步长参数

print('----------集合--------------')
"""
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典"""
basket={'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
#删除重复的元素
print(basket)
#检测成员
print('orange' in basket)
print('grape' in basket)

#以下演示两个集合的操作
a=set('abacabdefgh')
b=set('acabdegmx')
print(a)    #a中唯一的元素
print(a-b)  #在a中但不在b中的元素
print(a|b)  #在a或b中的元素
print(a&b)  #在a和b中的元素
print(a^b)  #在a或b中，但不同时在a和b中的元素
#集合也支持推导式
c={x for x in 'abracadabra' if x not in 'abc'}
print(c)   #{'r', 'd'}

print('------------字典------------------')
"""
序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同"""

#创建字典
tel={'jack': 4098, 'sape': 4139}
#添加元素
tel['guido']=4127
print(tel)
print(tel['jack'])
#删除元素
del tel['sape']
print(tel)
#修改元素
tel['guido']=4000
print(tel)
#获取键的集合并转成列表
print(list(tel.keys()))
#获取值得集合

#构造函数dict()可以从键值对列表或关键字参数构造字典
tel=dict(sape=4139, guido=4127, jack=4098)
#或tel=dict([('jack', 4098), ('sape', 4139), ('guido', 4127)])
print(tel)

#遍历技巧
#关键字和对应的值可以使用items()方法同时遍历
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

#在在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

#同时遍历两个或多个序列，可以使用zip()函数
questions=['name', 'quest', 'favorite color']
answers=['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#反向遍历序列
for i in sorted(range(1,10,2),reverse=True):
    print(i)