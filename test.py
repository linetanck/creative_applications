from turtle import *

t = Turtle()
#change of cursor speed, 0 is fastest
t.speed(30)

#position cursor
t.penup()
#define x-y coordinates
t.goto(-300, -100)
t.pendown()
side_length = 15
#code for squares
def square(t, side_length, color):
    t.color(color)
    t.begin_fill()
    for num in range(4):
        t.forward(side_length)
        t.right(90)
    t.end_fill()
    t.forward(side_length)

colors_list=['#264653', '#2a9d8f', '#e9c46a', '#f4a261', '#e76f51', '#e8e1ef','#d9fff8',"#c7ffda","#c4f4c7","#9bb291","#a7b99b","#acbfa4","#b4c5ac","#bbcab4","#c1cfbb", "#4b296b","#4c2c72","#77867f","#7f9d7d","#87b37a","#9ce37d","#a5e689","#aee895", "#14213d","#fca311","#f1c47b"]
colors_dict={'a':'#264653', 'b':'#2a9d8f', 'c':'#e9c46a', 'd':'#f4a261', 'e':'#e76f51', 'f':'#e8e1ef','g':'#d9fff8','h':'#c7ffda','i':'#c4f4c7','j':"#9bb291",'k':"#a7b99b",'l':"#acbfa4",'m':"#b4c5ac",'n':"#bbcab4",'o':"#c1cfbb", 'p':"#4b296b",'q':"#4c2c72",'r':"#77867f",'s':"#7f9d7d",'t':"#87b37a",'u':"#9ce37d",'v':"#a5e689",'w':"#aee895", 'x':"#14213d",'y':"#fca311",'z':"#f1c47b", ' ': '#ffffff'}



#y = -100
#for n in range(5):
 #   for c in colors_list:
  #      square(t, side_length, c)
   # t.penup()
    #y = y + side_length
    #t.goto(-300,y)
    #t.pendown()
def pixelword(input):
    input = input.lower()
    letters = []
    letters = [*input] #str d
    y = -100
    zahl = len(letters)
    höhe = zahl // zahl
    for i in letters:
        if x <= höhe:
            c = colors_dict[i]
            square(t, side_length, c)
        else:
            t.penup()
            y = y + side_length
            t.goto(-300, y)
            t.pendown()

        #nicht fertig, kann nicht mehr denken

    for n in range(höhe):
        for q in range(breite):
            c = colors_dict[i]
            square(t, side_length, c)
        #neu in höhe anfangen
        t.penup()
        y = y + side_length
        t.goto(-300,y)
        t.pendown()
pixelword('my name is karoline')
done()