def print_func(par):
    print("Hello :",par)
    return
"""
说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
说明：__name__ 与 __main__ 底下是双下划线，__是这样去掉中间的那个空格"""
if __name__=='__main__':
    print('程序自身在运行')
else:
    print('我来自另一个模块')