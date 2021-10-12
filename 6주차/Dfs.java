// DFS

import java.util.*;

public class Dfs {
  public static boolean[] visited = new boolean[9];
  static int[][] graph = {{}, {2,3,8}, {1,7}, {1,4,5}, {3,5}, {3,4}, {7}, {2,6,8}, {1,7}};

  public static void dfs(int x) {
    visited[x] = true;
    System.out.print(x + " ");

    for (int node : graph[x]) {
      if (!visited[node]) {
        dfs(node);
      }
    }
  }

  public static void main(String[] args) {
    dfs(1);
  }
}