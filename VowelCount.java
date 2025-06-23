/* Program reads in a sentence and sees how many vowels are in it
* October 16th 2024
*/ 
import java.util.Scanner;
public class VowelCount{
   public static void main(String[] args){
   
      // Gets input as a string
      Scanner keyboard = new Scanner(System.in);
      System.out.print("Please Enter a sentence: ");
      String sentence = keyboard.nextLine();
      
      // Variables for the vowels in a string
      int vowelA = 0; int vowelE = 0; int vowelI = 0; int vowelO = 0; int vowelU = 0;
      int i = 0;
      while (i < sentence.length()){
         // or added so uppercase vowels are counted
         if (sentence.charAt(i) == 'a'|| sentence.charAt(i) == 'A') {
            vowelA++;
         } else if (sentence.charAt(i) == 'e' || sentence.charAt(i) == 'E') {
            vowelE++;
         } else if (sentence.charAt(i) == 'i'|| sentence.charAt(i) == 'I') {
            vowelI++;
         } else if (sentence.charAt(i) == 'o'|| sentence.charAt(i) == 'O') {
            vowelO++;
         } else if (sentence.charAt(i) == 'u'|| sentence.charAt(i) == 'U') {
            vowelU++;
         }
         i++;
      }
      // displays the number of different vowels in the sentence
      System.out.println("The vowel count for " + sentence + " is:");
      System.out.println("a: " + vowelA);
      System.out.println("e: " + vowelE);
      System.out.println("i: " + vowelI);
      System.out.println("o: " + vowelO);
      System.out.println("u: " + vowelU);
      
   }
}