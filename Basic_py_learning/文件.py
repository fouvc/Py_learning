"""
open()将会返回一个file对象，基本格式如下：
file = open(filename, mode)
filename：要打开的文件名，可以是绝对路径或相对路径。
mode：打开文件的模式
"""

# 打开一个文件，并写入内容,f.write()将string写入文件中，如果不是string需要先转换。同时f.write()返回的是写入的字符数。
f = open("foo.text" ,"w")
f.write("python is easy \nYes, It is")
# 关闭文件
f.close()

# 打开一个文件，并读取内容,f.read(size)中size是一个可选类型参数，表示每次读取的字节数，默认为读取所有内容。
f = open("foo.text","r")
str = f.read()
print(str)
# 关闭文件
f.close()

# 打开一个文件，并读取一行内容
#f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行
f = open('foo.text','r')
str = f.readline()
print(str)
f.close()

#打开一个文件，并读取所以行内容
#f.readlines() 会从文件中读取所有行并返回列表，每个元素代表一行内容，列表中元素之间用换行符 '\n' 分隔。
f = open('foo.text','r')
str = f.readlines()
print(str)
f.close()

#f.tell() 用于返回文件当前的读/写位置（即文件指针的位置）。
# 文件指针表示从文件开头开始的字节数偏移量。f.tell() 返回一个整数，表示文件指针的当前位置
f = open('foo.text','r')
num = f.tell()
print(num)
f.close()

#如果要改变文件指针位置，可以使用f.seek(offset, from_what)方法。
# offset：表示相对于 from_what 的偏移量，可以是正数、负数或零。
# from_what：表示偏移量的参考位置，可以是 0（表示文件开头）、1（表示当前位置）、2（表示文件末尾）。
#f.seek(x,0)表示从文件开头移动x个字节。
#f.seek(x,1)表示从当前位置往后移动x个字节。
#f.seek(x,2)表示从文件末尾往前移动x个字节。

f = open('foo.text','wb+')
#'wb' 表示以二进制模式写入文件。如果你不使用 b 前缀，Python 会默认将字符串视为 Unicode 字符串，并尝试将其编码为字节序列，
#加 b 表示这是一个字节字符串（byte string），而不是普通的字符串（Unicode string）。字节字符串是由字节序列组成的，
sum = f.write(b'013456789abcdefg')
#移动到文件的第二个字节
place = f.seek(1)
str = f.read()
print('改变指针后，指针从{}位置开始移动，读取的内容是{}'.format(place,str))
print('总个数：',sum,'文件指针位置：',place,'内容是：',f.seek(1))
f.close()
#总结一下，b 前缀用于明确表示你正在处理的是字节数据，而不是文本数据，这在处理二进制文件或需要精确控制字节数据时非常重要。

#with 语句可以自动帮我们调用 close() 方法，确保文件在使用完后正确关闭。
with open('foo.text','r') as f:
    str = f.read()
    print(str)
#f.closed 属性用于判断文件是否已经关闭。
print(f.closed)

#文件删除
#为避免出现错误，您可能需要在尝试删除文件之前检查该文件是否存在
import os
if os.path.exists('foo.text'):
    os.remove('foo.text')
else:
    print('The file does not exist')
#如需删除整个文件夹，请使用 os.rmdir() 方法,只能删除空文件夹