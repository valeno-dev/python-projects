# 🧩 Hangman 

## 🧠 Description
Hangman is a classic guessing game where the player tries to identify a hidden word  
by suggesting one letter at a time. Each wrong guess brings the hangman closer to doom 😢.  
You win if you reveal all letters before running out of attempts!

---

## 📜 Features
- 🧩 3 Difficulty levels (Easy / Medium / Hard)
- ✅ Input validation (no numbers or repeated letters)
- 🎨 Simple ASCII hangman art
- 🧠 Randomized word selection
- 🎯 Clean, beginner-friendly structure
- 💬 Fun messages and emoji indicators


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

