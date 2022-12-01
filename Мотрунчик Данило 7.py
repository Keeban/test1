#1
q=int(input('Скільк років людині '))
if q<=0:
   print('Введено неверное число')
elif q<=21:
   print(q/10.5)
else:
   print(2+(q-21)/4)