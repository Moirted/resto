import matplotlib.pyplot as plt
import random
import time


def plot_convex_hull(points, hull):
    x, y = zip(*points)
    plt.scatter(x, y)

    if len(hull) > 0:
        # Добавляем первую вершину для замыкания
        hull.append(hull[0])
        hx, hy = zip(*hull)
        plt.plot(hx, hy, 'r-')
    plt.show()


def convex_hull(points):
    """Вычисляет выпуклую оболочку набора двумерных точек.

    Вход: итерируемая последовательность пар (x, y), представляющих точки.
    Выходные данные: список вершин выпуклого корпуса в порядке против часовой стрелки,
      начиная с вершины с лексикографически наименьшими координатами.
    Реализует монотонный цепной алгоритм Эндрю. Сложность O(n log n).
    """
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    # Двумерное поперечное произведение векторов OA и OB, т.е. z-компонента их трехмерного поперечного произведения.
    # Возвращает положительное значение, если OAB поворачивает против часовой стрелки,
    # отрицательное - если по часовой стрелке, и ноль - если точки коллинеарны.
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Построить нижний корпус
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Построить верхний корпус
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Объединение нижнего и верхнего корпусов дает выпуклый корпус.
    # Последний пункт каждого списка опущен, так как он повторяется в начале другого списка.
    return lower[:-1] + upper[:-1]


assert convex_hull([(i // 10, i % 10) for i in range(100)]) == [(0, 0), (9, 0), (9, 9), (0, 9)]

# Генерация случайных точек
num_points = 100
x_range = (0, 10)
y_range = (0, 15)
points = [(random.uniform(*x_range), random.uniform(*y_range)) for _ in range(num_points)]

hull = convex_hull(points)
plot_convex_hull(points, hull)
plt.show()
