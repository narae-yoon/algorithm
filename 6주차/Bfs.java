// BFS

import java.util.*;

public class Bfs {
  public static boolean[] visited = new boolean[9];
  public static int[][] graph = {{}, {2,3,8}, {1,7}, {1,4,5}, {3,5}, {3,4}, {7}, {2,6,8}, {1,7}};

  public static void bfs(int start) {
    Queue<Integer> q = new LinkedList<>();
    
    q.offer(start);
    visited[start] = true;

    while(!q.isEmpty()) {
      int x = q.poll();
      System.out.print(x + " ");
      
      for(int node : graph[x]) {
        if(!visited[node]) {
          q.offer(node);
          visited[node] = true;
        }
      }
    }
  }

  public static void main(String[] args) {
    bfs(1);
  }
}