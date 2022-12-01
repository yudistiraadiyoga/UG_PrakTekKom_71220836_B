def add(fn,cn):
    add = fn+cn
    print(fn,'+',cn,'=',add)
    return add

def subtract(fn,cn):
    subtract = fn-cn
    print(fn,'-',cn,'=',subtract)
    return subtract

def multiply(fn,cn):
    multiply = fn*cn
    print(fn,'*',cn,'=',multiply)
    return multiply

def divide(fn,cn):
    divide = fn/cn
    print(fn,':',cn,'=',divide)
    return divide

print('Select Operation')
print('1.Add')
print('2.subtract')
print('3.multiply')
print('4.divide')
ec = input('Enter choice(1/2/3/4):')
fn = float(input('Enter first number:'))
cn = float(input('Enter second number:'))
if ec == 1:
    add(fn,cn)
elif ec == 2:
    subtract(fn,cn)
elif ec == 3:
    print(multiply(fn,cn)) 
elif ec == 4:
    print(divide(fn,cn))