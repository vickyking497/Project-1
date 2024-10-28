# Basic Quiz Game

def display_question(question):
    """Display the question and its options."""
    print(question["question"])
    for option in question["options"]:
        print(option)

def get_user_answer():
    """Get the user's answer and validate it."""
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        else:
            print("Invalid input. Please enter A, B, C, or D.")

def check_answer(question, user_answer):
    """Check if the user's answer is correct."""
    return user_answer == question["answer"]

def display_final_score(score, total_questions):
    """Display the final score to the user."""
    print(f"\nYour final score is {score}/{total_questions}.")

def main():
    # Define the quiz questions
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
            "answer": "D"
        }
    ]

    score = 0
    total_questions = len(questions)

    # Loop through each question in the quiz
    for question in questions:
        display_question(question)
        user_answer = get_user_answer()
        
        if check_answer(question, user_answer):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {question['answer']}.")

    # Display final score
    display_final_score(score, total_questions)

if __name__ == "__main__":
    main()