# set unordered collection of unique elements

setA = set(["a","b","c", "d"])
setB = set(["c","d","e", "f"])
setC = {"x", "y", "z"}
empty_set = set()

print("e" in setA) # check whether element is in set

print(setA - setB) # elements in setA but not in setB
print(setA | setB) # set union all elements in either setA or in setB
print(setA & setB) # intersection all elements in both sets
print(setA ^ setB) # symmetric difference (union - intersection)

s = set()
for i in range(10):
    s |= set([i])

print(s)

l = [1,2,2,2,2,4,5,6,6,6,6]

l = list(set(l)) # remove duplicates

print(l)

for i in set(l):
    print(i)