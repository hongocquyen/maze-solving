
def findNeighbor(matrix, visited, cur, directions):
    neighbor = []

    for dir in directions:
        nextR = cur[0] + dir[0]
        nextC = cur[1] + dir[1]
        if matrix[nextR][nextC] != 'x' and visited[nextR][nextC] == False:
            neighbor.append((nextR, nextC))

    return neighbor


def bfs_route(matrix, bonus_points, start, end, directions):
    R, C = len(matrix), len(matrix[0])

    queue = []

    queue.append(start)
    # Set all square is not visitied
    visited = [[False]*C for _ in range(R)]
    visited[start[0]][start[1]] = True
    while len(queue) != 0:
        # Create list path
        if queue[0] == start:
            path = [queue.pop(0)]
        else:
            path = queue.pop(0)
        cur = path[-1]

        if cur == end:
            return path

        for s in findNeighbor(
                matrix, visited, cur, directions):
            newpath = list(path)
            newpath.append(s)
            queue.append(newpath)  # Add list path to queue
            visited[s[0]][s[1]] = True
        
    return None


def solveMaze(matrix, bonus_points, start, end, directions):
    route = bfs_route(matrix, bonus_points, start, end, directions)

    if route != None:
        point = len(route) - 1
        for x in bonus_points:
            if (x[0], x[1]) in route:
                point += x[2]
    else:
        point = 0
    print('Cost: ', point)
    return route
