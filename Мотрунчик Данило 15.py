print('#1')
import random
q=random.randint(1,49)
w=random.randint(1,49)
e=random.randint(1,49)
r=random.randint(1,49)
t=random.randint(1,49)
y=random.randint(1,49)
while q==w or q==e or q==r or q==t or q==y or w==e or w==r or w==t or w==y or e==r or e==t or e==y or r==t or r==y or t==y:
 q=random.randint(1,49)
 w=random.randint(1,49)
 e=random.randint(1,49)
 r=random.randint(1,49)
 t=random.randint(1,49)
 y=random.randint(1,49)
a=[q,w,e,r,t,y]
a.sort()
print(a)
print('#2')
a=[]
q=input('Додати нового студента?(+/-): ')
while q=='+':
 a.append(input('Введіть Прізвище І.О.:'))
 q=input('Додати нового студента?(+/-):')
a.sort()
print(a)