#include "maze.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define SIZE 1024

struct node {
    struct node* parent;
    int idx;

    // Keeping track of the nodes to easier free them later, sort of like a linked list
    struct node* next;
};

struct queue {
    struct node* elements[SIZE];
    int head;
    int tail;
};

struct queue*
create_queue() {
    struct queue* q = malloc(sizeof(struct queue));
    // -1, -1 indicates that the queue is empty
    q->head = -1;
    q->tail = -1;
    return q;
};

struct node* head;
struct node* create_node(struct node* parent, int idx) {
    struct node* n = malloc(sizeof(struct node));
    n->idx = idx;
    n->parent = parent;
    n->next = head->next;
    head->next = n;
    return n;
}

struct node* pop(struct queue* q);
void add(struct queue* q, struct node* idx);

// Copies all elements from old q to the new q
void reset_queue(struct queue* q) {
    struct queue* newq = create_queue();
    for (int i = q->head; i < q->tail; i++) {
        add(newq, pop(q));
    }
    memcpy(q, newq, sizeof(struct queue));
    q = newq;
    free(newq);
}

void add(struct queue* q, struct node* idx) {
    // if the queue is full reset it
    if (q->tail == SIZE - 1) {
        reset_queue(q);
    }

    if (q->head == -1) q->head = 0;

    q->tail++;
    q->elements[q->tail] = idx;
}

struct node* pop(struct queue* q) {
    if (q->tail == -1) return NULL;

    struct node* idx = q->elements[q->head];
    q->head++;
    // if all elements of the queue has been popped off, reset the queue
    if (q->head > q->tail) {
        q->head = -1;
        q->tail = -1;
    }
    return idx;
}

int pos_to_idx(int X, int Y, int edgelen) {
    return Y * edgelen + X;
}

// Recursivly marks the maze
void mark_maze(Maze* maze, struct node* n) {
    if (n->parent == NULL) return;
    maze->maze[n->idx] |= mark;
    mark_maze(maze, n->parent);
}

void free_nodes(struct node* cur) {
    if (cur->next) free_nodes(cur->next);
    free(cur);
    return;
}
// Classic bfs
int bfs(Maze* maze) {
    int solved = 0;
    struct queue* q = create_queue();
    int* visit_grid = calloc(sizeof(int), maze->size);
    struct node* start = create_node(NULL, pos_to_idx(maze->startX, maze->startY, maze->edgeLen));
    add(q, start);

    while (q->tail != -1) {
        struct node* cur_idx = pop(q);

        if (cur_idx->idx == pos_to_idx(maze->endX, maze->endY, maze->edgeLen)) {
            mark_maze(maze, cur_idx);
            solved = 1;
            break;
        }
        if (visit_grid[cur_idx->idx]) continue;
        visit_grid[cur_idx->idx] = 1;
        int val = maze->maze[cur_idx->idx];
        if (val & right) add(q, create_node(cur_idx, cur_idx->idx + 1));
        if (val & left) add(q, create_node(cur_idx, cur_idx->idx - 1));
        if (val & down) add(q, create_node(cur_idx, cur_idx->idx + maze->edgeLen));
        if (val & up) add(q, create_node(cur_idx, cur_idx->idx - maze->edgeLen));
    }
    free(q);
    free(visit_grid);
    free_nodes(head);
    return solved;
}

void mazeSolve(Maze* maze) {
    head = malloc(sizeof(struct node));
    head->idx = -1;
    head->parent = NULL;
    head->next = NULL;

    int solved = bfs(maze);
    if(!solved){
        fprintf(stderr, "L5: Did not find a solution!\n");
    }
}