

setA = set(["a", "b", "c" , "d"])
setB = set(["c", "d", "e" , "f"])
setC = {"x", "y", "z"}
empty_set = set() # leere Menge muss so definiert sein

print("e" in setA) # Mitgliedschaftsüberprüfung

print(setA - setB) # Mengendifferenz: Elemente, die in setA vorkommen, aber nicht in setB 
print(setA | setB) # Vereinigung: Elemente, die entweder in setA oder in setB sind
print(setA & setB) # Schnittmenge: Elemente, die in setA und in setB
print(setA ^ setB) # Vereinigung - Schnittmenge


l = [5,5,1,1,1,1,2,2,2,3,3,3,3,4,4,4,4,4]

l_no_dup = list(set(l))
print(l_no_dup)


s = set()

for i in range(10):
    s.add(i)

print(s)

s = set()

for i in range(10):
    s |= {i}

print(s)