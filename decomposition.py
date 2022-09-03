#!/usr/bin/env python

from NumberCreature.Zee import *
from manimlib.imports import *

class Plot1(GraphScene):
    CONFIG = {
        "y_max" : 10,
        "y_min" : 0,
        "x_max" : 10,
        "x_min" : 0,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color" : BLUE, 
        "y_labeled_nums": range(0,10,1),
        "x_labeled_nums": range(0,10,1),
        "x_label_decimal":1,
        "y_label_direction": RIGHT,
        "x_label_direction": UP,
        "y_label_decimal":3
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : 7-x,  
                                    color = GREEN,
                                    x_min = self.x_min, 
                                    x_max = 7,
                                    )
        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()
        self.clear()

class Plot2(GraphScene):
    CONFIG = {
        "y_max" : 10,
        "y_min" : 0,
        "x_max" : 10,
        "x_min" : 0,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color" : BLUE, 
        "y_labeled_nums": range(0,10,1),
        "x_labeled_nums": range(0,10,1),
        "x_label_decimal":1,
        "y_label_direction": RIGHT,
        "x_label_direction": UP,
        "y_label_decimal":3
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : (10-2*x)/3,  
                                    color = RED,
                                    x_min = self.x_min, 
                                    x_max = 5,
                                    )
        raph = self.get_graph(lambda x : 1+x,  
                                    color = GREEN,
                                    x_min = self.x_min, 
                                    x_max = 9,
                                    )
        graph_text = TexMobject("2x + 3y = 10").rotate(math.atan(-1.5/3.0)).shift(1.7*DOWN)
        raph_text = TexMobject("-x + y = 1").rotate(math.atan(0.7))
        one = TextMobject("One Solution").shift(DOWN*3.5)
        no = TextMobject("No Solution").shift(DOWN*3.5)
        infinite = TextMobject("Infinite Solutions").shift(DOWN*3.5)
        self.play(
            ShowCreation(graph),
            run_time = 1
        )
        self.play(ShowCreation(raph),run_time=1)
        self.play(Write(graph_text))
        self.play(Write(raph_text))
        self.play(Write(one))
        self.wait()
        self.remove(graph)
        self.remove(raph)
        self.remove(graph_text)
        self.remove(raph_text)
        self.remove(one)
        graph = self.get_graph(lambda x : 3+x,  
                                    color = RED,
                                    x_min = self.x_min, 
                                    x_max = 7,
                                    )
        raph = self.get_graph(lambda x : 1+x,  
                                    color = GREEN,
                                    x_min = self.x_min, 
                                    x_max = 9,
                                    )
        graph_text = TexMobject("-x + y = 3").rotate(math.atan(0.7)).shift(UP+0.7*LEFT)
        raph_text = TexMobject("-x + y = 1").rotate(math.atan(0.7))

        self.play(
            ShowCreation(graph),
            run_time = 1
        )
        self.play(ShowCreation(raph),run_time=1)
        self.play(Write(graph_text))
        self.play(Write(raph_text))
        self.play(Write(no))
        self.wait()
        self.remove(graph)
        self.remove(raph)
        self.remove(graph_text)
        self.remove(raph_text)
        self.remove(no)
        graph = self.get_graph(lambda x : 1+x,  
                                    color = RED,
                                    x_min = self.x_min, 
                                    x_max = 9,
                                    )
        raph = self.get_graph(lambda x : 1+x,  
                                    color = GREEN,
                                    x_min = self.x_min, 
                                    x_max = 9,
                                    )
        graph_text = TexMobject("-x + y = 1").rotate(math.atan(0.7)).set_color(RED)
        raph_text = TexMobject("-2x + 2y = 2").rotate(math.atan(0.7)).set_color(GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 1
        )
        self.play(Write(graph_text))
        self.wait(2)
        self.play(ShowCreation(raph),run_time=1)
        
        self.play(Transform(graph_text,raph_text))
        self.play(Write(infinite))
        self.wait()
        self.clear()

class Decomposition(Scene):
	def D2Matrix(self):
		pass
	def AugMatrix(self,a,b):
		l = Line(np.array((0,0,0)),np.array((0,0,0))+UP)
		l.scale(a.get_height()/l.get_height())
		l.next_to(a,RIGHT)
		l.shift(RIGHT/2.0)
		b.next_to(l,RIGHT)
		b.shift(RIGHT/2.0)
		left_bracket = TexMobject("\\big[")
		right_bracket = TexMobject("\\big]")
		left_bracket.scale((a.get_height()+2*a.bracket_v_buff)/left_bracket.get_height())
		right_bracket.scale((a.get_height()+2*a.bracket_v_buff)/right_bracket.get_height())
		left_bracket.next_to(a,LEFT,a.bracket_h_buff)
		right_bracket.next_to(b,RIGHT,b.bracket_h_buff)
		vg = VGroup(a,b,l,left_bracket,right_bracket)
		return vg

	def NumberOfSolutionsIntro(self,header):
		previous = TextMobject("Previously, we have seen how to find the solutions of a system").scale(0.9)
		crevious = TextMobject("of n equations with n unknowns. Today, we will investigate when").scale(0.9)
		trevious = TextMobject("and whether such system of equations has solutions and how many").scale(0.9)
		mrevious = TextMobject("there are and what they are.").scale(0.9)
		previous.next_to(header,DOWN)
		crevious.next_to(previous,DOWN)
		trevious.next_to(crevious,DOWN)
		mrevious.next_to(trevious,DOWN)
		mrevious.to_edge(LEFT)
		self.play(Write(previous),run_time=4)
		self.play(Write(crevious),run_time=4)
		self.play(Write(trevious),run_time=4)
		self.play(Write(mrevious),run_time=2)
		self.wait(2)
		there = TextMobject("There are 3 possibilities:")
		one = TextMobject("1. There is only one solution.")
		two = TextMobject("2. There are no solutions.")
		many = TextMobject("3. There are infinitely many solutions.")
		there.next_to(mrevious,DOWN)
		one.next_to(there,DOWN)
		two.next_to(one,DOWN)
		many.next_to(two,DOWN)
		there.to_edge(LEFT)
		one.to_edge(LEFT)
		two.to_edge(LEFT)
		many.to_edge(LEFT)
		vg = VGroup(there, one, two, many)
		vg.shift(2*RIGHT+0.5*DOWN)
		self.play(Write(there),run_time=2)
		self.play(Write(one),run_time=2)
		self.play(Write(two),run_time=2)
		self.play(Write(many),run_time=2)
		self.wait(2)
		self.remove(previous)
		self.remove(crevious)
		self.remove(trevious)
		self.remove(mrevious)
		self.remove(there)
		self.remove(one)
		self.remove(two)
		self.remove(many)

	def NumberOfSolutions(self):
		header = TextMobject("Number of solutions of a system of Linear Equations").scale(1.2).set_color(MY_DEEP_PURPLE).to_edge(UP)
		self.play(Write(header),run_time=3)
		#self.NumberOfSolutionsIntro(header)
		single = TextMobject("Single Unique Solution").next_to(header,DOWN).set_color(GOLD_E)
		self.play(Write(single))
		t_scale=0.9
		pivots = TextMobject("When there are exactly n pivots, we get a unique solution.").scale(t_scale).next_to(single,DOWN)
		self.play(Write(pivots),run_time=4)
		lookat = TextMobject("Let's look at the following example.").scale(t_scale).next_to(pivots,DOWN)
		self.play(Write(lookat))
		eq1 = TexMobject("-x +","x","y = 1")
		eq1[1].set_color(BLACK)
		eq2 = TexMobject("2x + 3y = 10")
		eq1.next_to(lookat,DOWN)
		eq2.next_to(eq1,DOWN)
		eq1.to_edge(LEFT)
		eq2.to_edge(LEFT)
		eq1.shift(3*RIGHT)
		eq2.shift(3*RIGHT)
		self.play(Write(eq1))
		self.play(Write(eq2))
		elimination = TextMobject("After the elimination step, they become").move_to(lookat)
		self.play(Transform(lookat,elimination))
		geq1 = TexMobject("-x +","x"," y = 1").move_to(eq1)
		geq2 = TexMobject("xxx","5y = 12").move_to(eq2)
		geq1[1].set_color(BLACK)
		geq2[0].set_color(BLACK)
		self.play(Transform(eq1,geq1))
		self.play(Transform(eq2,geq2))
		self.wait(2)



	def construct(self):
		self.NumberOfSolutions()
		