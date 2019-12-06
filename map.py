import graphics as g
class maze:

	def __init__(self, lvl):
		self.lvl = lvl
		self.game_going = True #is game currently being played, False when game over
		self.listOfWallPoints = []
		self.listOfTrapPoints = []
		if self.lvl == 1:
			self.create1()
		elif self.lvl == 2:
			self.create2()
		elif self.lvl == 3:
			self.create3()

	def make_boulder(self, ptC):
		'''
		Creates boulder of radius 25 and fills it gray. Returns graphic Circle object.
		ptC: center of where boulder should be first drawn, graphic Point object
		boulder: Circle object representing the boulder
		'''
		boulder = g.Circle(g.Point(ptC.getX(), ptC.getY()), 25)
		boulder.setFill('gray')
		boulder.draw(self.w)
		return boulder

#####check for boulder collisions but Player is needed for this to run

# 	def checkPlayerCollision(self,bould):
# 		'''
# 		Checks if the boulder colides with the player
# 		Return True/False
# 		'''
# 
# 		xDist = P.body.getCenter().getX()-bould.getCenter().getX()
# 		yDist = P.body.getCenter().getY()-bould.getCenter().getY()
# 		totalDist = math.sqrt(xDist**2 + yDist**2)
# 		if totalDist <= 50:
# 			H.damaged = True


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

		#self.checkPlayerCollision(bould)

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

		#self.checkPlayerCollision(bould)

		self.w.after(speed, self.move_boulder_V, bould, directionu, tbound, bbound, speed)
		
###### call to create 1st level map #########	
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
		
		#drawing walls
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
		
		self.w.getMouse()
		self.w.close()

###### call to create 2nd level map #########	
	def create2(self):

		w2 = g.GraphWin('Level 2', 750, 700, autoflush = False)
		self.w = w2

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
		
		#drawing walls
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
		self.make_box(g.Point(350, 500), g.Point(650, 550))
		self.make_box(g.Point(600, 350), g.Point(650, 500))

		self.make_box(g.Point(500, 350), g.Point(550, 400))

		self.make_box(g.Point(700, 400), g.Point(750, 600))
		self.make_box(g.Point(0, 650), g.Point(750, 700))


		bould = self.make_boulder(g.Point(75,325))
		self.move_boulder_H(bould, True, 50, 400, 50)


		self.trapl2t1 = fire_trap(self.w, g.Point(350, 350), g.Point(500, 400), 2000)
		self.listOfTrapPoints.append((g.Point(350, 350), g.Point(500, 400), self.trapl2t1))
		self.trapl2t2 = fire_trap(self.w, g.Point(150, 200), g.Point(300, 250), 2000)
		self.listOfTrapPoints.append((g.Point(150, 200), g.Point(300, 250), self.trapl2t2))
		
		self.w.getMouse()
		self.w.close()

###### call to create 3rd level map #########	
	def create3(self):
		w3 = g.GraphWin('Level 3', 950, 700, autoflush = False)
		self.w = w3

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

		self.trapl3t1 = fire_trap(self.w, g.Point(400, 100), g.Point(450, 200), 2500)
		self.listOfTrapPoints.append((g.Point(400, 100), g.Point(450, 200), self.trapl3t1))
		self.trapl3t2 = fire_trap(self.w, g.Point(550, 300), g.Point(600, 500), 1000)
		self.listOfTrapPoints.append((g.Point(550, 300), g.Point(600, 500), self.trapl3t2))
		self.trapl3t3 = fire_trap(self.w, g.Point(550, 150), g.Point(700, 200), 2000)
		self.listOfTrapPoints.append((g.Point(550, 150), g.Point(700, 200), self.trapl3t3))

		self.w.getMouse()
		self.w.close()

	def line_seg(self, p1, p2):
		mline = g.Line(g.Point(p1.getX(), p1.getY()), g.Point(p2.getX(), p2.getY()))
		mline.setWidth(5)
		mline.draw(self.w)

	def make_box(self, p1, p2):
		box = g.Rectangle(p1, p2)
		box.setFill('black')
		box.draw(self.w)
		self.listOfWallPoints.append((p1,p2))



class fire_trap:
	def __init__(self, window, pt1, pt2, dur):
		self.w = window
		self.p1 = pt1
		self.p2 = pt2
		self.time = dur
		self.create()
		self.run()

	def create(self):
		'''
		Draws the fire trap at the given coordinates defined in __init__
		'''
		self.trap = g.Rectangle(self.p1, self.p2)
		self.trap_on = True
		self.trap.setFill('red')
		self.trap.draw(self.w)

	def run(self):
		'''
		Turns trap on and off for intervals of a given duration defined in __init__. Draws 
		the trap in red or white depending if its on/off.
		'''
		if self.trap_on:
			self.trap.setFill('white')
			self.trap.undraw()
			self.trap.draw(self.w)
		else:
			self.trap.setFill('red')
			self.trap.undraw()
			self.trap.draw(self.w)
		self.trap_on = not self.trap_on
		self.w.after(self.time, self.run)
		
		
M1 = maze(1)
M2 = maze(2)
M3 = maze(3)
