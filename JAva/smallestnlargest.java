import java.util.Scanner;

public class smallestnlargest {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        String[] our = new String[s.length()-k+1];
        for (int x = 0; x < s.length()-k+1; x++){
            our[x] = s.substring(x, x+k);
            // System.out.print(our[x]+"\n");
        }
        smallest = our[0];
        largest = our[0];
        for (int x = 0; x<our.length;x++){
            // System.out.print(our[x]+" "+ smallest + " | " + largest + "\n");
            if (our[x].compareTo(smallest) < 0){
                // System.out.print("Smaller \n");
                smallest = our[x];
            }if (our[x].compareTo(largest) > 0){
                // System.out.print("Larger \n");
                largest = our[x];
            }
        }
        // System.out.print(our.toString());
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}