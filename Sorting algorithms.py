import time
from random import randint
from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, array):
        pass

class SelectionSort(SortingStrategy):
    def sort(self, array):
        arr = array.copy()
        for i in range(len(arr) - 1):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

class InsertionSort(SortingStrategy):
    def sort(self, array):
        arr = array.copy()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

class BubbleSort(SortingStrategy):
    def sort(self, array):
        arr = array.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

class MergeSort(SortingStrategy):
    def sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left = self.sort(array[:mid])
            right = self.sort(array[mid:])
            return self._merge(left, right)
        return array

    def _merge(self, left, right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left or right)
        return result

class QuickSort(SortingStrategy):
    def sort(self, array):
        if len(array) <= 1:
            return array
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy

    def sort(self, array):
        return self.strategy.sort(array)

def choose_strategy():
    strategies = {
        "1": ("Selection Sort", SelectionSort()),
        "2": ("Insertion Sort", InsertionSort()),
        "3": ("Bubble Sort", BubbleSort()),
        "4": ("Merge Sort", MergeSort()),
        "5": ("Quick Sort", QuickSort()),
    }

    print("Выберите алгоритм сортировки:")
    for key, (name, _) in strategies.items():
        print(f"{key}: {name}")

    choice = input("Ваш выбор: ")
    if choice in strategies:
        return strategies[choice]
    else:
        print("Некорректный ввод. Повторите попытку.")
        return choose_strategy()

def choose_input():
    print("Выберите источник данных:")
    print("1: Ввести массив с клавиатуры")
    print("2: Загрузить массив из файла")
    print("3: Случайно сгенерировать массив")

    choice = input("Ваш выбор: ")
    if choice == "1":
        return list(map(int, input("Введите числа через пробел: ").split()))
    elif choice == "2":
        file_name = input("Введите имя файла: ")
        try:
            with open(file_name, "r") as file:
                return list(map(int, file.read().strip().split()))
        except FileNotFoundError:
            print("Файл не найден. Повторите попытку.")
            return choose_input()
    elif choice == "3":
        mass_len = int(input("Введите длину массива: "))
        a, b = map(int, input("Введите диапазон чисел (через пробел): ").split())
        return [randint(min(a, b), max(a, b)) for _ in range(mass_len)]
    else:
        print("Некорректный ввод. Повторите попытку.")
        return choose_input()

if __name__ == "__main__":
    unsorted_array = choose_input()
    strategy_name, strategy = choose_strategy()

    sorter = Sorter(strategy)
    start_time = time.monotonic()
    sorted_array = sorter.sort(unsorted_array)
    end_time = time.monotonic()

    print(f"\nИсходный массив: {unsorted_array}")
    print(f"Отсортированный массив ({strategy_name}): {sorted_array}")
    print(f"Время сортировки: {end_time - start_time:.6f} секунд")
