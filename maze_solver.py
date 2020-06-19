import pygame
import os
import time
from pygame.locals import *

WHITE = (255, 255, 255)
GREEN = (0, 125, 0)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BOX_WIDTH = 12
WALL = '#'
FINISH = '$'
PATH = '+'
FLAG = 'X'
STARTING_X = 1
STARTING_Y = 0
FPS_CLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def solve_maze(maze, x, y):
    if y < 0 or y > len(maze) - 1 or x < 0 or x > len(maze[y]) - 1: # checks if position is outside of maze
        return False
    elif maze[y][x] == FINISH: # checks if we're at the end of the maze and returns the path
        print('Maze solved.')
        return True  
    elif maze[y][x] != '.': # returns false if position is not a valid path
         return False

    # mark the current position so the program knows we've already tried this way
    maze[y][x] = PATH

    DISPLAYSURF.fill(WHITE)
    draw_maze(maze)
    pygame.display.update()
    pygame.time.delay(500)

    if solve_maze(maze, x + 1, y): return True
    elif solve_maze(maze, x - 1, y): return True
    elif solve_maze(maze, x, y + 1): return True
    elif solve_maze(maze, x, y - 1): return True

    maze[y][x] = FLAG
    return False

def draw_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == WALL:
                draw_box(x, y, BLACK)
            elif maze[y][x] == PATH or maze[y][x] == FINISH:
                draw_box(x, y, GREEN)
            else:
                draw_box(x, y, WHITE)

def draw_box(x, y, color):
    pygame.draw.rect(DISPLAYSURF, color, (x * BOX_WIDTH, y * BOX_WIDTH, BOX_WIDTH, BOX_WIDTH))

def main():
    pygame.init()
    with open('test_maze.txt') as f:
        maze = [[c for c in line.strip('\n')] for line in f.readlines()]
    
    solve_maze(maze, STARTING_X, STARTING_Y) 

if __name__ == "__main__":
    main()    