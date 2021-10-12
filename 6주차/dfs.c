// DFS

#include <stdio.h>

int visited[9] = {1};
int graph[9][3] = {{}, {2,3,8}, {1,7}, {1,4,5}, {3,5}, {3,4}, {7}, {2,6,8}, {1,7}};

void dfs(int x) {
  int size = sizeof(graph[x]) / sizeof(int);
  visited[x] = 1;
  printf("%d", x);
  
  for(int i=0; i<size; i++) {
    int node = graph[x][i];
    if(!visited[node]) {
      dfs(node);
    }
  }
}

int main(void) {
  dfs(1);
  return 0;
}