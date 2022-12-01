import turtle as t
t.up ()
t.goto (0,0)
t.speed (20)
t.width (2)
t.bgcolor ("blue")
t.down ()
q=0
a=["yellow","lime",'green',"crimson","magenta","red"]
for i in range (300):
    t.forward(q+i*2)
    t.left(91)
    t.color(a[i%6])