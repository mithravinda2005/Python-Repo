import java.util.Scanner;

public class Donation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the incomes of Pavan and Ganapathi
        int X = scanner.nextInt(); // Pavan's income
        int Y = scanner.nextInt(); // Ganapathi's income

        // Calculate the donation amount
        int donation = Y - X;

        // Print the donation amount
        System.out.println(donation);

        scanner.close();
    }
}