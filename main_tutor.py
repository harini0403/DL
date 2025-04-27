import json
import random

def load_questions(file_path=r'C:\Users\nicky\Desktop\adaptive_ai_tutor\questions.json'):
    """
    Load questions from a JSON file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # Specify UTF-8 encoding
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print("❌ Error: Questions file not found.")
        return []
    except json.JSONDecodeError:
        print("❌ Error: Failed to decode JSON file.")
        return []

def ask_question(questions, current_difficulty):
    """
    Ask a question based on the current difficulty level.
    """
    if not questions:
        print("⚠️ No questions available.")
        return current_difficulty

    # Filter questions by difficulty
    filtered_questions = [q for q in questions if q["difficulty"] == current_difficulty]
    if not filtered_questions:
        print(f"⚠️ No questions available for difficulty level: {current_difficulty}.")
        return current_difficulty

    question = random.choice(filtered_questions)
    print(f"\n🧠 Difficulty: {current_difficulty}")
    print("🧠 Question:")
    print(question["question"])
    for option in question["options"]:
        print(option)

    user_answer = input("\nYour answer (e.g., a, b, c, d): ").strip().lower()
    if user_answer == question["answer"]:
        print("✅ Correct!")
        print("💡 Tip: Great job! Keep up the good work.")
        feedback = 1  # Correct answer
    else:
        print(f"❌ Incorrect. The correct answer is: {question['answer']}")
        print(f"💡 Tip: {question.get('tip', 'Review the related topic for better understanding.')}")
        feedback = 0  # Incorrect answer

    # Adjust difficulty based on feedback
    difficulty_map = {"easy": "medium", "medium": "hard", "hard": "medium"}
    if feedback == 1:  # Correct answer
        next_difficulty = difficulty_map.get(current_difficulty, "medium")
    else:  # Incorrect answer
        reverse_difficulty_map = {"medium": "easy", "hard": "medium"}
        next_difficulty = reverse_difficulty_map.get(current_difficulty, "easy")

    # Display the next predicted difficulty level
    print(f"\n🔮 The next question will be at '{next_difficulty}' difficulty.")

    return next_difficulty

def main():
    print("Welcome to the Adaptive AI Tutor!")

    # Load questions from JSON
    questions = load_questions(
        r'C:\Users\nicky\Desktop\adaptive_ai_tutor\questions.json')  # Adjust the path if needed

    if not questions:
        print("⚠️ No questions loaded. Exiting.")
        return

    # Start with an initial difficulty level
    current_difficulty = "easy"

    while True:
        # Ask a question and get the next difficulty level
        current_difficulty = ask_question(questions, current_difficulty)

        # Exit option
        choice = input("\n❓ Do you want to answer another question? (y/n): ").strip().lower()
        if choice != 'y':
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    main()