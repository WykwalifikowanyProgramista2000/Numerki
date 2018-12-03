import matplotlib.pyplot as plt
import math



# Zadanie 1

def myfun(x: float) -> float:
     return math.e**(-(x**2))


def simple_trapezoid_method(f, begin, end):
    return (end - begin)/2*(f(begin) + f(end))


def simple_rectangle_method(f, begin, end):
    return (end - begin)*f((begin+end)/2)


def simple_simson_method(f, begin, end):
    return (end - begin)/6*(f(begin) + 4 * f((begin - end)/2) + f(end))


def advanced_trapezoid_method(f, begin, end):
    ans = 0
    n = abs(end - begin)//1*10
    for i in range(0, n-1):
        x_i = begin + i*((end - begin)/n)
        x_i_1 = begin + (i+1)*((end - begin)/n)
        ans += (x_i_1 - x_i)/2 * (f(x_i) + f(x_i_1))
    return ans
    
    
def advanced_rectangle_method(f, begin, end):
    ans = 0
    n = abs(end - begin)//1*10
    for i in range(0 , n-1):
        x_i = begin + i*((end - begin)/n)
        x_i_1 = begin + (i+1)*((end - begin)/n)
        ans += f((x_i_1 - x_i)/2) * (x_i_1 - x_i)
    return ans


def advanced_simson_method(f, begin, end):
    ans = 0
    n = abs(end - begin)//1*10
    for i in range(0 , n-1):
        x_i = begin + i*((end - begin)/n)
        x_i_1 = begin + (i+1)*((end - begin)/n)
        ans += (x_i_1 - x_i)/6 * (f(x_i) + 4 * f((x_i_1 + x_i)/2) + f(x_i_1))
    return ans
        


a = 0
b = 1

print(simple_trapezoid_method(myfun, a, b))
print(simple_rectangle_method(myfun, a, b))
print(simple_simson_method(myfun, a, b))

print("advanced_trapezoid_method: {0}".format(advanced_trapezoid_method(myfun, a, b)))
print("advanced_rectangle_method: {0}".format(advanced_rectangle_method(myfun, a, b)))
print("advanced_simson_method:    {0}".format(advanced_simson_method(myfun, a, b)))


begin = 0
end = 1