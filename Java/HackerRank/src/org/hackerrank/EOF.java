package org.hackerrank;
import java.util.Scanner;

public class EOF {

  public static void main(String[] args) {
    // Create a new Scanner object to read input
    Scanner scanner = new Scanner(System.in);

    // Initialize the line number variable
    int lineNumber = 1;

    // Continue reading input until the end of file (EOF) is reached
    while (scanner.hasNext()) {
      // Read the next line of input
      String line = scanner.nextLine();

      // Print the line number and the line content
      System.out.println(lineNumber + " " + line);

      // Increment the line number for the next iteration
      lineNumber++;
    }

    // Close the Scanner object to release system resources
    scanner.close();
  }
}
