from turtle import*

colormode(255)

lt(90)

lv=10
l=100
s=40

width(lv)

r=0
g=0
b=0
pencolor(r,g,b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l,level):
    global r,g,b
    w=width()

    width(w*3.0/4.0)

    r=r+5
    g=g+8
    b=b+2
    pencolor(r%200,g%200,b%200)
    
    l=3.0/4.0*l
    
    lt(s)
    fd(l)
    
    if level<lv:
        draw_tree(l,level+1)
    bk(l)
    rt(2*s)
    fd(l)
    
    if level<lv:
        draw_tree(l,level+1)
    bk(l)
    lt(s)

    width(w)

speed("fastest")

draw_tree(l,4)

penup()
pensize(5)
goto(-100,-100)
color("red")
speed(5)
write("Liu Junliang HKU")

done()

