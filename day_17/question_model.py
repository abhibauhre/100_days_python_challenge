class Question:
    """Models a quiz question with text and answer"""
    
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        
    def __str__(self):
        return f"Question: {self.text}, Answer: {self.answer}"