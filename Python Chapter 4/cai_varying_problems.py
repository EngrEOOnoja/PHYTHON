(Computer-Assisted Instruction: Varying the Types of Problems) Modify the previous exercise to allow
 the user to pick a type of arithmetic problem to study—1 means addition problems only, 2 means subtraction problems only, 3 means multiplication
problems only, 4 means division problems only (avoid dividing by 0) and 5 means a random mixture of all these types.



import random

def generate_numbers(difficulty):
    """Return two random numbers based on difficulty."""
    if difficulty == 1:
        return random.randint(1, 9), random.randint(1, 9)
    else:
        return random.randint(10, 99), random.randint(10, 99)

def get_feedback(is_correct):
    """Return random feedback based on correctness."""
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

def generate_problem(problem_type, difficulty):
    """Generate a problem based on the selected type."""
    if problem_type == 5:
        problem_type = random.randint(1, 4)

    a, b = generate_numbers(difficulty)

    if problem_type == 1:  # Addition
        question = f"How much is {a} plus {b}? "
        answer = a + b

    elif problem_type == 2:  # Subtraction
        # Ensure non-negative result
        a, b = max(a, b), min(a, b)
        question = f"How much is {a} minus {b}? "
        answer = a - b

    elif problem_type == 3:  # Multiplication
        question = f"How much is {a} times {b}? "
        answer = a * b

    elif problem_type == 4:  # Division
        # Ensure whole number division, no zero divisor
        answer = random.randint(1, 9 if difficulty == 1 else 12)
        b = random.randint(1, 9 if difficulty == 1 else 12)
        a = answer * b
        question = f"How much is {a} divided by {b}? "
        # a is divisible by b; answer = a / b

    return question, answer

def cai_program():
    print("Welcome to the Arithmetic Practice Program!\n")

    # Get difficulty level
    while True:
        try:
            difficulty = int(input("Select difficulty (1 = 1-digit, 2 = 2-digit): "))
            if difficulty in (1, 2):
                break
            else:
                print("Please enter 1 or 2.")
        except ValueError:
            print("Enter a valid number.")

    # Get problem type
    print("\nSelect the type of arithmetic problems:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Random mixture")

    while True:
        try:
            problem_type = int(input("Enter 1–5: "))
            if problem_type in range(1, 6):
                break
            else:
                print("Please enter a number from 1 to 5.")
        except ValueError:
            print("Enter a valid number.")

    print("\nType Ctrl+C to stop at any time.\n")

    # Main practice loop
    while True:
        question, correct_answer = generate_problem(problem_type, difficulty)

        while True:
            try:
                user_input = input(question)
                user_answer = int(user_input)

                if user_answer == correct_answer:
                    print(get_feedback(True) + "\n")
                    break  # Move to next problem
                else:
                    print(get_feedback(False) + "\n")
            except ValueError:
                print("Please enter a valid number.\n")

# Start the CAI program
cai_program()











