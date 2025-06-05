# mutable collection of key-value pair
# keys are immutable and unique, values can be any type

d= {True: [1], False: [0]} # boolean keys

print(d)

d = {"one": 1, "two": [2], "three": "THREE"}

## Accessing the key

print(d["three"]) # KeyError if key not in d
print(d.get("four", "Key not in dict"))

### Removing elements

#del d["one"]
#print(d)

#value = d.pop("three")

#print(value)
#print(d)


print("one" in d)

for key in d:
    print(key, d[key])