import java.util.Scanner;
public class OnojaGradeCalculator {
public static void main(String[] args){
	Scanner input = new Scanner(System.in);
		boolean schoolGrade = true;
		while (schoolGrade){
		int score = getScore(input);
		char grade = calculateGrade(score);
		String message = getFeedback(grade);
		System.out.println(grade + "   " + message);
		
		System.out.println("Try another score? (yes/no): ");
	      String user = input.next().toLowerCase();
     		 schoolGrade = user.equals("yes");}
	}
	
public static int getScore(Scanner input){
	System.out.print("Please enter a value between 0 and 100  :");
	int score = input.nextInt();
	while (score < 0 || score > 100){
	System.out.print("Please enter a value between 0 and 100  :");
	score = input.nextInt();
		}	
	return score;
		}
		
		
public static char calculateGrade(int score) {
	if (score >= 90) {
		return 'A'; }
	else if (score >= 80){
		return  'B'; }
	else if (score >= 70){
		return  'C'; }
	else if (score >= 60){
		return  'D'; }
	else{
		return  'F'; }
}



public static String getFeedback(char grade){
	if (grade == 'A'){
		return "Excellent performance";}
	else if (grade == 'B'){
		return "Good job, Keep improving";}
	else if (grade == 'C'){
 		return "Fair effort, keep working on it";}
	else if (grade == 'D'){
		return "You can do better, don’t give up";}
	else{
		return "Needs Improvement, Ask for help"; }
		}	
}


