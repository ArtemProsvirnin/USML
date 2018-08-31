from collections import defaultdict

def Dijkstra(S, inputs, n):
    matrix = [[a if a != 0 else 100 for a in i] for i in inputs]

    valid = [True] * n
    weight = [100] * n
    weight[S] = 0
    for i in range(n):
        min_weight = 101
        ID_min_weight = -1
        for i in range(n):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(n):
            if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
        valid[ID_min_weight] = False
    return weight

minPath = float('inf')

def calcPathLen(path):
    '''Функция суммирует веса пути, который получает первым параметром (straightWay) c
    кратчайшим расстоянием от первой вершины до последней (backWay), вычисленным заранее с помощью алгоритма Дейкстры.
    При необходимости изменяет global minPath'''

    global minPath

    straightWay = sum([inputs[f][t] for f, t in path[1:]])

    # в примере матрица смежности симметрична, что свидетельствует о неориентированности графа
    # отсюда следует что кратчайшее расстояние от A до B, равно от B до A
    backWay = shortestPaths[path[-1][1]]

    lenPath = straightWay + backWay

    if lenPath < minPath:
        minPath = lenPath

def updateMinPath(u, d, fro_m, visited):
    '''Функция рекурсивно обходит граф, сохраняя в list visited переходы в виде tuple: (fro_m, to)'''

    visited.append((fro_m, u))

    #ограничие количества посещенных вершин для предотвращения комбинаторного взрыва, не самое лучшее решение
    if len(visited) <= 1.4 * n:
        if u == d:
            # Достигнyта нужная вершина
            # проверка на то что все вершины графа были посещены
            if len(set([to for fro_m, to in visited])) == n:
                calcPathLen(visited)
        else:
            for i in graph[u]:
                if (u, i) not in visited:
                    updateMinPath(i, d, u, visited)

    visited.remove((fro_m, u))

#запрашиваем ввод количества вершин
n = int(input())

#запрашиваем ввод строк, преобразовываем в матрицу N на N
inputs = [[int(d) for d in input().split()] for _ in range(n)]

#используем алгоритм Дейкстры для вычисления кратчайших путей от первой вершины до всех остальных
shortestPaths = Dijkstra(0, inputs, n)

#создаем и заполняем граф на основе матрицы смежности
graph = defaultdict(list)

#создаем только те связи где вес не равен 0 (по условию задачи)
for i in range(n):
    for j in range(n):
        if inputs[i][j] != 0:
            graph[i].append(j)

#вычисляем кратчайший путь полного обхода от первой вершины до всех остальных
for i in range(1, n):
    updateMinPath(0, i, None, [])

print(minPath)