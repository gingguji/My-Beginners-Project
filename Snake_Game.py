
from pdb import Restart
from tkinter import *
import random
from turtle import window_height, window_width

GameWidth = 1100
GameHeight=900
MoveSpeed=80
PixelSize=50
BodyParts=3
SnakeColor="Green"
FoodColor="Red"
BgColor="Black"

class Snake:
    def __init__(self):
        self.BodySize=BodyParts
        self.coordinates=[] 
        self.Squares=[]

        for i in range(self.BodySize):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = GameCanvas.create_rectangle(x,y,x+PixelSize,y+PixelSize,fill=SnakeColor,tags="Snake")
            self.Squares.append(square)


class Food:
    def __init__(self):
        x=random.randint(0,int(GameWidth/PixelSize)-1)*PixelSize
        y=random.randint(0,int(GameHeight/PixelSize)-1)*PixelSize
        self.coordinates=[x,y]
        GameCanvas.create_oval(x,y,x+PixelSize,y+PixelSize,fill=FoodColor,tag="food")
         
def turning(snake,food):
    x,y=snake.coordinates[0]

    if SnakeDirection=="up":
        y-=PixelSize
    elif SnakeDirection=="down":
        y+=PixelSize
    elif SnakeDirection=="left":
        x-=PixelSize
    elif SnakeDirection=="right":
        x+=PixelSize

    snake.coordinates.insert(0,(x,y))
    square=GameCanvas.create_rectangle(x,y,x+PixelSize,y+PixelSize,fill=SnakeColor)
    snake.Squares.insert(0,square)

    if x==food.coordinates[0] and y==food.coordinates[1]:
        global score
        score+=1
        ScoreLabel.config(text="Score: {}".format(score))

        GameCanvas.delete("food")
        food=Food()
    
    else:
        del snake.coordinates[-1]
        GameCanvas.delete(snake.Squares[-1])
        del snake.Squares[-1]
    
    if CheckCollisions(snake):
        GameOver()
    else:
        window.after(MoveSpeed,turning, snake,food)
    

def ChangeDirection(NewDirection):
    global SnakeDirection
    
    if NewDirection == "up":
        if SnakeDirection!="down":
            SnakeDirection=NewDirection
    if NewDirection == "down":
        if SnakeDirection!="up":
            SnakeDirection=NewDirection
    if NewDirection == "right":
        if SnakeDirection!="left":
            SnakeDirection=NewDirection
    if NewDirection == "left":
        if SnakeDirection!="right":
            SnakeDirection=NewDirection

def CheckCollisions(snake):
    x,y=snake.coordinates[0]
    if x <0 or x>= GameWidth:
        return True
    elif y<0 or y>= GameWidth:
        return True

    for body in snake.coordinates[1:]:
        if x == body[0] and y == body[1]:
            return True
    return False

def GameOver():
    GameCanvas.delete(ALL)
    GameCanvas.create_text(GameCanvas.winfo_width()/2,GameCanvas.winfo_height()/2, font=("roboto",40), text="GameOver",fill=FoodColor, tags="GameOver")
 

window=Tk()
window.title("Snake Game")
window.resizable(False,False)

score=0
SnakeDirection="down"

ScoreLabel=Label(window, text="Score: {}".format(score), font=("roboto", 40))
ScoreLabel.pack()

GameCanvas= Canvas(window, bg=BgColor, height=GameHeight,width=GameWidth)
GameCanvas.pack()

window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()

screenwidth=window.winfo_screenwidth()
ScreenHeigth=window.winfo_screenheight()

x=int((screenwidth/2)-(window_width/2))
y=int((ScreenHeigth/2)- (window_height/1.8))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Up>", lambda event:ChangeDirection("up"))
window.bind("<Down>", lambda event:ChangeDirection("down"))
window.bind("<Right>", lambda event:ChangeDirection("right"))
window.bind("<Left>", lambda event:ChangeDirection("left"))

snake=Snake()
food=Food()
turning(snake,food)

window.mainloop()

