from collections import deque
from math import sqrt
from os import path


class Cell:
    def __init__(self, cur, par):
        self.pos = cur
        self.parent = par
        self.f = float('inf')

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.pos == other.pos


def findNeighbor(matrix, visited, cur, directions):
    neighbor = []

    for dir in directions:
        nextR = cur[0] + dir[0]
        nextC = cur[1] + dir[1]
        if matrix[nextR][nextC] != 'x' and visited[nextR][nextC] == False:
            neighbor.append((nextR, nextC))

    return neighbor


def funcHeuristic(cur, end):
    return float(sqrt((cur[0] - end[0])**2 + (cur[1]-end[1])**2))  # Distance


def gbfs_route(matrix, bonus_points, start, end, directions):

    R, C = len(matrix), len(matrix[0])

    open = []  # Khoi tao OPEN list
    visited = [[False]*C for _ in range(R)]

    start_cell = Cell(start, None)
    end_cell = Cell(end, None)

    open.append(start_cell)
    path = []
    while(len(open) != 0):
        open.sort()
        cur = open.pop(0)
        visited[cur.pos[0]][cur.pos[1]] = True
        if cur == end_cell:
            while cur != start_cell:
                path.append(cur.pos)
                cur = cur.parent
            path.append(start_cell.pos)
            return path[::-1]

        neight = findNeighbor(matrix, visited, cur.pos, directions)

        for n in neight:
            neight_cell = Cell(n, cur)
            temp_f = funcHeuristic(neight_cell.pos, end)

            if neight_cell.f > temp_f:
                neight_cell.f = temp_f

            if neight_cell not in open and visited[n[0]][n[1]] == False:
                open.append(neight_cell)

    return None


def solveMaze(matrix, bonus_points, start, end, directions):
    route = gbfs_route(matrix, bonus_points, start, end, directions)

    if route != None:
        point = len(route) - 1
        for x in bonus_points:
            if (x[0], x[1]) in route:
                point += x[2]
    else:
        point = 0
    print('Cost: ', point)
    return route
