print('#1')
q=set(input('введіть на екран декілька символів'))
print(len(q))
print('#2')
print("Для завершення гри вкажіть '-' замість слова")
q=set(input('Алфавіт гри:'))
print('Літери можна використовувати неодноразово')
w=input("Ім'я першого учасника:")
e=input("Ім'я другого учасника:")
a=0
s=0
x=1
y=[]
u=[]
while a!='-'or s!='-':
    a=input(f'{w} (хід {x})')
    if a=='-':
        break
    r=set.union(q,a)
    if r!=q:
        print(f'Слово "{a}" не задовольняє умови гри')
    elif y.count(a)!=0 or u.count(a)!=0:
        print(f'Слово "{a}" вже було')
    else:
        y.append(a)

    s=input(f'{e} (хід {x})')
    t=set.union(q,s)
    if s=='-':
        break
    if t!=q:
        print(f'Слово "{s}" не задовольняє умови гри')
    elif y.count(s)!=0 or u.count(s)!=0:
        print(f'Слово "{s}" вже було')
    else:
        u.append(s)
    x+=1
print(f'Кошик слів ({w}) {y}')
print(f'Кошик слів ({e}) {u}')
print(f'{w if y>u else e}, вітаємо! Ви виграли!')