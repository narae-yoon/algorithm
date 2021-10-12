// DFS

#include <bits/stdc++.h>

using namespace std;
bool visited[9] = {true};
int graph[9][3] = {{}, {2,3,8}, {1,7}, {1,4,5}, {3,5}, {3,4}, {7}, {2,6,8}, {1,7}};

void dfs(int x) {
  visited[x] = true;
  cout << x << ' ';
  for (int node : graph[x]) {
  // 인접한 노드가 방문한 적이 없다면 DFS 수행
    if(!visited[node]) {
      dfs(node);
    }
  }
}

int main(void) {
  dfs(1);
}