def nokia_3310_function():
nokia = print("""

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
	
menu = int(input("choose out of the nokia option  :"))
match menu :
	case 1: 
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
	case 2:
		print("""
			1. Write Message.
			2. Inbox.
			3. Out Box.
			4. Picture Message
			5. Template
			6. Simleys
			7. Message Settings

		""")

		message = int(input("Enter message option  :"))
		match message :
			case 1:
				print('Write Message')
			case 2:
				print('Inbox')
			case 3:
				print('Out Box')
			case 4:
				print('Picture Message')
			case 5:
				print('Template')
			case 6:
				print('Simleys')
			case 7:
				print("""	
					1. Set.
					2. Common.
			""")
				message_setting = int(input("Enter Message Setting  :"))
				match message_setting : 
					case 1:
						print("""
						1. Message Center Number.
						2. Message Sent as
						3. Message validity.
					""")
					case 2:
						print("""
						1.Delivery Report.
						2. Reply Via Same Center. 
						3. Character Support.
					""")
					case _:
						print("Enter Correct Input")
					
			case 8:
				print('Info Service')
			case 9:
				print('Voice MailBox Number')
			case 10:
				print('Service Command Editor')	
			case _:
				print('Enter Correct Input  :')
	case 3:
		print('Chat')
	case 4:
		print("""
			1. Missed Calls
			2. Received Calls
			3. Received Calls
			4. Erased Recent Call Lists.
			5. Show Call Duration
			6. Show Call Cost.
			7. Call Cost Settings
			8. Prepaid Credit
		""")
		call_register = int(input("Enter Call Register option  :"))
		match call_register : 
			case 1:
				print('Missed Calls')
			case 2:
				print('Received Calls')
			case 3:
				print('Dialled Numbers')
			case 4:
				print("""
				1. Missed Calls
				2. Received Calls
				3. Dialled Numbers
				4. Erase Recent Call Lists.
				""")
				erased_recent_call_lists = int(input(""))
				match erased_recent_call_lists :
					case 1:
						print('Missed Calls')
					case 2:
						print('Received Calls')
					case 3:
						print('Dialled Numbers')
					case 4:
						print('Erase Recent Call Lists.')
					case _: 
						print('Enter Correct input')
			case 5:
				print("""
				1. Last Call Duration.
				2. All Calls Duration.
				3. Received Calls Duration.
				4. Dialled Calls Duration
				5. Clear Timers
				""")
				show_call_duration = int(input('Enter option  :'))
				match show_call_duration :
					case 1:
						print('Last Call Duration.')
					case 2:
						print('All Calls Duration.')
					case 3:
						print('Received Calls Duration.')
					case 4:
						print('Dialled Calls Duration')
					case 5:
						print('Clear Timers')
					case _:
						print('Enter Correct Input')

					
				
			case 6:
				print("""
				1. Last Call Cost
				2. All Calls Limit
				3. Clear Counters
			""")
				show_call_costs = int(input("Enter Options  :"))
				match show_call_costs :
					case 1:
						print('last Call Cost')
					case 2:
						print('All Calls Cost')
					case 3:
						print('Clear Counters')
					case _:
						print('Enter valid Input  :')
			case 7:
				print("""
				1.Call Cost Limit
				2.Show Costs in
				""")
				call_cost_settings = int(input(""))
				match call_cost_settings :
					case 1:
						print('Call Cost Limit')
					case 2:
						print('Show Costs in')
					case _:
						print('Enter valid Input  :')
			case 8:
				print('Prepaid Credit')
			case _:
				print('Enter valid Input  :')
					

	case 5:
		print("""
		1. Ringing Tone
		2. RInging Volume 
		3. Incoming Call Alert
		4. Composer
		5. message alert tone
		6. Keypad tones
		7. Warning and game tones
		8. Vibrating alert
		9. Screen Saver
		""")
		tones = int(input(''))
		match tones :
			case 1 :
				print('Ringing Tone')
			case 2 :
				print('RInging Volume')
			case 3 :
				print('Incoming Call Alert')
			case 4 :
				print('Composer')
			case 5 :
				print('message alert tone')
			case 6 :
				print('Keypad tones')
			case 7 :
				print('Warning and game tones')
			case 8 :
				print('Vibrating alert')
			case 9 :
				print('Screen Saver')
			
			case _: 
				print('Enter Correct input')
	case 6:
		print("""
		1. Call Settings
		2. Phone Settings
		3. Security Settings
		4. Restore Factory Settings		
		""")
		settings = int(input('Enter Option for Setting  :'))
		match settings :
			case 1:
				print("""
					1. Automatic redial
					2. Speed dailing
					3. Call waiting options
					4. Own number sending
					5. Phone line in use 
					6. Automatic answer			6
				""")
				call_settings = int(input('Enter Call Setting Option  :'))
				match call_settings :
					case 1:
						print('Automatic redial')
					case 2:
						print('Speed dailing')
					case 3:
						print('Call waiting options')
					case 4:
						print('Own number sending')
					case 5:
						print('Phone line in use')
					case 6:
						print('Automatic answer')
					
					case _: 
						print('Enter Correct input')
			case 2:
				print("""
					1. Laguage
					2. Cell Info display
					3. welcome note
					4. Network selection
					5. Lights
					6. Confrm SIm service actions
					""")
				phone_settings = int(input('Enter phone setting option'))
				match phone_settings :
						case 1 :
							print('Laguage')
						case 2 :
							print('Cell Info display')
						case 3 :
							print('welcome note')
						case 4 :
							print('Network selection')
						case 5 :
							print('Lights')
						case 6 :
							print('Confrm SIm service actions')
						
						case _: 
							print('Enter Correct input')
			case 3:
				print("""
				1.PIN code request
				2.Call barring service
				3.Fixed dialling
				4.Closed User group
				5.Phone security
				6.Change access codes
				""")
				security_settings = int(input('Enter Security Options  :'))
				match security_settings :
					case 1:
						print('PIN code request')
					case 2:
						print('Call barring service')
					case 3:
						print('Fixed dialling')
					case 4:
						print('Closed User group')
					case 5:
						print('Phone security')
					case 6:
						print('Change access codes')
					
					case _: 
						print('Enter Correct input')
					
			case 4:
				print('Restore Factory Settings')
			
			case _: 
				print('Enter Correct input')
	case 7:
		print('Call Divert')
	case 8:
		print('Games.')
	case 9: 
		print('Calculator.')
	case 10: 
		print('Reminders.')
	case 11:
		print("""
		1.Alarm Clock.
		2. Clock settings
		3. Date Settings
		4. Stopwatch.
		5. Countdown timer
		6. Auto update of date and time.
		""")
		clock = int(input('Enter Clock option  :'))
		match clcok :
			case 1:
				print('Alarm Clock.')
			case 2:
				print('Clock settings')
			case 3:
				print('Date Settings')
			case 4:
				print('Stopwatch.')
			case 5:
				print('Countdown timer')
			case 6:
				print('Countdown timer')
			case _: 
				print('Enter Correct input')
	case 12:
		print('Profiles')
	case 13:
		print('SIM Services.')
	case _: 
		print('Enter Correct input')
	










