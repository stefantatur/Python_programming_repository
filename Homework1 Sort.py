import unittest

class Sort:
    # Сортировка вставками:
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    # Сортировка выбором:
    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    # Сортировка пузырьком:
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

# Test cases to test Sort methods
class TestSort(unittest.TestCase):
    def setUp(self):
        self.sort = Sort()

    def test_insertion(self):
        self.assertEqual(self.sort.insertion_sort([2, 7, 1, 4, 5, 3, 6]), [1, 2, 3, 4, 5, 6, 7])

    def test_selection(self):
        self.assertEqual(self.sort.selection_sort([2, 7, 1, 4, 5, 3, 6]), [1, 2, 3, 4, 5, 6, 7])

    def test_bubble(self):
        self.assertEqual(self.sort.bubble_sort([2, 7, 1, 4, 5, 3, 6]), [1, 2, 3, 4, 5, 6, 7])

if __name__ == "__main__":
    unittest.main()