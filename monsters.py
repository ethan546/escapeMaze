#!/usr/bin/env python3

import graphics as g
import lab29
import math
import random
import time

class Monster():
    '''
    This is the parent monster class that does all the generic monster things
    We make it a thread so it moves, and waits, independently of the player

    MONSTERS MUST BE DECLARED AFTER PLAYER

    Still can't get the threading to work
    '''

#--------------------------------------
#This is initialization and drawing
#--------------------------------------
    def __init__(self,xPosition,yPosition,window,behavior,patrolP2=g.Point(100,100)):
        '''
        we pass arguments that do the following:
        give spawn position,
        give window to draw in
        set monster behavior
        point to patrol to (and from)
        '''
        #start as a new thread
        self.x = xPosition
        self.y = yPosition
        self.w = window
        self.behavior = behavior
        #change to the name of the player object that is created
        self.playerName = examplePlayer
        self.playerRadius = 40
        self.detectionRange = 500
        self.radius = 40
        self.speed = 5 #distance travelled per update
        self.patrolP2 = patrolP2

        self.create()

    def create(self):
        '''
        draw the sprite and call the proper behavior
        '''
        self.body = g.Circle(g.Point(self.x,self.y),self.radius)
        self.circle1=g.Circle(g.Point(self.x-self.radius*3/4,self.y+self.radius),self.radius/4)
        self.circle2=g.Circle(g.Point(self.x-self.radius/4,self.y+self.radius),self.radius/4)
        self.circle3=g.Circle(g.Point(self.x+self.radius/4,self.y+self.radius),self.radius/4)
        self.circle4=g.Circle(g.Point(self.x+self.radius*3/4,self.y+self.radius),self.radius/4)
        self.rectangle=g.Rectangle(
            g.Point(self.x-self.radius,self.y),g.Point(self.x+self.radius,self.y+self.radius))

        parts = [self.body, self.rectangle, self.circle1, self.circle2, self.circle3, self.circle4]
        for part in parts:
            part.setFill('grey')
            part.setOutline('grey')
            part.draw(self.w)

        if self.behavior =='wait':
            self.wait()
        elif self.behavior =='patrol':
            self.patrolDirecton = 'towards P2'
            self.patrol()
        elif self.behavior =='explore':
            self.exploreCounter = 0
            self.explore()
        if self.behavior =='chase':
            self.chasePlayer()

#--------------------------------------
#behavior-related functions
#--------------------------------------
    def move(self, dx, dy):
        parts = [self.body, self.rectangle, self.circle1, self.circle2, self.circle3, self.circle4]
        for part in parts:
            part.move(dx,dy)

    def checkIfShot(self):
        pass

    def playerInRange(self):
        '''
        Checks if dist to player is within detection range
        Returns True/False
        '''
        xDist = self.playerName.hitbox.getCenter().getX()-self.body.getCenter().getX()
        yDist = self.playerName.hitbox.getCenter().getY()-self.body.getCenter().getY()
        totalDist = math.sqrt(xDist**2 + yDist**2)
        if totalDist <= self.detectionRange:
            return True
        else:
            return False

    def playerCollision(self):
        '''
        Checks if the monster colides with the player
        Return True/False

        also assumes that the player is a sphere
        '''
        xDist = self.playerName.body.getCenter().getX()-self.body.getCenter().getX()
        yDist = self.playerName.body.getCenter().getY()-self.body.getCenter().getY()
        totalDist = math.sqrt(xDist**2 + yDist**2)
        if totalDist <= self.radius+self.playerRadius:
            return True
        else:
            return False

    def chasePlayer(self):
        '''
        This is how our monsters chase the player
        '''
        xDist = self.playerName.hitbox.getCenter().getX()-self.body.getCenter().getX()
        yDist = self.playerName.hitbox.getCenter().getY()-self.body.getCenter().getY()
        totalDist = math.sqrt(xDist**2 + yDist**2)
        unitVectorX = xDist/totalDist
        unitVectorY = yDist/totalDist
        self.move(unitVectorX*self.speed,unitVectorY*self.speed)
        if self.playerCollision():
            self.w.after(2000,self.chasePlayer)
        else:
            self.w.after(100, self.chasePlayer)

    def getExploreMove(self):
        x = random.randint(-5,5)/10
        y = random.randint(-5,5)/10
        self.exploreCounter = random.randint(0,100)
        return x,y

#--------------------------------------
#actual behavior functions
#--------------------------------------
    def wait(self):
        '''
        Wait until player is in range, then chase them
        '''
        if self.playerInRange():
            self.chasePlayer()
        else:
            self.w.after(100, self.wait)

    def patrol(self):
        '''
        Patrol between two points until player is in range, then chase them
        Starts at initial point, then goes to other point. Then back. And there. And back.
        '''
        if self.playerInRange():
            self.chasePlayer()
        else:
            #first we get the direction we patrol in:
            if self.body.getCenter()==self.patrolP2:
                self.patrolDirecton = 'towards origin'
            elif self.body.getCenter()==g.Point(self.x,self.y):
                self.patrolDirecton = 'towards P2'

            #get distance to P2
            xDist = self.patrolP2.getX() - self.body.getCenter().getX()
            yDist = self.patrolP2.getY() - self.body.getCenter().getY()
            DistToP2 = math.sqrt(xDist**2 + yDist**2)
            unitVectorX = xDist/DistToP2
            unitVectorY = yDist/DistToP2

            #get distance to origin
            xDist = self.x - self.body.getCenter().getX()
            yDist = self.y - self.body.getCenter().getY()
            DistToOrigin = math.sqrt(xDist**2 + yDist**2)


            #decide where we are heading
            if DistToP2 < self.speed:
                self.patrolDirecton = 'towards origin'
            elif DistToOrigin < self.speed:
                self.patrolDirecton = 'towards P2'

            #finally, we actually move
            if self.patrolDirecton == 'towards P2':
                self.move(unitVectorX*self.speed,unitVectorY*self.speed)
            elif self.patrolDirecton == 'towards origin':
                self.move(-unitVectorX*self.speed,-unitVectorY*self.speed)

            #then patrol again
            self.w.after(100, self.patrol)

    def explore(self):
        '''
        just walk around(and don't hit walls?) until player is in detection range. Then chase
        '''
        if self.playerInRange():
            self.chasePlayer()
        else:
            currentX = self.body.getCenter().getX()
            currentY = self.body.getCenter().getY()

            #get a random direction to move in
            if self.exploreCounter == 0:
                self.xMotion,self.yMotion = self.getExploreMove()

            #make sure the random move won't send the monster off the map
            if self.xMotion + currentX > self.w.getWidth()-self.radius:
                self.xMotion = -0.5
            elif self.xMotion+currentX < self.radius:
                self.xMotion = 0.5
            if self.yMotion + currentY >self.w.getHeight()-self.radius:
                self.yMotion = -0.5
            elif self.yMotion+currentY < self.radius:
                self.yMotion = 0.5


                #get a new direction
            self.move(self.xMotion*self.speed,self.yMotion*self.speed)
            self.exploreCounter-=1

            self.w.after(100, self.explore)

#--------------------------------------
#End of class, start of main
#--------------------------------------

if __name__ == '__main__':
    w = g.GraphWin('test window',1000,1000,autoflush=False)
    examplePlayer = lab29.Player(w,800,800)

    waitMonster = Monster(400,400,w,'wait')
    patrolMonster = Monster(50,800,w,'patrol',g.Point(300,300))
    #patrolChaseMonster = Monster(50,800,w,'patrol',g.Point(550,550))
    #chaseMonster = Monster(700,100,w,'chase')
    exploreMonster = Monster(200,200,w,'explore')

    #this is just used to see if we can detect a player's position
    def controlPlayer(player,window):
        key = None
        while key != "q":
            key = window.checkKey()
            player.control(key)
            click = window.checkMouse()
            player.fire(click)
        window.close()

    controlPlayer(examplePlayer,w)
    #imported from lab 29
    w.close()
