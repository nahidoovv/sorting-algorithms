# Алгоритмы сортировки


## Описание задачи
Реализовать различные алгоритмы сортировки (пузырьковая, быстрая, сортировка слиянием) с возможностью их сравнения. Реализовать динамический выбор сравниваемых алгоритмов сортировки. Реализовать динамический выбор источника входных данных (файл, вариант по умолчанию или с клавиатуры).
Программа должна:
1. Поддерживать несколько алгоритмов сортировки (пузырьковая, быстрая, сортировка слиянием и другие).
2. Предоставлять возможность выбора алгоритма сортировки пользователем.
3. Позволять выбирать источник входных данных: файл, ввод с клавиатуры или генерация случайного массива.
4. Сравнивать алгоритмы по времени выполнения.

## Используемые технологии
•  Язык программирования: Python  
•  Паттерн проектирования: "Стратегия"  

## Паттерн "Стратегия"
Паттерн "Стратегия" используется для того, чтобы менять алгоритмы сортировки во время выполнения программы. 

### Основные элементы:
1. Контекст (Sorter): использует выбранную стратегию для выполнения сортировки.
2. Интерфейс стратегии (SortingStrategy): определяет общий интерфейс для всех алгоритмов сортировки.
3. Конкретные стратегии (SelectionSort, InsertionSort, и др.): реализуют разные алгоритмы сортировки.

### Преимущества:
•  Упрощение добавления новых алгоритмов сортировки.  
•  Изоляция логики сортировки от остального кода.  
•  Удобство изменения алгоритма в процессе выполнения программы.  


