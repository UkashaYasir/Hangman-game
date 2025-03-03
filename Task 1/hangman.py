import random

def hangman():
    words = ['python', 'developer', 'hangman', 'programming', 'algorithm', 'beginner', 'learning', 'simple']
    word = random.choice(words)
    guessed_letters = set()
    correct_letters = set(word)
    attempts = 6

    print("🕵️‍♂️ Welcome to Mystery Hangman!")
    print("🧙‍♂️ Uncover the hidden magic word, one letter at a time!")
    print("✨ You have 6 attempts to save the word from disappearing!")

    while attempts > 0 and correct_letters != guessed_letters:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("\n🔍 Word: " + display_word)
        print(f"💖 Attempts left: {attempts}")
        print(f"📚 Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None yet'}")

        guess = input("🎯 Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in correct_letters:
            print("✅ Bravo! You revealed part of the magic word!")
        else:
            print("❌ Oops! That letter is not in the word.")
            attempts -= 1

    if correct_letters == guessed_letters:
        print(f"\n🎉 Victory! You revealed the magic word: {word}")
    else:
        print(f"\n💀 Alas! The magic word was: {word}")

    print("🌟 Thanks for playing Mystery Hangman! See you next time!")

if __name__ == "__main__":
    hangman()
