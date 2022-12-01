print('#1.1')
q=list(map(int,input(' введіть з клавіатури числа через пропуск').split()))
w=0
for i in (q):
    w+=1
print(w,' чисел')
print('#1.2')
q=list(map(int,input(' введіть з клавіатури числа через кому ').split(',')))
w=0
for i in (q):
    if i>=0:
        w+=1
print(w,' недодатніх чисел')
print('#1.3')
q=list(map(int,input(' введіть з клавіатури числа через кому ').split(',')))
w=0
for i in (q):
    if i>0 and i%3==0:
        w+=1
print(w,' додатніх чисел, кратних числу 3')
print('#2.1')
q=list(map(int,input(' введіть з клавіатури числа через пропуск').split()))
q1=[]
q2=[]
for i in (q):
    if i%2==0:
        q1.append(i)
    else:
        q2.append(i)
print(q1,q2)
print('#2.2')
q=list(map(int,input(' введіть з клавіатури числа через пропуск').split()))
q1=[]
q2=[]
for i in (q):
    if i>0:
        q1.append(i)
    else:
        q2.append(i)
print(q1,q2)
print('#2.3')
q=list(map(int,input(' введіть з клавіатури числа через пропуск').split()))
q1=[]
q2=[]
for i in (q):
    if i%5==0:
        q1.append(i)
    else:
        q2.append(i)
print(q1,q2)
print('#2.4')
q=list(map(int,input(' введіть з клавіатури числа через пропуск').split()))
q1=[]
q2=[]
q3=[]
for i in (q):
    if i%3==0 and i%9==0:
        q1.append(i)
    elif i%3==0:
        q2.append(i)
    else:
        q3.append(i)
print(q1,q2,q3)
print('#3*')
q=list(map(str,input(' введіть з клавіатури через пропуск').split()))
w=0
for i in (q):
    w+=1
print(w,' елементів')