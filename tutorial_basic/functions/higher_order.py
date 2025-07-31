def add_five(x):
    return x + 5

def do_twice(func, arg):
    return func(func(arg))

print(do_twice(add_five,3))

# Closure

def multiplier(factor):
    
    def multiply(number):
        return number*factor
    
    return multiply

double = multiplier(2)
print(double(14)) # 28

triple = multiplier(3)
print(triple(20)) # 60