import java.util.Scanner;
public class ArrayClassModify{
	public static void main(String[] args){
			Scanner input = new Scanner(System.in);
			int[] scores = new int[5];

		
	int i = 0;
	highest = 0;
	smallest = -1000;
	for(;i < 5;i++){
	System.out.println("Enter digit");
	scores[i] = input.nextInt();
	if (scores[i] > highest){ 
	highest = scores[i];}
	if (smallest > scores[i]){
	smallest = scores[i]
	}
			
	}
	System.out.println(highest - smallest);	
	
	}

}