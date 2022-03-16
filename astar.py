
from math import sqrt

class Cell:
    def __init__(self, cur, par):
        self.pos = cur
        self.parent = par
        self.g = float('inf')
        self.h = float('inf')
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


# def funcHeuristic(cur, end):
#     return float(sqrt((cur[0] - end[0])**2 + (cur[1]-end[1])**2))

def funcHeuristic_Manhattan(cur, end):
    return float(abs(cur[0] - end[0]) + abs(cur[1]-end[1]))


def astar_route(matrix, bonus, start, end, directions):
    open = [] # khoi tao ban dau path
    closed = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))] # cac dinh da di qua
    path = []

    start_cell = Cell(start, None)
    end_cell = Cell(end, None)
    start_cell.h = 0.0
    start_cell.g = 0.0
    start_cell.f = 0.0
    open.append(start_cell)

    while (len(open) != 0):
        open.sort()
        cur = open.pop(0)
        closed[cur.pos[0]][cur.pos[1]] = True

        if cur == end_cell:
            while cur != start_cell:
                path.append(cur.pos)
                cur = cur.parent
            path.append(start_cell.pos)
            break
            
        
        neighbor = findNeighbor(matrix, closed, cur.pos, directions)

        for neigh in neighbor:
            neigh_cell = Cell(neigh, cur)
            temp_g = cur.g
            for x in bonus:
                if (neigh[0],neigh[1]) == (x[0],x[1]):
                    temp_g = temp_g + x[2] - 1 # tru 1 vi sau do cong 1
                    break
            temp_g += 1
            temp_h = funcHeuristic_Manhattan(neigh, end)
            temp_f = temp_g + temp_h

            if (neigh_cell.f > temp_f):
                neigh_cell.g = temp_g
                neigh_cell.h = temp_h
                neigh_cell.f = temp_f
                neigh_cell.parent = cur
                c = True
                for x in open:
                    if neigh == x.pos:
                        c = False
                if c == True:
                    open.append(neigh_cell)
                

    return path[::-1]


def solveMaze(matrix, bonus_points,start, end, directions):
    route = astar_route(matrix, bonus_points,start, end, directions)

    point = len(route) - 1
    for x in bonus_points:
        if (x[0],x[1]) in route:
            point += x[2]
    if point == -1:
        point = 0
    print('Cost: ', point)
    return route