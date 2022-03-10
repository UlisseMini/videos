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



# Written on my own, after looking at the example
class BooleanOperations(Scene):
    def construct(self):
        text = MarkupText("<u>Boolean Operations</u>")
        text.shift(UP*3 + LEFT*3)

        s1 = Ellipse(3, 4.5, color=BLUE, fill_opacity=0.6).shift(LEFT*3)
        s2 = Ellipse(3, 4.5, color=RED, fill_opacity=0.6).shift(LEFT*2)
        self.add(text, s1, s2)
        self.pause(0.5)

        ops = [
            # I could deduplicate but that would cost flexibility.
            Intersection(s1, s2, color=GREEN, fill_opacity=0.6),
            Union(s1, s2, color=ORANGE, fill_opacity=0.6),
            Exclusion(s1, s2, color=YELLOW, fill_opacity=0.6),
            Difference(s1, s2, color=PINK, fill_opacity=0.6)
        ]
        TR = UP*2.8 + RIGHT*5
        for i, op in enumerate(ops):
            self.play(Create(op))
            self.pause(0.1)
            self.play(op.animate.scale(0.2).move_to(TR + 2*DOWN*i))

            text = Text(op.__class__.__name__, font_size=30)
            text.next_to(op, UP)
            self.play(FadeIn(text))


        self.wait()

