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
        self.create()
        self.move()

    def create(self):
        self.body = g.Circle(g.Point(self.x,self.y),10)
        self.body.setFill("black")
        self.body.draw(w)



    def move(self):
        totalDist = math.sqrt(self.xDist**2 + self.yDist**2)
        unitVectorX = self.xDist/totalDist
        unitVectorY = self.yDist/totalDist
        self.body.move(unitVectorX*self.speed,unitVectorY*self.speed)
        #check if off map
        if self.body.getCenter().getX()<0 or self.body.getCenter().getX()>self.w.getWidth() or self.body.getCenter().getY()<0 or self.body.getCenter().getY()>self.w.getHeight():
            self.body.undraw()
        #otherwise, keep going
        else:
            self.w.after(10, self.move)
