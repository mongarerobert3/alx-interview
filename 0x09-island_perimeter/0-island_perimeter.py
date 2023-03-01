#!/usr/bin/python3
""" 0-island_perimeter.py"""

def island_perimeter(grid):
    """ island_perimeter function"""
    perimeter = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # count the perimeter of the current cell
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1  # top edge
                if i == len(grid)-1 or grid[i+1][j] == 0:
                    perimeter += 1  # bottom edge
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1  # left edge
                if j == len(grid[0])-1 or grid[i][j+1] == 0:
                    perimeter += 1  # right edge
    
    return perimeter
