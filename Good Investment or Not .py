import java.util.Scanner;

public class GoodInvestment {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the interest rate (X) and inflation rate (Y)
        int interestRate = scanner.nextInt();
        int inflationRate = scanner.nextInt();

        // Check if the interest rate is at least twice the inflation rate
        if (interestRate >= 2 * inflationRate) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

        scanner.close();
    }
}