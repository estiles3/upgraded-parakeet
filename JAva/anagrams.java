import java.util.Scanner;

public class anagrams {
    static boolean isAnagram(String a, String b) {
        // Complete the function
        String checkA = a.toLowerCase();
        String checkB = b.toLowerCase();
        
        String[] aa = checkA.split("");
        String[] ab = checkB.split("");
        if (checkA.length() != checkB.length())return false;
        
        int[] counts = new int[26];
        for (int x = 0; x< aa.length;x++){
            counts[checkA.charAt(x) - 'a']++;
            counts[checkB.charAt(x) - 'a']--;
            System.out.print(aa[x]+"|"+ab[x]+"\n");
        }
        for (int count:counts){
            System.out.print("count:"+ count);
            
        }
        
        return true;
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}