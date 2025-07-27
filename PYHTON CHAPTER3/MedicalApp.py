medical = print("""
	What is You problem???
	1. Enter.






""")
ignore = input("Enter Your Problem")
print('press 1 to Enter')
diagnosis = int(input())
match diagnosis:
	case 1:
		print("""Have you had this problem before?
			1. YES.
			2. NO. 
					""")
		option = int(input())
		match option:
			case 1:
				print("Then You have it again.")
			case 2:
				print("Then You have it now.")