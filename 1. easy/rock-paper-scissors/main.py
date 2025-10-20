import random

def compare(x, y):
    """Compare user choice and bot choice, return result message."""
    if x == y:
        return "It's a tie 👏"
    
    winning_cases = {
        ("r", "s"),
        ("p", "r"),
        ("s", "p")
    }
    
    if (x, y) in winning_cases:
        return "You win 🥇"
    else:
        return "You lose 😢"


def rock_paper_scissors():
    """Main game logic."""
    choices = ["r", "p", "s"]
    bot_choice = random.choice(choices)
    
    user_input = input("\nChoose Rock (R) / Paper (P) / Scissors (S): ").lower()
    while user_input not in choices:
        print("Invalid input! Please enter R, P, or S.")
        user_input = input("\nChoose Rock (R) / Paper (P) / Scissors (S): ").lower()
    
    result = compare(user_input, bot_choice)
    print(f"\n{result}, user: ({user_input.upper()}), bot: ({bot_choice.upper()})\n")


def main():
    """Main loop for playing multiple rounds."""
    while True:
        rock_paper_scissors()
        play_again = input("Play again? (y/n): ").lower()
        if play_again not in ["y", "yes"]:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
