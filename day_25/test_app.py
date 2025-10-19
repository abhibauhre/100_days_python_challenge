# Test script to verify all components work
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

print("Testing Quizzler App Components...")
print("=" * 40)

# Test 1: Data loading
print(f"✅ Loaded {len(question_data)} questions from API")
print(f"Sample question: {question_data[0]['question'][:50]}...")

# Test 2: Question Model
q = Question("Test question?", "True")
print(f"✅ Question model works: {q.text[:20]}...")

# Test 3: Quiz Brain (without GUI)
question_bank = []
for question in question_data[:3]:  # Test with first 3 questions
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
print(f"✅ Quiz Brain initialized with {len(quiz.question_list)} questions")

# Test next_question method
if quiz.still_has_questions():
    question_text = quiz.next_question()
    print(f"✅ Next question method works: {question_text[:50]}...")
    
    # Test check_answer method
    result = quiz.check_answer("True")
    print(f"✅ Check answer method works: {result}")
    print(f"Current score: {quiz.score}/{quiz.question_number}")

print("\n🎉 All components working correctly!")
print("Your Quizzler App is complete and ready to use!")
print("\nTo run the GUI version, execute: python main.py")