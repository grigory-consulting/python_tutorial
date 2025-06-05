#for i in range(10):
#    print(i)
"""
for var in range(2,6):
    y = var*var
    print(y)
"""
for i in range(10,0,-2):
    print(i, end= " ")

l = [1,2,3]
print("\n" + str(l))

l2 = [1.,2,"3"]
print(l2)

l3 = [1.,2,"3",l2]
print(l3)

l4 = [1,1,1]

fruits = ["apple" , "banana", "cherry"]

for fruit in fruits:
    print(fruit)

for character in "apple":
    print(character)

### VERY IMPORTANT ###
### LIST COMPREHENSION ###

numbers = list(range(10))
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)


food = ["rice", "beans", "bread"]

food.append("broccoli") # appending "broccoli" to the end of the list
food +=  ["pizza", "hotdog"] # concatenating two lists

print(food)
# List slices
print(food[0]) # first element
print(food[-1]) # last element
print(food[2:]) # print from third element to end
print(food[:2]) # print upto second
print(food[2:5]) # print from third to fifth

breakfast = "eggs, fruit, orange juice".split(", ")
print(breakfast)


##### VERY IMPORTANT
#### MUTABILITY

breakfast[2] = "apple juice"
print(breakfast)


### IMMUTABILITY
## TUPLE

breakfast = ('eggs', 'fruit', 'orange juice')
breakfast[2] = "apple juice"
