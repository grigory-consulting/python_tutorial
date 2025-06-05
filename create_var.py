
my_string = "hello_WorLD"

print(str(len(my_string)) + " characters") # + is concatenation/merging of strings

string1 = "hello"
string2 = "WorLD"
print(string1 + "_" + string2)


res_string = "11 characters\n" # newline character, print statement adds this one per default

print(res_string[0]) # printing first character
print(res_string[5]) # printing 5th character
print(res_string[-1]) # printing last character (in this case newline)

string1 = "Animals"
string2 = "Badger     "
string3 = "Honey Bee"
string4 = "    Honeybadger"

print(string3.lower())
print(string3.upper())

print(string4.strip()) # remove leading white spaces

######


print(string1.startswith("ho"))
print(string2.startswith("ho"))
print(string3.lower().startswith("ho"))
print(string4.startswith("ho"))
