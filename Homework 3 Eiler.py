import unittest
from collections import defaultdict

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.result = []

    def find_euler_path(self, start_vertex):
        self.result = []
        self._dfs(start_vertex)
        return self.result

    def _dfs(self, current_vertex):
        while self.graph[current_vertex]:
            neighbor = self.graph[current_vertex].pop()
            self.graph[neighbor].remove(current_vertex)
            self._dfs(neighbor)
        self.result.append(current_vertex)

    def fleury(self, start_vertex):
        visited_edges = defaultdict(list)
        eulerian_path = []
        current_vertex = start_vertex
        while graph[current_vertex]:
            for neighbor in graph[current_vertex]:
                if len(graph[current_vertex]) != 0 or len(graph[neighbor]) != 0:
                    edge = (current_vertex, neighbor)
                    graph[current_vertex].remove(neighbor)
                    graph[neighbor].remove(current_vertex)
                    visited_edges[current_vertex].append(neighbor)
                    visited_edges[neighbor].append(current_vertex)
                    eulerian_path.append(edge)
                    current_vertex = neighbor
                    break
        return eulerian_path

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.sort = Graph(graph)
        
    def test_fleury(self):
        self.assertEqual(self.sort.fleury(start_vertex), [0, 4, 2, 5, 3, 2, 0, 3, 1, 0])
    def test_EulerPath(self):
        self.assertEqual(self.sort.find_euler_path(start_vertex),
                         [0, 1, 1, 0, 1, 0, 0])


graph = {
    0: [0, 1, 1, 1, 1, 0],
    1: [1, 0, 0, 1, 0, 0],
    2: [1, 0, 0, 1, 1, 1],
    3: [1, 1, 1, 0, 0, 1],
    4: [1, 0, 1, 0, 0, 0],
    5: [0, 0, 1, 1, 0, 0]
}

start_vertex = 0

if __name__ == "__main__":
    unittest.main()