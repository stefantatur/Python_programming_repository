import heapq
import unittest


class Graph():
    def prim(self, graph):
        visited = set()
        dist = []
        start = list(graph.keys())[0]
        visited.add(start)
        edges = [(weight, start, neighbor) for neighbor, weight in graph[start]]
        heapq.heapify(edges)
        while edges:
            weight, current, next = heapq.heappop(edges)
            if next not in visited:
                visited.add(next)
                dist.append((current, next, weight))
                for neighbor, weight in graph[next]:
                    if neighbor not in visited:
                        heapq.heappush(edges, (weight, next, neighbor))
        return dist


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.sort = Graph()

    def test_prim(self):
        expected_output = [('1', '4', 2), ('4', '3', 1), ('4', '2', 2), ('3', '6', 3), ('4', '7', 5), ('7', '5', 6)]
        actual_output = self.sort.prim(graph)
        self.assertEqual(actual_output, expected_output)

graph = {
    '1': [('2', 3), ('3', 4), ('4', 2), ('6', 5)],
    '2': [('1', 3), ('4', 1), ('5', 7)],
    '3': [('1', 4), ('4', 5), ('6', 3)],
    '4': [('1', 2), ('2', 2), ('3', 1), ('7', 5)],
    '5': [('2', 3), ('7', 5)],
    '6': [('1', 4), ('3', 3), ('7', 7)],
    '7': [('4', 5), ('5', 6), ('6', 7)],
}

if __name__ == "__main__":
    unittest.main()