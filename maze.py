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
		w = g.GraphWin('Level 2', 850, 650, autoflush = False)
		self.w = w
		#maze is 550 tall x 750 long but the extra 
		#is so u can display things on the side
		
		#outermost borders
		self.line_seg(g.Point(59, 9),g.Point(759, 9))
		self.line_seg(g.Point(9, 9),g.Point(9, 559))
		self.line_seg(g.Point(759, 9),g.Point(759, 559))
		self.line_seg(g.Point(9, 559),g.Point(759, 559))
		
		#upperleftside
		self.line_seg(g.Point(59,9),g.Point(59,59))
		self.line_seg(g.Point(59,59),g.Point(109,59))
		self.line_seg(g.Point(159,9),g.Point(159,59))
		self.line_seg(g.Point(159,59),g.Point(259,59))
		self.line_seg(g.Point(9,109),g.Point(59,109))
		self.line_seg(g.Point(109,109),g.Point(159,109))
		self.line_seg(g.Point(59,109),g.Point(59,159))
		self.line_seg(g.Point(109,109),g.Point(109,159))
		self.line_seg(g.Point(209,59),g.Point(209,259))
		self.line_seg(g.Point(159,109),g.Point(159,209))
		self.line_seg(g.Point(59,209),g.Point(159,209))
		self.line_seg(g.Point(59,209),g.Point(59,259))
		self.line_seg(g.Point(9,259),g.Point(59,259))
		self.line_seg(g.Point(259,109),g.Point(259,209))
		self.line_seg(g.Point(209,209),g.Point(259,209))
		self.line_seg(g.Point(309,9),g.Point(309,209))
		self.line_seg(g.Point(359,59),g.Point(359,159))
		self.line_seg(g.Point(309,159),g.Point(359,159))
		self.line_seg(g.Point(309,209),g.Point(359,209))
		self.line_seg(g.Point(359,209),g.Point(359,259))
		self.line_seg(g.Point(159,259),g.Point(309,259))
		self.line_seg(g.Point(159,259),g.Point(159,309))
		self.line_seg(g.Point(309,259),g.Point(309,309))
		self.line_seg(g.Point(109,209),g.Point(109,359))
		
		#lowerleftside
		self.line_seg(g.Point(9,309),g.Point(59,309))
		self.line_seg(g.Point(59,309),g.Point(59,509))
		self.line_seg(g.Point(59,509),g.Point(209,509))
		self.line_seg(g.Point(209,409),g.Point(209,509))
		self.line_seg(g.Point(109,409),g.Point(209,409))
		self.line_seg(g.Point(109,409),g.Point(109,459))
		self.line_seg(g.Point(109,459),g.Point(159,459))
		self.line_seg(g.Point(109,509),g.Point(109,559))
		self.line_seg(g.Point(159,359),g.Point(209,359))
		self.line_seg(g.Point(209,309),g.Point(209,359))
		self.line_seg(g.Point(209,309),g.Point(259,309))
		self.line_seg(g.Point(259,309),g.Point(259,359))
		self.line_seg(g.Point(259,359),g.Point(309,359))
		self.line_seg(g.Point(309,359),g.Point(309,459))
		self.line_seg(g.Point(309,459),g.Point(409,459))
		self.line_seg(g.Point(409,359),g.Point(409,459))
		self.line_seg(g.Point(409,359),g.Point(459,359))
		self.line_seg(g.Point(459,309),g.Point(459,359))
		self.line_seg(g.Point(309,309),g.Point(509,309))
		self.line_seg(g.Point(359,309),g.Point(359,409))
		self.line_seg(g.Point(259,409),g.Point(259,509))
		self.line_seg(g.Point(259,509),g.Point(409,509))
		self.line_seg(g.Point(309,509),g.Point(309,559))
		
		#lowerrightside
		self.line_seg(g.Point(459,509),g.Point(609,509))
		self.line_seg(g.Point(609,509),g.Point(609,559))
		self.line_seg(g.Point(559,409),g.Point(559,509))
		self.line_seg(g.Point(559,459),g.Point(659,459))
		self.line_seg(g.Point(659,459),g.Point(659,509))
		self.line_seg(g.Point(459,409),g.Point(459,459))
		self.line_seg(g.Point(459,459),g.Point(509,459))
		self.line_seg(g.Point(509,359),g.Point(509,459))
		self.line_seg(g.Point(509,359),g.Point(609,359))
		self.line_seg(g.Point(609,409),g.Point(659,409))
		self.line_seg(g.Point(659,259),g.Point(659,409))	
		self.line_seg(g.Point(659,309),g.Point(709,309))
		self.line_seg(g.Point(659,359),g.Point(759,359))	
		self.line_seg(g.Point(709,409),g.Point(709,509))
		self.line_seg(g.Point(709,509),g.Point(759,509))
		
		#upperrightside
		self.line_seg(g.Point(559,209),g.Point(559,359))
		self.line_seg(g.Point(509,209),g.Point(559,209))
		self.line_seg(g.Point(509,209),g.Point(509,309))
		self.line_seg(g.Point(409,259),g.Point(459,259))
		self.line_seg(g.Point(459,59),g.Point(459,259))
		self.line_seg(g.Point(409,209),g.Point(459,209))
		self.line_seg(g.Point(409,109),g.Point(409,209))
		self.line_seg(g.Point(409,59),g.Point(459,59))
		self.line_seg(g.Point(509,9),g.Point(509,59))
		self.line_seg(g.Point(509,59),g.Point(659,59))
		self.line_seg(g.Point(659,59),g.Point(659,209))
		self.line_seg(g.Point(609,209),g.Point(709,209))
		self.line_seg(g.Point(709,209),g.Point(709,259))
		self.line_seg(g.Point(609,209),g.Point(609,309))
		self.line_seg(g.Point(609,209),g.Point(609,309))
		self.line_seg(g.Point(509,109),g.Point(509,159))
		self.line_seg(g.Point(509,159),g.Point(659,159))
		self.line_seg(g.Point(509,109),g.Point(609,109))
		self.line_seg(g.Point(709,59),g.Point(709,159))
		self.line_seg(g.Point(709,59),g.Point(759,59))
		
		
		
		bould = self.make_boulder(g.Point(434,484))
		self.move_boulder_H(bould, True)

		self.w.getMouse()
		self.w.close()
		
				

		
	def line_seg(self, p1, p2):
		mline = g.Line(g.Point(p1.getX(), p1.getY()), g.Point(p2.getX(), p2.getY()))
		mline.setWidth(5)
		mline.draw(self.w)

 
M2 = maze(2)

































