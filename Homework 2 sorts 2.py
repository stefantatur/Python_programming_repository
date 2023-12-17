import unittest

# Сортировка слиянием
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Пирамидальная сортировка
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

# BFS
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')
        for neighbor in graph[vertex] - visited:
            visited.add(neighbor)
            queue.append(neighbor)
    return visited

class TestAlgorithms(unittest.TestCase):
    def test_merge_sort(self):
        arr = [12, 11, 13, 5, 6, 7]
        merge_sort(arr)
        self.assertEqual(arr, [5, 6, 7, 11, 12, 13])

    def test_quick_sort(self):
        arr = [12, 11, 13, 5, 6, 7]
        arr = quick_sort(arr)
        self.assertEqual(arr, [5, 6, 7, 11, 12, 13])

    def test_heap_sort(self):
        arr = [12, 11, 13, 5, 6, 7]
        heap_sort(arr)
        self.assertEqual(arr, [5, 6, 7, 11, 12, 13])

    def test_dfs(self):
        graph = {
            'A': {'B', 'C'},
            'B': {'A', 'D', 'E'},
            'C': {'A', 'F'},
            'D': {'B'},
            'E': {'B', 'F'},
            'F': {'C', 'E'}
        }
        result = dfs(graph, 'A')
        self.assertEqual(result, {'A', 'B', 'C', 'D', 'E', 'F'})

    def test_bfs(self):
        graph = {
            'A': {'B', 'C'},
            'B': {'A', 'D', 'E'},
            'C': {'A', 'F'},
            'D': {'B'},
            'E': {'B', 'F'},
            'F': {'C', 'E'}
        }
        result = bfs(graph, 'A')
        self.assertEqual(result, {'A', 'B', 'C', 'D', 'E', 'F'})

if __name__ == '__main__':
    unittest.main()
