from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_weighted_line import WeightedLine


class WeightedGraphs(VoiceoverScene, MovingCameraScene):
    def construct(self):
        self.set_speech_service(GTTSService(transcription_model=None), create_subcaption=False)
        # # self.set_speech_service(
        # #     RecorderService(
        # #         channels=2,
        # #         device_index=7,
        # #         transcription_model=None,
        # #         trim_buffer_end=500,
        # #         trim_buffer_start=500,
        # #     ),
        # #     create_subcaption=False,
        # # )

        # with self.voiceover(
        #     text="Have you ever wanted to create beautiful animated \
        #                     network graphs in Manim, but needed to show edge weights?\
        #                     Perhaps you have been looking for a way to create a graph\
        #                     like this one?"
        # ):
        #     vertices = [1, 2, 3, 4]
        #     edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        #     weights = [5, 3, 6, 11, 1]
        #     edge_weights = {e[0]: {"weight": e[1]} for e in zip(edges, weights)}
        #     g = DiGraph(
        #         vertices,
        #         edges,
        #         edge_type=WeightedLine,
        #         edge_config=edge_weights,
        #     )

        #     self.play(FadeIn(g), run_time=2)
        #     self.wait(2)

        # with self.voiceover(
        #     text="Maybe you would like to animate your weighted graphs with manim for \
        #                     your own videos or your youtube channel?"
        # ):
        #     self.play(
        #         g[1].animate.move_to([1, 1, 1]),
        #         g[2].animate.move_to([-1, 1, 2]),
        #         g[3].animate.move_to([1, -1, -1]),
        #         g[4].animate.move_to([-1, -1, 0]),
        #     )
        #     self.wait(2)
        #     self.play(FadeOut(g), run_time=2)

        # with self.voiceover(
        #     text="With this manim plugin you can create beautiful \
        #                     animated network graphs simply and easily."
        # ):
        #     G = nx.Graph()
        #     G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])
        #     G.add_weighted_edges_from(
        #         [
        #             (1, 7, 2),
        #             (1, 8, 3),
        #             (2, 3, 4),
        #             (2, 4, 5),
        #             (2, 5, 6),
        #             (2, 8, 1),
        #             (3, 4, 5),
        #             (6, 1, 0),
        #             (6, 2, 11),
        #             (6, 3, 15),
        #             (7, 2, 3),
        #             (7, 4, 9),
        #         ]
        #     )
        #     g2 = Graph(
        #         G.nodes,
        #         G.edges,
        #         layout="circular",
        #         layout_scale=3,
        #         labels=True,
        #         vertex_config={7: {"fill_color": RED}},
        #         edge_type=WeightedLine,
        #         edge_config={(u, v): G.get_edge_data(u, v) for u, v in G.edges},
        #     )
        #     self.play(FadeIn(g2), run_time=2)
        #     self.wait(2)
        #     self.play(FadeOut(g2), run_time=2)

        # with self.voiceover(text="Introducing the Weighted Line plugin for Manim!"):
        #     intro = Text(
        #         "manim-weighted-line: a plugin for Manim",
        #         t2c={"manim-weighted-line": RED},
        #     )
        #     self.play(Write(intro, run_time=2))
        #     self.wait(2)
        #     self.play(FadeOut(intro))

        with self.voiceover(
            "Here is a simple graph from the manim documentation examples"
        ):
            vertices = [1, 2, 3, 4]
            edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
            g3 = Graph(vertices, edges)
            self.play(Create(g3, run_time=2))
            self.wait(2)

        with self.voiceover(
            "With a few additions to the code we can go from this \
                            unweighted graph to a weighted graph."
        ):
            self.play(g3.animate.shift(LEFT * 2), run_time=2)
            vertices = [1, 2, 3, 4]
            edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
            g4 = Graph(
                vertices,
                edges,
                edge_type=WeightedLine,
                edge_config={
                    "weight": 5,
                },
            )
            g4.next_to(g3, RIGHT)
            self.play(Create(g4, run_time=2))

            self.wait(2)

        with self.voiceover(
            text="Weighted graphs can be animated and share all the same \
                            properties and features of manim graphs you already know and \
                            appreciate."
        ):
            self.play(FadeOut(g3))
            self.play(g4.animate.shift(LEFT))
            self.play(
                g4[1].animate.move_to([1, 1, 0]),
                g4[2].animate.move_to([-1, 1, 0]),
                g4[3].animate.move_to([1, -1, 0]),
                g4[4].animate.move_to([-1, -1, 0]),
                run_time=2,
            )
            self.wait(2)
            self.play(FadeOut(g4))

        with self.voiceover(
            text="So what do we need to do to start using this plugin?\
                <bookmark mark='A'/> Simply install it from pip and then you will be \
                ready to start animating!"
        ):
            install = Text("pip install manim-weighted-line")
            self.wait_until_bookmark("A")
            self.play(Write(install, run_time=2))
            self.play(FadeOut(install))

        with self.voiceover(
            text="To start using the plugin, add an import line to your file. \
                <bookmark mark='A'/> The code for the original graph looks like this.\
                <bookmark mark='B'/> To show the weights of the edges you can make \
                the following changes \
                to change the edge_type to WeightedLine and the edge_config to \
                include the weight."
        ):
            import_line = Code(
                code="from manim_weighted_line import WeightedLine",
                language="python",
                insert_line_no=False,
            )
            self.play(Write(import_line, run_time=2))
            # self.play(import_line.animate.shift(LEFT * 3, UP * 3), run_time=2)
            code1 = Code(
                code="""vertices = [1, 2, 3, 4]
            edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
            g = Graph(vertices, edges)""",
                language="python",
                insert_line_no=False,
            )
            self.wait_until_bookmark("A")
            code1.next_to(import_line, DOWN)
            self.play(Write(code1, run_time=2))

            code2 = Code(
                code="""vertices = [1, 2, 3, 4]
            edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
            g4 = Graph(
                vertices,
                edges,
                edge_type=WeightedLine,
                edge_config={
                    "weight": 5,
                },
            )""",
                language="python",
                insert_line_no=False,
            )
            self.wait_until_bookmark("B")
            self.play(Transform(code1, code2), run_time=2)
            self.wait(2)
