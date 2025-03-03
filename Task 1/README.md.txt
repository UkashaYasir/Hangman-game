Made by Muhammad Ukasha
**Hangman Game in Python**  

This project is a **command-line Hangman game** built using Python. Hangman is a classic word-guessing game where players attempt to guess a hidden word by suggesting letters within a limited number of tries. This implementation offers a simple yet interactive experience and serves as a great introduction to basic Python concepts.  

The game selects a word at random from a predefined list and displays underscores representing each letter. Players input their guesses one letter at a time. If the guessed letter is correct, it is revealed in the word. If incorrect, the player loses one attempt. The objective is to guess the entire word before running out of attempts.  

### Features:  
- **Random Word Generation:** The game randomly selects a word from a word list.  
- **User Input Validation:** Accepts only valid, single-character alphabet inputs.  
- **Limited Attempts:** Players have a restricted number of incorrect guesses.  
- **Dynamic Word Display:** Updates and reveals correctly guessed letters.  
- **Win/Loss Conditions:** Displays appropriate messages when the player wins or loses.  
- **Customizable:** Easy to modify the word list and attempt limits.  

### How to Run:  
Ensure you have Python installed on your system. Navigate to the project folder and run:  

```bash
python hangman.py
```

### Creating an Executable:  
You can convert the game into a standalone executable using **PyInstaller**:  

```bash
pyinstaller --onefile hangman.py
```

The executable will be located in the **dist** folder. You can share this file with others, allowing them to play the game without installing Python.  

### Customization:  
- **Add Words:** Extend the word list by modifying the source code.  
- **Change Attempts:** Adjust the maximum number of guesses.  
- **Visual Enhancements:** Incorporate ASCII art for a visual Hangman display.  

### Contributions:  
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request. This project is an excellent starting point for those learning Python and looking to understand how to build interactive console applications.  

---