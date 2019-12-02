#!/usr/bin/env python3
import graphics as g

class Player:
    def __init__(self,window,x,y):
        self.w = window
        self.x = x
        self.y = y
        self.create()

    def create(self):
        self.body = g.Circle(g.Point(self.x,self.y),40)
        self.body.setFill('red')
        self.body.draw(self.w)

    def control(self,key):
        if key == "Up":
            if self.y > 40:
                self.body.move(0,-5)
                self.y -= 5
        if key == "Down":
            if self.y < 460:
                self.body.move(0,5)
                self.y += 5
        if key == "Left":
            if self.x > 40:
                self.body.move(-5,0)
                self.x -= 5
        if key == "Right":
            if self.x < 460:
                self.body.move(5,0)
                self.x += 5

    def fire(self,point):
        if point:
            self.shot = g.Line(g.Point(self.x,self.y),point)
            self.shot.setFill("yellow")
            self.shot.setWidth(5)
            self.shot.draw(self.w)

def controlPlayer(player,window):
    key = None
    while key != "q":
        key = window.checkKey()
        player.control(key)
        click = window.checkMouse()
        player.fire(click)
    window.close()

if __name__ == '__main__':
    w = g.GraphWin("window",500,500)
    w.setBackground('black')
    p1 = Player(w,250,250)

    controlPlayer(p1,w)
