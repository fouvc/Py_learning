"""
输出格式美化：
Python两种输出值的方式: 表达式语句和 print() 函数。
第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现
str(): 将值转成字符串， 适用于一般的输出场景
repr(): 将值转成表达式字符串， 适用于调试场景
"""
import math
s="hello,world"
print(str(s),type(str(s)))
print(repr(s),type(repr(s)))

#repr()函数可以转义字符串中的特殊字符
print(repr("hello,world\n"))
print("----------------------------")

#输出一个平方和立方表
#rjust(width) 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串，默认空格
for i in range(1,4):
    print(repr(i).rjust(2),repr(i**2).rjust(3),end=" ")
    print(repr(i**3).rjust(4))
print("-----------------")

#使用str.format()函数格式化输出值
#{:2d} 表示输出值占2位， {:3d} 表示输出值占3位， {:4d} 表示输出值占4位，如果字符数小于指定位数则用空格填充,d表示十进制数
for i in range(1,4):
    print("{0:2d} {1:3d} {2:4d}".format(i,i**2,i**3))

#类似的方法还有zfill()函数，可以将字符串左边填充0
print("12".zfill(5))
print("-------------------------")

#str.format()基本用法
#1.括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换
print('{}网址： "{}!"'.format("菜鸟教程","www.runoob.com"))

#2.在括号里的数字用于指向传入对象在 format() 中的位置
print("{0} 和 {1}".format("Google","Runoob"))
print("{1} 和 {0}".format("Google","Runoob"))

#3.如果在 format() 中使用了关键字参数，那么它们将会指向相关的关键字
print("{name},{age}".format(age=25,name="John"))

#!a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化
print("常量PI的值是{!r}".format(math.pi))

#可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位
print("常量PI的值是{:.3f}".format(math.pi))
print("-------------------------------")

#在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name ,number in table.items():
    print('{0:10}-->{1:10d}'.format(name,number))

#如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情
print("Runoob:{0[Runoob]:d},Google:{0[Google]:d},Taobao:{0[Taobao]:d}".format(table))

#旧式字符串格式化
print("常量PI的值是%5.3f" % math.pi)
