// BFS

#include <stdio.h>

int visited[9] = {1};
int graph[9][3] = {{}, {2,3,8}, {1,7}, {1,4,5}, {3,5}, {3,4}, {7}, {2,6,8}, {1,7}};
int q[100] = {};

void bfs(int start) {
  int front = 0, rear = 0;
  q[0] = start;
  rear++;
  visited[start] = 1;
  
  while(front < rear) {
    int x = q[front++];
    printf("%d ", x);
    int size = sizeof(graph[x]) / sizeof(int);
		
    for(int i=0; i<size; i++) {
      int node = graph[x][i];
      if(!visited[node]) {
        q[rear++] = node;
        visited[node] = 1;
      }
    }
  }
}

int main(void) {
  bfs(1);
  return 0;
}