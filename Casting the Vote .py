import java.util.Scanner;

public class VotingEligibility {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int age = scanner.nextInt(); // Read the age of the candidate

        // Check eligibility
        if (age >= 18) {
            System.out.println("YES"); // Eligible to vote
        } else {
            System.out.println("NO"); // Not eligible to vote
        }

        scanner.close();
    }
}