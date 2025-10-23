import random

# List of possible words for the Hangman game
words = [
    "apple", "banana", "orange", "grape", "mango", "pineapple", "watermelon", 
    "strawberry", "blueberry", "kiwi", "papaya", "peach", "cherry", 
    "coconut", "dragonfruit", "melon", "blackberry", "lemon"
]

# Dictionary representing the hangman stages
hangman_art = {
    0: ("   ",
        "DEATH",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        " |\\",
        "   "),
    4: (" o ",
        "/|\\ ",
        "   "),
    5: (" o ",
        "/|\\ ",
        "/  "),
    6: (" o ",
        "/|\\ ",
        "/ \\"),
}


"""
🎮 Hangman Game
A simple word guessing game where you try to reveal the hidden word
before the hangman is complete.
"""

def main():
    """
    Main function for the Hangman Game.
    Handles word selection, difficulty level, and game loop.
    """

    # List to store words that match the selected difficulty
    words_selection = []

    # Difficulty levels
    print("\nDifficulty levels: ")
    print("1️⃣   Easy")
    print("2️⃣   Medium")
    print("3️⃣   Hard")
    
    # Ask user for difficulty selection
    difficulty_selection = input("\nEnter your choice (1, 2, 3): ").strip()
    if difficulty_selection not in ("1", "2", "3"):
        print("⚠️  Invalid input! Defaulting to Medium level")
        difficulty_selection = "2"
        
    # Filter words based on difficulty
    if difficulty_selection == "1":
        for x in range(len(words)):
            if len(words[x]) <= 5:
                words_selection.append(words[x])
                
    elif difficulty_selection == "2":
        for x in range(len(words)):
            if len(words[x]) > 5 and len(words[x]) <= 8:
                words_selection.append(words[x])
                
    else:
        for x in range(len(words)):
            if len(words[x]) > 8:
                words_selection.append(words[x])
    
    # Prevent error if no words are found for the chosen difficulty
    if not words_selection:
        print("⚠️  No words available for this difficulty level.")
        return

    # Choose a random word from the filtered list
    word = random.choice(words_selection)
    underscore_words = ["_"] * len(word)
    guessed_word = []
    attempts = 6
    wrong_attempts = 6
    
    # Game loop
    while attempts > 0:
        print("_" * len(word))
        for x in hangman_art[wrong_attempts]:
            print(x)
        
        print("_" * len(word))
        print("\n")
        print(" ".join(underscore_words))
        
        # User input
        user_guess = input("\nGuess a letter: ").strip().lower()
        
        # Input validation
        if not user_guess.isalpha():
            print("Sorry, you can't input a number!")
            print("Try again!")
            continue
        
        if len(user_guess) != 1:
            print("You can only input one letter!")
            print("Try again!")
            continue
        
        if user_guess in guessed_word:
            print("You already guessed that letter.")
            print("Try again!")
            continue
        
        guessed_word.append(user_guess)
        
        # Check if the guessed letter is in the word
        if user_guess in word:
            for i in range(len(word)):
                if word[i] == user_guess:
                    underscore_words[i] = user_guess
            print("Correct (✅)")
        else:
            attempts -= 1
            wrong_attempts -= 1
            if attempts != 0:    
                print(f"Wrong (❌), you have {attempts} attempt(s) left.")
            
        # Win condition
        if "_" not in underscore_words:
            print("_" * len(word))
            for x in hangman_art[wrong_attempts]:
                print(x)
            print("_" * len(word))
            print(f"\n🎉 Congratulations! You guessed the word: {word}")
            print("🏆 You win!\n")
            break
        
    # Lose condition
    else:
        print("_" * len(word))
        for x in hangman_art[wrong_attempts]:
            print(x)
        print("_" * len(word))
        print("\n💀 Game Over!")
        print(f"The word was {word}\n")
        

if __name__ == "__main__":
    main()