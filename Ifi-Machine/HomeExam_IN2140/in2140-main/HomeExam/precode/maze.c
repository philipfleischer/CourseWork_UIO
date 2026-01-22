#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "maze.h"

// Greedy depth-first search
int dfs(int* visit_grid, struct Maze* maze, int X, int Y) {
    // Basecase check
    if (visit_grid[Y * maze->edgeLen + X]) return 0;
    if (X == maze->endX && Y == maze->endY) return 1;

    visit_grid[Y * maze->edgeLen + X] = 1;

    // Recursion
    int solved = 0;
    char val = maze->maze[Y * maze->edgeLen + X];
    if (val & left && !solved) solved = dfs(visit_grid, maze, X - 1, Y);
    if (val & right && !solved) solved = dfs(visit_grid, maze, X + 1, Y);
    if (val & up && !solved) solved = dfs(visit_grid, maze, X, Y - 1);
    if (val & down && !solved) solved = dfs(visit_grid, maze, X, Y + 1);

    if (solved) maze->maze[Y * maze->edgeLen + X] = maze->maze[Y * maze->edgeLen + X] | mark;
    return solved;
}

void mazeSolve( struct Maze* maze ){
    int* visit_grid = calloc(sizeof(int), maze->size);
    int solve = dfs(visit_grid, maze, maze->startX, maze->startY);
    if (!solve) {
        fprintf(stderr, "Failed to complete maze\n");
    }
    free(visit_grid);
}
