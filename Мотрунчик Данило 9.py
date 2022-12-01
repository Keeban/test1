import math
#1
print('   1')
for i in range(0,101,10):
    print(i,' градусів ',32+i*1.8,'фаренгейт')

#2
print('   2')
q=str(input('вік людини, коли захочете закінчити введіть пробел '))
w=0
e=[]
while q!=' ':
    if q==" ":
        break
    e.append(int(q))
    q=str(input('вік людини '))
for i in (e):
    if i<=2:
        w+=0
    elif 3<=i<=12:
        w+=30
    elif 12<=i<=65:
        w+=100
    else:
        w+=50
print('сумма вартості квитків ',w)

#3
print('   3   ',  math.pi)

#4
print('   4')
q=1
w=0
q=input('вводьте ціни продукту, коли захочете закінчити введіть пробел  ')
while q!=[]:
    if q==" ":
        break
    w+=float(q)
    q=input('ціна продукту ')
if 0.75>w%1>=0.25:
    print('сума покупки ',w//1+0.5)
elif 1>w%1>=0.75:
    print('сума покупки ',w//1+1)
else:
    print('сума покупки ',w//1)

#5
print('   5')
q=[495,995,1495,1995,2495]
for i in q:
    print('ціна без знижки ',i,'  знижка ',i*0.6,'  ціна зі знижкою ',i*0.4)

#6
print('   6')
q=0
q=input('оцінка буквою, коли захочете закінчити введіть пробел  ')
w=[]
e=[]
while q!='':
    if q==" ":
        break
    w.append(q)
    q=input('оцінка буквою ')
for i in w:
    if i=='A':
        e.append(95)
    elif i=='B':
        e.append(87)
    elif i=='C':
        e.append(79.5)
    elif i=='D':
        e.append(69.5)
    elif i=='E':
        e.append(62)
    elif i=='FX':
        e.append(47)
    elif i=='F':
        e.append(17.5)
print('середня оцінка ',sum(e)/len(e))