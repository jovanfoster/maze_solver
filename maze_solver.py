WALL = '#'
FINISH = '$'
width = input('Enter the width: ')
height = input('Enter the height: ')

maze = [['' for x in range(width)] for y in range(height)]

with open('test_maze.txt') as f:
  for i in range(height):
      for j in range(width):
        maze[i][j] = f.read(1).strip('\n')

print(maze)

def solve_maze(maze):
    path = []