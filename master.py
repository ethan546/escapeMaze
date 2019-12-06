#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import graphics as g
import math
import random
import time


class Player:
    '''
    This class creates the graphics and basic movement controls of the player.
    A hitbox was added to interact with the environment. To simply coding, a circular
    hitbox was created instead of a rectangular hitbox.
    '''
    def __init__(self,win,x,y):
        self.w = win
        self.x = x
        self.y = y
        self.playerRadius = 20
        self.detectionRange = 500
        self.mazeName = M2
        self.create()


    def create(self): # draw the player

        self.body = g.Rectangle(g.Point(self.x-10, self.y-17.5),
                                g.Point(self.x+10, self.y+12.5))
        self.hitbox = g.Rectangle(g.Point(self.x-17.5, self.y-37.5),
                                g.Point(self.x+17.5, self.y+35))
        #self.hitbox = g.Circle(g.Point(self.x, self.y),self.playerRadius) #circular hitbox
        self.left_hand = g.Circle(g.Point(self.x+13.5, self.y+5), 4)
        self.right_hand = g.Circle(g.Point(self.x-13.5, self.y+5), 4)
        self.left_arm = g.Rectangle(g.Point(self.x-17.5, self.y-17.5),
                                    g.Point(self.x-10, self.y+5))
        self.right_arm = g.Rectangle(g.Point(self.x+10, self.y-17.5),
                                     g.Point(self.x+17.5, self.y+5))
        self.left_shoe = g.Circle(g.Point(self.x-5, self.y+30), 5)
        self.right_shoe = g.Circle(g.Point(self.x+5, self.y+30), 5)
        self.left_leg = g.Rectangle(g.Point(self.x, self.y+12.5),
                                    g.Point(self.x-10, self.y+30))
        self.right_leg = g.Rectangle(g.Point(self.x, self.y+12.5),
                                    g.Point(self.x+10, self.y+30))
        self.head = g.Circle(g.Point(self.x, self.y-25), 12.5)
        self.leye = g.Circle(g.Point(self.x-5, self.y-25), 3)
        self.reye = g.Circle(g.Point(self.x+5, self.y-25), 3)
        self.lpup = g.Circle(g.Point(self.x-5, self.y-25), 1)
        self.rpup = g.Circle(g.Point(self.x+5, self.y-25), 1)
        self.mouth = g.Circle(g.Point(self.x, self.y-18), 3)
        self.shield = g.Circle(g.Point(self.x, self.y), 37.5)

        self.hitbox.setFill('white')
        self.body.setFill('aqua')
        self.left_hand.setFill('orange')
        self.right_hand.setFill('orange')
        self.left_arm.setFill('blue')
        self.right_arm.setFill('blue')
        self.left_shoe.setFill('black')
        self.right_shoe.setFill('black')
        self.left_leg.setFill('brown')
        self.right_leg.setFill('brown')
        self.head.setFill('orange')
        self.leye.setFill('white')
        self.reye.setFill('white')
        self.lpup.setFill('black')
        self.rpup.setFill('black')
        self.mouth.setFill('black')
        self.shield.setFill('pink')

        #self.hitbox.draw(self.w) #see hitbox
        #self.shield.draw(self.w) #see shield
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
        self.leye.draw(self.w)
        self.reye.draw(self.w)
        self.lpup.draw(self.w)
        self.rpup.draw(self.w)
        self.mouth.draw(self.w)



    def control(self, key):
        if key == 'Up':
            canMove = True
            for tuple in self.mazeName.listOfWallPoints:
                if tuple[0].getX() < self.hitbox.getP1().getX() < tuple[1].getX() or tuple[0].getX() < self.hitbox.getP2().getX() < tuple[1].getX():
                    if tuple[0].getY() < self.hitbox.getP1().getY()-20 < tuple[1].getY():
                        canMove = False
            if canMove:
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
                self.leye.move(0, -20)
                self.reye.move(0, -20)
                self.lpup.move(0, -20)
                self.rpup.move(0, -20)
                self.mouth.move(0, -20)

        if key == 'Down':
            canMove = True
            for tuple in self.mazeName.listOfWallPoints:
                if tuple[0].getX() < self.hitbox.getP1().getX() < tuple[1].getX() or tuple[0].getX() < self.hitbox.getP2().getX() < tuple[1].getX():
                    if tuple[0].getY() < self.hitbox.getP2().getY()+20 < tuple[1].getY():
                        canMove = False
            if canMove:
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
                self.leye.move(0, 20)
                self.reye.move(0, 20)
                self.lpup.move(0, 20)
                self.rpup.move(0, 20)
                self.mouth.move(0, 20)

        if key == 'Right':
            canMove = True
            for tuple in self.mazeName.listOfWallPoints:
                if tuple[0].getX() < self.hitbox.getP2().getX() +20 < tuple[1].getX():
                    if tuple[0].getY() < self.hitbox.getP1().getY() < tuple[1].getY() or tuple[0].getY() < self.hitbox.getP2().getY() < tuple[1].getY():
                        canMove = False
            if canMove:
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
                self.leye.move(20, 0)
                self.reye.move(20, 0)
                self.lpup.move(20, 0)
                self.rpup.move(20, 0)
                self.mouth.move(20, 0)

        if key == 'Left':
            canMove = True
            for tuple in self.mazeName.listOfWallPoints:
                if tuple[0].getX() < self.hitbox.getP1().getX() -20 < tuple[1].getX():
                    if tuple[0].getY() < self.hitbox.getP1().getY() < tuple[1].getY() or tuple[0].getY() < self.hitbox.getP2().getY() < tuple[1].getY():
                        canMove = False
            if canMove:
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
                self.leye.move(-20, 0)
                self.reye.move(-20, 0)
                self.lpup.move(-20, 0)
                self.rpup.move(-20, 0)
                self.mouth.move(-20, 0)

        #elif key == 'space':
         #   Bullet(self.w, self.body.getCenter().getX(), self.body.getCenter().getY())
    def player_collision(self, other):
        self.other = other
        distX = self.body.getCenter().getX() - other.body.getCenter().getX()
        distY = self.body.getCenter().getY() - other.body.getCenter().getY()
        totDist = math.sqrt((distX**2)+(distY**2))
        #((distX**2)+(distY**2))**(1/2)
        if totDist <= other.radius + Player.playerRadius:
            self.body.move(0, 0)

    #if player_collision:

    def fire(self,point):
        if point:
            bullet = Bullet(self.w,self.right_hand.getCenter().getX(),self.right_hand.getCenter().getY(),point)

class Health:
    '''
    Make sure the name of the maze is correct
    '''
    def __init__(self,win,x,y):
        self.w = win
        self.x = x
        self.y = y
        self.length = 300
        self.damaged = False
        self.mazeName = M2
        self.create()
        self.maintain()


    def create(self):
        self.body = g.Rectangle(g.Point(self.x, self.y-10),
                                g.Point(self.x+self.length, self.y+10))
        self.body.setFill('red')
        self.body.draw(self.w)

    def maintain(self):
        '''
        This function makes sure the bar changes when we take damage
        '''
        if self.damaged:
            self.length -= 30
            self.body.undraw()
            self.create()
            self.damaged = False
            if self.length == 0:
                self.mazeName.game_going = False
        self.w.after(100, self.maintain)


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
        self.mazeName = M2
        #make sure the list of monsters is updated
        self.listOfMonsters = [monster1,monster2]
        self.create()
        self.move()

    def create(self):
        self.body = g.Circle(g.Point(self.x,self.y), self.radius)
        self.body.setFill("black")
        self.body.draw(self.w)

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

        #check if we hit a wall
        for tuple in self.mazeName.listOfWallPoints:
            if tuple[0].getX() < self.body.getCenter().getX() < tuple[1].getX():
                if tuple[0].getY() < self.body.getCenter().getY() < tuple[1].getY():
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
        self.playerRadius = P.playerRadius
        self.detectionRange = 500
        self.radius = 20
        self.speed = 5 #distance travelled per update
        self.patrolP2 = patrolP2
        self.isShot = False
        self.stunTime = 2000 #ms
        self.parts = []
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
        self.Leye = g.Circle(g.Point(self.x-self.radius*3/8,self.y), self.radius/3)
        self.Reye = g.Circle(g.Point(self.x+self.radius*3/8,self.y), self.radius/3)
        self.Lpup = g.Circle(g.Point(self.x-self.radius*3/8,self.y),self.radius/6)
        self.Rpup = g.Circle(g.Point(self.x+self.radius*3/8,self.y),self.radius/6)

        colorList = ['red', 'pink', 'cyan', 'orange']
        color = colorList[random.randint(0,3)]

        self.parts = [self.body, self.rectangle, self.circle1, self.circle2, self.circle3, self.circle4, self.Leye, self.Reye, self.Lpup, self.Rpup]
        for part in self.parts:

            part.setFill(color)
            part.setOutline(color)
            if part == self.Leye or part == self.Reye:
                part.setFill('white')
                part.setOutline('white')
            if part == self.Lpup or part == self.Rpup:
                part.setFill('black')
                part.setOutline('black')
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
        for part in self.parts:
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
            H.damaged = True
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

class maze:

	def __init__(self, lvl):
		self.lvl = lvl
		self.game_going = True #is game currently being played, False when game over
		self.listOfWallPoints = []
		if self.lvl == 1:
			self.create1()
		elif self.lvl == 2:
			self.create2()
		elif self.lvl == 3:
			self.create3()

	def make_boulder(self, ptC):
		boulder = g.Circle(g.Point(ptC.getX(), ptC.getY()), 25)
		boulder.setFill('gray')
		boulder.draw(self.w)
		return boulder

	def move_boulder_H(self, bould, directionr, lbound, rbound, speed):
		'''
		Function moves a boulder passed in left and right within the given bounds.
		bould: boulder graphic (type Circle)
		directionr: whether or not the boulder is currently moving right(boolean);
					True when boulder is moving right, False when it is moving left
		lbound: left-most bound boulder can reach; x-coordinate
		rbound: right-most bound boulder can reach; x-coordinate
		'''

		if directionr:
			if bould.getCenter().getX()+25 < rbound:
				bould.move(5, 0)
			elif bould.getCenter().getX()+25>=rbound:
				directionr = False
		else:
			if bould.getCenter().getX()-25 > lbound:
				bould.move(-5, 0)
			elif bould.getCenter().getX()-25<=lbound:
				directionr = True
		self.w.after(speed, self.move_boulder_H, bould, directionr, lbound, rbound, speed)

	def move_boulder_V(self, bould, directionu, tbound, bbound, speed):
		'''
		Function moves a boulder passed in left and right within the given bounds.
		bould: boulder graphic (type Circle)
		directionu whether or not the boulder is currently moving up(boolean);
					True when boulder is moving up, False when it is moving down
		tbound: top-most bound boulder can reach; y-coordinate
		bbound: bottom-most bound boulder can reach; y-coordinate
		'''
		if directionu:
			if bould.getCenter().getY()-25 > tbound:
				bould.move(0, -5)
			elif bould.getCenter().getY()-25 <= tbound:
				directionu = False
		else:
			if bould.getCenter().getY()+25 < bbound:
				bould.move(0, 5)
			elif bould.getCenter().getY()+25 >= bbound:
				directionu = True
		self.w.after(speed, self.move_boulder_V, bould, directionu, tbound, bbound, speed)



	def fire_trap(self, pt_topL, pt_bottR, trap_on, dur):
		trap = g.Rectangle(pt_topL, pt_bottR)
		if trap_on:
			trap.setFill('red')
			#trap.setOutline('red')
			trap.draw(self.w)
		else:
 			#trap = g.Rectangle(pt_topL, pt_bottR)
 			trap.setFill('white')
 			#trap.setOutline('white')
 			trap.draw(self.w)

		trap_on = not trap_on
		self.w.after(dur, self.fire_trap, pt_topL, pt_bottR, trap_on, dur)

	def create1(self):
		w1 = g.GraphWin('Level 1', 600, 600, autoflush = False)
		self.w = w1

		#drawing borders of map
		self.line_seg(g.Point(0,0),g.Point(0, 600))
		self.line_seg(g.Point(0,600),g.Point(600, 600))
		self.line_seg(g.Point(600,0),g.Point(600, 600))
		self.line_seg(g.Point(50,0),g.Point(600, 0))

		#the winning landing spot
		stairs = g.Rectangle(g.Point(0, 0),g.Point(70, 100))
		stairs.setFill('yellow')
		stairs.setOutline('yellow')
		stairs.draw(self.w)

		self.make_box(g.Point(70, 0), g.Point(100, 200))

		self.make_box(g.Point(200, 100), g.Point(250, 350))
		self.make_box(g.Point(0, 300), g.Point(200, 350))

		self.make_box(g.Point(300, 100), g.Point(600, 150))
		self.make_box(g.Point(300, 150), g.Point(350, 200))

		self.make_box(g.Point(300, 300), g.Point(450, 350))

		self.make_box(g.Point(500, 250), g.Point(550, 500))
		self.make_box(g.Point(350, 450), g.Point(500, 500))
		self.make_box(g.Point(350, 500), g.Point(400, 600))

		self.make_box(g.Point(50, 450), g.Point(300, 500))

		bould = self.make_boulder(g.Point(125, 75))
		self.move_boulder_H(bould, True, 100, 600, 50)


	def create2(self):

		w2 = g.GraphWin('Level 2', 750, 700, autoflush = False)
		self.w = w2
		#map is 700 tall x 750 long but the extra
		#is so u can display things on the side

		#drawing borders of map
		self.line_seg(g.Point(0,0),g.Point(0, 700))
		self.line_seg(g.Point(0,700),g.Point(750, 700))
		self.line_seg(g.Point(750,0),g.Point(750, 700))
		self.line_seg(g.Point(50,0),g.Point(750, 0))

		#the winning landing spot
		stairs = g.Rectangle(g.Point(0, 0),g.Point(70, 100))
		stairs.setFill('yellow')
		stairs.setOutline('yellow')
		stairs.draw(self.w)


		self.make_box(g.Point(70, 0), g.Point(250, 100))
		self.make_box(g.Point(200, 0), g.Point(250, 200))
		self.make_box(g.Point(0, 200), g.Point(150, 250))
		self.make_box(g.Point(0, 250), g.Point(50, 350))

		self.make_box(g.Point(100, 350), g.Point(350, 400))
		#self.make_box(g.Point(300, 300), g.Point(350, 350))
		self.make_box(g.Point(100, 400), g.Point(200, 450))
		self.make_box(g.Point(250, 400), g.Point(300, 450))

		self.make_box(g.Point(300, 100), g.Point(350, 200))
		self.make_box(g.Point(300, 200), g.Point(450, 250))
		self.make_box(g.Point(400, 0), g.Point(450, 350))

		self.make_box(g.Point(500, 0), g.Point( 750, 100))
		self.make_box(g.Point(700, 0), g.Point(750, 350))

		self.make_box(g.Point(500, 200), g.Point(650, 250))

		self.make_box(g.Point(0, 400), g.Point(50, 650))
		self.make_box(g.Point(100, 550), g.Point(250, 600))
		#self.make_box(g.Point(100, 600), g.Point(650, 650)) --
		self.make_box(g.Point(350, 500), g.Point(650, 550))
		self.make_box(g.Point(600, 350), g.Point(650, 500))
		#self.make_box(g.Point(550, 550), g.Point(600, 600))

		#self.make_box(g.Point(350, 450), g.Point(400, 500))
		#self.make_box(g.Point(400, 400), g.Point(550, 450))
		self.make_box(g.Point(500, 350), g.Point(550, 400))

		self.make_box(g.Point(700, 400), g.Point(750, 600))
		self.make_box(g.Point(0, 650), g.Point(750, 700))
		#self.make_box(g.Point(650, 600), g.Point(750, 650))--


		bould = self.make_boulder(g.Point(75,325))
		self.move_boulder_H(bould, True, 50, 400, 50)

		self.fire_trap(g.Point(350, 350), g.Point(500, 400), True, 2000)
		self.fire_trap(g.Point(150, 200), g.Point(300, 250), True, 2000)


	def create3(self):
		w3 = g.GraphWin('Level 3', 950, 700, autoflush = False)
		self.w = w3
		#map is 700 tall x 950 long

		#drawing borders of map
		self.line_seg(g.Point(0,0),g.Point(0, 700))
		self.line_seg(g.Point(0,700),g.Point(950, 700))
		self.line_seg(g.Point(950,0),g.Point(950, 700))
		self.line_seg(g.Point(50,0),g.Point(950, 0))

		#the winning landing spot
		stairs = g.Rectangle(g.Point(0, 0),g.Point(70, 100))
		stairs.setFill('yellow')
		stairs.setOutline('yellow')
		stairs.draw(self.w)

		#drawing the map
		self.make_box(g.Point(70, 0), g.Point(300, 50))

		self.make_box(g.Point(0, 150), g.Point(50, 400))

		self.make_box(g.Point(100, 150), g.Point(400, 200))
		self.make_box(g.Point(350, 100), g.Point(400, 150))
		self.make_box(g.Point(100, 200), g.Point(150, 500))

		self.make_box(g.Point(0, 650), g.Point(950, 700))
		self.make_box(g.Point(0, 450), g.Point(50, 650))
		self.make_box(g.Point(100, 600), g.Point(300, 650))
		self.make_box(g.Point(600, 500), g.Point(700, 650))
		self.make_box(g.Point(600, 450), g.Point(850, 500))
		self.make_box(g.Point(800, 200), g.Point(850, 450))
		self.make_box(g.Point(900, 450), g.Point(950, 650))


		self.make_box(g.Point(450, 0), g.Point(550, 300))

		self.make_box(g.Point(600, 0), g.Point(850, 50))
		self.make_box(g.Point(800, 50), g.Point(850, 100))

		self.make_box(g.Point(700, 150), g.Point(750, 200))

		self.make_box(g.Point(600, 200), g.Point(650, 350))
		self.make_box(g.Point(650, 300), g.Point(750, 350))

		self.make_box(g.Point(200, 300), g.Point(400, 500))
		self.make_box(g.Point(400, 400), g.Point(550, 500))

		self.make_box(g.Point(900, 100), g.Point(950, 400))

		#setting up obstacles
		bould = self.make_boulder(g.Point(175,275))
		self.move_boulder_H(bould, True, 150, 450, 50)

		bould2 = self.make_boulder(g.Point(775, 75))
		self.move_boulder_V(bould2, False, 50, 450, 50)

		self.fire_trap(g.Point(400, 100), g.Point(450, 200), True, 2500)
		self.fire_trap(g.Point(550, 300), g.Point(600, 500), True, 1000)
		self.fire_trap(g.Point(550, 150), g.Point(700, 200), True, 2000)


	def line_seg(self, p1, p2):
		mline = g.Line(g.Point(p1.getX(), p1.getY()), g.Point(p2.getX(), p2.getY()))
		mline.setWidth(5)
		mline.draw(self.w)

	def make_box(self, p1, p2):
		box = g.Rectangle(p1, p2)
		box.setFill('black')
		box.draw(self.w)
		self.listOfWallPoints.append((p1,p2))
		
#w = g.GraphWin('CS Project Game', 1250, 700, autoflush = False)
#w.setBackground('green')

lvl = 2


if lvl == 2:
    M2 = maze(2)
    P = Player(M2.w, 575, 350)
    H = Health(M2.w, 450, 660)
    monster1 = Monster(200,200,M2.w,'explore')
    monster2 = Monster(50,800,M2.w,'patrol',g.Point(300,300))

    key = None
    while key != 'q':
        key = M2.w.checkKey()
        P.control(key)
        click = M2.w.checkMouse()
        P.fire(click)
    M2.w.close()
