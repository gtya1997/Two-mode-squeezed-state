from manim import *

class QuantumSqueezingSideBySide(Scene):
    def construct(self):
        # Title
        title = Text("Quantum Noise Squeezing Comparison", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Create Axes for Both Plots
        left_axes = Axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            x_length=5, y_length=5,
            axis_config={"color": WHITE},
        ).add_coordinates().shift(LEFT * 3)

        right_axes = Axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            x_length=5, y_length=5,
            axis_config={"color": WHITE},
        ).add_coordinates().shift(RIGHT * 3)

        # Labels for Axes
        left_labels = left_axes.get_axis_labels(x_label="q", y_label="p")
        right_labels = right_axes.get_axis_labels(x_label="q", y_label="p")

        self.play(Create(left_axes), Create(right_axes))
        self.play(Write(left_labels), Write(right_labels))

        # Initial Circles for Both Plots
        left_vacuum = Circle(radius=0.8, color=BLUE, stroke_width=3).move_to(left_axes.c2p(0, 0))
        right_vacuum = Circle(radius=0.8, color=BLUE, stroke_width=3).move_to(right_axes.c2p(0, 0))

        left_quantum = Circle(radius=1.5, color=RED, stroke_width=3).move_to(left_axes.c2p(0, 0))
        right_quantum = Circle(radius=1.5, color=RED, stroke_width=3).move_to(right_axes.c2p(0, 0))

        self.play(Create(left_vacuum), Create(right_vacuum))
        self.wait(0.5)
        self.play(Create(left_quantum), Create(right_quantum))
        self.wait(1)

        # Add Labels for Left Plot
        left_vacuum_label = Text("Vacuum Noise", font_size=18, color=BLUE).next_to(left_vacuum, DOWN)
        left_quantum_label = Text("Quantum Noise", font_size=18, color=RED).next_to(left_quantum, UP)

        self.play(Write(left_vacuum_label), Write(left_quantum_label))
        self.wait(1)

        # Transition Right Plot into Squeezed Ellipse
        squeezed_ellipse = Ellipse(
            width=2.5, height=0.8,
            color=RED, stroke_width=3,
            fill_opacity=0.2,
        ).rotate(PI/4).move_to(right_axes.c2p(0, 0))

        self.play(Transform(right_quantum, squeezed_ellipse))
        self.wait(1)

        # Add Quadrature Lines and Labels to Right Plot
        squeezed_axis = DashedLine(
            start=right_axes.c2p(-2, -2), end=right_axes.c2p(2, 2), color=WHITE, stroke_width=2
        )
        anti_squeezed_axis = DashedLine(
            start=right_axes.c2p(-2, 2), end=right_axes.c2p(2, -2), color=WHITE, stroke_width=2
        )

        squeezed_label = Text("Squeezed", font_size=18, color=YELLOW).next_to(squeezed_axis, UR, buff=0.2)
        anti_squeezed_label = Text("Anti-Squeezed", font_size=18, color=YELLOW).next_to(anti_squeezed_axis, UL, buff=0.2)

        self.play(Create(squeezed_axis), Create(anti_squeezed_axis))
        self.play(Write(squeezed_label), Write(anti_squeezed_label))
        self.wait(2)

        # Fade Out to End Scene
        self.play(
            FadeOut(title),
            FadeOut(left_axes), FadeOut(right_axes),
            FadeOut(left_labels), FadeOut(right_labels),
            FadeOut(left_vacuum), FadeOut(right_vacuum),
            FadeOut(left_quantum), FadeOut(right_quantum),
            FadeOut(left_vacuum_label), FadeOut(left_quantum_label),
            FadeOut(squeezed_axis), FadeOut(anti_squeezed_axis),
            FadeOut(squeezed_label), FadeOut(anti_squeezed_label),
        )
