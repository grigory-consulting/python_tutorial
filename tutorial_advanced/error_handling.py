
# try except 


try: 
    riskanter_resultat = 10/0
except Exception as e:
    print("Fehler", e)


res = []

for i in range(10):
    try:
        res.append(1/i)
    except:
        continue

try: 
    f = open("myfile.txt")
except FileNotFoundError:
    print("File not found.")
else: # falls es nicht zum Exception kam
    s = f.read()
    print("File read successfully.")
    f.close()
finally: # läuft unabhängig was vorher passiert ist
    print("finally")
