#!/usr/bin/env python

from NumberCreature.Zee import *
from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)



class GT(Scene):
    def Intro(self):
        ds = TextMobject("G","R","A","P","H"," T","H","E","O","R","Y")
        color = [PURPLE_A,PURPLE_B,PURPLE_C,PURPLE_D, PURPLE_E,BLUE_C,BLUE_D,BLUE_E,RED_A,RED_B,RED_C]

        for i,j in zip(ds,color):
            i.set_color(j)
        ds.scale(2)
        zadid = TextMobject("M","A","T","3","2","4").scale(2)
        zadid_color = [GREEN_E,GREEN_D,GREEN_C,GREEN_B,GREEN_A,WHITE]
        zadid = self.ColorSetter(zadid,zadid_color)
        zadid.next_to(ds,UP)
        self.play(GrowFromCenter(ds),GrowFromCenter(zadid))
        self.wait(2)

    def ColorSetter(self, text, color):
        for i,j in zip(text,color):
            i.set_color(j)
        return text

    def construct(self):
        self.Intro()

class LA(Scene):
    def CourseIntro(self):
        ds = TextMobject("L","I","N","E","A","R"," ","A","L","G","E","B","R","A")
        color = [PURPLE_A,PURPLE_B,PURPLE_C,PURPLE_D, PURPLE_E, BLUE_A,BLUE_B,BLUE_C,BLUE_D,BLUE_E,RED_A,RED_B,RED_C, RED_D, RED_E]
        for i,j in zip(ds,color):
            i.set_color(j)
        ds.scale(2.7)
        zadid = TextMobject("\\&","F","O","U","R","I","E","R"," ","A","N", "A","L","Y","S","I","S")
        zadid.set_color(TEAL)
        zadid.shift(DOWN)
        self.play(GrowFromCenter(ds),GrowFromCenter(zadid))
        self.wait(2)
        self.clear()
    def ALUIntro(self):
        lec = TextMobject("Lecture 14").scale(2)
        rec = TextMobject("Projection")
        rec[0].set_color(GREEN_E)
        lec.shift(UP)
        lec.set_color(TEAL)
        rec.scale(2)
        fac = TextMobject("ZADID HASAN (MZH)").set_color(YELLOW)
        fac.next_to(rec,DOWN)
        self.play(Write(lec),Write(rec))
        self.wait(2)
        self.clear()
    
    def NumberCreature(self):
        Ale=Alex().to_edge(DOWN)
        palabras_ale = TextMobject("Welcome to Linear Algebra!!\\\\And I am Zadid.")
        self.add(Ale)
        self.play(NumberCreatureSays(
            Ale, palabras_ale, 
            bubble_kwargs = {"height" : 4, "width" : 6},
            target_mode="speaking"
        ))
        self.wait()
        self.play(Blink(Ale))
        self.wait(1)
        self.play(Blink(Ale))
        self.wait()
        self.clear()
    def construct(self):
        self.CourseIntro()
        self.ALUIntro()
        #self.NumberCreature()

class Intro(Scene):
    def NumberCreature(self):
        Ale=Alex().to_edge(DOWN)
        palabras_ale = TextMobject("Hi. I am Zadid.\\\\Nice to meet you all.")
        self.add(Ale)
        self.play(NumberCreatureSays(
            Ale, palabras_ale, 
            bubble_kwargs = {"height" : 4, "width" : 6},
            target_mode="speaking"
        ))
        self.wait()
        self.play(Blink(Ale))
        self.wait(1)
        self.play(Blink(Ale))
        self.wait(1)
        self.clear()

    def CourseIntro(self):
        ds = TextMobject("D","A","T","A"," ","S","T","R","U","C","T","U","R","E","S")
        color = [PURPLE_A,PURPLE_B,PURPLE_C,PURPLE_D, BLACK, BLUE_A,BLUE_B,BLUE_C,BLUE_D,BLUE_E,RED_A,RED_B,RED_C, RED_D, RED_E]
        for i,j in zip(ds,color):
            i.set_color(j)
        ds.scale(2.7)
        zadid = TextMobject("Z","A","D","I","D"," ","H","A","S","A","N", " ", "(MZH)")
        zadid.set_color(TEAL)
        zadid.shift(DOWN)
        self.play(GrowFromCenter(ds),GrowFromCenter(zadid))
        self.wait(2)
        self.clear()
    def RecursionIntro(self):
        lec = TextMobject("Lecture 11")
        rec = TextMobject("Sorting and Searching")
        lec.shift(UP)
        lec.set_color(TEAL)
        rec.set_color(ORANGE)
        rec.scale(2)
        self.play(Write(lec),Write(rec))
        self.wait(2)
        self.clear()
    def RecSquare(self,a,b,c,d,n):
        if n == 10:
            return
        fill = RED
        col = ORANGE
        if n%2 == 0:
            fill = BLUE
            col = GREEN
        square = Polygon(a,b,c,d,stroke_width=0.5,fill_opacity = 1,fill_color = fill)
        self.play(DrawBorderThenFill(square))
        p = (a+b)/2.0
        q = (b+c)/2.0
        r = (c+d)/2.0
        s = (d+a)/2.0
        self.RecSquare(p,q,r,s,n+1)
    def WriteSentenceList(self,sentences,upper_left_point,scale,color):
        first = True
        prev = None
        starter = upper_left_point
        for s in sentences:
            s.set_color(color)
            s.scale(scale)
            s.move_to(starter)
            self.play(FadeIn(s))
            prev = s
            starter = starter + DOWN/2.0
    def SquareDrawing(self):
        recur = TextMobject("What is", " \"Recursion\"","?")
        recur[1].set_color(PINK)
        recur.to_edge(UP)
        recur.scale(1.5)
        self.play(Write(recur))
        lookat = TextMobject("Look at the following video.")
        whatis = TextMobject("What is happening?")
        whatis.shift(DOWN)
        lookat.set_color(GREY)
        whatis.set_color(MAROON)
        self.play(Write(lookat))
        self.play(Write(whatis))
        self.wait()
        self.clear()
        b = np.array((2,2,0))
        a = np.array((-2,2,0))
        d = np.array((-2,-2,0))
        c = np.array((2,-2,0))
        self.RecSquare(a,b,c,d,0)
        self.clear()
        p = (a+b)/2.0
        q = (b+c)/2.0
        r = (c+d)/2.0
        s = (d+a)/2.0
        square = Polygon(a,b,c,d,stroke_width=0.5,fill_opacity = 1,fill_color = ORANGE)
        inner_square = Polygon(p,q,r,s,stroke_width=0.5,fill_opacity = 1,fill_color = GREEN_SCREEN)
        self.play(DrawBorderThenFill(square),DrawBorderThenFill(inner_square))
        A = TextMobject("A")
        B = TextMobject("B")
        C = TextMobject("C")
        D = TextMobject("D")
        P = TextMobject("P")
        Q = TextMobject("Q")
        R = TextMobject("R")
        S = TextMobject("S")
        A.move_to(a+UL/2)
        B.move_to(b+UR/2)
        C.move_to(c+DR/2)
        D.move_to(d+DL/2)
        P.move_to(p+UP/2)
        R.move_to(r+DOWN/2)
        Q.move_to(q+RIGHT/2)
        S.move_to(s+LEFT/2)
        self.play(Write(A),Write(B),Write(C),Write(D))
        self.wait(2)
        self.clear()
        squareGroup = VGroup(square,inner_square,A,B,C,D,P,Q,R,S)
        self.play(ApplyMethod(squareGroup.to_edge,LEFT))
        self.play(Write(P),Write(Q),Write(R),Write(S))
        self.wait(1)
        sentences = [
            TextMobject("We are drawing squares within squares."),
            TextMobject("The first square is given."),
            TextMobject("The subquent ones are dependent on their predecessors."),
        ]
        self.WriteSentenceList(sentences,np.array((3,1.5,0)),0.5,GOLD_A)
        self.wait(2)
    def AListOfNumbers(self):
        lookat = TextMobject("Look at the following list of numbers.").set_color(GREEN_E)
        numbers = TextMobject("1", "," ," 22", "," ," 9",",", " 12", "," ," 100", ",", " 79", ",", " 504").set_color(GREEN_E)
        ifwe = TextMobject("If we remove the first number, what remains is another list.").set_color(GREEN_E)
        dejavu = TextMobject("Are you seeing a list recur again? Having a deja-vu?").set_color(GREEN_E)
        wecan = TextMobject("We can define a list in the following recursive way.").set_color(GREEN_E)
        least = TextMobject("List is either a number or a list of numbers.").set_color(GREEN_E)
        defin = TextMobject("Number","xxxxxxxxxxx", "if list has one element").set_color(GREEN_E)
        defin[1].set_color(BLACK)
        defin2 = TextMobject("Number comma List, if it has more elements").set_color(GREEN_E)
        lest = TextMobject("List = ").set_color(GREEN_E)
        self.add(lookat)
        self.wait(3)
        self.play(Transform(lookat,numbers),run_time=2)
        self.wait(3)
        self.play(Transform(lookat,ifwe),run_time=2)
        self.wait(3)
        self.play(Transform(lookat,dejavu),run_time=2)
        self.wait(3)
        self.play(Transform(lookat,wecan),run_time=2)
        self.wait(3)
        self.play(Transform(lookat,least),run_time=2)
        self.wait(3)
        self.remove(lookat)
        defin2.next_to(defin,DOWN)
        vg = VGroup(defin,defin2)
        vg.shift(UP/2+RIGHT/2)
        brace = Brace(vg,LEFT,buff=SMALL_BUFF)
        lest.next_to(brace,LEFT,buff=SMALL_BUFF)
        self.play(Write(lest))
        self.play(ShowCreation(brace))
        self.play(Write(defin))
        self.play(Write(defin2))
        self.wait(2)


    def RecursiveSquare(self):
        self.SquareDrawing()
        self.clear()
        recur = TextMobject("The word 'recur' means to occur again.").set_color(DARK_BLUE)
        dreams = TextMobject("Ever had dreams within dreams?").set_color(DARK_BLUE)
        within = TextMobject("Or dreams within dreams within dreams?").set_color(DARK_BLUE)
        inception = TextMobject("Ever watched the movie called inception?").set_color(DARK_BLUE)
        those = TextMobject("Those are recursive dreams.").set_color(DARK_BLUE)
        draw = TextMobject("We were drawing squares within squares within squares.").set_color(DARK_BLUE)
        lets = TextMobject("Let's see some more examples.").set_color(DARK_BLUE)
        self.add(recur)
        self.wait(2)
        self.play(Transform(recur,dreams),run_time=3)
        self.wait()
        self.play(Transform(recur, within),run_time=4)
        self.play(Transform(recur,inception),run_time=3)
        self.wait()
        self.play(Transform(recur,those),run_time=3)
        self.wait()
        self.play(Transform(recur,draw),run_time=4)
        self.wait()
        self.play(Transform(recur,lets),run_time=3)
        self.wait()
        self.remove(recur)
        self.AListOfNumbers()
        self.clear()

    def Fibonacci(self,n,parent):
        r = 0.25
        text_scale = 0.6
        node_f4 = Circle(radius = r,fill_color = MY_DEEP_PURPLE,fill_opacity=1,color=MY_DEEP_PURPLE)
        node_f4.shift(parent)
        text_f4 = TexMobject("F_{5}")
        text_f4.scale(text_scale)
        text_f4.shift(node_f4.get_center())
        self.play(ShowCreation(node_f4))
        self.play(Write(text_f4))
        self.wait()
        node_f3 = node_f4.copy()
        node_f3.shift(1.5*DOWN+LEFT*1.5)
        text_f3 = TexMobject("F_{4}")
        text_f3.scale(text_scale)
        text_f3.shift(node_f3.get_center())
        self.play(ShowCreation(node_f3))
        self.play(Write(text_f3))
        self.wait()
        a3 = Arrow(node_f4.get_center()+r*LEFT-r*UP,node_f3.get_center()-r*LEFT+r*UP)
        a3.set_color(MY_CYAN)
        self.play(ShowCreation(a3))
        self.wait()
        node_f22 = node_f3.copy()
        node_f22.shift(1.5*DOWN+LEFT*1.5)
        text_f22 = TexMobject("F_{3}")
        text_f22.scale(text_scale)
        text_f22.shift(node_f22.get_center())
        self.play(ShowCreation(node_f22))
        self.play(Write(text_f22))
        self.wait()
        a3 = Arrow(node_f3.get_center()+r*LEFT-r*UP,node_f22.get_center()-r*LEFT+r*UP)
        a3.set_color(MY_CYAN)
        self.play(ShowCreation(a3))
        self.wait()
        node_f11 = node_f22.copy()
        node_f11.shift(1.5*DOWN+LEFT*1.5)
        text_f11 = TexMobject("F_{2}")
        text_f11.scale(text_scale)
        text_f11.shift(node_f11.get_center())
        self.play(ShowCreation(node_f11))
        self.play(Write(text_f11))
        self.wait()
        a3 = Arrow(node_f22.get_center()+r*LEFT-r*UP,node_f11.get_center()-r*LEFT+r*UP)
        a3.set_color(MY_CYAN)
        self.play(ShowCreation(a3))
        self.wait()
        b11_tex = TexMobject("1")
        b11_tex.move_to(node_f11.get_center()+UP*0.5)
        self.play(Write(b11_tex))
        self.wait()
        node_f01 = node_f22.copy()
        node_f01.shift(1.5*DOWN-LEFT*1.5)
        text_f01 = TexMobject("F_{1}")
        text_f01.scale(text_scale)
        text_f01.shift(node_f01.get_center())
        self.play(ShowCreation(node_f01))
        self.play(Write(text_f01))
        self.wait()
        a3 = Arrow(node_f22.get_center()-r*LEFT-r*UP,node_f01.get_center()+r*LEFT+r*UP)
        a3.set_color(MY_CYAN)
        self.play(ShowCreation(a3))
        self.wait()
        b01_tex = TexMobject("1")
        b01_tex.move_to(node_f01.get_center()+UP*0.5)
        self.play(FadeIn(b01_tex))
        self.wait()
        b22_tex = TexMobject("2")
        b22_tex.move_to(node_f22.get_center()+UP*0.5)
        vg22 = VGroup(b11_tex.copy(),b01_tex.copy())
        self.play(Transform(vg22,b22_tex))
        self.wait()
        node_f21 = node_f3.copy()
        node_f21.shift(1.5*DOWN-LEFT)
        text_f21 = TexMobject("F_{2}")
        text_f21.scale(text_scale)
        text_f21.shift(node_f21.get_center())
        self.play(ShowCreation(node_f21))
        self.play(Write(text_f21))
        self.wait()
        a3 = Arrow(node_f3.get_center()-r*LEFT-r*1.5*UP,node_f21.get_center()+r*LEFT+r*1.5*UP)
        a3.set_color(MY_CYAN)
        self.play(ShowCreation(a3))
        self.wait()
        b21_tex = TexMobject("1")
        b21_tex.move_to(node_f21.get_center()+UP*0.5)
        self.play(Write(b21_tex))
        self.wait()
        b3_tex = TexMobject("3")
        b3_tex.move_to(node_f3.get_center()+UP*0.5)
        vg3 = VGroup(b21_tex.copy(),b22_tex.copy())
        self.play(Transform(vg3,b3_tex))
        self.wait()
        node_f2 = node_f4.copy()
        node_f2.shift(1.5*DOWN-LEFT*1.5)
        text_f2 = TexMobject("F_{3}")
        text_f2.scale(text_scale)
        text_f2.shift(node_f2.get_center())
        self.play(ShowCreation(node_f2))
        self.play(Write(text_f2))
        self.wait()
        a3 = Arrow(node_f4.get_center()-r*LEFT-r*UP,node_f2.get_center()+r*LEFT+r*UP)
        a3.set_color(MY_CYAN)
        self.play(ShowCreation(a3))
        self.wait()
        node_f41 = node_f2.copy()
        node_f41.shift(1.5*DOWN+LEFT)
        text_f41 = TexMobject("F_{2}")
        text_f41.scale(text_scale)
        text_f41.shift(node_f41.get_center())
        self.play(ShowCreation(node_f41))
        self.play(Write(text_f41))
        self.wait()
        a3 = Arrow(node_f2.get_center()+r*LEFT-r*1.5*UP,node_f41.get_center()-r*LEFT+r*1.5*UP)
        a3.set_color(MY_CYAN)
        self.play(ShowCreation(a3))
        self.wait()
        b41_tex = TexMobject("1")
        b41_tex.move_to(node_f41.get_center()+UP*0.5)
        self.play(Write(b41_tex))
        self.wait()
        node_f44 = node_f2.copy()
        node_f44.shift(1.5*DOWN-LEFT*1.5)
        text_f44 = TexMobject("F_{1}")
        text_f44.scale(text_scale)
        text_f44.shift(node_f44.get_center())
        self.play(ShowCreation(node_f44))
        self.play(Write(text_f44))
        self.wait()
        a3 = Arrow(node_f2.get_center()-r*LEFT-r*UP,node_f44.get_center()+r*LEFT+r*UP)
        a3.set_color(MY_CYAN)
        self.play(ShowCreation(a3))
        self.wait()
        b44_tex = TexMobject("1")
        b44_tex.move_to(node_f44.get_center()+UP*0.5)
        self.play(Write(b44_tex))
        self.wait()
        b2_tex = TexMobject("2")
        b2_tex.move_to(node_f2.get_center()+UP*0.5)
        vg2 = VGroup(b41_tex.copy(),b44_tex.copy())
        self.play(Transform(vg2,b2_tex))
        self.wait()
        b4_tex = TexMobject("5")
        b4_tex.move_to(node_f4.get_center()+UP*0.5)
        vg4 = VGroup(b2_tex.copy(),b3_tex.copy())
        self.play(Transform(vg4,b4_tex))
        self.wait()

        return

    def ColorSetter(self, text, color):
        for i,j in zip(text,color):
            i.set_color(j)
        return text

    def FibonacciSimulator(self, n):
        fun = TextMobject("int ", "Fib","(", " int ", "n", ")", "{")
        fun_color = [MY_CYAN, GREEN_SCREEN, WHITE, MY_CYAN, ORANGE,WHITE,WHITE]
        fun = self.ColorSetter(fun,fun_color)
        base = TextMobject("xxxx","if","(","n"," == ","1"," or ", "n", " == ", "2", ")", "{")
        base_color = [BLACK,PINK, WHITE, ORANGE, PINK, PURPLE, PINK, PURPLE, PINK, PURPLE, WHITE, WHITE ]
        base = self.ColorSetter(base,base_color)
        ret = TextMobject("xxxxxxxx","return", " 1",";", "}")
        ret_color = [BLACK,PINK, PURPLE,WHITE, WHITE]
        ret = self.ColorSetter(ret,ret_color)
        retu = TextMobject("xxxx","else ","return ", "Fib","(", "n", "-", "1",")"," + " ,"Fib", "(" , "n", "-","2",")",";")
        retu_color = [BLACK,PINK, PINK, GREEN_SCREEN, WHITE, ORANGE, PINK, PURPLE, WHITE, PINK, GREEN_SCREEN, WHITE,ORANGE,PINK, PURPLE, WHITE,WHITE]
        retu = self.ColorSetter(retu,retu_color)
        fun.to_edge(LEFT)
        base.to_edge(LEFT)
        base.shift(DOWN/2)
        ret.to_edge(LEFT)
        ret.shift(DOWN)
        retu.to_edge(LEFT)
        retu.shift(3*DOWN/2.0)
        text_vg = VGroup(fun,base,ret,retu)
        text_vg.scale(0.7)
        vg = text_vg.copy()
        vg.shift(2*RIGHT)
        for i in range(4):
            self.play(Write(vg[i]),run_time=2)
        self.wait(5)
        text_vg.shift(UP*3)
        self.play(Transform(vg,text_vg))
        self.wait(2)
        self.Fibonacci(n,UP*3+3*RIGHT)
        self.wait()
        self.clear()
    def PermutationIntro(self):
        header = TextMobject("Permutations and Factorials")
        header.scale(1.5).set_color(MY_DEEP_PURPLE).to_edge(UP)
        self.play(FadeIn(header),run_time=3)
        suppose = TextMobject("Suppose, you are given n balls of n different colors. In how").set_color(GOLD_A)
        muppose = TextMobject("many different ways can you arrange the balls?", "xxxxxxxxxx").set_color(GOLD_A)
        muppose.next_to(suppose.get_center(),DOWN)
        muppose[1].set_color(BLACK)
        statement = VGroup(suppose,muppose)
        statement.shift(2.5*UP)
        self.play(Write(suppose),run_time=4)
        self.play(Write(muppose),run_time=4)
        self.wait(2)
        vec = 1.2*UP+2*LEFT
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                for k in range(3):
                    if j == k or i == k:
                        continue
                    a = Circle()
                    b = Circle()
                    c = Circle()
                    if i == 0:
                        a = Circle(radius = 0.3, fill_color=MY_RED,fill_opacity=1,stroke_width=0.5).set_color(MY_RED)
                    elif i == 1:
                        a = Circle(radius = 0.3, fill_color=MY_GREEN,fill_opacity=1,stroke_width=0.5).set_color(MY_GREEN)
                    else:
                        a = Circle(radius = 0.3, fill_color=MY_BLUE,fill_opacity=1,stroke_width=0.5).set_color(MY_BLUE)
                    if j == 0:
                        b = Circle(radius = 0.3, fill_color=MY_RED,fill_opacity=1,stroke_width=0.5).set_color(MY_RED)
                    elif j == 1:
                        b = Circle(radius = 0.3, fill_color=MY_GREEN,fill_opacity=1,stroke_width=0.5).set_color(MY_GREEN)
                    else:
                        b = Circle(radius = 0.3, fill_color=MY_BLUE,fill_opacity=1,stroke_width=0.5).set_color(MY_BLUE)
                    if k == 0:
                        c = Circle(radius = 0.3, fill_color=MY_RED,fill_opacity=1,stroke_width=0.5).set_color(MY_RED)
                    elif k == 1:
                        c = Circle(radius = 0.3, fill_color=MY_GREEN,fill_opacity=1,stroke_width=0.5).set_color(MY_GREEN)
                    else:
                        c = Circle(radius = 0.3, fill_color=MY_BLUE,fill_opacity=1,stroke_width=0.5).set_color(MY_BLUE)
                    a.move_to(vec)
                    b.next_to(a.get_center(),5*RIGHT)
                    c.next_to(b.get_center(),5*RIGHT)
                    self.play(ShowCreation(a))
                    self.play(ShowCreation(b))
                    self.play(ShowCreation(c))
                    self.wait(2)
                    vec = vec + 0.8*DOWN
        self.clear()
    def PermutationSecondPage(self):
        subproblem = TextMobject("So if we fix the first ball's color and try to arrange the later")
        subproblem1 = TextMobject("balls, we find that it is the same problem with fewer balls.")
        subproblem2 = TextMobject("Here is the recursive subproblem.")
        subproblem.set_color(GOLD_A)
        subproblem1.set_color(GOLD_A)
        subproblem2.set_color(GOLD_A)
        subproblem1.next_to(subproblem.get_center(),DOWN)
        subproblem2.next_to(subproblem1.get_center(),DOWN)
        subproblem.to_edge(LEFT)
        subproblem1.to_edge(LEFT)
        subproblem2.to_edge(LEFT)
        vg = VGroup(subproblem2,subproblem1,subproblem)
        vg.shift(0.5*RIGHT)
        self.play(Write(subproblem),run_time=4)
        self.play(Write(subproblem1),run_time=4)
        self.play(Write(subproblem2),run_time=4)
        self.wait(4)
        self.clear()

    def PermutationThirdPage(self):
        lets = TextMobject("Let's try to count the number of different arrangements.").set_color(GOLD_A)
        vg1 = TextMobject("Let $F_{n}$ be the number of ways to arrange $n$ balls.").set_color(GOLD_A)
        vg2 = TextMobject("And let the colors be $c_{1}, c_{2}, c_{3}, \\cdots , c_{n}.$").set_color(GOLD_A)
        vg3 = TextMobject("And let $F_{n-1,c_{i}}$ denote the number of ways we can color").set_color(GOLD_A)
        vg4 = TextMobject("remaining $n-1$ balls with the $n^{th}$ ball being of color $c_{i}$.").set_color(GOLD_A)
        lets.shift(1.5*UP)
        vg1.next_to(lets.get_center(),DOWN)
        vg2.next_to(vg1.get_center(),DOWN)
        vg3.next_to(vg2.get_center(),DOWN)
        vg4.next_to(vg3.get_center(),DOWN)
        self.play(Write(lets),run_time=4)
        self.play(Write(vg1),run_time=4)
        self.play(Write(vg2),run_time=4)
        self.play(Write(vg3),run_time=4)
        self.play(Write(vg4),run_time=4)
        self.wait(3)
        self.clear()
    
    def PermutationFourthPage(self):
        prev = TextMobject("From the previous animation, we have seen that,")
        form1 = TextMobject("$F_{3} = F_{2,red} + F_{2,green} + F_{2,blue}$.")
        racism = TextMobject("Since, there is no racism in combinatoritcs,")
        form2 = TextMobject("$F_{2,red} = F_{2,green} = F_{2,blue} = F_{2}$.")
        rec = TextMobject("$F_{3} = 3.F_{2}$.")
        general = TextMobject("In general, $F_{n} = F_{n-1,c_{1}} + F_{n-1,c_{2}} + F_{n-1,c_{3}} + \\cdots + F_{n-1,c_{n}}.$")
        inother = TextMobject("More concisely, $F_{n} = \\sum_{i=1}^{n} F_{n-1,c_{i}}$.")
        ora = TextMobject("Thus, $F_{n} = n.F_{n-1}.$")
        prev.set_color(GOLD_A)
        form1.set_color(GOLD_A)
        racism.set_color(GOLD_A)
        form2.set_color(GOLD_A)
        rec.set_color(GOLD_A)
        general.set_color(GOLD_A)
        inother.set_color(GOLD_A)
        ora.set_color(GOLD_A)
        prev.shift(2*UP)
        form1.next_to(prev.get_center(),DOWN)
        racism.next_to(form1.get_center(),DOWN)
        form2.next_to(racism.get_center(),DOWN)
        rec.next_to(form2.get_center(),DOWN)
        general.next_to(rec.get_center(),DOWN)
        inother.next_to(general.get_center(),DOWN)
        ora.next_to(inother.get_center(),DOWN)
        self.play(Write(prev),run_time=4)
        self.play(Write(form1),run_time=4)
        self.play(Write(racism),run_time=4)
        self.play(Write(form2),run_time=4)
        self.play(Write(rec),run_time=4)
        self.play(Write(general),run_time=4)
        self.play(Write(inother),run_time=4)
        self.play(Write(ora),run_time=4)
        self.wait(3)
        self.clear()

    def PermutationFifthPage(self):
        There = TextMobject("There is another way to derive the recursion. Permuting balls is equivalent")
        suppose = TextMobject("to putting them each in a separate room in the following grid.")

        ball1 = Circle(radius = 0.4,fill_color=YELLOW, fill_opacity=10, stroke_width=0.5,color=YELLOW)
        ball2 = Circle(radius = 0.4,fill_color=GREEN, fill_opacity=10, stroke_width=0.5,color=GREEN)
        ball3 = Circle(radius = 0.4,fill_color=RED, fill_opacity=10, stroke_width=0.5,color=RED)
        ball4 = Circle(radius = 0.4,fill_color=BLUE, fill_opacity=10, stroke_width=0.5,color=BLUE)
        dot1 = Circle(radius = 0.05,fill_color=WHITE, fill_opacity=10, stroke_width=0.5,color=WHITE)
        dot2 = Circle(radius = 0.05,fill_color=WHITE, fill_opacity=10, stroke_width=0.5,color=WHITE)
        dot3 = Circle(radius = 0.05,fill_color=WHITE, fill_opacity=10, stroke_width=0.5,color=WHITE)
        dot4= Circle(radius = 0.05,fill_color=WHITE, fill_opacity=10, stroke_width=0.5,color=WHITE)
        dot5 = Circle(radius = 0.05,fill_color=WHITE, fill_opacity=10, stroke_width=0.5,color=WHITE)
        dot6 = Circle(radius = 0.05,fill_color=WHITE, fill_opacity=10, stroke_width=0.5,color=WHITE)
        ball5 = Circle(radius = 0.4,fill_color=GOLD, fill_opacity=10, stroke_width=0.5,color=GOLD)

        rec1 = Rectangle(height=0.1,width=0.8,color=WHITE,fill_color=WHITE,fill_opacity=1)
        rec2 = Rectangle(height=0.1,width=0.8,color=WHITE,fill_color=WHITE,fill_opacity=1)
        rec3 = Rectangle(height=0.1,width=0.8,color=WHITE,fill_color=WHITE,fill_opacity=1)
        rec4 = Rectangle(height=0.1,width=0.8,color=WHITE,fill_color=WHITE,fill_opacity=1)
        rec5 = Rectangle(height=0.1,width=0.8,color=WHITE,fill_color=WHITE,fill_opacity=1)

        cross1 = Cross(ball1).set_color(RED)

        ball1.shift(2*UP+3*LEFT)
        ball2.next_to(ball1,RIGHT)
        ball3.next_to(ball2,RIGHT)
        ball4.next_to(ball3,RIGHT)
        dot1.next_to(ball4,RIGHT)
        dot2.next_to(dot1,RIGHT)
        dot3.next_to(dot2,RIGHT)
        dot4.next_to(dot1,DOWN)
        dot5.next_to(dot2,DOWN)
        dot6.next_to(dot3,DOWN)
        ball5.next_to(dot3,RIGHT)

        rec1.next_to(ball1,DOWN)
        rec1.shift(DOWN)
        rec2.next_to(rec1,RIGHT)
        rec3.next_to(rec2,RIGHT)
        rec4.next_to(rec3,RIGHT)
        rec5.next_to(ball5,DOWN)
        rec5.shift(DOWN)
        dot4.next_to(rec4,RIGHT)
        dot5.next_to(dot4,RIGHT)
        dot6.next_to(dot5,RIGHT)

        c1 = TextMobject("$c_{1}$").scale(0.6).set_color(BLACK)
        c2 = TextMobject("$c_{2}$").scale(0.6).set_color(BLACK)
        c3 = TextMobject("$c_{3}$").scale(0.6).set_color(BLACK)
        c4 = TextMobject("$c_{4}$").scale(0.6).set_color(BLACK)
        c5 = TextMobject("$c_{n}$").scale(0.6).set_color(BLACK)

        c1.move_to(ball1.get_center())
        c2.move_to(ball2.get_center())
        c3.move_to(ball3.get_center())
        c4.move_to(ball4.get_center())
        c5.move_to(ball5.get_center())

        self.play(ShowCreation(ball1))
        self.play(ShowCreation(c1))
        self.play(ShowCreation(ball2))
        self.play(ShowCreation(c2))
        self.play(ShowCreation(ball3))
        self.play(ShowCreation(c3))
        self.play(ShowCreation(ball4))
        self.play(ShowCreation(c4))
        self.play(ShowCreation(dot1))
        self.play(ShowCreation(dot2))
        self.play(ShowCreation(dot3))
        self.play(ShowCreation(ball5))
        self.play(ShowCreation(c5))
        self.wait(2)

        self.play(ShowCreation(rec1))
        self.play(ShowCreation(rec2))
        self.play(ShowCreation(rec3))
        self.play(ShowCreation(rec4))
        self.play(ShowCreation(dot4))
        self.play(ShowCreation(dot5))
        self.play(ShowCreation(dot6))
        self.play(ShowCreation(rec5))
        self.wait(2)

        cross1 = Cross(ball1).set_color(MY_RED)
        cross2 = Cross(ball2).set_color(MY_RED)
        cross3 = Cross(ball3).set_color(MY_RED)
        cross4 = Cross(ball4).set_color(MY_RED)
        cross5 = Cross(ball5).set_color(MY_RED)

        n = TextMobject("$n$").scale(0.6)
        x = TextMobject("x").scale(0.6)
        n1 = TextMobject("$n-1$").scale(0.6)
        x1 = TextMobject("x").scale(0.6)
        n2 = TextMobject("$n-2$").scale(0.6)
        x2 = TextMobject("x").scale(0.6)
        n3 = TextMobject("$n-3$").scale(0.6)
        x3 = TextMobject("x").scale(0.6)
        x4 = TextMobject("x").scale(0.6)
        n4 = TextMobject("$1$").scale(0.6)

        n.next_to(rec1,UP)
        n1.next_to(rec2,UP)
        n2.next_to(rec3,UP)
        n3.next_to(rec4,UP)
        n4.next_to(rec5,UP)

        x.move_to((rec1.get_center()+rec2.get_center())/2+(n.get_center()-rec1.get_center()))
        x1.move_to((rec2.get_center()+rec3.get_center())/2+(n.get_center()-rec1.get_center()))
        x2.move_to((rec3.get_center()+rec4.get_center())/2+(n.get_center()-rec1.get_center()))
        x3.next_to(n3,RIGHT)
        x4.next_to(n4,LEFT)

        self.play(ShowCreation(n))
        self.play(ShowCreation(cross1))
        self.play(ShowCreation(x))
        self.play(ShowCreation(n1))
        self.play(ShowCreation(cross2))
        self.play(ShowCreation(x1))
        self.play(ShowCreation(n2))
        self.play(ShowCreation(cross3))
        self.play(ShowCreation(x2))
        self.play(ShowCreation(n3))
        self.play(ShowCreation(cross4))
        self.play(ShowCreation(x3))
        self.play(ShowCreation(x4))
        self.play(ShowCreation(n4))
        self.play(ShowCreation(cross5))
        self.wait(2)

        so = TextMobject("So, the number of different arrangements is:").scale(0.8)
        form = TextMobject("$n$"," x ","$(n-1)$"," x ","$(n-2)$"," x ","......","$2$"," x ","$1$.").scale(0.8)
        which = TextMobject("This is the definition of factorial $n$ and written as:").scale(0.8)
        fact = TextMobject("n! = $n$"," x ","$(n-1)$"," x ","$(n-2)$"," x ","......","$2$"," x ","$1$.").scale(0.8)
        but = TextMobject("But then, ", "$(n-1)! = $","$(n-1)$"," x ","$(n-2)$"," x ","......","$2$"," x ","$1$.").scale(0.8)
        thus = TextMobject("So, ", "$n! = n$"," x " "$(n-1)!$").scale(0.8)

        so.next_to(rec3,DOWN)
        form.next_to(so,DOWN)
        which.next_to(form, DOWN)
        fact.next_to(which,DOWN)
        but.next_to(fact,DOWN)
        thus.next_to(but,DOWN)

        self.play(Write(so),run_time=4)
        self.play(Write(form),run_time=4)
        self.play(Write(which),run_time=4)
        self.play(Write(fact),run_time=4)
        self.play(Write(but),run_time=4)
        self.play(Write(thus),run_time=4)
        self.wait(2)
        self.clear()

    def PermutationSixthPage(self):
        lets= TextMobject("The following is a simple recursive code to compute Factorials.")
        fact = TextMobject("int ", "fact", "(", " int ", " n ", ")")
        color_fact = [MY_CYAN, GREEN_SCREEN, WHITE, MY_CYAN, ORANGE, WHITE]
        base = TextMobject("if", "(", "n", " == ", " 1 ", ")", " return ", "1", ";")
        color_base = [PINK,WHITE,WHITE, PINK,MY_DEEP_PURPLE,WHITE,PINK,MY_DEEP_PURPLE,WHITE]
        ret = TextMobject("else"," return ", "n", "*", "fact", "(", "n", "-", "1", ")",";")
        color_ret = [PINK,PINK,WHITE,PINK,GREEN_SCREEN,WHITE,WHITE,PINK,MY_DEEP_PURPLE,WHITE,WHITE]

        fact = self.ColorSetter(fact,color_fact)
        base = self.ColorSetter(base,color_base)
        ret = self.ColorSetter(ret,color_ret)

        fact.next_to(lets,DOWN)
        base.next_to(fact,DOWN)
        ret.next_to(base,DOWN)

        lets.to_edge(LEFT)
        fact.to_edge(LEFT)
        base.to_edge(LEFT)
        ret.to_edge(LEFT)

        base.shift(RIGHT)
        ret.shift(RIGHT)

        fact.scale(0.7)
        base.scale(0.7)
        ret.scale(0.7)

        code = VGroup(fact,base,ret)
        code.shift(RIGHT*3)

        self.add(lets)
        self.play(Write(fact),run_time=3)
        self.play(Write(base),run_time=3)
        self.play(Write(ret),run_time=3)
        self.wait(2)
        self.remove(lets)
        self.play(ApplyMethod(code.shift,(LEFT*3+UP*3)),run_time=3)
        self.wait()

    def PermutationSeventhPage(self):
        fact5 = TextMobject("fact(5)")
        fact4 = TextMobject("5","*","fact(4)")
        fact3 = TextMobject("4","*","fact(3)")
        fact2 = TextMobject("3","*","fact(2)")
        fact1 = TextMobject("2","*","fact(1)")


        fact5.shift(UP*3.5+RIGHT)
        fact4.next_to(fact5,DOWN)
        fact4.shift(DOWN)
        fact3.next_to(fact4,DOWN)
        fact3.shift(DOWN)
        fact2.next_to(fact3,DOWN)
        fact2.shift(DOWN)
        fact1.next_to(fact2,DOWN)
        fact1.shift(DOWN)

        arrow4 = Arrow(fact5,fact4)
        arrow3 = Arrow(fact4,fact3)
        arrow2 = Arrow(fact3,fact2)
        arrow1 = Arrow(fact2,fact1)

        self.play(Write(fact5))
        self.play(ShowCreation(arrow4))
        self.play(Write(fact4))
        self.play(ShowCreation(arrow3))
        self.play(Write(fact3))
        self.play(ShowCreation(arrow2))
        self.play(Write(fact2))
        self.play(ShowCreation(arrow1))
        self.play(Write(fact1))

        self.wait(2)
        act1 = TextMobject("1")
        act1.move_to(fact1)
        tact1 = TextMobject("2")
        tact1.move_to(fact1)
        self.play(Transform(fact1[2],act1))
        self.wait()

        self.play(Transform(fact1,tact1),run_time=1)     
        self.wait()
        self.remove(fact1)  
        act2 = TextMobject("2")
        act2.move_to(fact2)
        tact2 = TextMobject("6")
        tact2.move_to(fact2)
        self.remove(arrow1)
        self.wait()
        self.play(Transform(fact2[2],act2))
        self.wait()

        self.play(Transform(fact2,tact2),run_time=1)   
        self.wait()
        self.remove(fact2)
        act3 = TextMobject("6")
        act3.move_to(fact3)
        tact3 = TextMobject("24")
        tact3.move_to(fact3)
        self.remove(arrow2)
        self.wait()
        self.play(Transform(fact3[2],act3))
        self.wait()

        self.play(Transform(fact3,tact3),run_time=1)   
        self.wait()  
        self.remove(fact3)
        act4 = TextMobject("24")
        act4.move_to(fact4)
        tact4 = TextMobject("120")
        tact4.move_to(fact4)
        self.remove(arrow3)
        self.wait()
        self.play(Transform(fact4[2],act4))
        self.wait()

        self.play(Transform(fact4,tact4),run_time=1)     
        self.wait()
        self.remove(fact4)

        act5 = TextMobject("120")
        act5.move_to(fact5)
        self.remove(arrow4)
        self.wait()
        self.play(Transform(fact5,act5))
        self.wait(2)
        self.remove(fact5)

    def Permutation(self):
        self.PermutationIntro()
        self.PermutationSecondPage()
        self.PermutationThirdPage()
        self.PermutationFourthPage()
        self.PermutationFifthPage()
        self.PermutationSixthPage()
        self.PermutationSeventhPage()

    def TilingIntro(self):
        header = TextMobject("A Tiling Problem")
        header.scale(1.5)
        header.to_edge(UP)
        header.set_color(MY_DEEP_PURPLE)
        self.play(FadeIn(header))
        suppose = TextMobject("Suppose, you have a 1x6 grid. And you have")
        tiles = TextMobject("tiles of two colors. Red and Blue. But there ")
        condition = TextMobject("is a condition. Between any two red tiles,")
        there = TextMobject("There should be at least one blue tile. In how")
        many = TextMobject("many ways can you tile the grid?")
        suppose.to_edge(LEFT)
        tiles.to_edge(LEFT)
        condition.to_edge(LEFT)
        there.to_edge(LEFT)
        many.to_edge(LEFT)
        tiles.shift(DOWN*0.5)
        condition.shift(DOWN)
        there.shift(DOWN*1.5)
        many.shift(DOWN*2)
        problem = VGroup(suppose,tiles,condition,there,many)
        problem.set_color(GOLD_A)
        problem.to_edge(LEFT)
        problem.shift(2.5*UP)
        problem.scale(0.8)
        for i in range(5):
            self.play(Write(problem[i]),run_time=3)
        self.wait(1)
        square_scale = 0.375
        sq = Square().scale(square_scale)
        squares = []
        num_of_square = 6
        for i in range(num_of_square):
            squares.append(sq.copy())
        prev = sq
        prev.shift(LEFT*2.5)
        for i in range(num_of_square):
            squares[i].move_to(prev.get_center()+RIGHT*square_scale*2)
            prev = squares[i]
        self.play(FadeIn(squares[0]),FadeIn(squares[1]),FadeIn(squares[2]),FadeIn(squares[3]),FadeIn(squares[4]),FadeIn(squares[5]), run_time=3)
        self.wait()
        color1 = [MY_PINK,BLUE_E,BLUE_E,MY_PINK,BLUE_E,MY_PINK]
        colored_squares_1 = []
        for i,square in enumerate(squares):
            s = Square(fill_opacity=0.8,fill_color=color1[i]).scale(square_scale)
            s.move_to(square.get_center())
            colored_squares_1.append(s)
        for s in colored_squares_1:
            s.shift(DOWN)
        tex_1 = TextMobject("Correct Coloring:")
        tex_1.set_color(BLUE_E)
        tex_1.next_to(colored_squares_1[0],LEFT)
        self.play(FadeIn(tex_1))
        self.play(FadeIn(colored_squares_1[0]),FadeIn(colored_squares_1[1]),FadeIn(colored_squares_1[2]),FadeIn(colored_squares_1[3]),FadeIn(colored_squares_1[4]),FadeIn(colored_squares_1[5]))
        self.wait()
        color2 = [MY_PINK,BLUE_E,MY_PINK,MY_PINK,BLUE_E,MY_PINK]
        colored_squares_2 = []
        for i,square in enumerate(squares):
            s = Square(fill_opacity=0.8,fill_color=color2[i]).scale(square_scale)
            s.move_to(square.get_center())
            colored_squares_2.append(s)
        for s in colored_squares_2:
            s.shift(2*DOWN)
        cross = Cross(colored_squares_2[2])
        cross.set_stroke(BLACK,6)
        crosss = Cross(colored_squares_2[3])
        crosss.set_stroke(BLACK,6)
        tex_2 = TextMobject("Incorrect Coloring:")
        tex_2.set_color(RED_E)
        tex_2.next_to(colored_squares_2[0],LEFT)
        self.play(FadeIn(tex_2))
        self.play(FadeIn(colored_squares_2[0]),FadeIn(colored_squares_2[1]),FadeIn(colored_squares_2[2]),FadeIn(colored_squares_2[3]),FadeIn(colored_squares_2[4]),FadeIn(colored_squares_2[5]))
        self.wait()
        self.play(ShowCreation(cross),ShowCreation(crosss))
        self.wait()
        self.clear()

    def PageOfFormulas(self):
        latex_scale = 0.8
        formula1 = TexMobject("X_{n-1}")
        formula2 = TexMobject("X_{n-2}")
        formula = TexMobject("X_{n} = ")
        formula.scale(latex_scale)
        formula1.scale(latex_scale)
        formula2.scale(latex_scale)
        formula2.shift(DOWN)
        sub1 = TextMobject(", when the leftmost tile is blue")
        sub2 = TextMobject(", when the leftmost tile is red")
        sub1.scale(latex_scale)
        sub2.scale(latex_scale)
        vg = VGroup(formula1,formula2)
        vg.shift(RIGHT)
        brace = Brace(vg,LEFT,buff=SMALL_BUFF)
        formula.next_to(brace.get_center(),LEFT)
        sub1.next_to(formula1.get_center(),RIGHT)
        sub1.shift(RIGHT/2)
        sub2.next_to(formula2.get_center(),RIGHT)
        sub2.shift(RIGHT/2)
        vg = VGroup(vg,sub1,sub2,brace,formula)
        vg.shift(3*UP)
        vg.shift(1.5*LEFT)
        vg.set_color(ORANGE)
        self.play(Write(formula))
        self.wait()
        self.play(Write(brace))
        self.wait()
        self.play(Write(formula1))
        self.wait()
        self.play(Write(sub1))
        self.wait()
        self.play(Write(formula2))
        self.wait()
        self.play(Write(sub2))
        self.wait()
        so = TextMobject("So,")
        form = TexMobject("X_{n} = X_{n-1} + X_{n-2}.")
        form1 = TexMobject("X_{1} = 2, X_{2} = 3, X_{3} = 5...")
        anyone = TextMobject("There is another series with the same values")
        fibo = TextMobject("The fibonacci series has the following recursion and the same values")
        rec = TexMobject("F_{n} = F_{n-1} + F_{n-2}")
        values = TexMobject("1, 1, 2, 3, 5, 8, ...")
        actually = TextMobject("actually, ")
        equal = TexMobject(" X_{n} = F_{n+1}")

        so.scale(latex_scale)
        form.scale(latex_scale)
        form1.scale(latex_scale)
        anyone.scale(latex_scale)
        fibo.scale(latex_scale)
        rec.scale(latex_scale)
        values.scale(latex_scale)
        actually.scale(latex_scale)
        equal.scale(latex_scale)

        form.next_to(so.get_center(),DOWN)
        form1.next_to(form.get_center(),DOWN)
        anyone.next_to(form1.get_center(),DOWN)
        fibo.next_to(anyone.get_center(),DOWN)
        rec.next_to(fibo.get_center(),DOWN)
        values.next_to(rec.get_center(),DOWN)
        actually.next_to(values.get_center(),DOWN)
        equal.next_to(actually.get_center(),DOWN)
        vg = VGroup(so,form,form1,anyone,fibo,rec,values,actually,equal)
        vg.shift(1.5*UP)
        vg.set_color(MAROON_E)
        self.play(Write(so))
        self.wait()
        self.play(Write(form),run_time=3)
        self.wait()
        self.play(Write(form1),run_time=3)
        self.wait()
        self.play(Write(anyone),run_time=3)
        self.wait()
        self.play(Write(fibo),run_time=3)
        self.wait()
        self.play(Write(rec),run_time=3)
        self.wait()
        self.play(Write(values),run_time=3)
        self.wait()
        self.play(Write(actually))
        self.wait()
        self.play(Write(equal))
        self.wait()
        howdo = TextMobject("So how do we calculate these values?")
        pretty = TextMobject("Pretty simple. Let's look at the following code.")
        howdo.next_to(equal.get_center(),DOWN)
        pretty.next_to(howdo.get_center(),DOWN)
        howdo.scale(0.8)
        pretty.scale(0.8)
        howdo.set_color(ORANGE)
        pretty.set_color(ORANGE)
        self.play(Write(howdo),run_time=4)
        self.wait()
        self.play(Write(pretty),run_time=4)
        self.wait()
        self.clear()


    def PageOfTilingSolution(self):
        recur = TextMobject("So what is the recurring subproblem here? Don't you think I ")
        dont = TextMobject("could give you the same problem where the grid is of length 5?")
        lets = TextMobject("Let's try to tile the grid from left to right in the following")
        ways = TextMobject("ways:")
        case1 = TextMobject("Case 1", " -"," Use a red tile in the leftmost cell:")
        recur.scale(0.7)
        dont.scale(0.7)
        lets.scale(0.7)
        ways.scale(0.7)
        case1.scale(0.7)
        case1[0].set_color = RED_A
        case1[2].set_color = GREEN_A
        
        case2 = TextMobject("Case 2"," -"," Use a blue tile in the leftmost cell:")
        case2.scale(0.7)
        case2_texts = [TexMobject("If the leftmost tile is blue, the next tile can either be red or blue."),TextMobject(" So, the number of valid tiling in this case will be equal"),
        TexMobject(" to the number of ways we can tile the rest of the n-1 cells which is equal to X_{n-1}"), TexMobject("Notice that to solve the problem for n, we need to solve the problem for smaller values such as n-1 and n-2 . The problem is recurring itself")]
        recur.shift(3*UP)
        dont.move_to(recur.get_center()+DOWN/2)
        lets.move_to(dont.get_center()+DOWN/2)
        ways.move_to(lets.get_center()+DOWN/2)
        case1.move_to(ways.get_center()+DOWN/2)
        recur.to_edge(LEFT)
        dont.to_edge(LEFT)
        lets.to_edge(LEFT)
        ways.to_edge(LEFT)
        case1.to_edge(LEFT)
        self.play(Write(recur),run_time=4)
        self.play(Write(dont),run_time=4)
        self.play(Write(lets),run_time=4)
        self.play(Write(ways),run_time=1)
        self.play(Write(case1),run_time=2)
        self.wait()

        case2.move_to(case1.get_center())
        case2.to_edge(LEFT) 

        square_scale = 0.375
        sq = Square().scale(square_scale)
        squares = []
        num_of_square = 6
        for i in range(num_of_square):
            squares.append(sq.copy())
        prev = sq
        prev.shift(RIGHT*1.5)
        for i in range(num_of_square):
            squares[i].move_to(prev.get_center()+RIGHT*square_scale*2)
            prev = squares[i]


        color1 = [MY_PINK,BLUE_E,BLACK,BLACK,BLACK,BLACK]
        colored_squares_1 = []
        for i,square in enumerate(squares):
            s = Square(fill_opacity=0.8,fill_color=color1[i]).scale(square_scale)
            s.move_to(square.get_center())
            colored_squares_1.append(s)
        for s in colored_squares_1:
            s.shift(DOWN)
        self.play(FadeIn(colored_squares_1[0]),FadeIn(colored_squares_1[1]),FadeIn(colored_squares_1[2]),FadeIn(colored_squares_1[3]),FadeIn(colored_squares_1[4]),FadeIn(colored_squares_1[5]))
        self.wait()
        vg4 = VGroup(colored_squares_1[2],colored_squares_1[3],colored_squares_1[4],colored_squares_1[5])
        brace = Brace(vg4,DOWN,buff = SMALL_BUFF)
        latec = TexMobject("n-2")
        latec.next_to(brace,DOWN,buff=SMALL_BUFF)
        arrow1 = Arrow(colored_squares_1[1].get_center()+3*DOWN/2,colored_squares_1[1].get_center()+DOWN/2)
        arrow1.set_color(YELLOW)
        arrow2 = Arrow(colored_squares_1[0].get_center()+3*UP/2,colored_squares_1[0].get_center()+UP/2)
        arrow2.set_color(YELLOW)
        arrow1_text = TextMobject("The 2nd tile must be blue").scale(0.5).set_color(BLUE_C)
        arrow2_text = TextMobject("If the first tile is red").scale(0.5).set_color(BLUE_C)
        arrow1_text.next_to(arrow1,DOWN)
        arrow2_text.next_to(arrow2,UP)
        self.play(ShowCreation(arrow2))
        self.play(Write(arrow2_text))
        self.play(ShowCreation(arrow1))
        self.play(Write(arrow1_text))
        self.play(GrowFromCenter(brace))
        self.play(Write(latec))
        self.wait()
        leftex1 = TextMobject("Let ")
        leftex2 = TexMobject("X_{n}")
        leftex3 = TextMobject("denote the number of ways such")
        leftex1.scale(0.7)
        leftex2.scale(0.7)
        leftex3.scale(0.7)
        leftex2.next_to(leftex1,RIGHT)
        leftex3.next_to(leftex2,RIGHT)
        leftex4 = TextMobject("a grid can be tiled so that no two red")
        leftex4.scale(0.7)
        leftex4.next_to(leftex1,DOWN)
        leftex5 = TextMobject("tiles remain adjacent.")
        leftex5.scale(0.7)
        vg = VGroup(leftex2,leftex1,leftex3)
        leftex4.to_edge(LEFT)
        vg.to_edge(LEFT)
        leftex5.next_to(leftex4,DOWN)
        leftex5.to_edge(LEFT)
        self.play(Write(leftex1))
        self.play(Write(leftex2))
        self.play(Write(leftex3),run_time=1.5)
        self.play(Write(leftex4),run_time = 2)
        self.play(Write(leftex5),run_time = 2)
        self.wait()
        self.remove(leftex4)
        self.remove(leftex3)
        self.remove(leftex2)
        self.remove(leftex1)
        self.remove(leftex5)
        leftex1 = TextMobject("But notice that if the leftmost tile is")
        leftex2 = TextMobject("red, then the next tile has to be blue to")
        leftex3 = TextMobject("not violate the condition.")
        leftex1.scale(0.7)
        leftex2.scale(0.7)
        leftex3.scale(0.7)
        leftex1.to_edge(LEFT)
        leftex2.to_edge(LEFT)
        leftex3.to_edge(LEFT)
        leftex2.next_to(leftex1,DOWN)
        leftex3.next_to(leftex2,DOWN)
        leftex1.to_edge(LEFT)
        leftex2.to_edge(LEFT)
        leftex3.to_edge(LEFT)
        self.play(Write(leftex1),run_time=2)
        self.play(Write(leftex2),run_time=2)
        self.play(Write(leftex3),run_time=2)
        self.wait(2)
        self.remove(leftex1)
        self.remove(leftex2)
        self.remove(leftex3)
        leftex = [
            TextMobject("And the rest of the grid has length "),
            TexMobject("n-2."),
            TextMobject("Since, the color of the first two tiles"),
            TextMobject("are fixed now, the problem of tiling the"),
            TextMobject("whole grid has come down to tiling a smaller"),
            TextMobject("grid of length"),
            TexMobject("n-2."),
            TextMobject("So, in this case,"),
            TextMobject("we can tile the grid in "),
            TexMobject("X_{n-2} "),
            TextMobject("ways.")
        ]
        for t in leftex:
            t.scale(0.7)
        leftex[1].next_to(leftex[0],RIGHT)
        leftex[2].next_to(leftex[1],DOWN)
        leftex[3].next_to(leftex[2],DOWN)
        leftex[4].next_to(leftex[3],DOWN)
        leftex[5].next_to(leftex[4],DOWN)
        leftex[6].next_to(leftex[5],RIGHT)
        leftex[7].next_to(leftex[6],RIGHT)
        leftex[8].next_to(leftex[7],DOWN)
        leftex[9].next_to(leftex[8],RIGHT)
        leftex[10].next_to(leftex[9],RIGHT)
        vg = VGroup(leftex[1],leftex[0])
        vg.to_edge(LEFT)
        vg = VGroup(leftex[6],leftex[5],leftex[7])
        vg.to_edge(LEFT)
        vg = VGroup(leftex[8],leftex[9],leftex[10])
        vg.to_edge(LEFT)
        for i in range(2,5):
            leftex[i].to_edge(LEFT)
        for t in leftex:
            self.play(Write(t),run_time=2)
        self.wait(5)
        for t in leftex:
            self.remove(t)
        self.wait(2)
        vg = VGroup(colored_squares_1[1],colored_squares_1[2],colored_squares_1[3],colored_squares_1[4],colored_squares_1[5])
        newbrace = Brace(vg,UP,buff = SMALL_BUFF)
        newlatec = TexMobject("n-1")
        newlatec.next_to(newbrace,UP,buff=SMALL_BUFF)

        newarrow1_text = TextMobject("The 2nd tile can be any color").scale(0.5).set_color(BLUE_C)
        newarrow2_text = TextMobject("If the first tile is blue").scale(0.5).set_color(BLUE_C)
        newarrow1_text.next_to(arrow1,DOWN)
        newarrow2_text.next_to(arrow2,UP)
        self.play(Transform(case1,case2))
        self.wait()
        S = Square(fill_color=BLACK,fill_opacity=0.8).scale(square_scale)
        S.move_to(colored_squares_1[1].get_center())
        M = Square(fill_opacity = 0.8, fill_color = BLUE_E).scale(square_scale)
        M.move_to(colored_squares_1[0].get_center())
        self.play(Transform(colored_squares_1[0],M))
        self.wait()
        self.play(Transform(colored_squares_1[1],S))
        self.wait()
        self.play(Transform(arrow2_text,newarrow2_text))
        self.wait()
        self.play(Transform(arrow1_text,newarrow1_text))
        self.wait()
        self.play(Transform(brace,newbrace))
        self.wait()
        self.play(Transform(latec,newlatec))
        self.wait()
        leftex = [
            TextMobject("If the first tile is blue, then the next "),
            TextMobject("tile can be of any color. So, the problem"),
            TextMobject("is equivalent to tiling a smaller grid of"),
            TextMobject("length "),
            TexMobject("n-1."),
            TextMobject("So, in this case, the number of ways we can"),
            TextMobject("tile the grid is "),
            TexMobject("X_{n-1}.")
        ]
        for t in leftex:
            t.scale(0.7)
        leftex[1].next_to(leftex[0],DOWN)
        leftex[2].next_to(leftex[1],DOWN)
        leftex[3].next_to(leftex[2],DOWN)
        leftex[4].next_to(leftex[3],RIGHT)
        leftex[5].next_to(leftex[4],DOWN)
        leftex[6].next_to(leftex[5],DOWN)
        leftex[7].next_to(leftex[6],RIGHT)

        vg = VGroup(leftex[4],leftex[3])
        vg.to_edge(LEFT)
        vg = VGroup(leftex[6],leftex[7])
        vg.to_edge(LEFT)
        leftex[0].to_edge(LEFT)
        leftex[1].to_edge(LEFT)
        leftex[2].to_edge(LEFT)
        leftex[5].to_edge(LEFT)
        for t in leftex:
            self.play(Write(t),run_time=2)
        self.wait(5)
        for t in leftex:
            self.play(FadeOut(t))
        self.wait(2)
        self.clear()
    def TilingProblem(self):
        self.TilingIntro()
        self.PageOfTilingSolution()
        self.PageOfFormulas()
        self.FibonacciSimulator(5)

    def GridStatement(self):
        header = TextMobject("The Grid Walking Problem")
        header.to_edge(UP).set_color(MY_DEEP_PURPLE).scale(1.5)
        suppose = TextMobject("Suppose, you are given an m x n grid. In how many ways can").set_color(GOLD_A)
        bottom = TextMobject("you go from the bottom-left corner to the top-right corner?").set_color(GOLD_A)
        S = Square().scale(2)
        suppose.next_to(header,DOWN)
        bottom.next_to(suppose,DOWN)
        S.next_to(bottom,DOWN)
        self.play(Write(header),run_time=2)
        self.play(Write(suppose),run_time=3)
        self.play(Write(bottom),run_time=3)
        self.add(S)

        z = S.get_center()
        a = z +2*LEFT + 2*UP
        c = z +2*RIGHT+ 2*DOWN
        b = a +4*RIGHT
        d = a +4*DOWN

        x3 = (a+b)/2.0
        y3 = (c+d)/2.0
        x1 = (5*a+b)/6.0
        x2 = (4*a+2*b)/6.0
        x4 = (2*a+4*b)/6.0
        x5 = (1*a+5*b)/6.0

        y1 =(1*c+5*d)/6.0
        y2 =(2*c+4*d)/6.0
        y4 =(4*c+2*d)/6.0
        y5 =(5*c+1*d)/6.0

        u1 = (1*d+5*a)/6.0
        u2 = (2*d+4*a)/6.0
        u3 = (3*d+3*a)/6.0
        u4 = (4*d+2*a)/6.0
        u5 = (5*d+1*a)/6.0

        v1 = (5*b+1*c)/6.0
        v2 = (4*b+2*c)/6.0
        v3 = (3*b+3*c)/6.0
        v4 = (2*b+4*c)/6.0
        v5 = (1*b+5*c)/6.0


        vertical1 = Line(x1,y1)
        vertical2 = Line(x2,y2)
        vertical3 = Line(x3,y3)
        vertical4 = Line(x4,y4)
        vertical5 = Line(x5,y5)

        horizontal1 = Line(u1,v1)
        horizontal2 = Line(u2,v2)
        horizontal3 = Line(u3,v3)
        horizontal4 = Line(u4,v4)
        horizontal5 = Line(u5,v5)
        square = VGroup(S,vertical1,vertical2,vertical3,vertical4,vertical5,horizontal1,horizontal2, horizontal3,horizontal4,horizontal5)
        self.play(ShowCreation(square),run_time=5)
        self.wait(5)

        p1 = (1*x1+5*y1)/6.0
        p2 = (1*x2+5*y2)/6.0
        p3 = (2*x2+4*y2)/6.0
        p4 = (2*x5+4*y5)/6.0

        path1 = Line(d,y1).set_color(MY_BLUE)
        path2 = Line(y1,p1).set_color(MY_RED)
        path3 = Line(p1,p2).set_color(MY_BLUE)
        path4 = Line(p2,p3).set_color(MY_RED)
        path5 = Line(p3,p4).set_color(MY_BLUE)
        path6 = Line(p4,x5).set_color(MY_RED)
        path7 = Line(x5,b).set_color(MY_BLUE)

        pathgroup = VGroup(path1,path2,path3,path4,path5,path6,path7)

        self.play(ShowCreation(path1))
        self.play(ShowCreation(path2))
        self.play(ShowCreation(path3))
        self.play(ShowCreation(path4))
        self.play(ShowCreation(path5),run_time=3)
        self.play(ShowCreation(path6),run_time=4)
        self.play(ShowCreation(path7))

        self.wait(3)

        self.remove(suppose)
        self.remove(bottom)
        self.wait()
        for i in range(7):
            self.remove(pathgroup[i])
        self.wait()
        self.play(square.next_to,header,DOWN,run_time=2)

        up_arrow = Arrow(d,u5).scale(4).set_color(MY_RED).shift(1.4*UP)
        right_arrow = Arrow(d,y1).scale(4).set_color(MY_BLUE).shift(1.4*UP)
        lets = TextMobject("Let $B_{m,n}$ denote the number of ways we can")
        travel = TextMobject("travel from the bottom-left corner of an m x n")
        tothe = TextMobject("grid to it's top-right corner.")
        when = TextMobject("When we are at the bottom-left corner, our first")
        first = TextMobject("move will be either to go right or to go up.")

        lets.next_to(square,DOWN)
        travel.next_to(lets,DOWN)
        tothe.next_to(travel,DOWN)
        when.next_to(square,DOWN)
        first.next_to(when,DOWN)

        self.play(Write(lets),run_time=3)
        self.play(Write(travel),run_time=3)
        self.play(Write(tothe),run_time=3)
        self.wait(2)
        self.remove(lets)
        self.remove(travel)
        self.remove(tothe)
        self.wait(2)

        self.play(Write(when),run_time=3)
        self.play(Write(first),run_time=3)
        self.wait(2)
        self.remove(when)
        self.remove(first)
        ifwe = TextMobject("If we go up, we arrive at the bottom-left corner")
        ofa = TextMobject("of an m-1 x n grid. By definition, from here we can")
        goto = TextMobject("go to the top-right corner in $B_{m-1,n}$ ways.")
        ifwe.next_to(square,DOWN)
        ofa.next_to(ifwe,DOWN)
        goto.next_to(ofa,DOWN)
        self.play(Write(ifwe),ShowCreation(up_arrow),run_time=3)
        self.play(Write(ofa),run_time=3)
        self.play(Write(goto),run_time=3)
        self.wait(2)
        self.remove(ifwe)
        self.remove(ofa)
        self.remove(goto)
        self.wait(2)
        ifwe = TextMobject("If we go right, we arrive at the bottom-left corner")
        ofa = TextMobject("of an m x n-1 grid. By definition, from here we can")
        goto = TextMobject("go to the top-right corner in $B_{m,n-1}$ ways.")
        ifwe.next_to(square,DOWN)
        ofa.next_to(ifwe,DOWN)
        goto.next_to(ofa,DOWN)
        self.remove(up_arrow)
        self.play(Write(ifwe),ShowCreation(right_arrow),run_time=3)
        self.play(Write(ofa),run_time=3)
        self.play(Write(goto),run_time=3)
        self.wait(2)
        self.remove(ifwe)
        self.remove(ofa)
        self.remove(goto)
        self.remove(right_arrow)
        self.wait(2)
        sothe = TextMobject("So, the total number of ways is:")
        form = TextMobject("$B_{m,n} = B_{m-1,n} + B_{m, n-1}$")
        sothe.next_to(square,DOWN)
        form.next_to(sothe,DOWN)
        self.play(Write(sothe),run_time=3)
        self.play(Write(form),run_time=3)
        self.wait(2)
        self.remove(sothe)
        self.remove(square)
        self.remove(vertical5)
        self.remove(vertical3)
        self.remove(vertical2)
        self.remove(vertical4)
        self.remove(vertical1)
        self.remove(horizontal1)
        self.remove(horizontal2)
        self.remove(horizontal3)
        self.remove(horizontal4)
        self.remove(horizontal5)
        self.wait()
        self.play(form.next_to,header,DOWN)
        self.wait()
        letsee = TextMobject("Let's see how we turn this recursion into a recursive function.")
        actually = TextMobject("Actually, $B_{m,n} = \\binom{m + n}{n}$. Think why.")
        letsee.next_to(form,DOWN)
        actually.next_to(letsee,DOWN)

        binom = TextMobject("int ", "Grid", "(", "int ", "m", ", ", "int ", "n", ")")
        binom_color = [PINK, GREEN_SCREEN, WHITE, PINK, ORANGE, WHITE, PINK, ORANGE, WHITE]
        binom = self.ColorSetter(binom,binom_color)
        base = TextMobject("if", "(", "m", " == ", "0", " or ", "n", " == ", " 0 ",")", " return", " 1", ";")
        base_color = [PINK,WHITE,ORANGE,PINK,MY_DEEP_PURPLE, PINK, ORANGE,PINK,MY_DEEP_PURPLE,WHITE,PINK, MY_DEEP_PURPLE,WHITE]
        base = self.ColorSetter(base,base_color)
        ret = TextMobject("else", " return ", "Grid", "(", "m", "-", "1", ",","n", ")", "+", "Grid", "(", "m", ",", "n","-","1",")", ";")
        ret_color = [PINK, PINK, GREEN_SCREEN, WHITE, ORANGE, PINK, MY_DEEP_PURPLE,WHITE, ORANGE,WHITE,PINK,GREEN_SCREEN,WHITE,ORANGE,WHITE,ORANGE,PINK, MY_DEEP_PURPLE,WHITE,WHITE]
        ret = self.ColorSetter(ret,ret_color)
        binom.next_to(actually,DOWN)
        base.next_to(binom,DOWN)
        ret.next_to(base,DOWN)
        binom.to_edge(LEFT)
        base.to_edge(LEFT)
        base.shift(RIGHT)
        ret.to_edge(LEFT)
        ret.shift(RIGHT)
        code = VGroup(binom,base,ret)
        code.shift(3*RIGHT)
        self.play(Write(letsee),run_time=4)
        self.play(Write(actually),run_time=3)
        self.play(Write(binom),run_time=2)
        self.play(Write(base),run_time=3)
        self.play(Write(ret),run_time=3)
        self.wait(5)


    def GridWalkingProblem(self):
        self.GridStatement()
        self.clear()

    def LengthOfString(self):
        header = TextMobject("Length of a String")
        header.to_edge(UP).set_color(MY_DEEP_PURPLE).scale(1.5)
        string = TextMobject("s"," = \"", "A","BCDEF", "\"")
        string[2].set_color(MY_RED)
        string[3].set_color(MY_BLUE)
        string.next_to(header,DOWN)
        wehave = TextMobject("We have previously seen that subsets of lists are also lists.")
        wewant = TextMobject("Even though in JAVA, s.length() returns the length of string s,")
        even = TextMobject("we want to find the length of a string using recursion.")
        form = TextMobject("Len(s) = 1 + Len(s.substring(1))")
        fun = TextMobject("int", " Fun", "(", "String ", "s", ")")
        fun_color = [PINK,GREEN_SCREEN,WHITE,PINK,ORANGE,WHITE]
        fun = self.ColorSetter(fun,fun_color)
        base = TextMobject("if","(", "s",".","equals","(","\"", "\"",")",")", " return ", "0", ";")
        base_color = [PINK,WHITE,ORANGE,WHITE,MY_BLUE,WHITE,WHITE,WHITE,WHITE,PINK,MY_DEEP_PURPLE,WHITE]
        base = self.ColorSetter(base,base_color)
        ret = TextMobject("return ", "1", "+", "Len", "(", "s", ".", "substring", "(", "1", ")", ")", ";")
        ret_color = [PINK,MY_DEEP_PURPLE, PINK,GREEN_SCREEN,WHITE,ORANGE,WHITE,MY_BLUE,WHITE,MY_DEEP_PURPLE,WHITE,WHITE,WHITE]
        ret = self.ColorSetter(ret,ret_color)

        wehave.next_to(string,DOWN)
        wewant.next_to(wehave,DOWN)
        even.next_to(wewant,DOWN)
        form.next_to(even,DOWN)

        fun.next_to(form,DOWN)
        base.next_to(fun,DOWN)
        ret.next_to(base,DOWN)


        fun.next_to(form,DOWN)
        base.next_to(fun,DOWN)
        ret.next_to(base,DOWN)
        fun.to_edge(LEFT)
        base.to_edge(LEFT)
        ret.to_edge(LEFT)
        base.shift(RIGHT)
        ret.shift(RIGHT)
        code = VGroup(fun,base,ret)
        code.shift(2*RIGHT)

        self.play(Write(header),run_time=2)
        self.play(Write(string),run_time=2)
        self.play(Write(wehave),run_time=4)
        self.play(Write(wewant),run_time=4)
        self.play(Write(even),run_time=4)
        self.play(Write(form),run_time=3)
        self.wait(3)
        self.play(Write(fun),run_time=3)
        self.play(Write(base),run_time=3)
        self.play(Write(ret),run_time=3)
        self.wait(3)

        self.remove(string)
        self.remove(wehave)
        self.remove(wewant)
        self.remove(even)
        self.remove(form)
        self.remove(fun)
        self.remove(base)
        self.remove(ret)

        r1 = TextMobject("Len(\"ABCDEF\")")
        r2 = TextMobject("= 1 + Len(\"BCDEF\")")
        r3 = TextMobject("= 1 + 1 + Len(\"CDEF\")")
        r4 = TextMobject("= 1 + 1 + 1 + Len(\"DEF\")")
        r5 = TextMobject("= 1 + 1 + 1 + 1 + Len(\"EF\")")
        r6 = TextMobject("= 1 + 1 + 1 + 1 + 1 + Len(\"F\")")
        r7 = TextMobject("= 1 + 1 + 1 + 1 + 1 + 1 + Len(\"\")")
        r8 = TextMobject("= 1 + 1 + 1 + 1 + 1 + 1 + 0")
        r9 = TextMobject("= 6")

        r1.next_to(header,DOWN)
        r2.next_to(r1,DOWN)
        r3.next_to(r2,DOWN)
        r4.next_to(r3,DOWN)
        r5.next_to(r4,DOWN)
        r6.next_to(r5,DOWN)
        r7.next_to(r6,DOWN)
        r8.next_to(r7,DOWN)
        r9.next_to(r8,DOWN)

        r1.to_edge(LEFT)
        r2.to_edge(LEFT)
        r3.to_edge(LEFT)
        r4.to_edge(LEFT)
        r5.to_edge(LEFT)
        r6.to_edge(LEFT)
        r7.to_edge(LEFT)
        r8.to_edge(LEFT)
        r9.to_edge(LEFT)

        rgroup = VGroup(r1,r2,r3,r4,r5,r6,r7,r8,r9)
        rgroup.shift(3*RIGHT)

        self.play(Write(r1),run_time=1)
        self.wait()
        self.play(Write(r2),run_time=1)
        self.wait()
        self.play(Write(r3),run_time=2)
        self.wait()
        self.play(Write(r4),run_time=2)
        self.wait()
        self.play(Write(r5),run_time=3)
        self.wait()
        self.play(Write(r6),run_time=3)
        self.wait()
        self.play(Write(r7),run_time=3)
        self.wait()
        self.play(Write(r8),run_time=3)
        self.wait()
        self.play(Write(r9))
        self.wait(3)

    def LengthOfLinkedList(self):
        header = TextMobject("Length of a Linked List")
        header.scale(1.5).to_edge(UP).set_color(MY_DEEP_PURPLE)
        wecan = TextMobject("We can similarly find the length of a linked list.")
        form = TextMobject("Len(list) = 1 + Len(list.next)")
        wecan.next_to(header,DOWN)
        form.next_to(wecan,DOWN)
        rad = 0.4
        A = Circle(fill_opacity=1,fill_color=DARK_GREY,radius=rad,color=WHITE)
        B = Circle(fill_opacity=1,fill_color=DARK_GREY,radius=rad,color=WHITE)
        C = Circle(fill_opacity=1,fill_color=DARK_GREY,radius=rad,color=WHITE)
        D = Circle(fill_opacity=1,fill_color=DARK_GREY,radius=rad,color=WHITE)
        E = Circle(fill_opacity=1,fill_color=DARK_GREY,radius=rad,color=WHITE)

        least = TextMobject("List")
        null = TextMobject("null")
        A.shift(LEFT*3)
        B.next_to(A,3.5*RIGHT)
        C.next_to(B,3.5*RIGHT)
        D.next_to(C,3.5*RIGHT)
        E.next_to(D,3.5*RIGHT)
        least.next_to(A,3.5*LEFT)
        null.next_to(E,3.5*RIGHT)
        arrow = Arrow(least.get_center(),A.get_center()).scale(0.7)
        Aarrow = Arrow(A.get_center(),B.get_center()).scale(0.7)
        Barrow = Arrow(B.get_center(),C.get_center()).scale(0.7)
        Carrow = Arrow(C.get_center(),D.get_center()).scale(0.7)
        Darrow = Arrow(D.get_center(),E.get_center()).scale(0.7)
        Earrow = Arrow(E.get_center(),null.get_center()).scale(0.7)

        a = TextMobject("A")
        b = TextMobject("B")
        c = TextMobject("C")
        d = TextMobject("D")
        e = TextMobject("E")

        a.move_to(A.get_center())
        b.move_to(B.get_center())
        c.move_to(C.get_center())
        d.move_to(D.get_center())
        e.move_to(E.get_center())

        LL = VGroup(least,null,a,b,c,d,e,A,B,C,D,E,arrow,Aarrow,Barrow,Carrow,Darrow,Earrow)
        LL.next_to(form,DOWN)


        self.play(Write(header),run_time=2)
        self.play(Write(wecan),run_time=4)
        self.play(Write(form),run_time=3)
        self.play(Write(least))
        self.play(ShowCreation(arrow))
        self.play(ShowCreation(A))
        self.play(Write(a))
        self.play(ShowCreation(Aarrow))
        self.play(ShowCreation(B))
        self.play(Write(b))
        self.play(ShowCreation(Barrow))
        self.play(ShowCreation(C))
        self.play(Write(c))
        self.play(ShowCreation(Carrow))
        self.play(ShowCreation(D))
        self.play(Write(d))
        self.play(ShowCreation(Darrow))
        self.play(ShowCreation(E))
        self.play(Write(e))
        self.play(ShowCreation(Earrow))
        self.play(Write(null))
        self.wait(2)

        fun = TextMobject("int ", "Fun", "(", "Node ", "list", ")")
        fun_color = [PINK,GREEN_SCREEN,WHITE,PINK,ORANGE,WHITE]
        fun = self.ColorSetter(fun,fun_color)
        base = TextMobject("if", "(", "list", " == ", "null", ")", " return ", "0" ,";")
        base_color = [PINK, WHITE, ORANGE, PINK, MY_DEEP_PURPLE, WHITE,PINK,MY_DEEP_PURPLE, WHITE]
        base = self.ColorSetter(base,base_color)
        ret = TextMobject("return ", "1", "+", "Fun", "(", "list",".","next",")",";")
        ret_color = [PINK,MY_DEEP_PURPLE,PINK,GREEN_SCREEN,WHITE,ORANGE,WHITE,MY_BLUE,WHITE,WHITE]
        ret = self.ColorSetter(ret,ret_color)


        fun.next_to(A,DOWN)
        base.next_to(fun,DOWN)
        ret.next_to(base,DOWN)
        fun.to_edge(LEFT)
        base.to_edge(LEFT)
        ret.to_edge(LEFT)
        base.shift(RIGHT)
        ret.shift(RIGHT)
        code = VGroup(fun,base,ret)
        code.shift(2*RIGHT+DOWN)

        self.play(Write(fun),run_time=2)
        self.play(Write(base),run_time=3)
        self.play(Write(ret),run_time=3)
        self.wait(3)
        for v in LL:
            self.remove(v)
        self.remove(wecan)
        self.remove(form)
        for i in code:
            self.remove(i)

        r1 = TextMobject("Len(A)")
        r2 = TextMobject("= 1 + Len(B)")
        r3 = TextMobject("= 1 + 1 + Len(C)")
        r4 = TextMobject("= 1 + 1 + 1 + Len(D)")
        r5 = TextMobject("= 1 + 1 + 1 + 1 + Len(E)")
        r6 = TextMobject("= 1 + 1 + 1 + 1 + 1 + Len(null)")
        r7 = TextMobject("= 1 + 1 + 1 + 1 + 1 + 0")
        r8 = TextMobject("= 5")

        r1.next_to(header,DOWN)
        r2.next_to(r1,DOWN)
        r3.next_to(r2,DOWN)
        r4.next_to(r3,DOWN)
        r5.next_to(r4,DOWN)
        r6.next_to(r5,DOWN)
        r7.next_to(r6,DOWN)
        r8.next_to(r7,DOWN)

        r1.to_edge(LEFT)
        r2.to_edge(LEFT)
        r3.to_edge(LEFT)
        r4.to_edge(LEFT)
        r5.to_edge(LEFT)
        r6.to_edge(LEFT)
        r7.to_edge(LEFT)
        r8.to_edge(LEFT)

        rgroup = VGroup(r1,r2,r3,r4,r5,r6,r7,r8)
        rgroup.shift(3*RIGHT)

        self.play(Write(r1),run_time=1)
        self.wait()
        self.play(Write(r2),run_time=1)
        self.wait()
        self.play(Write(r3),run_time=2)
        self.wait()
        self.play(Write(r4),run_time=2)
        self.wait()
        self.play(Write(r5),run_time=3)
        self.wait()
        self.play(Write(r6),run_time=3)
        self.wait()
        self.play(Write(r7),run_time=3)
        self.wait()
        self.play(Write(r8))
        self.wait(3)


    def SumOfIntegers(self):
        header = TextMobject("Sum of Integers from 1 to N").to_edge(UP).scale(1.5).set_color(MY_DEEP_PURPLE)
        form = TextMobject("sum(n) ="," $n$", " + ", "$(n-1) +  ....  + 3 + 2 + 1$")
        brace = Brace(form[3],DOWN,buff=SMALL_BUFF)
        rec = TextMobject("Sum(n) = n + Sum(n-1)")
        brace_text = TextMobject("Sum(n-1)").next_to(form[3],1.8*DOWN).scale(0.7)
        formula = VGroup(form,brace,brace_text).next_to(header,DOWN)
        rec.next_to(form,4*DOWN)
        
        self.play(Write(header),run_time=2)
        self.play(Write(form),run_time=3)
        self.play(ShowCreation(brace),Write(brace_text), run_time=2)
        self.play(Write(rec),run_time=2)
        self.wait()

        fun = TextMobject("int ", "Sum", "(", "int ", "n", ")")
        fun_color = [PINK,GREEN_SCREEN,WHITE,PINK,ORANGE,WHITE]
        fun = self.ColorSetter(fun,fun_color)
        base = TextMobject("if", "(", "n", " == ", "0", ")", " return ", "0" ,";")
        base_color = [PINK, WHITE, ORANGE, PINK, MY_DEEP_PURPLE, WHITE,PINK,MY_DEEP_PURPLE, WHITE]
        base = self.ColorSetter(base,base_color)
        ret = TextMobject("return ", "n", "+", "Sum", "(", "n","-","1",")",";")
        ret_color = [PINK,ORANGE,PINK,GREEN_SCREEN,WHITE,ORANGE,PINK,MY_BLUE,WHITE,WHITE]
        ret = self.ColorSetter(ret,ret_color)


        fun.next_to(rec,DOWN)
        base.next_to(fun,DOWN)
        ret.next_to(base,DOWN)
        fun.to_edge(LEFT)
        base.to_edge(LEFT)
        ret.to_edge(LEFT)
        base.shift(RIGHT)
        ret.shift(RIGHT)
        code = VGroup(fun,base,ret)
        code.shift(2*RIGHT+DOWN)

        self.play(Write(fun),run_time=2)
        self.play(Write(base),run_time=3)
        self.play(Write(ret),run_time=3)
        self.wait(3)
        
        self.remove(rec)
        self.remove(form)
        self.remove(brace)
        self.remove(brace_text)
        for i in code:
            self.remove(i)

        r1 = TextMobject("Sum(5)")
        r2 = TextMobject("= 5 + Sum(4)")
        r3 = TextMobject("= 5 + 4 + Sum(3)")
        r4 = TextMobject("= 5 + 4 + 3 + Sum(2)")
        r5 = TextMobject("= 5 + 4 + 3 + 2 + Sum(1)")
        r6 = TextMobject("= 5 + 4 + 3 + 2 + 1 + Sum(0)")
        r7 = TextMobject("= 5 + 4 + 3 + 2 + 1 + 0")
        r8 = TextMobject("= 15")

        r1.next_to(header,DOWN)
        r2.next_to(r1,DOWN)
        r3.next_to(r2,DOWN)
        r4.next_to(r3,DOWN)
        r5.next_to(r4,DOWN)
        r6.next_to(r5,DOWN)
        r7.next_to(r6,DOWN)
        r8.next_to(r7,DOWN)

        r1.to_edge(LEFT)
        r2.to_edge(LEFT)
        r3.to_edge(LEFT)
        r4.to_edge(LEFT)
        r5.to_edge(LEFT)
        r6.to_edge(LEFT)
        r7.to_edge(LEFT)
        r8.to_edge(LEFT)

        rgroup = VGroup(r1,r2,r3,r4,r5,r6,r7,r8)
        rgroup.shift(3*RIGHT)

        self.play(Write(r1),run_time=1)
        self.wait()
        self.play(Write(r2),run_time=1)
        self.wait()
        self.play(Write(r3),run_time=2)
        self.wait()
        self.play(Write(r4),run_time=2)
        self.wait()
        self.play(Write(r5),run_time=3)
        self.wait()
        self.play(Write(r6),run_time=3)
        self.wait()
        self.play(Write(r7),run_time=3)
        self.wait()
        self.play(Write(r8))
        self.wait(3)

    def ExpoFirstTwoPages(self):
        header = TextMobject("Exponentiation")
        ts = 1
        suppose = TextMobject("Suppose, you need to find $7^{5002003}$. Of course you can do it").scale(ts)
        using = TextMobject("using library functions or a loop. In JAVA, you can't store").scale(ts)
        python = TextMobject("such a big number. But you can do it in python. In JAVA, ").scale(ts)
        java = TextMobject("you can use the BigInteger library. But for now, use small").scale(ts)
        fornow = TextMobject("values. Let's find a recurrence relation for exponentiation.").scale(ts)
        ltx = 0.8
        form1 = TextMobject("$a^{n} =$").scale(ltx)
        form111 = TextMobject("$a^{n-1} \\times a$,","x","if $n>0$.").scale(ltx)
        form11 = TextMobject("$1$,","xxxxxxx","if $n$ $=$ $0.$").scale(ltx)

        form2 =   TextMobject("$a^{n} =$").scale(ltx)
        form2222 = TextMobject("$a^{n-2} \\times a^{2}$,","x","if $n$ $>$ $1$.").scale(ltx)
        form22 =TextMobject("$1$,","xxxxixxxx","if $n$ $=$ $0$.").scale(ltx)
        form222 =  TextMobject("$a$,","xxxxxxxx","if $n$ $=$ $1$.").scale(ltx)

        form3 = TextMobject("$a^{n} =$").scale(ltx)
        form333 =  TextMobject("$a^{\\frac{n}{2}}\\times a^{\\frac{n}{2}}$,","xxxx","if $n$ $=$ $0$ mod $2$.").scale(ltx)
        form3333 = TextMobject("$a^{\\frac{n}{2}}\\times a^{\\frac{n}{2}}\\times a$,","x","if $n$ $=$ $1$ mod $2$.").scale(ltx)
        form33 =   TextMobject("$1$,","xazxxxxxxxi", "if $n$ $=$ $0.$").scale(ltx)

        form4 = TextMobject("$a^{n} =$").scale(ltx)
        form44 =   TextMobject("$1$, ","xxxxxxxxxxxxxxx","if $n = 0.$").scale(ltx)
        form4444 = TextMobject("$a^{\\frac{n}{3}}\\times a^{\\frac{n}{3}}\\times a^{\\frac{n}{3}}\\times a$,  ","x","if $n$ $=$ $1$ mod $3$.").scale(ltx)
        form44444 =TextMobject("$a^{\\frac{n}{3}}\\times a^{\\frac{n}{3}}\\times a^{\\frac{n}{3}}\\times a^{2}$,","x","if $n$ $=$ $2$ mod $3$.").scale(ltx)
        form444 =  TextMobject("$a^{\\frac{n}{3}}\\times a^{\\frac{n}{3}}\\times a^{\\frac{n}{3}}$,","xxxxx","if $n$ $=$ $0$ mod $3$.").scale(ltx)

        form44444[1].set_color(BLACK)
        form44[1].set_color(BLACK)
        form444[1].set_color(BLACK)
        form4444[1].set_color(BLACK)

        form22[1].set_color(BLACK)
        form222[1].set_color(BLACK)
        form2222[1].set_color(BLACK)

        form33[1].set_color(BLACK)
        form333[1].set_color(BLACK)
        form3333[1].set_color(BLACK)

        form11[1].set_color(BLACK)
        form111[1].set_color(BLACK)

        header.to_edge(UP).scale(1.5).set_color(MY_DEEP_PURPLE)
        suppose.shift(UP)
        using.next_to(suppose,DOWN)
        python.next_to(using,DOWN)
        java.next_to(python,DOWN)
        fornow.next_to(java,DOWN)
        form11.shift(2*LEFT+2*UP)
        form111.next_to(form11,DOWN)
        form22.shift(2*RIGHT-2*UP)
        form222.next_to(form22,DOWN)
        form2222.next_to(form222,DOWN)
        form33.shift(2*RIGHT-DOWN)
        form333.next_to(form33,DOWN)
        form3333.next_to(form333,DOWN)
        form44.shift(2*LEFT+DOWN)
        form444.next_to(form44,DOWN)
        form4444.next_to(form444,DOWN)
        form44444.next_to(form4444,DOWN)

        form1.to_edge(LEFT)
        form11.to_edge(LEFT)
        form111.to_edge(LEFT)
        form2.to_edge(LEFT)
        form22.to_edge(LEFT)
        form222.to_edge(LEFT)
        form2222.to_edge(LEFT)
        form3.to_edge(LEFT)
        form33.to_edge(LEFT)
        form333.to_edge(LEFT)
        form3333.to_edge(LEFT)
        form4.to_edge(LEFT)
        form44.to_edge(LEFT)
        form444.to_edge(LEFT)
        form4444.to_edge(LEFT)
        form44444.to_edge(LEFT)
        

        g4 = VGroup(form44,form444,form4444,form44444)
        g1 = VGroup(form11,form111)
        g2 = VGroup(form22, form222,form2222)
        g3 = VGroup(form33, form333,form3333)

        g1.shift(9*RIGHT)
        g2.shift(1*RIGHT+UP)
        g3.shift(1*RIGHT+UP)
        g4.shift(7*RIGHT)

        b1 = Brace(g1,LEFT,buff=SMALL_BUFF)
        b2 = Brace(g2,LEFT,buff=SMALL_BUFF)
        b3 = Brace(g3,LEFT,buff=SMALL_BUFF)
        b4 = Brace(g4,LEFT,buff=SMALL_BUFF)

        form1.next_to(b1,LEFT)
        form2.next_to(b2,LEFT)
        form3.next_to(b3,LEFT)
        form4.next_to(b4,LEFT)

        self.play(Write(header),run_time=2)
        self.play(Write(suppose),run_time=4)
        self.play(Write(using),run_time=4)
        self.play(Write(python),run_time=4)
        self.play(Write(java),run_time=4)
        self.play(Write(fornow),run_time=3)

        self.wait(2)
        self.remove(suppose)
        self.remove(using)
        self.remove(python)
        self.remove(java)
        self.remove(fornow)
        self.wait()

        
        self.play(Write(form33))
        self.play(Write(form333))
        self.play(Write(form3333))
        self.play(ShowCreation(b3))
        self.play(Write(form3))
        self.play(Write(form11))
        self.play(Write(form111))
        self.play(ShowCreation(b1))
        self.play(Write(form1))
        self.play(Write(form22))
        self.play(Write(form222))
        self.play(Write(form2222))
        self.play(ShowCreation(b2))
        self.play(Write(form2))
        self.play(Write(form44))
        self.play(Write(form444))
        self.play(Write(form4444))
        self.play(Write(form44444))
        self.play(ShowCreation(b4))
        self.play(Write(form4))
        self.wait(2)

        for i in g1:
            self.remove(i)

        for j in g2:
            self.remove(j)

        for k in g3:
            self.remove(k)

        for l in g4:
            self.remove(l)

        self.remove(b1)
        self.remove(b2)
        self.remove(b3)
        self.remove(b4)
        self.remove(form1)
        self.remove(form2)
        self.remove(form3)
        self.remove(form4)
        self.wait()

    def ExpoCodePage(self):
        code2 = [
                TextMobject("int", " Expo", "(", " int ", "a ", ",", " int ", "n", ")"),
                TextMobject("if", "(", "n", " == ", "0", ")", " return ", "1", ";"),
                TextMobject("int ", "x" , " = ", "Expo", "(", "a", ",", " n", "-", "1",")", ";"),
                TextMobject("return ", "x", "*", "a",";"),
        ]
        color2 = [
                [PINK, GREEN_SCREEN, WHITE, PINK, ORANGE, WHITE, PINK, WHITE],
                [PINK, WHITE, ORANGE, WHITE, MY_DEEP_PURPLE, WHITE, PINK, MY_DEEP_PURPLE, WHITE],
                [PINK, ORANGE, PINK, GREEN_SCREEN, WHITE, ORANGE, WHITE, ORANGE, PINK, MY_DEEP_PURPLE, WHITE,WHITE],
                [PINK, ORANGE, PINK, ORANGE, WHITE],
        ]
        color_code2 = []

        for i in range(4):
            x = self.ColorSetter(code2[i], color2[i])
            color_code2.append(x)

        color_code2[0].to_edge(UP)
        color_code2[0].shift(DOWN)
        for i in range(1,4):
            color_code2[i].next_to(color_code2[i-1],DOWN)

        for i in range(4):
            color_code2[i].to_edge(LEFT)
            if i > 0:
                color_code2[i].shift(RIGHT)


        for i in range(4):
            self.play(Write(color_code2[i]),run_time=3)

        self.wait(3)

        simu2 = [
                TextMobject("Expo(2,7)"),
                TextMobject("=2*Expo(2,6)"),
                TextMobject("=2*2*Expo(2,5)"),
                TextMobject("=2*2*2*Expo(2,4)"),
                TextMobject("=2*2*2*2*Expo(2,3)"),
                TextMobject("=2*2*2*2*2*Expo(2,2)"),
                TextMobject("=2*2*2*2*2*2*Expo(2,1)"),
                TextMobject("=2*2*2*2*2*2*2*Expo(2,0)"),
                TextMobject("=2*2*2*2*2*2*2*1"),
                TextMobject("=128"),
        ]


        simu2[0].to_edge(UP)
        simu2[0].shift(DOWN)
        for i in range(1,10):
            simu2[i].next_to(simu2[i-1],DOWN)

        for i in range(10):
            simu2[i].to_edge(LEFT)
            simu2[i].shift(7*RIGHT)

        for i in range(10):
            self.play(Write(simu2[i]),run_time=3)
        self.wait(3)

        for i in range(10):
            self.remove(simu2[i])

        for i in range(4):
            self.remove(code2[i])

        code1 = [
                TextMobject("int", " Expo", "(", " int ", "a ", ",", " int ", "n", ")"),
                TextMobject("if", "(", "n", " == ", "0", ")", " return ", "1", ";"),
                TextMobject("int ", "x" , " = ", "Expo", "(", "a", ",", " n", "/", "2",")", ";"),
                TextMobject("if", "(",  "n", " \\% ", "2" , " == ", "0", ")"),
                TextMobject("return ", "x", "*", "x", ";"),
                TextMobject("else ", "return ", "x", "*", "x", "*", "a",";"),
        ]
        color1 = [
                [PINK, GREEN_SCREEN, WHITE, PINK, ORANGE, WHITE, PINK, WHITE],
                [PINK, WHITE, ORANGE, WHITE, MY_DEEP_PURPLE, WHITE, PINK, MY_DEEP_PURPLE, WHITE],
                [PINK, ORANGE, WHITE, GREEN_SCREEN, WHITE, ORANGE, WHITE, ORANGE, PINK, MY_DEEP_PURPLE, WHITE,WHITE],
                [PINK, WHITE, ORANGE, PINK, MY_DEEP_PURPLE, PINK, MY_DEEP_PURPLE, WHITE],
                [PINK, ORANGE, PINK, ORANGE, WHITE],
                [PINK, PINK, ORANGE, PINK, ORANGE, PINK, ORANGE, WHITE]
        ]
        color_code1 = []

        for i in range(6):
            x = self.ColorSetter(code1[i], color1[i])
            color_code1.append(x)

        color_code1[0].to_edge(UP)
        color_code1[0].shift(DOWN)
        for i in range(1,6):
            color_code1[i].next_to(color_code1[i-1],DOWN)

        for i in range(6):
            color_code1[i].to_edge(LEFT)
            if i > 0:
                color_code1[i].shift(RIGHT)
        color_code1[4].shift(RIGHT)

        for i in range(6):
            self.play(Write(color_code1[i]),run_time=3)

        self.wait(3)

        simu2 = [
                TextMobject("Expo(2,7)"),
                TextMobject("x = Expo(2,3)"),
                TextMobject("x = Expo(2,1)"),
                TextMobject("x = Expo(2,0)"),
                TextMobject("return 1"),
                TextMobject("return 1*1*2"),
                TextMobject("return 2*2*2"),
                TextMobject("return 8*8*2"),
                TextMobject("return 128")
        ]


        simu2[0].to_edge(UP)
        simu2[0].shift(DOWN)
        for i in range(1,9):
            simu2[i].next_to(simu2[i-1],DOWN)

        for i in range(9):
            simu2[i].to_edge(LEFT)
            simu2[i].shift(7*RIGHT)

        for i in range(9):
            self.play(Write(simu2[i]),run_time=3)
        self.wait(3)

        for i in range(9):
            self.remove(simu2[i])
        for i in range(6):
            self.remove(color_code1[i])


    def Exponentiation(self):
        self.ExpoFirstTwoPages()
        self.ExpoCodePage()

    def BTDStatement(self):
        header = TextMobject("Binary to Decimal").scale(1.5).to_edge(UP).set_color(MY_DEEP_PURPLE)

        suppose = TextMobject("You will be given a string that represents the binary representation").scale(0.8)
        number = TextMobject("of a number. Your job is convert it to a decimal number. I know you").scale(0.8)
        guys = TextMobject("guys will very easily do it with loops. Recursion is an alternate for").scale(0.8)
        loops = TextMobject("loops. We will see how.").scale(0.8)

        binary = TextMobject("1011011").scale(1.5).set_color(MY_CYAN)
        decimal = TextMobject("91").scale(1.5).set_color(MY_RED)
        decimal.next_to(binary, RIGHT)
        arrow = Arrow(binary.get_center(), decimal.get_center())
        decimal.shift(RIGHT)
        binary.shift(LEFT)
        arrow.shift(RIGHT*0.5)

        vg = VGroup(decimal, binary, arrow)
        vg.shift(DOWN+LEFT)

        suppose.next_to(header,DOWN)
        number.next_to(suppose,DOWN)
        guys.next_to(number,DOWN)
        loops.next_to(guys,DOWN)


        self.play(FadeIn(header),run_time=3)
        self.play(Write(suppose),run_time=4)
        self.play(Write(number),run_time=4)
        self.play(Write(guys),run_time=4)
        self.play(Write(loops),run_time=4)

        self.play(Write(binary), run_time=2)
        self.play(ShowCreation(arrow), run_time = 2)
        self.play(Write(decimal), run_time = 2)
        self.wait(3)

        self.remove(suppose)
        self.remove(number)
        self.remove(guys)
        self.remove(loops)
        self.remove(binary)
        self.remove(decimal)
        self.remove(arrow)

    def RecursiveBTD(self):
        loop = [
            TextMobject("int", " RecursiveBTD", "(", "String ", "s","," ," int" , " i", ","," int", " num", ")"),
            TextMobject("if", "(", "s", ".", "length", "(", ")", " == " , " i", ") ", "return", " num", ";" ),
            TextMobject("if", "(", "s", ".", "charAt", "(", "i", ")", " == ", "\"", "0","\"",")" ),
            TextMobject("num" , " = ", "2", "*", "num", ";"),
            TextMobject("else ", "num" , " = ", "2", "*", "num", "+", "1", ";"),
            TextMobject("return", " RecursiveBTD", "(", "s",",", "i", "+", "1", ",","num", ")",";")
        ]
        iterative1 = TextMobject("Recursive solution for binary to decimal").set_color(GOLD_E)
        iterative1.shift(UP*2)
        loop2 = loop
        for l in loop:
            l.scale(0.7)
        loop_color = [
            [PINK, GREEN_SCREEN, WHITE, PINK, ORANGE, WHITE ,PINK, ORANGE, WHITE, PINK, ORANGE, WHITE],
            [PINK, WHITE, ORANGE, WHITE, GREEN_SCREEN, WHITE, WHITE, PINK, ORANGE, WHITE, PINK,  ORANGE, WHITE],
            [PINK, WHITE, ORANGE, WHITE, BLUE_E, WHITE, ORANGE, WHITE, PINK, WHITE, MY_DEEP_PURPLE, WHITE, WHITE],
            [ORANGE, PINK, MY_DEEP_PURPLE, PINK, ORANGE, WHITE],
            [PINK, ORANGE, PINK, MY_DEEP_PURPLE, PINK, ORANGE, PINK, MY_DEEP_PURPLE, WHITE],
            [PINK, GREEN_SCREEN, WHITE, ORANGE,WHITE, ORANGE,PINK,MY_DEEP_PURPLE, WHITE,ORANGE,WHITE,WHITE],
        ]

        for i in range(len(loop)):
            loop[i] = self.ColorSetter(loop[i], loop_color[i])
            if i == 0:
                loop[i].next_to(iterative1,DOWN)
            else:
                loop[i].next_to(loop[i-1],DOWN)

        for l in loop:
            l.to_edge(LEFT)
            l.shift(6.5*RIGHT)

        for i in range(len(loop)):
            if i > 0:
                loop[i].shift(RIGHT)
        loop[3].shift(RIGHT)

        self.play(Write(iterative1),run_time=3)
        for l in loop:
            self.play(Write(l),run_time=3)

        self.wait(3)
        

        sim = [
            TextMobject("RecursiveBTD(\"1011011\",0)"),
            TextMobject("=RecursiveBTD(\"011011\",1)"),
            TextMobject("=RecursiveBTD(\"11011\",2)"),
            TextMobject("=RecursiveBTD(\"1011\",5)"),
            TextMobject("=RecursiveBTD(\"011\",11)"),
            TextMobject("=RecursiveBTD(\"11\",22)"),
            TextMobject("=RecursiveBTD(\"1\",45)"),
            TextMobject("=RecursiveBTD(\"\",91)"),
            TextMobject("=91")
        ]
        for i in sim:
            i.scale(0.8)
        sim[0].next_to(loop[0],LEFT)
        sim[0].shift(LEFT)

        for i in range(len(sim)):
            if i > 0:
                sim[i].next_to(sim[i-1],DOWN)
        for i in sim:
            i.to_edge(LEFT)
        for i in sim:
            self.play(Write(i))
        self.wait(2)

        self.remove(iterative1)
        for l in loop:
            self.remove(l)

    def IterativeBTD(self):
        loop = [
            TextMobject("int", " IterativeBTD", "(", "String ", "s", ")"),
            TextMobject("int", " num", " = ", "0", ";"),
            TextMobject("for", "(", "int ", "i" , " = ", "0", ";", "i ", "<", " s",".","length","()", ";", "i", "++",")"),
            TextMobject("if", "(", "s", ".", "charAt", "(", "i", ")", " == ", "\"", "0","\"",")" ),
            TextMobject("num" , " = ", "2", "*", "num", ";"),
            TextMobject("else ", "num" , " = ", "2", "*", "num", "+", "1", ";"),
            TextMobject("return", " num", ";")
        ]
        loop1 = loop
        for l in loop:
            l.scale(0.7)
        loop_color = [
            [PINK, GREEN_SCREEN, WHITE, PINK, ORANGE, WHITE],
            [PINK, ORANGE, PINK, MY_DEEP_PURPLE, WHITE],
            [PINK, WHITE, PINK, ORANGE, PINK, MY_DEEP_PURPLE, WHITE, ORANGE, PINK, ORANGE, WHITE, BLUE_E, WHITE, WHITE, ORANGE, PINK,WHITE],
            [PINK, WHITE, ORANGE, WHITE, BLUE_E, WHITE, ORANGE, WHITE, PINK, WHITE, MY_DEEP_PURPLE, WHITE, WHITE],
            [ORANGE, PINK, MY_DEEP_PURPLE, PINK, ORANGE, WHITE],
            [PINK, ORANGE, PINK, MY_DEEP_PURPLE, PINK, ORANGE, PINK, MY_DEEP_PURPLE, WHITE],
            [PINK, ORANGE, WHITE],
        ]
        iterative1 = TextMobject("Iterative solution for binary to decimal").set_color(GOLD_E)
        iterative1.shift(UP*2)
        for i in range(len(loop)):
            loop[i] = self.ColorSetter(loop[i], loop_color[i])
            if i == 0:
                loop[i].next_to(iterative1,DOWN)
            else:
                loop[i].next_to(loop[i-1],DOWN)

        for l in loop:
            l.to_edge(LEFT)

        for i in range(len(loop)):
            if i > 0:
                loop[i].shift(RIGHT)
        loop[3].shift(RIGHT)
        loop[4].shift(RIGHT*2)
        loop[5].shift(RIGHT)
        self.play(Write(iterative1),run_time=3)
        for l in loop:
            self.play(Write(l),run_time=3)

        self.wait(3)

        binary = TextMobject("1","0","1","1","0","1","1").scale(1.5).set_color(MY_CYAN)
        binary.shift(RIGHT*2.5+UP)

        self.play(Write(binary),run_time=2)
        arr = Arrow(binary.get_center(),binary.get_center())
        num = 0
        Num = TextMobject("num = %d"%num)
        Num.next_to(binary)
        Num.shift(DOWN)
        self.play(Write(Num))
        for i in range(7):
            arr = Arrow(binary[i].get_center()+DOWN,binary[i].get_center())
            self.play(ShowCreation(arr))
            if i == 1 or i == 4:
                num = num*2
                bum = TextMobject("num = %d"%num)
                bum.move_to(Num)
                self.play(Transform(Num,bum))
            else:
                num = num*2+1
                bum = TextMobject("num = %d"%num)
                bum.move_to(Num)
                self.play(Transform(Num,bum))
            self.wait()
            self.remove(arr)
        self.remove(iterative1)
        for l in loop1:
            self.remove(l)
        self.remove(binary)
        self.remove(arr)
        self.remove(Num)

    def BTDCodeComparison(self):
        loop = [
            TextMobject("int", " IterativeBTD", "(", "String ", "s", ")"),
            TextMobject("int", " num", " = ", "0", ";"),
            TextMobject("for", "(", "int ", "i" , " = ", "0", ";", "i ", "<", " s",".","length","()", ";", "i", "++",")"),
            TextMobject("if", "(", "s", ".", "charAt", "(", "i", ")", " == ", "\"", "0","\"",")" ),
            TextMobject("num" , " = ", "2", "*", "num", ";"),
            TextMobject("else ", "num" , " = ", "2", "*", "num", "+", "1", ";"),
            TextMobject("return", " num", ";")
        ]
        loop1 = loop
        for l in loop:
            l.scale(0.7)
        loop_color = [
            [PINK, GREEN_SCREEN, WHITE, PINK, ORANGE, WHITE],
            [PINK, ORANGE, PINK, MY_DEEP_PURPLE, WHITE],
            [PINK, WHITE, PINK, ORANGE, PINK, MY_DEEP_PURPLE, WHITE, ORANGE, PINK, ORANGE, WHITE, BLUE_E, WHITE, WHITE, ORANGE, PINK,WHITE],
            [PINK, WHITE, ORANGE, WHITE, BLUE_E, WHITE, ORANGE, WHITE, PINK, WHITE, MY_DEEP_PURPLE, WHITE, WHITE],
            [ORANGE, PINK, MY_DEEP_PURPLE, PINK, ORANGE, WHITE],
            [PINK, ORANGE, PINK, MY_DEEP_PURPLE, PINK, ORANGE, PINK, MY_DEEP_PURPLE, WHITE],
            [PINK, ORANGE, WHITE],
        ]
        iterative1 = TextMobject("Comparison between iterative and recursive approach").set_color(GOLD_E)
        iterative1.shift(UP*2)
        for i in range(len(loop)):
            loop[i] = self.ColorSetter(loop[i], loop_color[i])
            if i == 0:
                loop[i].next_to(iterative1,DOWN)
            else:
                loop[i].next_to(loop[i-1],DOWN)

        for l in loop:
            l.to_edge(LEFT)

        for i in range(len(loop)):
            if i > 0:
                loop[i].shift(RIGHT)
        loop[3].shift(RIGHT)
        loop[4].shift(RIGHT*2)
        loop[5].shift(RIGHT)
        self.play(Write(iterative1),run_time=3)
        for l in loop:
            self.play(Write(l),run_time=3)

        self.wait(3)

        loop = [
            TextMobject("int", " RecursiveBTD", "(", "String ", "s","," ," int" , " i", ","," int", " num", ")"),
            TextMobject("if", "(", "s", ".", "length", "(", ")", " == " , " i", ") ", "return", " num", ";" ),
            TextMobject("if", "(", "s", ".", "charAt", "(", "i", ")", " == ", "\"", "0","\"",")" ),
            TextMobject("num" , " = ", "2", "*", "num", ";"),
            TextMobject("else ", "num" , " = ", "2", "*", "num", "+", "1", ";"),
            TextMobject("return", " RecursiveBTD", "(", "s",",", "i", "+", "1", ",","num", ")",";")
        ]

        loop2 = loop
        for l in loop:
            l.scale(0.7)
        loop_color = [
            [PINK, GREEN_SCREEN, WHITE, PINK, ORANGE, WHITE ,PINK, ORANGE, WHITE, PINK, ORANGE, WHITE],
            [PINK, WHITE, ORANGE, WHITE, GREEN_SCREEN, WHITE, WHITE, PINK, ORANGE, WHITE, PINK,  ORANGE, WHITE],
            [PINK, WHITE, ORANGE, WHITE, BLUE_E, WHITE, ORANGE, WHITE, PINK, WHITE, MY_DEEP_PURPLE, WHITE, WHITE],
            [ORANGE, PINK, MY_DEEP_PURPLE, PINK, ORANGE, WHITE],
            [PINK, ORANGE, PINK, MY_DEEP_PURPLE, PINK, ORANGE, PINK, MY_DEEP_PURPLE, WHITE],
            [PINK, GREEN_SCREEN, WHITE, ORANGE,WHITE, ORANGE,PINK,MY_DEEP_PURPLE, WHITE,ORANGE,WHITE,WHITE],
        ]

        for i in range(len(loop)):
            loop[i] = self.ColorSetter(loop[i], loop_color[i])
            if i == 0:
                loop[i].next_to(iterative1,DOWN)
            else:
                loop[i].next_to(loop[i-1],DOWN)

        for l in loop:
            l.to_edge(LEFT)
            l.shift(6.5*RIGHT)

        for i in range(len(loop)):
            if i > 0:
                loop[i].shift(RIGHT)
        loop[3].shift(RIGHT)

        self.play(Write(iterative1),run_time=3)
        for l in loop:
            self.play(Write(l),run_time=3)

        self.wait(3)
        self.remove(iterative1)
        for l in loop1:
            self.remove(l)
        for l in loop2:
            self.remove(l)


    def BinaryToDecimal(self):
        self.BTDStatement()
        self.BTDCodeComparison()
        self.IterativeBTD()
        self.RecursiveBTD()
        

    def SODIntro(self):
        header = TextMobject("Sum of Digits of a Number").scale(1.5).set_color(MY_DEEP_PURPLE).to_edge(UP)

        intro = [
            TextMobject("Here is yet another example of transforming loop codes to"),
            TextMobject("recursion codes. You will be given a decimal number. You"),
            TextMobject("will need to find the sum of it's digits. For example,")
        ]

        for i in range(len(intro)):
            intro[i].scale(0.8)
            if i == 0:
                intro[i].next_to(header,DOWN)
            else:
                intro[i].next_to(intro[i-1],DOWN)

        example_num1 = TextMobject("827475021").set_color(MY_CYAN)
        example_sum1 = TextMobject("36").set_color(MY_RED)

        example_num1.next_to(intro[2],DOWN)
        example_num1.shift(DOWN)
        example_sum1.next_to(example_num1,RIGHT)

        example_num2 = TextMobject("101011011").set_color(MY_CYAN)
        example_sum2 = TextMobject("6").set_color(MY_RED)

        example_num2.next_to(example_num1,DOWN)
        example_sum2.next_to(example_sum1,DOWN)

        arrow1 = Arrow(example_num1.get_center(), example_sum1.get_center())
        arrow2 = Arrow(example_num2.get_center(), example_sum2.get_center())

        example_num1.shift(LEFT)
        example_num2.shift(LEFT)

        example_sum1.shift(RIGHT)
        example_sum2.shift(RIGHT)

        arrow1.shift(RIGHT/2)
        arrow2.shift(RIGHT/2)
        self.play(FadeIn(header),run_time=2)

        for i in intro:
            self.play(Write(i),run_time=3)
        self.wait(2)
        self.play(Write(example_num1), run_time=2)
        self.play(ShowCreation(arrow1))
        self.play(Write(example_sum1))
        self.wait(2)
        self.play(Write(example_num2),run_time=2)
        self.play(ShowCreation(arrow2))
        self.play(Write(example_sum2))
        self.wait(3)

        for i in intro:
            self.remove(i)

        self.remove(example_num1)
        self.remove(arrow1)
        self.remove(example_sum1)
        self.remove(example_num2)
        self.remove(arrow2)
        self.remove(example_sum2)

    def SumOfDigits(self):
        self.SODIntro()
        
    def construct(self):
        #self.CourseIntro()                              #0 min 3 sec
        #self.RecursionIntro()                           #0 min 3 sec
        #self.NumberCreature()                           #0 min 7 sec
        #self.RecursiveSquare()                          #1 min 43 sec
        #self.LengthOfString()                           #1 min 4 sec
        #self.LengthOfLinkedList()                       #1 min 6 sec
        #self.SumOfIntegers()                            #0 min 47 sec
        self.TilingProblem()                            #4 min 31 sec
        #self.Permutation()                              #3 min 54 sec
        #self.GridWalkingProblem()                       #1 min 55 sec
        #self.Exponentiation()                           #2 min 37 sec
        #self.BinaryToDecimal()
        #self.SumOfDigits()


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
        

class CameraPosition3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=80 * DEGREES,theta=45*DEGREES)
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.wait()

class graphtheory(Scene):
    def construct(self):
       graph = Graph()
       graphscene = DiscreteGraphScene(graph)
       graphscene.play() 
class VenDiagram(Scene):
    def construct(self):
        A = Circle(stroke_width = 0.5, fill_color = YELLOW, fill_opacity = 0.7,color = WHITE)
        B = Circle(stroke_width = 0.5, fill_color = BLUE, fill_opacity = 0.7, color=WHITE)
        A.move_to(LEFT/2.0)
        B.move_to(RIGHT/2.0)
        self.play(DrawBorderThenFill(A), DrawBorderThenFill(B))
        self.wait(2)

class MatrixScene(Scene):
    def construct(self):
        matrix = Matrix([(1,2),(0,1)])
        natrix = Matrix([(3,1),(1,5)])
        self.add(matrix)
        self.add(TexMobject("+").next_to(matrix))
        self.add(natrix)
        self.wait(2)
class NumberScene(Scene):
    def construct(self):
        Ale=Alex().to_edge(DOWN)
        palabras_ale = TextMobject("Hi. I am Zadid.\\\\Nice to meet you all.")
        self.add(Ale)
        self.play(NumberCreatureSays(
            Ale, palabras_ale, 
            bubble_kwargs = {"height" : 4, "width" : 6},
            target_mode="speaking"
        ))
        self.wait()
        self.play(Blink(Ale))
        self.wait(1)
        self.play(Blink(Ale))
        self.wait(1)
        self.play(Blink(Ale))
        self.wait(1)
        self.play(Blink(Ale))
        self.wait(1)

class NumberCreature(Scene):
    def construct(self):
        creature = SVGMobject("PiCreatures_plain")\
        .scale(2)
        creature[4].set_color(RED)
        self.add(creature)
class PythagoreanProof(Scene):
    CONFIG = {
        "square_scale": 2,
    }
    def construct(self):
        left_square, right_square =  Square(), Square()
        VGroup(left_square,right_square)\
                .scale(self.square_scale)\
                .arrange_submobjects(RIGHT,buff=2)

        # LEFT SQUARE SETTINGS
        dots = [
            left_square.point_from_proportion(i * 1/4 + 1/16) 
            for i in range(4)
        ]
        dots_corners = [
            left_square.point_from_proportion(i * 1/4)
            for i in range(4)
        ]
        triangles = VGroup(*[
            Polygon(
                dots[i],
                dots_corners[i],
                dots[i-1],
                stroke_width=0,
                fill_opacity=0.7
            )
            for i in range(4)
        ])
        # RIGHT SQUARE SETTINGS
        dots2 = [
            right_square.point_from_proportion(i * 1/4 + j * 1/16)
            for i,j in zip(range(4),[1,3,3,1])
        ]
        dots_corners2 = [
            right_square.point_from_proportion(i * 1/4) 
            for i in range(4)
        ]
        middle = np.array([
            dots2[0][0],
            dots2[1][1],
            0
        ])

        all_rectangles = VGroup(*[
            Polygon(
                dots_corners2[i],
                dots2[i],
                middle,
                dots2[i-1],
            )
            for i in range(4)
        ])
        # rectancles: rectangles of the triangles
        rectangles = all_rectangles[0::2]
        # Big and small squares
        squares = all_rectangles[1::2]
        # IMPORTANT
        # use total_points = 3 if you are using the 3/feb release
        # use total_points = 4 if you are using the most recent release
        total_points = 3
        rect_dot = [
            [
                rectangles[i].points[total_points*j]
                for j in range(4)
            ]
            for i in range(2)
        ]
        triangles2 = VGroup(*[
            Polygon(
                rect[i+1],
                rect[i],
                rect[i-1],
                fill_opacity=0.7
            )
            for rect in rect_dot
            for i in [0,2]
        ])
        # FORMULAS
        theorem = TexMobject("c^2","=","a^2","+","b^2",color=BLUE).to_edge(DOWN)
        parts_theorem = VGroup(
            TexMobject("a^2").move_to(left_square),
            TexMobject("b^2").move_to(squares[0]),
            TexMobject("c^2").move_to(squares[1])
        )
        #print(len(triangles2))

        self.play(
            *list(map(
                DrawBorderThenFill,
                [left_square,right_square,triangles.copy()
            ]))
        )
        
        self.play(
            *[
                ApplyMethod(
                    triangles[i].move_to,
                    triangles2[i].get_center()
                )
                for i in range(len(triangles))
            ]
        )

        self.play(
                Rotate(triangles[1],-PI/2),
                Rotate(triangles[2],PI/2),
        )

        self.play(
            ShowCreation(squares),
            Write(parts_theorem)
        )
        '''

        self.play(
            *[
                ReplacementTransform(
                    t_.copy()[:],r_,
                    run_time=4
                )
                for t_,r_ in zip(parts_theorem,[theorem[2],theorem[-1],theorem[0]])
            ],
            Write(theorem[1]),Write(theorem[-2])
        )
'''
        self.wait(3)

class Pythagoras(Scene):
    def construct(self):
        a = np.array((-2, 2, 0))
        b = np.array((2, 2, 0))
        c = np.array((2, -2, 0))
        d = np.array((-2,-2,0))
        
        p = a + 4*RIGHT
        q = b + 4*RIGHT
        r = c + 4*RIGHT
        s = d + 4*RIGHT
        right_square = Polygon(p,q,r,s, stroke_width = 0.5,fill_opacity = 1,fill_color = RED, color = WHITE)
        self.play(FadeInFromDown(right_square))
        self.wait()
        square = Polygon(a,b,c,d,stroke_width = 0.5, fill_opacity = 1, fill_color = BLUE, color = WHITE)
        i = (p + 3.0*q)/4.0
        j = (q + 3.0*r)/4.0
        k = (r + 3.0*s)/4.0
        l = (s + 3.0*p)/4.0
        right_inner_square = Polygon(i,j, k, l,stroke_width = 0.5,fill_opacity=1,fill_color = RED, color = WHITE)
        u = a + 4*LEFT
        v = b + 4*LEFT
        w = c + 4*LEFT
        x = d + 4*LEFT
        left_square = Polygon(u,v,w,x,stroke_width=0.5,fill_opacity = 1,fill_color = GREEN, color = WHITE)
        self.play(FadeInFromDown(left_square))
        self.wait()
        e = (u+3.0*v)/4.0
        f = (v+3.0*w)/4.0
        g = (w+3.0*x)/4.0
        h = (x+3.0*u)/4.0
        inner_square = Polygon(e,f, g, h,stroke_width = 0.5, fill_opacity = 1,fill_color = RED, color = WHITE)
        formula = TexMobject("a^2 = b^2 + c^2")

        self.play(ShowCreation(inner_square))
        self.wait()
        triangle_a = Polygon(u, e, h,stroke_width = 0.5,fill_opacity = 1,fill_color = GREEN, color = WHITE)
        triangle_b = Polygon(v, f, e,stroke_width = 0.5,fill_opacity = 1,fill_color = GREEN, color = WHITE)
        triangle_c = Polygon(w, g, f,stroke_width = 0.5,fill_opacity = 1,fill_color = GREEN, color = WHITE)
        triangle_d = Polygon(x, h, g,stroke_width = 0.5,fill_opacity = 1,fill_color = GREEN, color = WHITE)
        triangle_A = triangle_a.copy()
        triangle_B = triangle_b.copy()
        triangle_C = triangle_c.copy()
        triangle_D = triangle_d.copy()

        t = (3*s+q)/4.0
        m = (3*p+q)/4.0
        n = (3*r+q)/4.0
        z = (3*s+p)/4.0
        y = (3*s+r)/4.0

        text_a = TexMobject("a^2")
        text_b = TexMobject("b^2")
        text_c = TexMobject("c^2")

        self.play(
            ApplyMethod(triangle_A.move_to,triangle_A.get_center()+(q-e)+(f-v)),
            ApplyMethod(triangle_B.move_to,triangle_B.get_center()+(p-e)),
            ApplyMethod(triangle_D.move_to,triangle_D.get_center()+(k-g)+(u-h)),
            ApplyMethod(triangle_C.move_to,triangle_C.get_center()+(r-w)),
            )
        self.wait()
        self.play(
            ApplyMethod(text_a.move_to,(u+w)/2.0),
            ApplyMethod(text_b.move_to,(s+t)/2.0),
            ApplyMethod(text_c.move_to,(q+t)/2.0)
            )
        self.wait()
        final_text = TexMobject("a^2", "+", "b^2", "=", "c^2")
        self.add(final_text.to_edge(DOWN))
        self.wait(2)
        self.play(
        Transform(text_a.copy(),final_text[0]),
        Transform(text_b.copy(),final_text[2]),
        Transform(text_c.copy(),final_text[4]),
        )
        self.wait(2)

class FirstScene(Scene):
    def construct(self):
        text = TextMobject("mama")
        self.add(text)

class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()


class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "This is a text",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()


class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()

# See old_projects folder for many, many more
