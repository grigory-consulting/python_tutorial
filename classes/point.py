# Classes -> define what is the object and which function operate
# on this object
# Object is called class instance 
# class contains attributes (definition of object) and 
# methods (functions)

class Point2D: 

    def __init__(self, x = 0, y = 0 ): ## __init__ -> create a class instance,
    #  self -> is the class instance itself
        self.x = x
        self.y = y 
    
    def norm(self): #distance from the origin
        return (self.x**2 + self.y**2)**0.5
    
    def __repr__(self): # __str__ or __repr__ 
        try:
            return f"({self.x},{self.y},{self.z})"
        except:
            return f"({self.x},{self.y})"
    
    def distance_between_two_points(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        pd = Point2D(dx,dy)
        return pd.norm()
    
    def __add__(self,other):
        return Point2D(self.x + other.x, self.y + other.y)
    
    

p1 = Point2D(2,1)
print(p1)

p1.z = 3 # dynamic attibutes (not recommended)
p1.tag = "This is very important point"
print(p1)

p1 = Point2D(2,1)
p2 = Point2D(1,4)
print(p1+p2)

p1 = Point2D(2,1)
p2 = Point2D(1,4)
p3 = Point2D(4,5)

# Inheritance 

class Point3D(Point2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y) # initialize Point2D
        self.z = z
