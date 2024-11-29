from manim import *

class TwoModeSqueezing(Scene):
    def construct(self):
        # Title
        title = Text("Two-Mode Squeezing Animation", font_size=36)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Axes
        axes = Axes(
            x_range=[-4, 4, 1], y_range=[-4, 4, 1],
            x_length=8, y_length=8,
            axis_config={"color": WHITE},
        ).add_coordinates()
        labels = axes.get_axis_labels(x_label="X", y_label="P")

        self.play(Create(axes), Write(labels))

        # Initial Coherent State (circle in phase space)
        coherent_circle = Circle(radius=1, color=YELLOW).move_to(axes.c2p(0, 0))
        self.play(Create(coherent_circle))
        self.wait(1)

        # Squeezing Transformation (Ellipse)
        squeezed_ellipse = Ellipse(width=0.5, height=3, color=BLUE).move_to(axes.c2p(0, 0))
        self.play(Transform(coherent_circle, squeezed_ellipse))
        self.wait(1)

        # Below Vacuum (Enhance squeezing effect)
        below_vacuum = Ellipse(width=0.3, height=4, color=RED).move_to(axes.c2p(0, 0))
        self.play(Transform(squeezed_ellipse, below_vacuum))
        self.wait(1)

        # Add Annotations
        coherent_label = Text("Coherent State", font_size=24).next_to(coherent_circle, UP)
        squeezed_label = Text("Squeezed State", font_size=24).next_to(squeezed_ellipse, UP)
        below_vacuum_label = Text("Below Vacuum", font_size=24).next_to(below_vacuum, UP)

        self.play(Write(coherent_label))
        self.wait(1)
        self.play(Transform(coherent_label, squeezed_label))
        self.wait(1)
        self.play(Transform(coherent_label, below_vacuum_label))
        self.wait(2)

        # Fade out all
        self.play(FadeOut(axes), FadeOut(labels), FadeOut(coherent_label), FadeOut(below_vacuum))

