(Computer-Assisted Instruction: Difficulty Levels) Modify the previous exercise to
allow the user to enter a difficulty level. At a difficulty level of 1, the program should use
only single-digit numbers in the problems and at a difficulty level of 2, numbers as large
as two digits.

Levels + Varying Responses
import random

def generate_question(difficulty):
    """Generate two random numbers based on the difficulty level."""
    if difficulty == 1:
        return random.randint(1, 9), random.randint(1, 9)
    elif difficulty == 2:
        return random.randint(10, 99), random.randint(10, 99)

def get_feedback(is_correct):
    """Return a random feedback message based on correctness."""
    correct_responses = [
        "Very good!",
        "Nice work!",
        "Keep up the good work!"
    ]
    incorrect_responses = [
        "No. Please try again.",
        "Wrong. Try once more.",
        "No. Keep trying."
    ]
    return random.choice(correct_responses if is_correct else incorrect_responses)

def multiplication_cai():
    print("Welcome to the Multiplication Practice Program!")
    print("Select difficulty level:")
    print("1 - Easy (one-digit numbers)")
    print("2 - Hard (two-digit numbers)")

    # Get difficulty input
    while True:
        try:
            difficulty = int(input("Enter 1 or 2: "))
            if difficulty in (1, 2):
                break
            else:
                print("Please enter either 1 or 2.")
        except ValueError:
            print("Please enter a valid number.")

    print("\nType Ctrl+C or close the window to stop.\n")

    # Main practice loop
    while True:
        a, b = generate_question(difficulty)
        correct_answer = a * b

        while True:
            try:
                user_input = int(input(f"How much is {a} times {b}? "))
                if user_input == correct_answer:
                    print(get_feedback(True) + "\n")
                    break
                else:
                    print(get_feedback(False) + "\n")
            except ValueError:
                print("Please enter a valid number.\n")

# Run the CAI program
multiplication_cai()