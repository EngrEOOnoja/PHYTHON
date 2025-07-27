def get_score():
	user_score = int(input('Please enter a value between 0 and 100'))
	while user_score < 0 or user_score > 100:
	return user_score					
		
	print('Invalid score. Please enter a value between 0 and 100')