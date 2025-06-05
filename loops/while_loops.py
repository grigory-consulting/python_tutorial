# while loop: execute statements in a loop 
# until some condition is true

num = 1

while num < 200:
    num *= 2
    if num >= 200:
        break         
    print(num)
else: 
    print("Loop finished without break statement")

password = ""

while password != "very_secret_password":
    password = input("Enter the password: ") # <- here the while loop blocks
    print(password)
print("Access granted")