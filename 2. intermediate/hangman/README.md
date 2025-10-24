# 🎮 Hangman Game (Python)

A simple and fun console-based Hangman game built with Python.  
Try to guess the hidden word before your character is fully hanged!

---

## 🧠 Description
This project is a console version of the classic Hangman game.  
It features multiple difficulty levels, random word selection,  
and early hints to make gameplay more interesting.

---

## 🧩 Features
- 🟢 3 difficulty levels: Easy, Medium, Hard  
- 💡 Early hints (1–2 random letters revealed depending on difficulty)  
- 🎨 ASCII-based hangman visualization  
- ✅ Input validation (no numbers or duplicate guesses)
- 🎯 Clean, beginner-friendly structure
- 🏆 Win & Lose system with feedback messages  

---

## ⚙️ Example Difficulty Levels
| Difficulty | Word Length | Hints |
|-------------|--------------|-------|
| Easy        | ≤ 7          | 2 letters revealed |
| Medium      | 8–10         | 1 letter revealed |
| Hard        | 11–13        | No hints |

---

## ⚙️ How It Works
- The program randomly selects a word from a predefined list.  
- You choose a **difficulty level**, which determines how long or short the words are:
  - 🟢 **Easy** → Words with ≤ 5 letters  
  - 🟡 **Medium** → Words with 6–8 letters  
  - 🔴 **Hard** → Words with > 8 letters  
- You have **6 total attempts**.  
- For every incorrect guess, part of the hangman will be gone.  
- The game ends when:
  - You guess the full word ✅
  - or all attempts are used up 💀

---

## 🕹️ Example Output
Difficulty levels: <br>
1️⃣  Easy <br>
2️⃣  Medium <br>
3️⃣  Hard

Enter your choice (1, 2, 3): 2 <br>
------ <br>
 o <br>
/|\ <br>
/ \ <br>
------ <br>

_ _ _ _ _ _ <br>

Guess a letter: a <br>
Correct (✅) <br>
------ <br>
 o <br>
/|\ <br>
/ \ <br>
------ <br>

_ _ a _ _ _

Guess a letter: q <br>
Wrong (❌), you have 5 attempt(s) left. <br>
------ <br>
 o <br>
/|\ <br>
/ <br>
------ <br>

_ _ a _ _ _

Guess a letter:

---

## 🏆 Author
Created by valeno <br>
If you like this project, consider giving it a star(⭐) on GitHub!

