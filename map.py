import graphics as g
import math

class maze:
	def __init__(self, lvl):
		self.lvl = lvl
		self.game_going = True #is game currently being played, False when game over
		
		if self.lvl == 2:
			self.create2()
			
	def make_boulder(self, ptC):
		boulder = g.Circle(g.Point(ptC.getX(), ptC.getY()), 25)
		boulder.setFill('gray')
		boulder.draw(self.w)
		return boulder
		
	def move_boulder_H(self, bould, directionr):#should also include paramaters for (left + right) bounds like 259 and 559 are here
		#directionr: True when moving right, False when moving left
		if directionr:
			#559 is right bound in conditional, 259 is left
			if bould.getCenter().getX()+25 < 559:
				bould.move(5, 0)
			elif bould.getCenter().getX()+25>=559:
				directionr = False
		else:
			if bould.getCenter().getX()-25 > 259:
				bould.move(-5, 0)
			elif bould.getCenter().getX()-25<=259:
				directionr = True
		self.w.after(4, self.move_boulder_H, bould, directionr)

	def fire_trap(self, pt_topL, pt_topR, pt_bottL, pt_bottR):
		#pass
		#use after() to time the on and off
		self.trap_on = False
 		
		self.trap_on = not self.trap_on
		self.w.after(5, self.fire_trap, self.trap_on)
			
		
			
		

		
	def create2(self):
	
		w = g.GraphWin('Level 2', 750, 800, autoflush = False)
		self.w = w
		#maze is 550 tall x 750 long but the extra 
		#is so u can display things on the side
		
		self.make_box(g.Point(50, 0), g.Point(250, 100))
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
		self.make_box(g.Point(100, 600), g.Point(650, 650)) 
		self.make_box(g.Point(350, 500), g.Point(650, 550))
		self.make_box(g.Point(600, 350), g.Point(650, 500))
		self.make_box(g.Point(550, 550), g.Point(600, 600))
		
		#self.make_box(g.Point(350, 450), g.Point(400, 500))
		#self.make_box(g.Point(400, 400), g.Point(550, 450))
		self.make_box(g.Point(500, 350), g.Point(550, 400))
		
		self.make_box(g.Point(700, 400), g.Point(750, 600))
		self.make_box(g.Point(650, 600), g.Point(750, 650))
		
		
		bould = self.make_boulder(g.Point(434,484))
		self.move_boulder_H(bould, True)

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
	

 
M2 = maze(2)