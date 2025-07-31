# veränderliche Sammlung von Schlüssel-Wert Paaren
# Schlüssel immutable, Werte alles mögliche


d = {True: [1], False: [0]}

print(d)

d = {"one": 1, "two": [2], "three": "THREE", 4: {"four": "FOUR"}}

print(d)


# was nicht geht

# d = {[1,2,3]: 3}

# was geht:

d = {(1,2,3): 3}

print(d)

d = {"one": 1, "two": [2], "three": "THREE", 4: {"four": "FOUR"}}

# print(d["five"]) KeyError falls "five" nicht in dict

print(d.get("five", "Key not in dict"))


#### Löschen

del d["one"]

print(d)

value = d.pop(4)
print(value)
print(d)

# Iterieren

for key in d:
    print(key, d[key])

# Items = Liste von Schlüssel-Wert-Tupel 
print(list(d.items()))

# Values = Liste der Werte
print(list(d.values()))


##  Übung

farben = ["rot", "rot", "blau", "gelb", "blau", "rot"]

# Zählen Sie mit Hilfe eines Dictionaries, wie oft jede Farbe in der Liste vorkommt
# Ergebnis

d_farben = { "rot": 3, "blau:": 2, "gelb": 1}

d_farben = {} # leeres Dictionary
d_farben["rot"] = 5 # Zuweisung


d_farben = {}
for farbe in farben:
    if farbe in d_farben:
        d_farben[farbe] += 1
    else:
        d_farben[farbe] = 1

d_farben = {}
for farbe in farben:
    d_farben[farbe] = d_farben.get(farbe,0) + 1



# Übung

noten_1 = {"Anna": 2, "Marc": 3, "Lisa": 1}
noten_2 = {"Lisa": 2, "Marc": 1, "Benjamin": 5}

# Berechnen Sie die Schnittmenge der Schlüsseln 
# Berechnen Sie die Schnittmenge der Werte 

print(set(noten_1.keys()) & set(noten_2.keys()))
print(set(noten_1.values()) & set(noten_2.values()))


