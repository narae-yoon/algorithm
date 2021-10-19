// 미로탈출 (DFS)
import java.io.*;
import java.util.*;

public class MazeDFS {
  public static int N,M;
  public static int [][] graph = new int [200][200];
  public static int dx[] = {-1, 1, 0, 0};
  public static int dy[] = {0, 0, -1, 1};
  
  public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);
    N = scanner.nextInt();
    M = scanner.nextInt();
    scanner.nextLine();
    System.out.println("n " + N + "m" + M);

    for(int i=0; i <N; i++){
      String str = scanner.nextLine();
      
      for(int j=0; j<M; j++){
        graph[i][j] = str.charAt(j) - '0';
      }
    }
    scanner.close();

    System.out.println("result = " + dfs(0,0));
  }

  private static int dfs(int x, int y) {
    Stack<Node> stack = new Stack<Node>();
    Node node = new Node(x, y);
    
    stack.push(node);
    while (!stack.empty()) {
      node = stack.pop();
      x = node.getX();
      y = node.getY();
      
      for(int i=0;i<4;i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        
        if(nx < 0 || ny < 0 || nx >= N || ny >= M ) continue;
        if (graph[nx][ny] == 1) {
          System.out.println("[" + nx + "," + ny + "]");
          graph[nx][ny] = graph[x][y] + 1;
          stack.push(new Node(nx, ny));
        }
      }
    }
    
    return graph[N-1][M-1];
  }
  
  static class Node{
    final private int x;
    final private int y;
    
    Node(int x, int y) {
      this.x = x;
      this.y = y;
    }

    public int getX() { return x; }
    public int getY() { return y; }
  }
}