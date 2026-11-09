# Hangman Game

A simple text-based Hangman game built in Python for the **CodeAlpha Python Internship**.

## Description
The computer randomly picks a secret word from a list of 5 predefined words.
The player guesses one letter at a time and has a maximum of 6 incorrect guesses
to find the full word.

## Features
- Exactly 5 predefined words (`python`, `program`, `keyboard`, `internet`, `computer`)
- Random word selection using the `random` module
- One letter guess at a time
- Maximum of 6 incorrect guesses
- Displays correctly guessed letters (e.g. `p _ t _ o _`) and remaining attempts
- Repeated guesses do not reduce attempts
- Input validation (only single letters accepted)
- Win and lose messages
- Option to play again

## Concepts Used
Lists, strings, loops (`while`, `for`), if-else statements, functions, and the `random` module.

## Requirements
- Python 3.6 or higher
- No external libraries needed

## How to Run
1. Open the project folder in VS Code (File > Open Folder).
2. Open `main.py`.
3. Click the Run button (triangle, top right) or open the terminal (Ctrl + `) and type:
   ```
   python main.py
   ```
   (Use `python3 main.py` on macOS/Linux.)

## Sample Output
```
Word: _ _ _ _ _ _
Remaining attempts: 6

Enter a letter: p
Good guess!
```

## Project Structure
```
hangman_game/
├── main.py
├── README.md
└── requirements.txt
```
