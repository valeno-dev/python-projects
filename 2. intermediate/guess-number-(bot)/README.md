# 🤖 Random Guess (Bot)

## 📝 Description
This project simulates a **number guessing game**, but this time the **bot** is the one trying to guess **your secret number**!  
You think of a number between `1` and a chosen limit, and the bot will attempt to find it using one of two strategies:
- 🎲 **Random Mode:** The bot guesses randomly within the range.
- 🧠 **Smart Mode:** The bot uses a binary search algorithm to narrow down guesses efficiently.

This project is part of the **Intermediate Python Projects** collection — great for practicing logic, loops, and input validation.

---

## 💡 Features
- Two guessing modes: Random & Smart (Binary Search)
- Input validation for user responses
- Friendly user prompts and emojis for better interaction
- Docstring documentation inside the main function
- Clean and modular structure using `if __name__ == "__main__":`

---

## ⚙️ How It Works
1. You decide a range (e.g., 1–100) and the number of attempts (e.g., 7).
2. The bot asks which mode you want to use:
   - **1 → Random Mode**
   - **2 → Smart Mode (binary search)**
3. The bot starts guessing:
   - After each guess, you tell it whether the guess was correct, too high, or too low.
4. The game continues until the bot guesses correctly or runs out of attempts.

---

## 🖥️ Example Output
🎯 Think of a number between 1 and 100, and I will try to guess it!<br>
🤖 I have 7 attempts to guess correctly! After each guess, tell me if I'm too high or too low!

1️⃣ Random Mode (guess randomly each time)<br>
2️⃣ Smart Mode (binary search)

Enter your choice (1 or 2): 2

My guess is: 50<br>
Is it correct? (yes/no): no<br>
Too low (L) or too high (H)? l<br>
I've 6 attempt(s) left 🤔

My guess is: 75<br>
Is it correct? (yes/no): no<br>
Too low (L) or too high (H)? h<br>
I've 5 attempt(s) left 🤔<br>
...

---

## 🏆 Author
Created by valeno <br>
If you like this project, consider giving it a star(⭐) on GitHub!

