class QuizBrain:
    """Manages the quiz flow and scoring"""
    
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        """Check if there are more questions in the quiz"""
        return self.question_number < len(self.question_list)
        
    def next_question(self):
        """Ask the next question and get user input"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        """Check if user's answer is correct and update score"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right! ✅")
        else:
            print("That's wrong! ❌")
        
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n" + "-" * 50 + "\n")
    
    def final_score(self):
        """Display final quiz results"""
        print("🎉 QUIZ COMPLETED! 🎉")
        print(f"Your final score was: {self.score}/{self.question_number}")
        
        # Calculate percentage
        percentage = round((self.score / self.question_number) * 100)
        print(f"Percentage: {percentage}%")
        
        # Give feedback based on score
        if percentage >= 80:
            print("🏆 Excellent! You're a quiz master!")
        elif percentage >= 60:
            print("👍 Good job! Well done!")
        elif percentage >= 40:
            print("📚 Not bad, but you can do better!")
        else:
            print("💪 Keep studying and try again!")
