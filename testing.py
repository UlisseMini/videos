from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.next_to(circle, UP, buff=0.5)

        self.play(Create(circle) ,Create(square))


class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))

        self.play(ReplacementTransform(square, circle))
        self.play(circle.animate.set_fill(PINK, opacity=0.5))


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE).shift(2*LEFT)
        right_square = Square(color=GREEN).shift(2*RIGHT)

        # subtle difference: .animate will interpolate between the start and
        # end states, while Rotate will animate intelligently.
        self.play(
            left_square.animate.rotate(PI),
            Rotate(right_square, angle=PI),
        )
        self.wait()


class HelloText(Scene):
    def construct(self):
        # Text       - Compile pure text with pango
        # Tex        - Compile latex in normal mode (no intro animation)
        # MathTex    - Compile latex in math mode
        # MarkupText - Compile text as pango markup, see docs
        text = MarkupText(f'<b>Hello</b> <tt>World</tt><span fgcolor="{RED}">!</span>')
        quadratic = MathTex(r"\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
        # quadratic.next_to(text, DOWN)

        g = VGroup(text, quadratic).arrange(DOWN)
        self.play(Create(g))
        self.wait()
