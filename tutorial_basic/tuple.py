

x = (1,2,3)

#x[0] = 10 # shallow immutability

l = ["a", "b", "c"]

x = (l,2)
print(x)

l[0] = "D" 
print(x)
