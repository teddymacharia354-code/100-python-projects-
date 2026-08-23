# A simple multiple choice quiz game that keeps score

# Each question is stored as a dictionary with the question, options, and answer
questions = [
    {
        "question": "What does 'print()' do in Python?",
        "options": ["A. Deletes a file", "B. Displays output", "C. Saves a variable"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #"],
        "answer": "C"
    },
    {
        "question": "What data type is the value 'True'?",
        "options": ["A. String", "B. Boolean", "C. Integer"],
        "answer": "B"
    }
]

print("====== Python Quiz Game ======")
print()

score = 0  # Keeps track of correct answers

# Loop through every question in our list
for i, q in enumerate(questions):  # "enumerate" gives us both the position and the item
    print(f"Question {i + 1}: {q['question']}")

    # Show each option on its own line
    for option in q["options"]:
        print(option)

    answer = input("Your answer (A/B/C): ").upper()  # ".upper()" avoids case issues

    if answer == q["answer"]:
        print("Correct!")
        score += 1  # Same as: score = score + 1
    else:
        print(f"Wrong. The correct answer was {q['answer']}.")

    print("-" * 30)

print("=" * 30)
print(f"You scored {score} out of {len(questions)}")
