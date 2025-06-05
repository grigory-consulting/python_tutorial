my_string_type1= "6"
my_string_type2= "7"

print(my_string_type1 + my_string_type2)


my_int_type1 = 6
my_int_type2 = 7
print(my_int_type1 + my_int_type2)


print(int(my_string_type1) + int(my_string_type2))

my_float_type1 = 6.
my_float_type2 = 7.

print(my_float_type1)
print(my_float_type2)
print(my_float_type1 + my_float_type2)


print(float(my_string_type1) + float(my_string_type2))

a = input("Enter a number: ")
b = input("Enter another number: ")
product = float(a)*float(b)
print("The product of " + a + " and "+ b + " is " + str(product) + ".") # ordinary strin
print(f"The product of {a} and {b} is {product}.") # formatted string 