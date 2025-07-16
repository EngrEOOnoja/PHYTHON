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
	
menu = int(input(nokia))
match menu :
	case 1:
		phonebook = print("""
			1. Search.
			2. Service Nos.
			3. Add name
			4. Erase.
			5. Edit.
			6. Assign tone.
			7. Send b'card.
			8. Options.
			9. Spped dials.
			10. Voice tags								
					""")
		book = int(input(phonebook))
		match book :
			case 1 :














