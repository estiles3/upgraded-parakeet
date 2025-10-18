import java.util.*;
import java.text.NumberFormat;

public class currency {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        
        // Write your code here.
        Locale ind = new Locale("en","IN","Rs.");
        String us = NumberFormat.getCurrencyInstance(Locale.US).format(payment);
        System.out.println("US: " + us);
        String india = NumberFormat.getCurrencyInstance(ind).format(payment);
        String china = NumberFormat.getCurrencyInstance(Locale.CHINA).format(payment);
        String france = NumberFormat.getCurrencyInstance(Locale.FRANCE).format(payment);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
