package org.hackerrank;
import java.util.Scanner;

public class Loops2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt(); // Read the number of test cases

        for (int i = 0; i < t; i++) { // Loop over each test case
            int a = scanner.nextInt(); // Read the value of 'a'
            int b = scanner.nextInt(); // Read the value of 'b'
            int n = scanner.nextInt(); // Read the value of 'n'
            int sum = a; // Initialize the sum with 'a'

            for (int j = 0; j < n; j++) { // Loop to calculate each term of the series
                // Calculate the term: a + (2^j) * b and add it to the sum
                sum += Math.pow(2, j) * b;
                System.out.print(sum + " "); // Print the current sum
            }
            System.out.println(); // Print a newline to separate the series of each test case
        }

        scanner.close(); // Close the scanner
    }
}
