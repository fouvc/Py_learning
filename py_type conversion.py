# Converts type to another type
'''
    int():float(round down)or a string of complete number->int
    float():int,a string of float-point number or a string of complete number->float
    str():int and float->str
'''

x=int(1)            # x is 1
y=int(2.14)         # y is 2
z=int('2')          # z is 2

x=float(2)          # x is 2.0
y=float('2')        # y is 2.0
z=float('3.14')     # z is 3.14

x=str(1)            # x is '1'
y=str(2.14)         # y is '2.14'
z=str('ad')         # z is 'ad'