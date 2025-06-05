fruits = ["apple" , "banana", "cherry"]

# enumeration loop
for idx,fruit in enumerate(fruits):
    print(idx,fruit)

# break statement 

for i in range(1,10):
    if i == 5: 
        break
    print(i)

# continue statement

for i in range(1,10):
    if i == 5: 
        continue
    print(i)

# for 

for i in range(1,10):
    print(i)
else:
    print("Loop finished")

for i in range(1,10):
    if (i == 5):
        break
    print(i)
else:
    print("Loop finished")


# Cumulative Loops

sum = 0

for i in range(11):
    sum += (i*i) # sum of squares 

print(sum)

product = 1

for i in range(1,6):
    product *= i # cumulative product
    print(product)

