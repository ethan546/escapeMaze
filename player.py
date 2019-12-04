#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:43:15 2019

@author: yoojinkim1797
"""

import graphics as g
import math

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
        self.playerRadius = 35 
        self.detectionRange = 500
        self.create()
        
          
    def create(self): # draw the player
        
        self.body = g.Rectangle(g.Point(self.x-10, self.y-17.5), 
                                g.Point(self.x+10, self.y+12.5))
        #self.hitbox = g.Rectangle(g.Point(self.x-17.5, self.y-37.5), 
                                #g.Point(self.x+17.5, self.y+35))
        self.hitbox = g.Circle(g.Point(self.x, self.y),self.playerRadius) #circular hitbox
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
        self.leye = g.Circle(g.Point(self.x-5, self.y-25), 2.5)
        self.reye = g.Circle(g.Point(self.x+5, self.y-25), 2.5)
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
        self.leye.setFill('black')
        self.reye.setFill('black')
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
            self.leye.move(0, -20)
            self.reye.move(0, -20)
            
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
            self.leye.move(0, 20)
            self.reye.move(0, 20)
            
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
            self.leye.move(20, 0)
            self.reye.move(20, 0)
            
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
            self.leye.move(-20, 0)
            self.reye.move(-20, 0)
            
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
        
        
        
         
'''
Got rid of shield

class Shield:
    def __init__(self,win,x,y):
        self.w = win
        self.x = x
        self.y = y
        self.radius = 15
        self.create()
        self.activation()
    
    def create(self):
        self.body = g.Circle(g.Point(self.x, self.y), self.radius)
        self.body.setFill('purple')
        self.body.draw(self.w)
    
    def picked_up(self): # when player collides with shield, 
                        # shield gets deleted and player gains shielding powers
        distX = Player.hitbox.getCenter().getX() - self.body.getCenter().getX()
        distY = Player.hitbox.getCenter().getY() - self.body.getCenter().getY()
        totDist = math.sqrt((distX**2)+(distY**2))
        if totDist <= self.radius + Player.playerRadius:
            return True
        else:
            return False
        
    def activation(self):
        if self.picked_up():
            print('yo')
            
            self.w.after(100,self.body.undraw())
'''
            
        
    
class Health:
    def __init__(self,win,x,y):
        self.w = win
        self.x = x
        self.y = y
        self.length = 300
        self.damaged = False
        self.create()
        self.maintain()
        
    def create(self):
        self.body = g.Rectangle(g.Point(self.x, self.y-10),
                                g.Point(self.x+self.length, self.y+10))
        self.body.setFill('red')
        self.body.draw(self.w)
        
    def maintain(self):
        '''
        This function makes sure that the bar changes when player takes damage.
        '''
        if self.damaged:
            self.length -= 30
            self.body.undraw()
            self.create()
            self.damaged = False
            self.w.after(100, self.maintain)
    
    
            
            
        
    

w = g.GraphWin('CS Project Game', 1250, 700, autoflush = False) # autoflush equals 
                                                                # False for smoother movements
w.setBackground('white')
# S = Shield(w, 200, 100)
P = Player(w, 575, 350)
H = Health(w, 950, 685)
key = None
while key != 'q':
    key = w.checkKey()
    P.control(key)
w.close()