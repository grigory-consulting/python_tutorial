def cube(num):
    cube_num = num**3
    return cube_num

def greeting(name="Welt"):
    print("Hallo, ", name + "!") # kein Rückgabewert



import random

def random_ziffer(): # Funktion ohne Parameter
    return random.randint(0,9)



# Das ist korrekt:
def add_two_numbers(a, b=1):
    """Addiert zwei Zahlen, b ist optional"""
    return a+b

#help(add_two_numbers) # mit q Terminal-Editor verlassen


# def add_two_numbers(a=1, b): # Syntaxfehler
#    # Parameter without a default follows parameter with a default
#    return a+b

def other_sum(*args):
    return sum(args)


def dateneingabetool(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key,value)
    

def everything(a,b=1, *args, **kwargs):
    print("a", a)
    print("b", b)
    print("args", args)
    print("kwargs", kwargs)



if __name__ == "__main__":
    greeting() 
    x = greeting("Grigory")
    print(x)
    print(other_sum(1,2,2,3,3,4,4,5,4,4,4,4,4,5,5,5,4))
    tup = (1,2)
    print(add_two_numbers(*tup))
    dateneingabetool(Name = "Prof. Döbeln", Alter = 24, Stadt = "Döbeln")
    everything(1,2,3,4,5,6,x=12, y = [])


