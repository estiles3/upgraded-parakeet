import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Staticmethods {

//AREA OF MAIN FOCUS ===>

    public static int B; 
    public static int H; 
    public static boolean flag = true;
    static{
        Scanner inp = new Scanner(System.in);
        B = inp.nextInt();
        H = inp.nextInt();
        if(0 >= B || 0 >= H){
            flag = false;
            System.out.print("java.lang.Exception: Breadth and height must be positive");
        }
        inp.close();        
    }

    public static void main(String[] args){
        if(flag){
            int area=B*H;
            System.out.print(area);
        }
            
	}//end of main

}//end of class

