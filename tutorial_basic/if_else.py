


gpa = 1.4

if gpa < 2.0: 
    print("Willkommen!")
else: 
    print("Auf Wiedersehen!")


if gpa < 2.0: 
    print("Willkommen!")


score = 85

if score >= 90:
    print("Note 1")
elif score >= 80:
    print("Note 2")
elif score >= 70:
    print("Note 3")
else:
    print("Auf Wiedersehen!")

# Sehr wichtig:

name = "Alice"

if name:
    print(name)

num = 1

if num:
    print(num)

l = []

if l:
    print(l)
else:
    print("Leere Liste")

# Logische Operatoren

x,y = 5,8

if x>0 and y<10:
    print("x ist positiv und y kleiner 10")

if x<0 or  y<10:
    print("x ist negativ oder y kleiner 10")

if not(x==0):
    print("x is ungleich Null")

a,b,c = 3,7,10

if (a<b and b<c) or not(a==3 and c==10):
    print("Komplexe Bedingung ist wahr")




