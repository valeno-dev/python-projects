import random

class HangmanGame:
    WORDS = [
        "plastic", "journey", "worship", "caption", "vampire",
        "flaming", "kitchen", "sandbox", "treacle", "founder",
        "bracket", "harmful", "digitsy", "cupcake", "joyment",
        "harvest", "twinkle", "sandbox", "lighten", "foreman",
        "adventure", "paintwork", "formulate", "submarine", "vibration",
        "wonderful", "blackouts", "marketing", "currency", "adjective",
        "framework", "polygonal", "secluding", "vocalizer", "drumstick",
        "turbofan", "landpiece", "patchwork", "minotaur", "volcanist",
        "backgrounds", "documentary", "journalistic", "countervails", "volunteering",
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

    def __init__(self, difficulty=""):
        self.difficulty = difficulty
        self.word = ""
        self.guessed_letters = []
        self.display_word = []
        self.attempts = 10

    @staticmethod
    def show_difficulty_menu():
        print("\nDifficulty levels:")
        print("1️⃣   Easy")
        print("2️⃣   Medium")
        print("3️⃣   Hard")

    def select_words_by_difficulty(self, difficulty: str):
        if difficulty == "1":
            return [w for w in self.WORDS if len(w) <= 7]
        elif difficulty == "2":
            return [w for w in self.WORDS if 7 < len(w) <= 10]
        elif difficulty == "3":
            return [w for w in self.WORDS if 10 < len(w) <= 13]
        print("⚠️  Invalid input! Defaulting to Medium level.")
        return [w for w in self.WORDS if 7 < len(w) <= 10]

    def choose_word(self, difficulty: str):
        selection = self.select_words_by_difficulty(difficulty)
        if not selection:
            raise ValueError("No words available for this difficulty level.")
        self.word = random.choice(selection).lower()
        self.display_word = ["_"] * len(self.word)
        self.guessed_letters = []
        self.attempts = 10

    def give_early_hint(self):
        revealed_letters = set()
        if self.difficulty == "1":
            num_hint = 2
        elif self.difficulty == "2":
            num_hint = 1
        else:
            num_hint = 0

        while len(revealed_letters) < min(num_hint, len(set(self.word))):
            letter = random.choice(self.word)
            revealed_letters.add(letter)
            self.guessed_letters.append(letter)

        for letter in revealed_letters:
            for i, w in enumerate(self.word):
                if w == letter:
                    self.display_word[i] = letter

    def validate_input(self, user_guess: str):
        if not user_guess.isalpha():
            print("Sorry, you can't input a number!")
            return False
        if len(user_guess) != 1:
            print("You can only input one letter!")
            return False
        if user_guess in self.guessed_letters:
            print("The letter has been guessed.")
            return False
        return True

    def handle_correct_guess(self, user_guess: str):
        for i, letter in enumerate(self.word):
            if letter == user_guess:
                self.display_word[i] = user_guess
        print("Correct (✅)")

    def handle_wrong_guess(self):
        self.attempts -= 1
        if self.attempts != 0:
            print(f"Wrong (❌), you have {self.attempts} attempt(s) left.")

    def display_hangman(self):
        for line in self.HANGMAN_ART[self.attempts]:
            print(line)

    def show_game_state(self):
        print("_" * len(self.word))
        self.display_hangman()
        print("\n" + " ".join(self.display_word))

    def main(self):
        print("\n🎮 HANGMAN GAME")
        print("Guess the word before the hangman is complete!\n")
        self.show_difficulty_menu()
        self.difficulty = input("\nEnter your choice (1, 2, 3): ").strip()
        self.choose_word(self.difficulty)
        self.give_early_hint()

        while self.attempts > 0:
            self.show_game_state()
            user_guess = input("\nGuess a letter: ").strip().lower()

            if not self.validate_input(user_guess):
                continue

            self.guessed_letters.append(user_guess)

            if user_guess in self.word:
                self.handle_correct_guess(user_guess)
            else:
                self.handle_wrong_guess()

            if "_" not in self.display_word:
                self.show_game_state()
                print(f"\n🎉 Congratulations! You guessed the word: {self.word}")
                print("🏆 You win!\n")
                return

        self.show_game_state()
        print("\n💀 Game Over!")
        print(f"The word was {self.word}\n")
