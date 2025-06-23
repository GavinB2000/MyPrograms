/* Program gets number of values from the user
* After getting the values, it will ask for temperatures
* Lastly, it will calculate the average tempreature from those values
Program displays error messages if needed and uses JOptionPane to show windows
Rather than plain text to the user
Program was completed in my IT 106 course during my Fall 2024 semester
*/
import javax.swing.JOptionPane;
public class AverageTemperatureCalculator{
   public static void main (String[] args){
      // asks for number of temperature values user wants to enter by calling getNumTemp
      int values = getNumTemp("Please enter number of temperatures",0);
      int count = 0;
      int sum = 0;
      String input;
      while (values > 0){ // Loop runs and gets temperatures based on what int values is
         int temp = getInt("Please input a temperature in Fahrenheit (-20 to 120):", -20, 120);           
         sum += temp;
         values--;
         count++;
                    
         }
      double avgTemp=sum/count;
      JOptionPane.showMessageDialog(null,String.format("The average temp for the week is: %.2f", avgTemp));
      }
      
      // method that gets number of temperatures to calculate, verifies valid number is entered, not string
      public static int getNumTemp(String message, int temps){
      int values = 0;
      boolean runs = true;
      while (runs) {
         String input = JOptionPane.showInputDialog(message);
         try {
            values = Integer.parseInt(input);
            if(values < 1) {
            JOptionPane.showMessageDialog(null, "Please enter a value greater than zero"); 
            } // end if
            else { 
            runs = false; 
            }
         } // end try
         catch(NumberFormatException e) {
            JOptionPane.showMessageDialog(null, "Invalid input");
            continue;
            }
      } // end while true
      return values;
   } // end method
   
   // method verifies that temperatures are within the range -20 to 120
   public static int getInt(String message,int lowerLimit, int upperLimit){
      int temp = 0;
      boolean loopRuns = true;
      while(loopRuns) {
         String input = JOptionPane.showInputDialog(message);
         try {
               temp = Integer.parseInt(input);
               if(temp < lowerLimit || temp > upperLimit){ // checks given input is within an acceptable range
                  JOptionPane.showMessageDialog(null, "Please enter a valid number in the range of -20 and 120.");
               } else {
                  loopRuns = false; // loop ends once the valid input is done
               }
               
         }catch(NumberFormatException e){// checks if a non number was entered, runs the loop afterwards
               JOptionPane.showMessageDialog(null, "Invalid input");
               continue;
         }
      }
      //complete the code
      return temp;

      } // end main
   } // end class