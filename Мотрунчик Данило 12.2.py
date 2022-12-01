print("Вправа 4")
import turtle as t
for j in range (5):
    for i in range (3):
        t.begin_fill ()
        t.color("orange","orange")
        t.forward(50)
        t.right (120)
        if i==2:
            t.forward(55)
        t.end_fill()
t.reset()
print("Вправа 5")
import turtle as t
q=["orange","green","orange","green","orange"]
for j in range (5):
    for i in range (3):
        t.begin_fill ()
        t.color (q[j],q[j])
        t.forward(50)
        t.right (120)
        if i==2:
            t.forward(55)
        t.end_fill()