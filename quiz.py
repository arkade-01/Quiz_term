import PyPDF2
import random
import os
from typing import List, Dict, Tuple

class QuizGame:
    def __init__(self, pdf_path: str):
        self.pdf_path = os.path.abspath(pdf_path)
        print(f"Loading quiz from: {self.pdf_path}")
        self.questions = self.extract_questions_from_pdf()
        self.score = 0
        self.total_questions = len(self.questions)
        print(f"Loaded {self.total_questions} questions")

    def extract_questions_from_pdf(self) -> List[Dict]:
        questions = []
        current_question = None
        
        try:
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                print(f"PDF loaded successfully. Number of pages: {len(pdf_reader.pages)}")
                
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    lines = text.split('\n')
                    
                    for line in lines:
                        line = line.strip()
                        if not line:
                            continue
                            
                        # Start of a new question
                        if not line.startswith(('A)', 'B)', 'C)', 'D)', 'Answer:')):
                            if current_question and current_question['options'] and current_question['correct']:
                                questions.append(current_question)
                            current_question = {
                                'question': line,
                                'options': {},
                                'correct': None
                            }
                        # Option line
                        elif line.startswith(('A)', 'B)', 'C)', 'D)')):
                            if current_question:
                                option_letter = line[0]
                                option_text = line[2:].strip()
                                current_question['options'][option_letter] = option_text
                        # Answer line
                        elif line.startswith('Answer:'):
                            if current_question:
                                current_question['correct'] = line.split(':')[1].strip()

                # Add the last question
                if current_question and current_question['options'] and current_question['correct']:
                    questions.append(current_question)
                    
                print(f"Successfully parsed {len(questions)} questions")
                
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return []
            
        return questions

    def display_question(self, question: Dict) -> None:
        """Display a single question with its options."""
        print("\n" + "="*50)
        print(f"\nQuestion: {question['question']}")
        print("\nOptions:")
        for letter, text in sorted(question['options'].items()):
            print(f"{letter}) {text}")

    def get_user_answer(self) -> str:
        """Get and validate user input."""
        while True:
            answer = input("\nYour answer (A/B/C/D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                return answer
            print("Invalid input! Please enter A, B, C, or D.")

    def run_quiz(self) -> None:
        """Run the main quiz loop."""
        if not self.questions:
            print("No questions found in the PDF!")
            return

        print("\nWelcome to the Quiz Game!")
        print(f"There are {self.total_questions} questions in total.")
        input("Press Enter to start...")

        # Shuffle questions for randomization
        random.shuffle(self.questions)

        for i, question in enumerate(self.questions, 1):
            self.display_question(question)
            user_answer = self.get_user_answer()
            
            if user_answer == question['correct']:
                print("\n✓ Correct!")
                self.score += 1
            else:
                print(f"\n✗ Wrong! The correct answer was {question['correct']}")
            
            print(f"Current score: {self.score}/{i}")
            
            if i < self.total_questions:
                input("\nPress Enter for the next question...")

        self.display_final_results()

    def display_final_results(self) -> None:
        """Display the final quiz results."""
        print("\n" + "="*50)
        print("\nQuiz Complete!")
        print(f"Final Score: {self.score}/{self.total_questions}")
        percentage = (self.score / self.total_questions) * 100
        print(f"Percentage: {percentage:.1f}%")
        
        if percentage >= 90:
            print("Excellent performance! 🌟")
        elif percentage >= 70:
            print("Good job! 👍")
        elif percentage >= 50:
            print("Not bad! Keep practicing! 💪")
        else:
            print("You might want to review the material again! 📚")

def main():
    while True:
        pdf_path = input("\nEnter the path to your quiz PDF file: ").strip()
        
        # Remove any surrounding quotes if present
        pdf_path = pdf_path.strip("'").strip('"')
        
        # Expand user directory if path starts with ~
        if pdf_path.startswith('~'):
            pdf_path = os.path.expanduser(pdf_path)
            
        # Convert to absolute path
        pdf_path = os.path.abspath(pdf_path)
        
        if not os.path.exists(pdf_path):
            print(f"File not found! Tried to access: {pdf_path}")
            print("Please check the path and try again.")
            continue
            
        if not pdf_path.lower().endswith('.pdf'):
            print("Please provide a PDF file!")
            continue
            
        break

    quiz = QuizGame(pdf_path)
    quiz.run_quiz()

if __name__ == "__main__":
    main()