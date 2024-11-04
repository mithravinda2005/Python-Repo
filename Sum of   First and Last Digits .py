import java.util.Scanner;

public class SumOfFirstAndLastDigits {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the input number
        int number = scanner.nextInt();

        // Find the last digit
        int lastDigit = number % 10;

        // Find the first digit
        int firstDigit = number;
        while (firstDigit >= 10) {
            firstDigit /= 10;
        }

        // Calculate the sum of the first and last digits
        int sum = firstDigit + lastDigit;

        // Print the result
        System.out.println(sum);

        scanner.close();
    }
}