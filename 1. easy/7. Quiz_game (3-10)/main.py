#Quiz game
import random

def get_quiz_questions():
    return [
        {
            "question": "What does CPU stand for?",
            "A": "Central Processing Unit",
            "B": "Computer Personal Unit",
            "C": "Central Program Utility",
            "D": "Control Processing User",
            "answer": "A"
        },
        {
            "question": "Which language is mainly used for web development?",
            "A": "Python",
            "B": "HTML",
            "C": "C++",
            "D": "Java",
            "answer": "B"
        },
        {
            "question": "What is the result of 5 + 3 * 2?",
            "A": "16",
            "B": "11",
            "C": "13",
            "D": "10",
            "answer": "B"
        },
        {
            "question": "Which device is used to display output?",
            "A": "Keyboard",
            "B": "Mouse",
            "C": "Monitor",
            "D": "Scanner",
            "answer": "C"
        },
        {
            "question": "What does RAM stand for?",
            "A": "Read Access Memory",
            "B": "Random Access Memory",
            "C": "Run Access Machine",
            "D": "Random Application Memory",
            "answer": "B"
        },
        {
            "question": "Which of these is an operating system?",
            "A": "Python",
            "B": "Windows",
            "C": "Google",
            "D": "HTML",
            "answer": "B"
        },
        {
            "question": "What symbol is used to comment in Python?",
            "A": "//",
            "B": "#",
            "C": "/* */",
            "D": "<!-- -->",
            "answer": "B"
        },
        {
            "question": "Which data type stores True or False?",
            "A": "int",
            "B": "string",
            "C": "bool",
            "D": "float",
            "answer": "C"
        },
        {
            "question": "What does AI stand for?",
            "A": "Automatic Interface",
            "B": "Artificial Intelligence",
            "C": "Advanced Internet",
            "D": "Applied Information",
            "answer": "B"
        },
        {
            "question": "Which loop repeats a fixed number of times?",
            "A": "while",
            "B": "if",
            "C": "for",
            "D": "switch",
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "A": "Earth",
            "B": "Mars",
            "C": "Jupiter",
            "D": "Venus",
            "answer": "B"
        },
        {
            "question": "What does URL stand for?",
            "A": "Uniform Resource Locator",
            "B": "Universal Register Link",
            "C": "User Resource Location",
            "D": "Unified Routing Link",
            "answer": "A"
        },
        {
            "question": "Which file extension is used for Python files?",
            "A": ".java",
            "B": ".cpp",
            "C": ".py",
            "D": ".html",
            "answer": "C"
        },
        {
            "question": "What keyword is used to define a function in Python?",
            "A": "func",
            "B": "define",
            "C": "def",
            "D": "function",
            "answer": "C"
        },
        {
            "question": "Which device is used to input text?",
            "A": "Monitor",
            "B": "Speaker",
            "C": "Keyboard",
            "D": "Printer",
            "answer": "C"
        },
        {
            "question": "What is the opposite of 'increase'?",
            "A": "Grow",
            "B": "Expand",
            "C": "Decrease",
            "D": "Rise",
            "answer": "C"
        },
        {
            "question": "Which number is a prime number?",
            "A": "4",
            "B": "6",
            "C": "9",
            "D": "7",
            "answer": "D"
        },
        {
            "question": "What does GPU stand for?",
            "A": "General Processing Unit",
            "B": "Graphical Performance Utility",
            "C": "Graphics Processing Unit",
            "D": "Graph Program Unit",
            "answer": "C"
        },
        {
            "question": "Which one is a programming language?",
            "A": "Python",
            "B": "Chrome",
            "C": "Windows",
            "D": "Linux",
            "answer": "A"
        },
        {
            "question": "What keyword is used to check a condition?",
            "A": "loop",
            "B": "if",
            "C": "print",
            "D": "def",
            "answer": "B"
        },
        {
            "question": "What is 10 squared?",
            "A": "20",
            "B": "100",
            "C": "50",
            "D": "10",
            "answer": "B"
        },
        {
            "question": "Which of these is a web browser?",
            "A": "Python",
            "B": "VS Code",
            "C": "Google Chrome",
            "D": "Linux",
            "answer": "C"
        },
        {
            "question": "What does HTTP stand for?",
            "A": "HyperText Transfer Protocol",
            "B": "High Text Transfer Program",
            "C": "Hyper Tool Transfer Protocol",
            "D": "Host Text Transport Program",
            "answer": "A"
        },
        {
            "question": "Which symbol is used for multiplication?",
            "A": "+",
            "B": "-",
            "C": "*",
            "D": "/",
            "answer": "C"
        },
        {
            "question": "What is the first month of the year?",
            "A": "February",
            "B": "January",
            "C": "March",
            "D": "December",
            "answer": "B"
        },
        {
            "question": "Which one is NOT a data type in Python?",
            "A": "int",
            "B": "float",
            "C": "char",
            "D": "string",
            "answer": "C"
        },
        {
            "question": "What is used to store multiple values in Python?",
            "A": "Variable",
            "B": "List",
            "C": "Function",
            "D": "Loop",
            "answer": "B"
        },
        {
            "question": "What does 'bug' mean in programming?",
            "A": "A feature",
            "B": "A hardware device",
            "C": "An error",
            "D": "A database",
            "answer": "C"
        },
        {
            "question": "Which operator checks equality?",
            "A": "=",
            "B": "!=",
            "C": "==",
            "D": "<=",
            "answer": "C"
        },
        {
            "question": "Which one is an IDE?",
            "A": "Python",
            "B": "VS Code",
            "C": "HTML",
            "D": "CPU",
            "answer": "B"
        }
    ]

def configure_difficulty():
        print("\n")
        print("1️⃣   Easy   : 5 Questions")
        print("2️⃣   Medium : 10 Questions")
        print("3️⃣   Hard   : 20 Questions")
        
        difficulty_configuration = input("\nWhich difficulty would you like to choose: ").lower().strip()
        
        questions = get_quiz_questions()
        random.shuffle(questions)
        
        if difficulty_configuration in ["easy", "1"]:
            return questions[:5]
        elif difficulty_configuration in ["medium", "2"]:
            return questions[:10]
        elif difficulty_configuration in ["hard", "3"]:
            return questions[:20]
        else:
            print("⚠️  Invalid input! Defaulting to Medium level.")
            return questions[:10]

def run_quiz():
    user_score = 0
    number = 1
    
    #Print out Question
    questions = configure_difficulty()
    total_questions = len(questions)
    
    for question in questions:
        for x, y in question.items():
            if x == "question":
                print(f"\n{number}. {y}")
                number += 1
            elif x == "answer":
                continue
            else:
                print(f"{x}). {y}")
            
        #User input
        user_answer = input("\nInput your answer? (A, B, C, D): ").upper().strip()
        while user_answer not in ["A", "B", "C", "D"]:
            print("\nInvalid choice. Choose A, B, C, or D.")
            user_answer = input("Input your answer? (A, B, C, D): ").upper().strip()
        if user_answer == question["answer"]:
            print("Correct!")
            user_score += 1
        else:
            print(f"Wrong! The answer was {question['answer']}")
    
    return user_score, total_questions       
    
            
def show_results(user_score, total_questions):
    print(f"\nYou scored {user_score} out of {total_questions}")
    percentage = (user_score / total_questions) * 100
    print(f"Accuracy: {percentage:.2f}%")


def main():
    while True:
        score, total = run_quiz()
        show_results(score, total)
        replay_system = input("\nPlay again? (y/n): ").strip().lower()
        while replay_system not in ["yes", "y", "no", "n"]:
            print("Invalid input. Choose between (y/n).")
            replay_system = input("Play again? (y/n): ").strip().lower()
        if replay_system in ["yes", "y"]:
            continue
        else:
            print("Thank you for playing!")
            break
                
    
    
if __name__ == "__main__":
    main()