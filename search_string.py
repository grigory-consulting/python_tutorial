string1 = "Honeybadger"
print(string1.find("a")) # returns the position of a
print(string1.find("A")) # - 1 means no such position found
print(string1.find("bad")) # subword is in string and the lowest possible position is printed

a = input("Enter a number: ")
b = input("Enter another number: ")
a = a.replace("," , ".")
b = b.replace(",", ",")

product = float(a)*float(b)

print(f"The product of {a} and {b} is {product}.") # formatted string 