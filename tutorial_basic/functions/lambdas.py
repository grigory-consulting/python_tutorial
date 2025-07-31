
square = lambda x: x*x # Anonyme function

print(square(2))

nums = [1,2,3,4,5]
res = map(lambda x: 2*x , nums)
print(list(res))

res = [2*i for i in nums]

nums = [1,2,3,4,5]
nums2 = [10,20,30,40,50]

res = map(lambda x,y: x+y, nums, nums2)
print(list(res))

# Filter
odds = filter(lambda x: x%2 == 1, nums)
print(list(odds))

# List comprehension
odds = [i for i in nums if i%2==1]
print(odds)

from functools import reduce

# Produkt aller Zahlen in einer Liste
prod = reduce(lambda x,y: x*y, nums2)
print(prod)


# Kumulative Schleife
prod = 1
for x in nums2: prod *= x

print(prod)