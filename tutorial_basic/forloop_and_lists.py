for i in range(10):
    print(i)

for var in range(2,6):
    y = var*var
    print(y)

for i in range(10, 0 , -2):
    print(i, end=" ")

l = [1,2,3]
print("\n" + str(l))

l2 = [1.0, 2, "3"]
print(l2)

l3 = [1., 2, "3", l2]
print(l3)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


for each in fruits:
    print(each)

#### SEHR WICHTIG ####
#### List comprehension ####

numbers = list(range(10))
quadrate = [num**2 for num in numbers]
print(quadrate)

# klassisch For-Loop

quadrate = []
for num in numbers: quadrate.append(num**2)
print(quadrate)

# Kumulative Loop
quadrate = []
for num in numbers: quadrate+=[num**2]
print(quadrate)

food = ["rice", "beans", "bread"]

food.append("broccoli") # Anhängen ans Ende der Liste O(1)
food += ["pizza", "hotdog"] # Listenkonkatenation

print(food)
# List slices 

print(food[0]) # Erstes Element
print(food[-1]) # Letztes Element
print(food[2:]) # vom dritten bis zum Ende
print(food[:2]) # bis zum zweiten
print(food[5:2:-1]) # vom dritten zum fünften

### SEHR WICHTIG
# MUTABILITY
food[0] = "apple juice"

print(food)











