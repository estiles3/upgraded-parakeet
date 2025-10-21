import java.util.*;

public class Stringcheck {

    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        String A = scan.next();
        String B = scan.next();
        /* Enter your code here. Print output to STDOUT. */
        int c = A.length() + B.length();
        System.out.print(c+"\n");
        if (A.compareTo(B) > 0){
            System.out.print("Yes\n");
        }else{
            System.out.print("No\n");
        }
        A = A.substring(0, 1).toUpperCase() + A.substring(1);
        B = B.substring(0, 1).toUpperCase() + B.substring(1);
        System.out.print(A+" "+B);
    }
}



