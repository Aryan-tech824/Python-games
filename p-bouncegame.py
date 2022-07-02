from tkinter import *
import random
import time
root=Tk()
root.title("My First Game")
root.resizable(0,0)
root.wm_attributes("-topmost",1)
a=Canvas(root,width=500,height=500,bd=0,highlightthickness=0)
a.pack()
root.update()

class Ball:
    def __init__(self,a,p,color):
        self.a=a
        self.p=p
        self.id=a.create_oval(10,10,25,25,fill=color)
        self.a.move(self.id,245,100)
        start=[-3,-2,-1,1,2,3]
        random.shuffle(start)
        self.x=start[0]
        self.y=-3
        self.z=-1
        self.height=self.a.winfo_height()
        self.width=self.a.winfo_width()
        self.hit_bottom=False

    def hit_paddle(self,pos):
        paddle_pos=self.a.coords(self.p.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
            return False

    def draw(self):
        self.a.move(self.id,self.x,self.y)
        pos=self.a.coords(self.id)
        if pos[1]<=0:
            self.y=3
            self.z=self.z+1
        if pos[3]>=self.height:
            self.hit_bottom=True
            a.create_text(245,100,text="Game Over, your score is:")
            a.create_text(245,120,text=self.z)
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.width:
            self.x=-3
        if self.hit_paddle(pos)==True:
            self.y=-3
            
class paddle:
    def __init__(self,a,color):
        self.a=a
        self.id=a.create_rectangle(0,0,100,10,fill=color)
        self.a.move(self.id,200,300)
        self.x=0
        self.width=self.a.winfo_width()
        self.a.bind_all('a', self.turn_left)
        self.a.bind_all('d', self.turn_right)

    def draw(self):
        self.a.move(self.id,self.x,0)
        pos=self.a.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=self.width:
            self.x=0
        
    def turn_left(self,evt):
        self.x=-2
    def turn_right(self,evt):
        self.x=2
    
p=paddle(a,'blue')
ball=Ball(a,p,'red')

while 1:
    if ball.hit_bottom==False:
        ball.draw()
        p.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
