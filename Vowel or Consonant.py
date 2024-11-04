import java.util.Scanner;

public class VowelOrConsonant {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        char character = scanner.next().charAt(0);
        
        // Check if the character is a vowel
        if (character == 'A' || character == 'E' || character == 'I' || character == 'O' || character == 'U' ||
            character == 'a' || character == 'e' || character == 'i' || character == 'o' || character == 'u') {
            System.out.println("VOWEL");
        } else {
            System.out.println("CONSONANT");
        }
        
        scanner.close();
    }
}