import java.util.Scanner;
public class Test {
 
 public static void main(String[] args) {
 Scanner scanner = new Scanner (System.in);
 byte z1,z2, z3, z;
 // input
 System.out.print("Erste Zahl: ");
 //zwischen -128 und 127
 z1 = scanner.nextByte();
 System.out.print("Zweite Zahl: ");
 z2 = scanner.nextByte();
 System.out.print("Zweite Zahl: ");
 z3 = scanner.nextByte();
 z= (byte) (z1+z2+z3); //100 + 100 ?
 System.out.println("Die Summe ist " + z);
 scanner.close();
 } // end of main
 
} // end of class TestByte