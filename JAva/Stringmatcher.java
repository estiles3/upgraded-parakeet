import java.io.*;
import java.util.*;

public class Stringmatcher {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        StringBuilder sb = new StringBuilder(A);
        String reversedStr1 = sb.reverse().toString();
        // System.out.print(A);
        // System.out.print(reversedStr1);
        if (A.equals(reversedStr1)){
            System.out.print("Yes");
        }else{
            System.out.print("No");
        }
    }
}



