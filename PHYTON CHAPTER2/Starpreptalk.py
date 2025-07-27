mylist = [12,6,4,5,7] 
	int i = 0
	int answer = 0
	int highest = 0
	int smallest = 100
	while(i < 4;i++):
		print("Enter digit")
		myList[i] = input.nextDouble()
		if (scores[i] > highest): 
			highest = scores[i]
		if (scores[i] < smallest):
			smallest = myList[i]
		
		answer = highest - smallest		
		
		print(answer)