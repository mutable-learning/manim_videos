import networkx as nx
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_weighted_line import WeightedLine


class WeightedGraphs(VoiceoverScene, MovingCameraScene):
    def construct(self):
        self.set_speech_service(GTTSService())
        # self.set_speech_service(
        #     RecorderService(
        #         channels=2,
        #         device_index=7,
        #         transcription_model=None,
        #         trim_buffer_end=500,
        #         trim_buffer_start=500,
        #     ),
        #     create_subcaption=False,
        # )

        with self.voiceover(
            text="Have you ever wanted to create beautiful animated \
                            network graphs in Manim, but needed to show edge weights?\
                            Perhaps you have been looking for a way to create a graph\
                            like this one?"
        ):
            vertices = [1, 2, 3, 4]
            edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
            weights = [5, 3, 6, 11, 1]
            edge_weights = {e[0]: {"weight": e[1]} for e in zip(edges, weights)}
            g = DiGraph(
                vertices,
                edges,
                edge_type=WeightedLine,
                edge_config=edge_weights,
            )

            self.play(FadeIn(g), run_time=2)
            self.wait(2)

        with self.voiceover(text="Maybe you would like to animate your graphs?"):
            self.play(
                g[1].animate.move_to([1, 1, 1]),
                g[2].animate.move_to([-1, 1, 2]),
                g[3].animate.move_to([1, -1, -1]),
                g[4].animate.move_to([-1, -1, 0]),
            )
            self.wait(2)
            self.play(FadeOut(g), run_time=2)

        with self.voiceover(
            text="With this manim plugin you can create beautiful \
                            animated network graphs in Manim simply and easily."
        ):
            G = nx.Graph()
            G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])
            G.add_weighted_edges_from(
                [
                    (1, 7, 2),
                    (1, 8, 3),
                    (2, 3, 4),
                    (2, 4, 5),
                    (2, 5, 6),
                    (2, 8, 1),
                    (3, 4, 5),
                    (6, 1, 0),
                    (6, 2, 11),
                    (6, 3, 15),
                    (7, 2, 3),
                    (7, 4, 9),
                ]
            )
            g2 = Graph(
                G.nodes,
                G.edges,
                layout="circular",
                layout_scale=3,
                labels=True,
                vertex_config={7: {"fill_color": RED}},
                edge_type=WeightedLine,
                edge_config={(u, v): G.get_edge_data(u, v) for u, v in G.edges},
            )
            self.play(FadeIn(g2), run_time=2)
            self.wait(2)
            self.play(FadeOut(g2), run_time=2)

        with self.voiceover(text="Introducing the Weighted Line Manim plugin!"):
            self.play(
                Write(
                    Text(
                        "manim-weighted-line: a plugin for Manim",
                        t2c={"manim-weighted-line": RED},
                    ),
                    run_time=2,
                )
            )
            self.wait(2)
