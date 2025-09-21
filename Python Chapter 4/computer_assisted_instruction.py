(Computer-Assisted Instruction) Computer-assisted instruction (CAI) refers to the
use of computers in education. Write a script to help an elementary school student learn
multiplication. Create a function that randomly generates and returns a tuple of two pos
itive one-digit integers. Use that function’s result in your script to prompt the user with a
question, such as
How much is 6 times 7?
For a correct answer, display the message "Very good!" and ask another multiplication
question. For an incorrect answer, display the message "No. Please try again." and let
the student try the same question repeatedly until the student finally gets it right.



import random

def generate_one_digit_question():
    """Return a tuple of two random one-digit positive integers (1 to 9)."""
    return random.randint(1, 9), random.randint(1, 9)

def multiplication_cai():
    print("Welcome to the Multiplication Practice Program!")
    print("Type Ctrl+C or close the window to stop.\n")

    while True:
        a, b = generate_one_digit_question()
        correct_answer = a * b

        while True:
            try:
                user_input = int(input(f"How much is {a} times {b}? "))
                if user_input == correct_answer:
                    print("Very good!\n")
                    break  # Go to next question
                else:
                    print("No. Please try again.\n")
            except ValueError:
                print("Please enter a valid number.\n")

# Start the program
multiplication_cai()
