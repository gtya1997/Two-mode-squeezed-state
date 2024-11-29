from manim import *

class QuantumSqueezing45Degree(Scene):
    def construct(self):
        # Title
        title = Text("Quantum Noise Squeezing at 45°", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Create Axes
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            x_length=6, y_length=6,
            axis_config={"color": WHITE},
        ).add_coordinates()
        labels = axes.get_axis_labels(x_label="q", y_label="p")
        self.play(Create(axes), Write(labels))

        # Initial Circular Distributions
        vacuum_noise = Circle(radius=0.8, color=BLUE, stroke_width=3).move_to(axes.c2p(0, 0))
        quantum_noise = Circle(radius=1.5, color=RED, stroke_width=3).move_to(axes.c2p(0, 0))
        vacuum_label = Text("Vacuum Noise", font_size=18, color=BLUE).next_to(vacuum_noise, DOWN)
        quantum_label = Text("Quantum Noise", font_size=18, color=RED).next_to(quantum_noise, UP)

        self.play(Create(vacuum_noise), Write(vacuum_label))
        self.play(Create(quantum_noise), Write(quantum_label))
        self.wait(1)

        # Transition to Squeezed Ellipse (Rotated at 45°)
        squeezed_ellipse = Ellipse(
            width=2.5, height=0.8, 
            color=RED, 
            stroke_width=3, 
            fill_opacity=0.2
        ).rotate(PI/4).move_to(axes.c2p(0, 0))

        self.play(Transform(quantum_noise, squeezed_ellipse))
        self.wait(1)

        # Add Dashed Blue Circle for Vacuum Noise
        dashed_vacuum_noise = DashedVMobject(
            vacuum_noise, num_dashes=50, color=BLUE, stroke_width=2
        )
        self.play(Transform(vacuum_noise, dashed_vacuum_noise))
        self.wait(1)

        # Quadrature Axes for Squeezed State
        squeezed_axis = DashedLine(
            start=axes.c2p(-2, -2), end=axes.c2p(2, 2), color=WHITE, stroke_width=2
        )
        anti_squeezed_axis = DashedLine(
            start=axes.c2p(-2, 2), end=axes.c2p(2, -2), color=WHITE, stroke_width=2
        )
        self.play(Create(squeezed_axis), Create(anti_squeezed_axis))

        # Add Labels for Squeezed and Anti-Squeezed Directions
        squeezed_label = Text("Squeezed", font_size=18, color=YELLOW).next_to(squeezed_axis, UR, buff=0.2)
        anti_squeezed_label = Text("Anti-Squeezed", font_size=18, color=YELLOW).next_to(anti_squeezed_axis, UL, buff=0.2)
        self.play(Write(squeezed_label), Write(anti_squeezed_label))
        self.wait(2)

        # Fade Out to End Scene
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(labels),
            FadeOut(squeezed_axis),
            FadeOut(anti_squeezed_axis),
            FadeOut(squeezed_label),
            FadeOut(anti_squeezed_label),
            FadeOut(vacuum_noise),
            FadeOut(quantum_noise),
        )
