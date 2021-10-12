import java.io.*;
import java.util.Scanner;

public class FreezeDrinks {
  public static int N,M;
  public static int [][] graph = new int[1000][1000];

  public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);
    
    N = scanner.nextInt();
    M = scanner.nextInt();
    scanner.nextLine();
    System.out.println("+++++++");
    System.out.println("n " + N + "m" + M);
    
    for(int i=0; i <N; i++) {
      String str = scanner.nextLine();
      for(int j=0; j<M; j++) {
        graph[i][j] = str.charAt(j) - '0';
      }
    }

    scanner.close();
    
    int result = 0;
    for(int i=0; i <N; i++) {
      for(int j=0; j<M; j++) {
        if(dfs(i, j)) {
          result+=1;
        }
      }
    }
    
    System.out.println(result);
  }
  
  public static boolean dfs(int x, int y) {
    if(x <= -1 || x>= N || y <= -1 || y >= M)
      return false;
    
    if(graph[x][y] == 0) {
      graph[x][y] = 1;
      
      dfs(x -1, y);
      dfs(x, y -1);
      dfs(x + 1, y );
      dfs(x, y + 1);
      return true;
    }
    
    return false;
  }
}