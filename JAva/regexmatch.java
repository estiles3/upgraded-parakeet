import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Scanner;

class regexmatch{

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        while(in.hasNext()){
            String IP = in.next();
            System.out.println(IP.matches(new MyRegex().pattern));
        }

    }
}

//Write your code here
class MyRegex {
    // This regex validates an IPv4 address (e.g., 192.168.0.1)
    String zeroTo255 = "([0-9]{1,2}|(0|1)[0-9]{2}|2[0-4][0-9]|25[0-5])";

    // Combine four groups separated by dots
    public String pattern = zeroTo255 + "\\." + zeroTo255 + "\\." + zeroTo255 + "\\." + zeroTo255;
}