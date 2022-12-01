#1
print('  1.1')
q=0
for i in range(1,6):
    for j in range(1,3):
        q=q+1
print(q)
#1.2
print('  1.2')
q=0
for i in range(1,3):
    for j in range(1,6):
        q=q+1
print(q)
#2.1
print('  2.1')
for i in range(25,51):
    print(i)
#2.2
print('  2.2')
for i in range(26,51,2):
    print(i)
#2.3
print('  2.3')
for a in range(25,50):
    if a>45:
        continue
    print(a)
#3.1
print('  3.1')
n=50
while n>=25:
    print(n)
    n=n-1
#3.2
print('  3.2')
n=25
while n<=50:
    print(n)
    n=n+2
#3.3
print('  3.3')
n=26
while n<=50:
    if a==46:
        continue
    print(n)
    n=n+2
#4
print('  4')
n=int(input('введіть натуральне число '))
while n>0:
    print(n%10)
    n=n//10
#5
print('  5')
n=int(input('факторіал якого числа потрібно знайти '))
q=1
while n>0:
    q=q*n
    n=n-1
if n<0:
    print('число відемне')
else:
    print(q)
#6
print('  6')
q=str(input('введіть дійсне число яке потрібно перевірити '))
w=len(q)
e=0
w=w-1
r=0
while w-e>=e:
    if q[w-e]==q[e]:
        e+=1
    else:
        r=1
        break
if r==1:
  print("непаліндром")
else:
  print("паліндром")
#7
print('  7')
q=int(input('введіть перше дійсне число '))
w=int(input('введіть друге дійсне число '))
while q!=w:
    if q>w:
        q=q-w
    else:
        w=w-q
print(q)