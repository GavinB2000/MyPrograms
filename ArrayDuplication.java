// creates two arrays of variables and tells the sum of the values, average, and number of even and odd values
// Created by Gavin Birk on 11/3/24
import javax.swing.JOptionPane;
import java.util.Arrays;

public class ArrayDuplication{   
  public static void main (String[] args){             
  
   // variable for size of the original array, along with initializing the array
   final int ARRAYSIZE = Integer.parseInt(JOptionPane.showInputDialog("Enter the size for your list:"));
   int [] referenceVariables = new int[ARRAYSIZE]; 
   
   // values for number of even/odd numbers, string of the array, and total numbers
   int evenNums = 0;
   int oddNums = 0;
   String variables = "";
   int sumOfArray = 0;
   
   // for loop to create random integers 
   for (int i = 0; i < referenceVariables.length; i++) {
      int randomVariable = (int) (Math.random() * 100);
      referenceVariables[i] = randomVariable; 
      variables = (Arrays.toString(referenceVariables));
   } // end for loop

   // displays the variables in the array  
     JOptionPane.showMessageDialog(null, "The values in the array are \n" + variables);
     
     // doubles the size of the length of the original array
     final int NEWARRAYSIZE = ARRAYSIZE * 2;
     // variable for a string of the variables in the new array
     String newVariables = "";

     // copy of the array
     int [] referenceVariableCopy = Arrays.copyOf(referenceVariables, NEWARRAYSIZE);
     
     // loop for adding the new variables to the array
     for (int i = 0; i < NEWARRAYSIZE; i++) {
     // gets variable from user, but raises an error if value isn't between 50 - 100
     if (i >= ARRAYSIZE) {
      try {
      referenceVariableCopy[i] = Integer.parseInt(JOptionPane.showInputDialog("Enter a number between 50 and 100"));
      } // exception if a number isn't entered and exits program
      catch (Exception e) {
      JOptionPane.showMessageDialog(null, "Number must be between 50 and 100");
      System.exit(0);
      } // end exception 
      if (referenceVariableCopy[i] < 50 || referenceVariableCopy[i] > 100) {
      JOptionPane.showMessageDialog(null, "Number must be between 50 and 100");
      System.exit(0);
      } // end if statement
      }
      
      // Calculate sum of values
      sumOfArray += referenceVariableCopy[i];
      
      // calculate sum of even and odd numbers
      if (referenceVariableCopy[i] % 2 == 0) {
      evenNums += 1;
      } else {
      oddNums += 1;
      }
      newVariables = (Arrays.toString(referenceVariableCopy));
   } // end for loop
   
   // calculates the average of the numbers and converts new array to a string
   double sumofnums = sumOfArray;
   double length = referenceVariableCopy.length;
   double avgNums = sumofnums / length;
   
   // displays the variables in the new list, the sum of the list, the even numbers and the odd numbers
   JOptionPane.showMessageDialog(null, "The values in the array are \n" + newVariables +
   "\nThe sum of the variables " + sumOfArray + "\nThe count of even variables " + evenNums + 
   "\nThe count of odd variables " + oddNums + "\nThe average of all values is " + avgNums);
     
     

} // end main
} // end class