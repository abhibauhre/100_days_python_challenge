from question_model import Question
from data import question_data
from quizbrain import QuizBrain

print("🧠 WELCOME TO THE ULTIMATE TRUE/FALSE QUIZ! 🧠")
print("=" * 50)
print("Answer each question with 'True' or 'False'")
print("Let's see how much you know!")
print("=" * 50)

# Create question bank from the imported data
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)  # Fixed: was question_data instead of question_answer
    question_bank.append(new_question)

# Create quiz object and start the quiz
quiz = QuizBrain(question_bank)  # Fixed: removed unnecessary parameter

# Main quiz loop
while quiz.still_has_questions():
    quiz.next_question()

# Show final results
quiz.final_score()

print("\n🎯 Thanks for playing!")
print("Want to play again? Just run the program again!")
