import random

# Word list for the Hangman game
words = [
    "plastic", "journey", "worship", "caption", "vampire",
    "flaming", "kitchen", "sandbox", "treacle", "founder",
    "bracket", "harmful", "digitsy", "cupcake", "joyment",
    "harvest", "twinkle", "sandbox", "lighten", "foreman", "adventure", "paintwork", "formulate", "submarine", "vibration",
    "wonderful", "blackouts", "marketing", "currency", "adjective",
    "framework", "polygonal", "secluding", "vocalizer", "drumstick",
    "turbofan", "landpiece", "patchwork", "minotaur", "volcanist", "backgrounds", "documentary", "journalistic", "countervails", "volunteering",
    "exclusionary", "flamethrower", "brainwashed", "pseudomythic", "unforgivable",
    "mastercoding", "configurable", "predictalism", "harmonizable", "unexploited",
    "fractogenous", "diplomancer", "adventurous", "reclaimghost", "touchingware"
]

# Hangman display stages based on remaining attempts
hangman_art = {
    9: ("       ",
        "       ",
        "|      ",
        "|      ",
        "|      ",
        "|      "),
    8: ("       ",
        "|/     ",
        "|      ",
        "|      ",
        "|      ",
        "|      "),
    7: ("______ ",
        "|/     ",
        "|      ",
        "|      ",
        "|      ",
        "|      "),
    6: ("______ ",
        "|/  |  ",
        "|      ",
        "|      ",
        "|      ",
        "|      "),
    5: ("______ ",
        "|/  |  ",
        "|   o  ",
        "|      ",
        "|      ",
        "|      "),
    4: ("______ ",
        "|/  |  ",
        "|   o  ",
        "|  /   ",
        "|      ",
        "|      "),
    3: ("______ ",
        "|/  |  ",
        "|   o  ",
        "|  /|  ",
        "|      ",
        "|      "),
    2: ("______ ",
        "|/  |  ",
        "|   o  ",
        "|  /|\\",
        "|      ",
        "|      "),
    1: ("______ ",
        "|/  |  ",
        "|   o  ",
        "|  /|\\",
        "|  /   ",
        "|      "),
    0: ("______ ",
        "|/  |  ",
        "|   o  ",
        "|  /|\\",
        "|  / \\",
        "|      "),
    
}


"""
🎮 Hangman Game
A simple word guessing game where the player tries to reveal
the hidden word before the hangman is complete.
"""

def main():
    # Prepare word selection list
    words_selection = []

    # Difficulty selection
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
            if len(x) <= 7:
                words_selection.append(x)
    elif difficulty_selection == "2":
        for x in words:
            if 7 < len(x) <= 10:
                words_selection.append(x)
    else:
        for x in words:
            if 10 < len(x) <= 13:
                words_selection.append(x)

    # Stop game if no words match the difficulty
    if not words_selection:
        print("⚠️  No words available for this difficulty level.")
        return

    word = random.choice(words_selection).lower()
    guessed_word = []
    underscore_words = ["_"] * len(word)
    revealed_letters = set()

    # Early hint
    if difficulty_selection == "1":
        while len(revealed_letters) < min(2, len(set(word))):
            random_letter = random.choice(word)
            guessed_word.append(random_letter)
            revealed_letters.add(random_letter)
            
        for letter in revealed_letters:    
            for x in range(len(word)):
                if word[x] == letter:
                    underscore_words[x] = letter
    elif difficulty_selection == "2":
        while len(revealed_letters) < min(1, len(set(word))):
            random_letter = random.choice(word)
            guessed_word.append(random_letter)
            revealed_letters.add(random_letter)
            
        for letter in revealed_letters:    
            for x in range(len(word)):
                if word[x] == letter:
                    underscore_words[x] = letter
    else:
        pass
            
    
    attempts = 9  # Number of incorrect guesses allowed

    # --- Game loop ---
    while attempts > 0:
        print("_" * len(word))
        for x in hangman_art[attempts]:
            print(x)
        
        
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
            print("The letter has been guessed.")
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
