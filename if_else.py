gpa = 1.4 

if gpa > 2.0:
    print( "Welcome to SRH Univerity")
else: 
    print("F**K OFF")

# dont need always to have else for if
if gpa > 2.0:
    print( "Welcome to SRH Univerity")

#  If and Elif - Statements

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("F**K OFF")

### VERY IMPORTANT

name = "Alice"

if name:
    print(name)
else:
    print("Empty String")

num = 1

if num:
    print(num)
else:
    print("Num is Zero")

l = []

if l: 
    print(l)
else:
    print("List is Empty")


# Logical operators
# == ... equals
# != ... not equal
# <,>  ... less,greater than
# <=,=> ... less equal than, greater equal than
# and ... True if both sides True
# or ... True if one side True
# not ... Invert the truth value 

x,y = 5, 8

if x>0 and y < 10:
    print("x is positive and y is less than 10")

if x<0 or y < 10:
    print("Either x is negative or y is less than 10.")

if not(x==0):
    print("x is not zero")

a,b,c = 3,7,10

if (a<b and b <c) or (a==3 and c == 10):
    print("Very complex condition is True")