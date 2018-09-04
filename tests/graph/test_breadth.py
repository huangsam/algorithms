from collection.graph import Graph
from graph.breadth import bfs


class TestBFS(object):

    def test_bfs(self):
        graph = Graph(
            ('a', 'b'),
            ('a', 'c'),
            ('b', 'd'),
            ('c', 'e')
        )
        order = bfs(graph, 'a')
        assert len(order) == len(graph.get_nodes())
        assert 'a,b,c,d,e' == ','.join(order)
