(Computer-Assisted Instruction: Reducing Student Fatigue) Varying the computer’s responses can help hold the student’s attention. Modify the previous exercise so that
various comments are displayed for each answer. Possible responses to a correct answer
should include 'Very good!', 'Nice work!' and 'Keep up the good work!' Possible responses to an incorrect answer should include 'No. Please try again.', 'Wrong. Try
once more.' and 'No. Keep trying.' Choose a number from 1 to 3, then use that value
to select one of the three appropriate responses to each correct or incorrect answer.


import random

def generate_one_digit_question():
    """Return a tuple of two random one-digit positive integers (1 to 9)."""
    return random.randint(1, 9), random.randint(1, 9)

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

    if is_correct:
        return random.choice(correct_responses)
    else:
        return random.choice(incorrect_responses)

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
                    print(get_feedback(True) + "\n")
                    break  # Go to next question
                else:
                    print(get_feedback(False) + "\n")
            except ValueError:
                print("Please enter a valid number.\n")

# Run the program
multiplication_cai()
?? Sample Output (With Random Responses)
pgsql
Copy code
How much is 3 times 6? 18
Nice work!

How much is 7 times 8? 56
Keep up the good work!

How much is 4 times 9? 33
Wrong. Try once more.

How much is 4 times 9? 36
Very good!
? Summary of Enhancements:
Randomized, encouraging responses keep the student motivated.

Script is still simple and kid-friendly.

Can run continuously without boredom from repetition.

Let me know if you'd li




