import java.util.Scanner;

public class Password {

    public static String getPassword(Scanner scanner) {
        System.out.print("Enter a password of your choice or type 'stop' to exit app: ");
        return scanner.nextLine();
    }

    public static int[] checkComplexity(String password) {
        int alphaCount = 0;
        int digitCount = 0;

        for (char ch : password.toCharArray()) {
            if (Character.isLetter(ch)) {
                alphaCount++;
            } else if (Character.isDigit(ch)) {
                digitCount++;
            }
        }

        return new int[]{alphaCount, digitCount};
    }

    public static String evaluateStrength(int alphaCount, int digitCount, int length) {
        if (length < 6 || digitCount == 0) {
            return "Weak password";
        } else if (length >= 6 && length <= 8 && digitCount >= 1) {
            return "Moderate password strength";
        } else if (length > 8 && digitCount >= 2) {
            return "Very strong password";
        } else {
            return "Weak password";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            String password = getPassword(scanner);
            if (password.equalsIgnoreCase("stop")) {
                System.out.println("Thank you for using my app. Come back later.");
                break;
            }

            int[] counts = checkComplexity(password);
            int alphaCount = counts[0];
            int digitCount = counts[1];
            int length = password.length();

            String strength = evaluateStrength(alphaCount, digitCount, length);

            System.out.println("\nPassword Analysis:");
            System.out.println("Length: " + length);
            System.out.println("Letters: " + alphaCount);
            System.out.println("Digits: " + digitCount);
            System.out.println("Strength: " + strength + "\n");
        }

    }
}