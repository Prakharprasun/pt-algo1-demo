import java.util.Scanner;
class HelloGoodbye{
public static void main(String [] args){
    var con = System.console();
    if (con != null) {
       
        Scanner sc = new Scanner(con.reader());
        
        System.out.println("Enter name1");
        String x = sc.nextLine();
        System.out.println("Enter name2");
        String y = sc.nextLine();
        System.out.println("Hello "+x+" and "+y);
        System.out.print("Goodbye "+y+" and "+x);
    
}}}