
import random

# =============
# DATA SECTION
# =============

WORDS = [
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

HANGMAN_ART = {
    10: ("      ",
        "       ",
        "       ",
        "       ",
        "       ",
        "       "),
    9: ("       ",
        "       ",
        "|      ",
        "|      ",
        "|      ",
        "|      "),
    8: ("______ ",
        "|      ",
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
        "|   |  ",
        "|      ",
        "|      "),
    3: ("______ ",
        "|/  |  ",
        "|   o  ",
        "|   |\\",
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
        "|    \\",
        "|      "),
    0: ("______ ",
        "|/  |  ",
        "|   o  ",
        "|  /|\\",
        "|  / \\",
        "|      "),
}


# =================
# FUNCTION SECTION
# =================

def display_hangman(attempts: int):
    #Display hangman art according to remaining attempts
    for line in HANGMAN_ART[attempts]:
        print(line)


def show_difficulty_menu():
    #Show difficulty menu
    print("\nDifficulty levels: ")
    print("1️⃣   Easy")
    print("2️⃣   Medium")
    print("3️⃣   Hard")


def select_words_by_difficulty(difficulty: str):
    #Return list of words based on chosen difficulty
    if difficulty == "1":
        return [w for w in WORDS if len(w) <= 7]
    elif difficulty == "2":
        return [w for w in WORDS if 7 < len(w) <= 10]
    elif difficulty == "3":
        return [w for w in WORDS if 10 < len(w) <= 13]
    else:
        print("⚠️  Invalid input! Defaulting to Medium level.")
        return [w for w in WORDS if 7 < len(w) <= 10]


def give_early_hint(difficulty: str, word: str, underscore_words: list, guessed_word: list):
    #Reveal 1–2 letters based on difficulty
    revealed_letters = set()
    if difficulty == "1":
        num_hint = 2
    elif difficulty == "2":
        num_hint = 1
    else:
        num_hint = 0

    while len(revealed_letters) < min(num_hint, len(set(word))):
        letter = random.choice(word)
        revealed_letters.add(letter)
        guessed_word.append(letter)

    for letter in revealed_letters:
        for i, w in enumerate(word):
            if w == letter:
                underscore_words[i] = letter


def validate_input(user_guess: str, guessed_word: list):
    #Validasi player input
    if not user_guess.isalpha():
        print("Sorry, you can't input a number!")
        return False
    if len(user_guess) != 1:
        print("You can only input one letter!")
        return False
    if user_guess in guessed_word:
        print("The letter has been guessed.")
        return False
    return True


def handle_correct_guess(user_guess: str, word: str, underscore_words: list):
    #Update display for correct guess
    for i, letter in enumerate(word):
        if letter == user_guess:
            underscore_words[i] = user_guess
    print("Correct (✅)")


def handle_wrong_guess(attempts: int):
    #Handle wrong guess and reduce attempt count
    attempts -= 1
    if attempts != 0:
        print(f"Wrong (❌), you have {attempts} attempt(s) left.")
    return attempts


def show_game_state(word: str, attempts: int, underscore_words: list):
    #Display hangman and word progress
    print("_" * len(word))
    display_hangman(attempts)
    print("\n" + " ".join(underscore_words))


# ===============
# MAIN GAME LOOP
# ===============

def main():
    print("\n🎮 HANGMAN GAME")
    print("Guess the word before the hangman is complete!\n")

    show_difficulty_menu()
    difficulty = input("\nEnter your choice (1, 2, 3): ").strip()

    words_selection = select_words_by_difficulty(difficulty)
    if not words_selection:
        print("⚠️  No words available for this difficulty level.")
        return

    word = random.choice(words_selection).lower()
    guessed_word = []
    underscore_words = ["_"] * len(word)

    give_early_hint(difficulty, word, underscore_words, guessed_word)

    attempts = 10

    while attempts > 0:
        show_game_state(word, attempts, underscore_words)
        user_guess = input("\nGuess a letter: ").strip().lower()

        if not validate_input(user_guess, guessed_word):
            continue

        guessed_word.append(user_guess)

        if user_guess in word:
            handle_correct_guess(user_guess, word, underscore_words)
        else:
            attempts = handle_wrong_guess(attempts)

        if "_" not in underscore_words:
            show_game_state(word, attempts, underscore_words)
            print(f"\n🎉 Congratulations! You guessed the word: {word}")
            print("🏆 You win!\n")
            break

    else:
        show_game_state(word, attempts, underscore_words)
        print("\n💀 Game Over!")
        print(f"The word was {word}\n")


if __name__ == "__main__":
    main()
