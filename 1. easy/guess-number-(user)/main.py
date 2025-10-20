import random

def guess_num(max_number, max_attempt):    
    print("🎯 Welcome to the Number Guessing Game!")
    print("Try to guess the correct number before you run out of attempts.\n")

    correct_num = random.randint(1, max_number)
    attempt = max_attempt

    while attempt != 0:
        try:    
            user_guess = int(input(f"\nGuess the number from scale (1-{max_number}): "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue
                
        # check if guess is out of range
        if user_guess > max_number or user_guess < 1:
            print("❗ Number out of range, try again.")
            continue
                
        # compare guesses    
        if user_guess == correct_num:
            print("🎉 Congratulations! You guessed it right!")
            break
        else:
            attempt -= 1
            if attempt == 0:
                print(f"💀 You lost! The correct number was {correct_num}.")
            else:                           
                print(f"❌ Wrong! You have {attempt} attempt(s) left.")

    print("Thanks for playing!\n")
                    
if __name__ == "__main__":
    guess_num(10, 5)   # max_number = upper limit of range, max_attempt = number of tries
