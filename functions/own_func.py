def cube(num=1): # default argument
    cube_num = num**3 
    return cube_num


a = 5
b = 7

print(cube(a))
print(cube(b))

print(cube())

def plus(num1, num2=1): return num1 + num2


def convert_cel_to_far(temperature_cel): # 
    temperature_far =  temperature_cel * (9/5) +32
    return temperature_far

def convert_far_to_cel(temperature_far):
    temperature_cel = (temperature_far -32) * (5/9)
    return temperature_cel

temperature_far = input("Enter a temperature in degrees F: ")
temperature_cel = convert_far_to_cel(float(temperature_far))

print(f"{temperature_far} degrees F = {temperature_cel:.2f} degrees C")

temperature_cel = input("\nEnter a temperature in degrees C: ")
temperature_far = convert_cel_to_far(float(temperature_cel))

print(f"{temperature_cel} degrees C = {temperature_far:.2f} degrees F")
