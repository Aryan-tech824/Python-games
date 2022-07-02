from tkinter import *
import random
import time
m=0
n=0
root=Tk()
root.title("Pong")
root.resizable(0,0)
root.wm_attributes("-topmost",1)
cana=Canvas(root,width=500,height=400,bd=0,highlightthickness=0)
cana.config(bg="yellow")
cana.pack()
root.update()

cana.create_line(250,0,250,400,fill="black")

#Just think about two balls!

class Ball:
    def __init__(self,cana,color,p,p1):
        self.cana=cana
        self.id=cana.create_oval(240,190,260,210,fill=color)
        self.color=color
        self.p=p
        self.p1=p1
        start=[-3,3]
        random.shuffle(start)
        self.x=start[0]
        self.y=-3
        
    def draw(self):
        self.cana.move(self.id,self.x,self.y)
        pos=self.cana.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[0]<=0:
            self.x=3
            global n
            b=self.cana.create_text(375,50,text=n,font=("Arial",60),fill="black")
            self.cana.itemconfig(b,fill="yellow")
            n = n + 1
            b=self.cana.create_text(375,50,text=n,font=("Arial",60),fill="black")
            
        if pos[2]>=500:
            self.x=-3
            global m
            a=self.cana.create_text(125,50,text=m,font=("Arial",60),fill="black")
            self.cana.itemconfig(a,fill="yellow")
            m = m + 1
            a=self.cana.create_text(125,50,text=m,font=("Arial",60),fill="black")
            
        if pos[3]>=400:
            self.y=-3
        if self.hit_paddle(pos)==True:
            self.x=3
        if self.hit_paddle1(pos):
            self.x=-3

    def hit_paddle(self,pos):
        paddle_pos=self.cana.coords(self.p.id)
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
            if pos[0]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
                return True
            return False
        
    def hit_paddle1(self,pos):
        paddle_pos=self.cana.coords(self.p1.id)
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
            if pos[2]>=paddle_pos[0] and pos[2]<=paddle_pos[2]:
                return True
            return False
 

class Paddle:
    def __init__(self,cana,color):
        self.cana=cana
        self.id=cana.create_rectangle(0,162,10,238,fill=color)
        self.y=0
        self.cana.bind_all('w',self.move_up)
        self.cana.bind_all('s',self.move_down)

    def draw(self):
        self.cana.move(self.id,0,self.y)
        pos=self.cana.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=400:
            self.y=0

    def move_up(self,evt):
        self.y=-3
    def move_down(self,evt):
        self.y=3
        
        
class Paddle1:
    def __init__(self,cana,color):
        self.cana=cana
        self.id=cana.create_rectangle(490,162,500,238,fill=color)
        self.y=0
        self.cana.bind_all('<KeyPress-Up>',self.move_up)
        self.cana.bind_all('<KeyPress-Down>',self.move_down)


    def draw(self):
        self.cana.move(self.id,0,self.y)
        pos=self.cana.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=400:
            self.y=0

    def move_up(self,evt):
        self.y=-3
    def move_down(self,evt):
        self.y=3


p=Paddle(cana,"blue")
p1=Paddle1(cana,"blue")
ball=Ball(cana,"red",p,p1)

while True:
    ball.draw()
    p.draw()
    p1.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)

    if m==5:
        cana.create_text(250,200,text="Player on the LEFT wins",font=("Arial",20))
        root.update()
        time.sleep(10000)
    if n==5:
        cana.create_text(250,200,text="Player on the RIGHT wins",font=("Arial",20))
        root.update()
        time.sleep(10000)
    

    


