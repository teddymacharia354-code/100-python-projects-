# A program that calculates an average grade and assigns a letter grade

print("====== Grade Calculator ======")

# Ask how many scores the user wants to enter
num_scores = int(input("How many scores do you want to enter? "))

scores = []  # An empty list to store each score

# Collect each score from the user
for i in range(num_scores):
    score = float(input(f"Enter score {i + 1}: "))
    scores.append(score)  # Add this score to our list

# Calculate the average: total of all scores divided by how many there are
average = sum(scores) / len(scores)

# Decide the letter grade based on the average
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print("=" * 30)
print(f"Average score: {average:.2f}")  # ":.2f" rounds to 2 decimal places
print(f"Letter grade: {letter_grade}")
