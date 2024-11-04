import java.util.Scanner;
import java.text.DecimalFormat;

public class ElectricityBill {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.00");

        // Read the number of units consumed
        int units = scanner.nextInt();
        double costPerUnit;
        double bill;
        double surcharge = 0.0;

        // Determine cost per unit based on units consumed
        if (units < 200) {
            costPerUnit = 1.20;
        } else if (units < 400) {
            costPerUnit = 1.40;
        } else if (units < 600) {
            costPerUnit = 1.60;
        } else if (units < 800) {
            costPerUnit = 1.80;
        } else {
            costPerUnit = 2.00;
        }

        // Calculate the bill
        bill = units * costPerUnit;

        // Calculate surcharge if the bill exceeds Rs. 400
        if (bill > 400) {
            surcharge = bill * 0.15;
                surcharge = bill * 0.15;
        }

        // Calculate total amount
        double totalAmount = bill + surcharge;

        // Output the results
        System.out.println("Units Consumed: " + units);
        System.out.println("Cost per Unit: " + df.format(costPerUnit));
        System.out.println("Bill: " + df.format(bill));
        System.out.println("Surcharge: " + df.format(surcharge));
        System.out.println("Total Amount: " + df.format(totalAmount));

        scanner.close();
    }    
}