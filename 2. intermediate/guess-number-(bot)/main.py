import random

def guess_num_bot(max_number, max_attempt):
    """
    🎯 Let the bot try to guess the number you're thinking of.

    The bot will attempt to guess a number between 1 and `max_number`.
    After each guess, you must tell the bot if its guess was correct,
    too high, or too low. The bot continues until it either guesses correctly
    or runs out of attempts.

    Parameters:
        max_number (int): The upper limit of the number range (e.g., 100).
        max_attempt (int): The maximum number of guesses the bot can make.

    Returns:
        None
    """
    
    print(f"\n🎯 Think of a number between 1 and {max_number}, and I will try to guess it!")
    print(f"🤖 I have {max_attempt} attempts to guess your number! After each guess, tell me if I'm too high or too low!\n")
    print("1️⃣  Random Mode (guess randomly each time)")
    print("2️⃣  Smart Mode (binary search)\n")
    
    #ask user for mode selection
    mode_selection = input("Enter your choice (1 or 2): ").strip()
    
    if mode_selection not in ("1", "2"):
        print("⚠️ Invalid choice! Defaulting to Smart Mode.")
        mode_selection = "2"
        
    low = 1
    high = max_number
    attempt = max_attempt

    while attempt > 0:
        # prevent invalid range
        if low > high:
            print("⚠️ Hmm, your hints seem inconsistent. Let's stop here!")
            break
        
        # select guessing method based on mode
        if mode_selection == "1":
            guess = random.randint(low, high)
        else:
            guess = (low + high) // 2
        
        print("-" * 40)
        print(f"\nMy guess is: {guess}")
        
        checking = input("Is it correct? (yes/no): ").strip().lower()

        # if bot guessed it right
        if checking == "yes" or checking == "y":
            print("🎉 Yay! I got it!")
            return
        
        # if bot guessed it wrong
        elif checking == "no" or checking == "n":
            attempt -= 1
            hint = input("Too low (L) or too high (H)? ").strip().lower()

            # adjust guessing range
            if hint == "l":
                low = guess + 1
            elif hint == "h":
                high = guess - 1
            else:
                print("⚠️ Please enter only L or H.")
                continue

            if attempt > 0:
                print(f"I've {attempt} attempt(s) left 🤔")
        else:
            print("⚠️ Please answer only 'yes' or 'no'.")
            
    # if bot runs out of attempts
    else:
        print("\n💀 I couldn’t guess your number... You win!")
        print("Thanks for playing! 👋")

if __name__ == "__main__":
    guess_num_bot(100, 7) #max_number to guess, max attempt to have


