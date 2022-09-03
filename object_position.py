from manimlib.imports import *
from tutorial.screen_grid import *
class Positions(Scene):
	def construct(self):
		grid = ScreenGrid()
		object = Dot()
		self.add(grid)
		for i in range(1,101):
			object.to_edge(LEFT,buff=2.0-((i*1.0)/100.0))
			self.add(object)
			self.wait(0.1)
		self.wait()