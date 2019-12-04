#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import graphics as g
import math
import random
import time


class Player:
    def __init__(self,win,x,y):
        self.w = win
        self.x = x
        self.y = y
        self.create()

    def create(self): # draw the player

        self.body = g.Rectangle(g.Point(self.x-20, self.y-35),
                                g.Point(self.x+20, self.y+25))
        self.hitbox = g.Rectangle(g.Point(self.x-35, self.y-75),
                                g.Point(self.x+35, self.y+70))
        self.left_hand = g.Circle(g.Point(self.x+27, self.y+10), 8)
        self.right_hand = g.Circle(g.Point(self.x-27, self.y+10), 8)
        self.left_arm = g.Rectangle(g.Point(self.x-35, self.y-35),
                                    g.Point(self.x-20, self.y+10))
        self.right_arm = g.Rectangle(g.Point(self.x+20, self.y-35),
                                     g.Point(self.x+35, self.y+10))
        self.left_shoe = g.Circle(g.Point(self.x-10, self.y+60), 10)
        self.right_shoe = g.Circle(g.Point(self.x+10, self.y+60), 10)
        self.left_leg = g.Rectangle(g.Point(self.x, self.y+25),
                                    g.Point(self.x-20, self.y+60))
        self.right_leg = g.Rectangle(g.Point(self.x, self.y+25),
                                    g.Point(self.x+20, self.y+60))
        self.head = g.Circle(g.Point(self.x, self.y-50), 25)

        self.hitbox.setFill('white')
        self.body.setFill('blue')
        self.left_hand.setFill('orange')
        self.right_hand.setFill('orange')
        self.left_arm.setFill('blue')
        self.right_arm.setFill('blue')
        self.left_shoe.setFill('black')
        self.right_shoe.setFill('black')
        self.left_leg.setFill('brown')
        self.right_leg.setFill('brown')
        self.head.setFill('orange')

        # self.hitbox.draw(self.w) see hitbox
        self.body.draw(self.w)
        self.left_hand.draw(self.w)
        self.right_hand.draw(self.w)
        self.left_arm.draw(self.w)
        self.right_arm.draw(self.w)
        self.left_shoe.draw(self.w)
        self.right_shoe.draw(self.w)
        self.left_leg.draw(self.w)
        self.right_leg.draw(self.w)
        self.head.draw(self.w)

    def control(self, key):
        if key == 'Up':
            self.hitbox.move(0, -20)
            self.body.move(0, -20)
            self.left_hand.move(0, -20)
            self.right_hand.move(0, -20)
            self.left_arm.move(0, -20)
            self.right_arm.move(0, -20)
            self.left_leg.move(0, -20)
            self.right_leg.move(0, -20)
            self.left_shoe.move(0, -20)
            self.right_shoe.move(0, -20)
            self.head.move(0, -20)

        if key == 'Down':
            self.hitbox.move(0, 20)
            self.body.move(0, 20)
            self.left_hand.move(0, 20)
            self.right_hand.move(0, 20)
            self.left_arm.move(0, 20)
            self.right_arm.move(0, 20)
            self.left_leg.move(0, 20)
            self.right_leg.move(0, 20)
            self.left_shoe.move(0, 20)
            self.right_shoe.move(0, 20)
            self.head.move(0, 20)

        if key == 'Right':
            self.hitbox.move(20, 0)
            self.body.move(20, 0)
            self.left_hand.move(20, 0)
            self.right_hand.move(20, 0)
            self.left_arm.move(20, 0)
            self.right_arm.move(20, 0)
            self.left_leg.move(20, 0)
            self.right_leg.move(20, 0)
            self.left_shoe.move(20, 0)
            self.right_shoe.move(20, 0)
            self.head.move(20, 0)

        if key == 'Left':
            self.hitbox.move(-20, 0)
            self.body.move(-20, 0)
            self.left_hand.move(-20, 0)
            self.right_hand.move(-20, 0)
            self.left_arm.move(-20, 0)
            self.right_arm.move(-20, 0)
            self.left_leg.move(-20, 0)
            self.right_leg.move(-20, 0)
            self.left_shoe.move(-20, 0)
            self.right_shoe.move(-20, 0)
            self.head.move(-20, 0)

        #elif key == 'space':
         #   Bullet(self.w, self.body.getCenter().getX(), self.body.getCenter().getY())
    def player_collision(self, other):
        self.other = other
        distX = self.body.getCenter().getX() - other.body.getCenter().getX()
        distY = self.body.getCenter().getY() - other.body.getCenter().getY()
        totDist = math.sqrt((distX**2)+(distY**2))
        #((distX**2)+(distY**2))**(1/2)
        if totDist <= other.getCenter() + Player.hitbox.getCenter():
            return True
        else:
            return False

    def fire(self,point):
        if point:
            bullet = Bullet(self.w,self.right_hand.getCenter().getX(),self.right_hand.getCenter().getY(),point)


    #if player_collision:


class Shield:
    def __init__(self,win,x,y):
        self.w = win
        self.x = x
        self.y = y
        self.create()

    def create(self):
        self.body = g.Circle(g.Point(self.x, self.y), 15)
        self.body.setFill('purple')
        self.body.draw(self.w)

    def picked_up(self): # when player collides with shield,
                        # shield gets deleted and player gains shielding powers
        distX = Player.body.getCenter().getX() - self.body.getCenter().getX()
        distY = Player.body.getCenter().getY() - self.body.getCenter().getY()
        totDist = math.sqrt((distX**2)+(distY**2))
        if totDist <= self.getCenter() + Player.hitbox.getCenter():
            Shield.remove()
            return True
        else:
            return False


class Health:
    def __init__(self,win,x,y):
        self.w = win
        self.x = x
        self.y = y
        self.create()

    def create(self):
        self.body = g.Rectangle(g.Point(self.x-140, self.y-10),
                                g.Point(self.x+140, self.y+10))
        self.body.setFill('red')
        self.body.draw(self.w)

    def loseHealth(self):
        if player_collision:
            Health.remove()

class Bullet:
    '''
    don't forget to add the fire function to the player:
    def fire(self,point):
        if point:
            bullet = Bullet(self.w,self.right_hand.getCenter().getX(),self.right_hand.getCenter().getY(),point)

    and put this in the "while key != 'q':" loop:
    click = w.checkMouse()
    P.fire(click)
    '''
    def __init__(self,window,x,y,point):
        self.w = window
        self.x = x
        self.y = y
        self.xDist = point.getX()-x
        self.yDist = point.getY()-y
        self.speed = 10
        self.radius = 10
        #make sure the list of monsters is updated
        self.listOfMonsters = [monster1,monster2]
        self.create()
        self.move()

    def create(self):
        self.body = g.Circle(g.Point(self.x,self.y), self.radius)
        self.body.setFill("black")
        self.body.draw(w)

    def determineCollisions(self):
        '''
        See if the object will collide with a monster or wall or screen border.
        If it doesn't collide, keep moving
        '''
        collision = False
        #check if it hits a monster
        for monster in self.listOfMonsters:
            xDist = monster.body.getCenter().getX()-self.body.getCenter().getX()
            yDist = monster.body.getCenter().getY()-self.body.getCenter().getY()
            totalDist = math.sqrt(xDist**2 + yDist**2)
            if totalDist <= self.radius+monster.radius:
                monster.isShot = True
                self.body.undraw()
                collision = True

        #check if off map
        if self.body.getCenter().getX()<0 or self.body.getCenter().getX()>self.w.getWidth() or self.body.getCenter().getY()<0 or self.body.getCenter().getY()>self.w.getHeight():
            self.body.undraw()
            collision = True

        #otherwise, keep going
        if not collision:
            self.w.after(10, self.move)


    def move(self):
        totalDist = math.sqrt(self.xDist**2 + self.yDist**2)
        unitVectorX = self.xDist/totalDist
        unitVectorY = self.yDist/totalDist
        self.body.move(unitVectorX*self.speed,unitVectorY*self.speed)
        self.determineCollisions()

class Monster:
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
        self.playerName = P
        self.playerRadius = 40
        self.detectionRange = 500
        self.radius = 40
        self.speed = 5 #distance travelled per update
        self.patrolP2 = patrolP2
        self.isShot = False
        self.stunTime = 2000 #ms
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

    def playerInRange(self):
        '''
        Checks if dist to player is within detection range
        Returns True/False
        '''
        xDist = self.playerName.body.getCenter().getX()-self.body.getCenter().getX()
        yDist = self.playerName.body.getCenter().getY()-self.body.getCenter().getY()
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
        if self.isShot:
            self.isShot = False
            self.w.after(self.stunTime,self.chasePlayer)
        else:
            xDist = self.playerName.body.getCenter().getX()-self.body.getCenter().getX()
            yDist = self.playerName.body.getCenter().getY()-self.body.getCenter().getY()
            totalDist = math.sqrt(xDist**2 + yDist**2)
            unitVectorX = xDist/totalDist
            unitVectorY = yDist/totalDist
            self.move(unitVectorX*self.speed,unitVectorY*self.speed)
            if self.playerCollision():
                self.w.after(self.stunTime,self.chasePlayer)
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
        if self.isShot:
            self.isShot = False
            self.w.after(self.stunTime,self.chasePlayer)
        else:
            if self.playerInRange():
                self.chasePlayer()
            else:
                self.w.after(100, self.wait)

    def patrol(self):
        '''
        Patrol between two points until player is in range, then chase them
        Starts at initial point, then goes to other point. Then back. And there. And back.
        '''
        if self.isShot:
            self.isShot = False
            self.w.after(self.stunTime,self.chasePlayer)
        else:
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
        if self.isShot:
            self.isShot = False
            self.w.after(self.stunTime,self.chasePlayer)
        else:
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


w = g.GraphWin('CS Project Game', 1250, 700, autoflush = False)
w.setBackground('green')
S = Shield(w, 200, 100)
P = Player(w, 575, 350)
H = Health(w, 1100, 685)
monster1 = Monster(200,200,w,'explore')
monster2 = Monster(50,800,w,'patrol',g.Point(300,300))

key = None
while key != 'q':
    key = w.checkKey()
    P.control(key)
    click = w.checkMouse()
    P.fire(click)
w.close()