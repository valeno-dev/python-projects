import random

# Word list for the Hangman game
words = [
    "apple", "banana", "orange", "grape", "mango", "pineapple", "watermelon", 
    "strawberry", "blueberry", "kiwi", "papaya", "peach", "cherry", 
    "coconut", "dragonfruit", "melon", "blackberry", "lemon"
]

# Hangman display stages based on remaining attempts
hangman_art = {
    6: (" o ",
        "/|\\ ",
        "/ \\"),
    5: (" o ",
        "/|\\ ",
        "/  "),
    4: (" o ",
        "/|\\ ",
        "   "),
    3: (" o ",
        " |\\",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    0: ("   ",
        "DEATH",
        "   "),
}


"""
🎮 Hangman Game
A simple word guessing game where the player tries to reveal
the hidden word before the hangman is complete.
"""

def main():
    # Prepare word selection list
    words_selection = []

    # --- Difficulty selection ---
    print("\nDifficulty levels: ")
    print("1️⃣   Easy")
    print("2️⃣   Medium")
    print("3️⃣   Hard")
    
    difficulty_selection = input("\nEnter your choice (1, 2, 3): ").strip()
    if difficulty_selection not in ("1", "2", "3"):
        print("⚠️  Invalid input! Defaulting to Medium level.")
        difficulty_selection = "2"
        
    # Filter words based on difficulty level
    if difficulty_selection == "1":
        for x in words:
            if len(x) <= 5:
                words_selection.append(x)
    elif difficulty_selection == "2":
        for x in words:
            if 5 < len(x) <= 8:
                words_selection.append(x)
    else:
        for x in words:
            if len(x) > 8:
                words_selection.append(x)
    
    # Stop game if no words match the difficulty
    if not words_selection:
        print("⚠️  No words available for this difficulty level.")
        return

    word = random.choice(words_selection)
    underscore_words = ["_"] * len(word)
    guessed_word = []
    attempts = 6  # Number of incorrect guesses allowed
    
    # --- Game loop ---
    while attempts > 0:
        print("_" * len(word))
        for x in hangman_art[attempts]:
            print(x)
        print("_" * len(word))
        print("\n" + " ".join(underscore_words))
        
        user_guess = input("\nGuess a letter: ").strip().lower()
        
        # Input validation
        if not user_guess.isalpha():
            print("Sorry, you can't input a number!")
            continue
        if len(user_guess) != 1:
            print("You can only input one letter!")
            continue
        if user_guess in guessed_word:
            print("You already guessed that letter.")
            continue
        
        guessed_word.append(user_guess)
        
        # Correct guess
        if user_guess in word:
            for i in range(len(word)):
                if word[i] == user_guess:
                    underscore_words[i] = user_guess
            print("Correct (✅)")
        
        # Wrong guess
        else:
            attempts -= 1
            if attempts != 0:
                print(f"Wrong (❌), you have {attempts} attempt(s) left.")
            
        # Win condition
        if "_" not in underscore_words:
            print("_" * len(word))
            for x in hangman_art[attempts]:
                print(x)
            print("_" * len(word))
            print(f"\n🎉 Congratulations! You guessed the word: {word}")
            print("🏆 You win!\n")
            break
        
    # Lose condition
    else:
        print("_" * len(word))
        for x in hangman_art[attempts]:
            print(x)
        print("_" * len(word))
        print("\n💀 Game Over!")
        print(f"The word was {word}\n")
        

if __name__ == "__main__":
    main()