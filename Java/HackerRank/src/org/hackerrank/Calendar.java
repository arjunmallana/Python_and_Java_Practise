package org.hackerrank;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

 class Result {

  /*
   * Complete the 'findDay' function below.
   *
   * The function is expected to return a STRING.
   * The function accepts following parameters:
   *  1. INTEGER month
   *  2. INTEGER day
   *  3. INTEGER year
   */
  public static String findDay(int month, int day, int year) {
    Scanner in = new Scanner(System.in);
    month = in.nextInt();
    day = in.nextInt();
    year = in.nextInt();
    return null;
  }
}

public class Calendar {

  public static void main(String[] args) throws IOException {
    BufferedReader bufferedReader = new BufferedReader(
      new InputStreamReader(System.in)
    );
    BufferedWriter bufferedWriter = new BufferedWriter(
      new FileWriter(System.getenv("OUTPUT_PATH"))
    );

    String[] firstMultipleInput = bufferedReader
      .readLine()
      .replaceAll("\\s+$", "")
      .split(" ");

    int month = Integer.parseInt(firstMultipleInput[0]);

    int day = Integer.parseInt(firstMultipleInput[1]);

    int year = Integer.parseInt(firstMultipleInput[2]);

    String res = Result.findDay(month, day, year);

    bufferedWriter.write(res);
    bufferedWriter.newLine();

    bufferedReader.close();
    bufferedWriter.close();
  }
}
/*import java.time.LocalDate;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the date input in the format: MM DD YYYY
        int month = scanner.nextInt();
        int day = scanner.nextInt();
        int year = scanner.nextInt();

        // Create a LocalDate object using the input date
        LocalDate date = LocalDate.of(year, month, day);

        // Get the day of the week from the LocalDate object
        String dayOfWeek = date.getDayOfWeek().name();

        // Convert the day of the week to uppercase
        dayOfWeek = dayOfWeek.toUpperCase();

        // Print the day of the week
        System.out.println(dayOfWeek);

        scanner.close();
    }
}
*Create a new instance of the Calendar class
Calendar calendar = Calendar.getInstance();

// Set the month, year, and day of the calendar object based on the input values
calendar.set(Calendar.MONTH, month - 1); // Month is zero-based, so subtract 1
calendar.set(Calendar.YEAR, year);
calendar.set(Calendar.DAY_OF_MONTH, day);

// Get the date as a string
String dayDate = calendar.getTime().toString();

// Extract the first three characters from the date string
String subsDay = dayDate.substring(0, 3);

// Initialize the dayOfWeek variable
String dayOfWeek = "";

// Use a switch statement to match the subsDay value and assign the corresponding day of the week
switch (subsDay) {
    case "Mon":
        dayOfWeek = "MONDAY";
        break;
    case "Tue":
        dayOfWeek = "TUESDAY";
        break;
    case "Wed":
        dayOfWeek = "WEDNESDAY";
        break;
    case "Thu":
        dayOfWeek = "THURSDAY";
        break;
    case "Fri":
        dayOfWeek = "FRIDAY";
        break;
    case "Sat":
        dayOfWeek = "SATURDAY";
        break;
    case "Sun":
        dayOfWeek = "SUNDAY";
        break;
}

// Return the dayOfWeek value
return dayOfWeek;
 */