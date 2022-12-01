print ("#1")
q=list(map(int,input("Ведіть цілі числа ").split()))
q.remove(0)
print (sorted(q))

print ("#2")
q=list(map(int,input("Ведіть цілі числа ").split()))
if len (q)<=3:
    print ("помилка!!")
else:
    q.remove (max(q))
    q.remove (min(q))
    print (q)

print ("#3")
q=list(map(str,input("Ведіть слова ").split()))
q.sort ()
q.reverse ()
print (q)

print ("#4")
q=list(input('Ведіть слова '))
w=list(input('Ведіть слова '))
w.reverse ()
print ('Анаграма' if q==w else "Не анаграма")