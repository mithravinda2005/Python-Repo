import java.util.Scanner;

public class FractionHeight {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the numerator and denominator
        int x = scanner.nextInt();
        int y = scanner.nextInt();

        // The height is the maximum of x and y
        int height = Math.max(x, y);

        // Output the height
        System.out.println(height);

        scanner.close();
    }
}