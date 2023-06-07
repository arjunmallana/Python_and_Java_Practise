package org.hackerrank;
import java.util.Scanner;

public class Multiples {

  public static void main(String[] args) {
    

    Scanner ip = new Scanner(System.in);
    System.out.println("Enter the Number to get the multiple of :");
    int n = ip.nextInt();
    ip.close();
    for (int i = 1; i <= 10; i++) {
      int multi = n * i;
      System.out.println(n + " X " + i + "=" + multi);
    
    }

  }
}
