import java.io.*;
import java.util.*;

public class stringSplit {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine().trim();
        // Write your code here.
        scan.close();
        if (s.length() == 0)System.out.println(0);
        else{
            String[] words = s.split("[^a-zA-Z0-9]+");
            System.out.println(words.length);
            for (String x:words){
                System.out.println(x);
            }
        }
        }
}

