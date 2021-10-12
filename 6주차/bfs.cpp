// BFS

#include <bits/stdc++.h>

using namespace std;

bool visited[9] = {true};
int graph[9][3] = {{}, {2,3,8}, {1,7}, {1,4,5}, {3,5}, {3,4}, {7}, {2,6,8}, {1,7}};

void bfs(int start) {
  queue<int> q;
  q.push(start);
  visited[start] = true;
  
  while(!q.empty()) {
    int x = q.front();
    q.pop();
    cout << x << ' ';
    for(int node : graph[x]) {
      if(!visited[node]) {
        q.push(node);
        visited[node] = true;
      }
    }
  }
}

int main(void) {
  bfs(1);
  return 0;
}