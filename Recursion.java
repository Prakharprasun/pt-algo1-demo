//Count total paths in a maze to move from (0,0) to (n,m)

import java.util.Scanner;

public class Recursion {
    public static int countPaths(int i,int j,int n,int m){
        if(i==n || j==m){
            return 0;
        }
        if(i==n-1 && j==m-1){
            return 1;
        }
        //move downwards
        int downPaths = countPaths(i+1, j, n, m);
        //move right
        int rightPaths = countPaths(i, j+1, n, m);
        return downPaths + rightPaths;
    }
    public static void main (String args[]){
    var con = System.console();
    if (con != null) {
       
        Scanner sc = new Scanner(con.reader());
        
        System.out.println("Enter n");
        int n = sc.nextInt();
        System.out.println("Enter m");
        int m = sc.nextInt();
        int totalPaths = countPaths(0, 0, n, m);
        System.out.println(totalPaths);
}
    
}
}