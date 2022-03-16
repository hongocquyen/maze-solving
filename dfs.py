
def findNeighbor(matrix, visited, cur, directions):
    neighbor = []

    for dir in directions:
        nextR = cur[0] + dir[0]
        nextC = cur[1] + dir[1]
        if matrix[nextR][nextC] != 'x' and visited[nextR][nextC] == False:
            neighbor.append((nextR, nextC))
    
    return neighbor


def dfs_route(matrix, bonus_points, start, end, directions):
    route = [start] # khoi tao ban dau path
    visited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))] # cac dinh da di qua
    visited[start[0]][start[1]] = True

    while (len(route) != 0 and route[-1] != end):
        cur = route[-1]
        neighbor = findNeighbor(matrix, visited, cur, directions)
        if len(neighbor) == 0 :
            route.pop()
        else:
            s = neighbor[-1]
            neighbor.pop()
            route.append(s)
            visited[s[0]][s[1]] = True
            

            
    if len(route) == 0:
        print('Failure')
        return
    else:
        return route
        

def solveMaze(matrix, bonus_points,start, end, directions):
    route = dfs_route(matrix, bonus_points,start, end, directions)

    point = len(route) - 1
    for x in bonus_points:
        if (x[0],x[1]) in route:
            point += x[2]
    print('Cost: ', point)
    return route