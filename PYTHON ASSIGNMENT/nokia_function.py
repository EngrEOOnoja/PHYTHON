def nokia_menu():
	nokia_menu = print("""
	LIST OF FUNCTION..

	
	1. Phonebook.
	2. Messages.
	3. Chat.
	4. Call Register.
	5. Tones.
	6. Settings.
	7. Call Divert.
	8. Games.
	9. Calculator.
       10. Reminders.
       11. Clock.
       12. Profiles
       13. SIM Services.
	 """)

	case 1: phonebook()



		menu = int(input("goto phone_book :"))
match menu :
	case 1: 
		print("PhoneBook") 
		phonebook = print("""
			1. Search.
			2. Service Nos.
			3. Add Name
			4. Erase.
			5. Edit.
			6. Assign Tone.
			7. Send b'card.
			8. Options.
			9. Speed Dials.
			10. Voice Tags								
					""")
	
		phonebook = int(input("Select PhoneBook option  :"))
		match phonebook :
			case 1 :
				print('Search')
			case 2 : 
				print('Service Nos.')
			case 3:
				print('Add Name.')
			case 4: 
				print('Erase.')
			case 5:
				print('Edit.')
			case 6:
				print('Assign Tone.')
			case 7:
				print("Send b'card.")
			case 8:
				print("""
				1. Type of View.
				2. Memory Status.	
				""")
				option = int(input("select Option  :"))
				match option:
					case 1: 
						print('Type of View')
					case 2:
						print('Memory Status')
					case _: 
						print('Enter Correct input')
			case 9:
				print('Speed Dials.')
			case 10:
				print('Voice Tags')
			case _: 
				print('Enter Correct input')












nokia_menu()