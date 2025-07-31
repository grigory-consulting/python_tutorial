# Punkte auf Ebene

class Point2D:

    def __init__(self,x = 0,y = 0):
        self.x = x # Wert der x-Koordinate vom Punkt
        self.y = y # Wert der y-Koordinate vom Punkt
    def __str__(self):
        return f"({self.x},{self.y})"
    def __repr__(self):
        return f"Point2D({self.x},{self.y})"
    
    def __add__(self,other): # Operatorüberladung
        return Point2D(self.x + other.x, self.y + other.y)

    def move(self,dx, dy):
        self.x += dx
        self.y += dy
    
    def distance_0(self):
        return (self.x**2 + self.y**2)**.5
    

p1 = Point2D(2,1)
#print(p1)
p2 = Point2D(3,5)
#print(p1+p2)

p1.move(2,3)
#print(p1)


## Nicht empfohlen
p1.z = 3

p1.tag = "Blau"



### ÜBUNG
# 1. Erstellen Sie 50 zufällige Punkte (-10<=x<=10, -10<=y<=10) random.randint
# 2. Bestimmen Sie alle Punkte, welche den Abstand vom Urspung > 5.0 haben


import random

punkte = []
for _ in range(50):
    punkte.append(Point2D(random.randint(-10,10),random.randint(-10,10) ))


filter_punkte = []
for point in punkte:
    if point.distance_0()>5.0:
        filter_punkte.append(point)



# Vererbung


class Point3DError(Exception):
    pass

class MoveNegativeError(Point3DError):
    pass


class Point3D(Point2D): ## Point3D ... Subklasse, Point2D ... Superklasse

    def __init__(self, x,y,z):
        super().__init__(x,y) # Konstruktor aus Point2D aufrufen
        self.z = z
    
    def __str__(self):
        return f"({self.x},{self.y}, {self.z})"

    def __repr__(self):
        return f"Point2D({self.x},{self.y},{self.z})"
    
    def __sub__(self,other): # Operatorüberladung
        return Point2D(self.x - other.x, self.y - other.y, self.z - other.z)

    def liegt_auf_xy_ebene(self):
        return self.z == 0
    
    def liegt_auf_yz_ebene(self):
        return self.x == 0

    def move(self,dx,dy,dz):
        super().move(dx,dy)
        self.z += dz
    
    def move_positive(self,dx,dy,dz):
        if (dx<=0 or dy<=0 or dz<=0):
            raise MoveNegativeError("Move is not positive")
        self.move(dx,dy,dz)

    def distance_0(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    #def distance_0(self):
    #    return (super().distance_0(self)**2 + self.z**2)**0.5

#  Initialisieren Sie einen Punkt der Klasse Point3D mit den Koordinaten (3,4,5)

p = Point3D(3,4,5)

#  Erstellen Sie einen weiteren Punkt im Ursprung und verschieben Sie ihn um (-1, 7, 0)

q = Point3D(0,0,0) 
q.move(-1,7,0)
q.move_positive(-1,7,0)



#  Erstellen Sie geeignete __str__ und __repr__ Methoden

#  Erstellen Sie eine Methode liegt_auf_xy_ebene(self) in Point3D, die True zurückgibt, falls
#  z == 0
#  Entsprechen erstellen Sie die Methoden für andere Koordinatenebenen
#  Überladen Sie den Operator __sub__ sodass die Differenz zweier Punkte 
#  Point3D zurückgegeben wird
#  Erstellen Sie 50 zufällige Point3D-Punkte und finden Sie den Punkt mit dem größten (kleinsten)
#  Abstand zum Ursprung

punkte = []
for _ in range(50):
    punkte.append(Point3D(random.randint(-10,10),random.randint(-10,10), random.randint(-10,10)))

print(punkte)

max_value = 0
min_value = Point3D(10,10,10).distance_0()+5
for punkt in punkte:
    d_0 = punkt.distance_0()
    if d_0 > max_value:
        max_value = d_0
        arg_max = punkt
    if d_0 < min_value:
        min_value = d_0
        arg_min = punkt

print(arg_max)
print(arg_min)

######## Mehrfachvererbung

class A:
    def methodeA(self):
        print("Methode von A")

class B:
    def methodeB(self):
        print("Methode von B")
 
class C(A,B): # Vererbung von beiden
    pass

obj = C()
#obj.methodeA()
#obj.methodeB()

class A:
    def methode(self):
        print("Methode von A")

class B:
    def methode(self):
        print("Methode von B")
 
class C(B,A): # Vererbung von beiden
    pass

obj = C()
obj.methode()

print(C.mro())


class A:
    def show(self):
        print("A.show()")

class B(A):
    def show(self):
        print("B.show()")
        super().show()

class C(A):
    def show(self):
        print("C.show()")
        super().show()

class D(B,C):
    def show(self):
        print("D.show()")
        super().show()

print(D.mro())

d = D()
d.show()