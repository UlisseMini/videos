"""
I'm treating https://docs.manim.community/en/stable/examples.html as exercises,
Writing my verison then looking at the official one.
"""

from manim import *

# Written on my own, after looking at the example
class BraceAnnotationMine(Scene):
    def construct(self):
        # manim uses 3d coords in the background
        a = np.array([-1,-1, 0])
        b = np.array([1, 1, 0])

        text = MathTex("x_0 - x_1")
        text.move_to(a + 2*UP)

        p1 = Circle(radius=0.1, color=WHITE).move_to(a).set_fill(WHITE, opacity=1.)
        p2 = Circle(radius=0.1, color=WHITE).move_to(b).set_fill(WHITE, opacity=1.)
        line = Line(a, b, color=ORANGE)
        # Brace
        #   direction - The direction the brace faces the mobject
        # ie. we want to rotate the line 90 degrees to make it work.
        d = b-a
        # x + iy -> -y + ix (90 degree rotation)
        brace = Brace(line, direction=[-d[1], d[0], 0])
        # There's also BraceBetweenPoints which does this.

        self.add(line, p1, p2, text, brace)


# Written after reading the example code
class BraceAnnotation(Scene):
    def construct(self):
        d1 = Dot([-1, -1, 0])
        d2 = Dot([1, 1, 0])
        # without get_center it uses the t
        line = Line(d1.get_center(), d2.get_center())
        # see above for why rotate
        brace = Brace(line, direction=line.copy().rotate(PI/2).get_unit_vector())
        # could also hardcode
        # brace = Brace(line, direction=[-1, 1, 0])
        # internally get_tex uses put_at_tip
        text = brace.get_tex("x_0-x_1")
        self.add(line, d1, d2, brace, text)



