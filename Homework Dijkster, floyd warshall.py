import unittest


class Sort:

    def dijkstra(self, graph, start):
        n = len(graph)
        dist = [INF] * n
        dist[start] = 0
        used = [False] * n
        min_dist = 0
        min_vertex = start
        while min_dist < INF:
            i = min_vertex
            used[i] = True
            for j, weight in graph[i].items():
                if dist[i] + weight < dist[j]:
                    dist[j] = dist[i] + weight
            min_dist = INF
            for i in range(n):
                if not used[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    min_vertex = i
        return dist

    def floyd_warshall(self, graph):
        n = len(graph)
        distances = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j, weight in graph[i].items():
                distances[i][j] = weight
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distances[i][k] + distances[k][j] < distances[i][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]
        return distances

    def topological_sort(eslf, graph):
        def dfs(vertex):
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)
            topological_order.append(vertex)

        visited = set()
        topological_order = []
        for vertex in graph:
            if vertex not in visited:
                dfs(vertex)
        return topological_order[::-1]


class TestSort(unittest.TestCase):
    def setUp(self):
        self.sort = Sort()

    def test_dijkstra(self):
        self.assertEqual(self.sort.dijkstra(graph, start_vertex), [3, 2, 0, 1])

    def test_floyd_warshall(self):
        self.assertEqual(self.sort.floyd_warshall(graph_2), [[6, 3, 5], [3, 4, 2], [5, 2, 4]])

    def test_topological_sort(self):
        self.assertEqual(self.sort.topological_sort(graph_3), ['A', 'C', 'F', 'B', 'E', 'D', 'G'])


start_vertex = 2
INF = float('inf')
graph = {
    0: {1: 1, 2: 4},
    1: {0: 1, 2: 2, 3: 5},
    2: {0: 4, 1: 2, 3: 1},
    3: {1: 5, 2: 1}
}
graph_2 = {
    0: {1: 3, 2: 6},
    1: {0: 3, 2: 2},
    2: {0: 6, 1: 2}
}
graph_3 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['D', 'F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}
