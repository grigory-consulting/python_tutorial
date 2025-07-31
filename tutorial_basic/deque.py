# Double Ended Queue 

from collections import deque

d = deque() # leere Deque
d = deque([10,20,30])
d = deque(maxlen = 5)


d = deque()
d.append(1)
d.append(1)
d.append(2)
d.appendleft(0)
print(d)

d.pop()     # Entfernt 2
d.popleft() # Entfernt 0

print(d)


text = "lager|regal"
d = deque(text)
print(d)

# Schreiben Sie ein Programm, welches überprüft ob ein Wort ein Palindrom ist
# 

bool_flag = True

while len(d)>1:
    if d.popleft() != d.pop():
        bool_flag = False
        break

# Gegeben:

a = deque([1,2,3])
b = deque(["a", "b" , "c", "d"])

# Output
# Das alternierende Zusammenführen 
# deque([1, "a", 2 , "b", 3, "c", "d"])

c= deque()

while a or b:
    if a:
        c.append(a.popleft())
    if b:
        c.append(b.popleft())

print(c)



# Sliding-Window-Sum

# Gegeben: 
# Liste l = [1,3,5,2,8,1,5] , Fenstergröße = 3
# für ein Window der Größe k jeweils eine aktuelle Summe berechnen und Fenster verschieben
# Output: [9, 10, 15, 11, 14]

l = [1,3,5,2,8,1,5]
k = 3
d=deque()
res = []
curr_sum = 0

for num in l:
    d.append(num)
    curr_sum += num
    if len(d) > k:
        curr_sum -= d.popleft()
    if len(d) == k:
        res.append(curr_sum)
print(res)





#  Output




