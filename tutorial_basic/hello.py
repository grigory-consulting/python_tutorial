print("Hallo, Welt!")


my_string1 = "hello"
my_string2 = "WorlD"

print(my_string1 + "_" + my_string2) # Konkatenation 

print(str(len(my_string2)) + " Zeichen\n") # \n .. neue Zeile

print(my_string1[0]) # erstes Element
print(my_string1[1]) # zweites
print(my_string1[-1]) # letztes

string1 = 'Animals'
string2 = "Badger   " # + TAB
string3 = "Honey Bee"
string4 = "    \nHoneybadger" 

print(string3.lower())
print(string3.upper())

#### 

print(string4.strip()) # Alle führende und abschließende Leerzeichen löschen

print(string1.startswith("ho"))
print(string2.startswith("ho"))
print(string3.lower().startswith("ho"))
print(string4.startswith("ho"))


my_string_type1 = "6"
my_string_type2 = "7"

print(my_string_type1 + my_string_type2) # "67"

my_int_type1 = 6
my_int_type2 = 7

print(my_int_type1  + my_int_type2 ) # 13


my_float_type1 = 6. # 6.0
my_float_type2 = 7.0 # 7.0 
my_float_type3 = .8 # 0.8

print(my_float_type1 + my_float_type2) # Float 
print(my_float_type1 + my_int_type2) # Float + Int

print(float(my_string_type1) + float(my_string_type2)) # 13.0

a = input("Zahl eingeben: ")
b = input("Zweite Zahl eingeben: ")
product = float(a) * float(b)

print("Das Produkt von " + a + " und " + b + " ist " + str(product) + ".")
print(f"Das Produkt von {a} und {b} ist {product}.")

