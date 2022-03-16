import dfs
import astar
import maze
import sys
import bfs
import greedybfs


def main():
    if len(sys.argv) == 3:
        matrix, bonus_points = maze.readMaze(sys.argv[2])
        print(f'The height of the matrix: {len(matrix)}')
        print(f'The width of the matrix: {len(matrix[0])}')

        start, end = maze.findStartAndEnd(matrix)
        #LEFT, RIGHT, UP, DOWN
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        methor = sys.argv[1]
        if methor == '-astar':
            route = astar.solveMaze(
                matrix, bonus_points, start, end, directions)
        elif methor == '-dfs':
            route = dfs.solveMaze(matrix, bonus_points, start, end, directions)
        elif methor == '-bfs':
            route = bfs.solveMaze(matrix, bonus_points, start, end, directions)
        elif methor == '-greedybfs':
            route = greedybfs.solveMaze(
                matrix, bonus_points, start, end, directions)

        if len(route) == 0 or route == None:
            print("Can't solve")
        elif len(route) == 1:
            print('You have already reached the end point')
            route.append(start)  # to fix bug visualize star == end

        maze.visualize_maze(matrix, bonus_points, start, end, route)
    else:
        print("Error: Input")


main()
