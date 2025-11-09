import random

def word_guess_game():
    print("🎯 Welcome to the Word Guessing Game!")
    print("Try to guess the secret word, one letter at a time.\n")

    # List of words
    words = ["python", "developer", "computer", "programming", "artificial", "intelligence", "project", "hangman"]
    word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6

    print(f"The word has {len(word)} letters.")
    display = ["_"] * len(word)

    while attempts > 0:
        print("\n" + " ".join(display))
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong! You have {attempts} attempts left.")

        if "_" not in display:
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("\n😢 Out of attempts! The word was:", word)

if __name__ == "__main__":
    word_guess_game()
