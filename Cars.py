import java.util.Scanner;

public class Cars {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the number of friends
        int N = scanner.nextInt();

        // Calculate the minimum number of cars required
        int carsRequired = (N + 3) / 4; // Adding 3 ensures proper rounding up for any remainder

        // Print the result
        System.out.println(carsRequired);

        scanner.close();
    }
}