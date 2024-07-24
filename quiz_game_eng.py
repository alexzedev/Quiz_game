import random

class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the unit of force in the SI system?",
                "answer": "Newton",
                "options": ["Joule", "Watt", "Newton", "Pascal"]
            },
            {
                "question": "Which of the following is not a fundamental force in physics?",
                "answer": "Friction",
                "options": ["Gravity", "Electromagnetic force", "Weak nuclear force", "Friction"]
            },
            {
                "question": "What does the Kelvin scale measure?",
                "answer": "Temperature",
                "options": ["Pressure", "Temperature", "Electric current", "Light intensity"]
            },
            {
                "question": "What is the speed of light in vacuum (approximately)?",
                "answer": "300,000 km/s",
                "options": ["150,000 km/s", "200,000 km/s", "250,000 km/s", "300,000 km/s"]
            },
            {
                "question": "Who formulated the theory of relativity?",
                "answer": "Albert Einstein",
                "options": ["Isaac Newton", "Niels Bohr", "Albert Einstein", "Marie Curie"]
            },
            {
                "question": "What is a quantum?",
                "answer": "The smallest discrete unit of energy",
                "options": ["An elementary particle", "The smallest discrete unit of energy", "An electromagnetic wave", "A nuclear force"]
            },
            {
                "question": "What is the unit of electric charge?",
                "answer": "Coulomb",
                "options": ["Ampere", "Volt", "Ohm", "Coulomb"]
            },
            {
                "question": "What does the equation E=mc^2 describe?",
                "answer": "Mass-energy equivalence",
                "options": ["Speed of light", "Gravitational force", "Mass-energy equivalence", "Expansion of the universe"]
            },
            {
                "question": "Which particle is responsible for carrying the electromagnetic force?",
                "answer": "Photon",
                "options": ["Electron", "Proton", "Neutron", "Photon"]
            },
            {
                "question": "What is the acceleration due to gravity on Earth (approximately)?",
                "answer": "9.8 m/s^2",
                "options": ["5.6 m/s^2", "7.2 m/s^2", "9.8 m/s^2", "11.4 m/s^2"]
            }
        ]
        self.score = 0

    def display_welcome(self):
        print("Welcome to the Physics Quiz!")
        print("Answer 10 questions to test your knowledge.")
        print("Good luck!\n")

    def ask_question(self, question):
        print(question["question"])
        random.shuffle(question["options"])
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")
        
        while True:
            try:
                user_answer = int(input("Your answer (1-4): "))
                if 1 <= user_answer <= 4:
                    return question["options"][user_answer - 1]
                else:
                    print("Please choose a number between 1 and 4.")
            except ValueError:
                print("Please enter a number.")

    def run_quiz(self):
        self.display_welcome()
        random.shuffle(self.questions)
        
        for question in self.questions:
            user_answer = self.ask_question(question)
            if user_answer == question["answer"]:
                print("Correct answer!")
                self.score += 1
            else:
                print(f"Sorry, that's not correct. The right answer is: {question['answer']}")
            print(f"Your current score: {self.score}/{len(self.questions)}\n")

        print(f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")
        percentage = (self.score / len(self.questions)) * 100
        print(f"Percentage score: {percentage:.2f}%")

        if percentage >= 80:
            print("Excellent! You're a physics expert!")
        elif percentage >= 60:
            print("Good job! You have solid knowledge of physics.")
        elif percentage >= 40:
            print("Not bad, but there's room for improvement.")
        else:
            print("Looks like you need more study. Don't give up!")

if __name__ == "__main__":
    quiz = QuizGame()
    quiz.run_quiz()