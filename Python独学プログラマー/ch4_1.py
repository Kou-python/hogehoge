#1
def f1(x=2):
    """
    :return: twice of x
    """
    return x**2


#2
def f2(x):
    print(x)

#3
def f3(a,b,c,d=4,e=5):
    print(a+b+c+d+e)
#4
def f4_1(int):
    return int/2

def f4_2(int):
    return int*4

def f4(x):
    half_value= f4_1(x)
    print(f4_2(half_value))

#5
def f5(str):
    try:
        return float(str)
    except(ValueError):
        print(str,"はFloatにできないよ！！")

c= f5("77.9")
print(c)