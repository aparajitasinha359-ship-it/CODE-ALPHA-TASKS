import random

# List of 5 predefined words
words = ["python", "apple", "school", "computer", "garden"]

# Select a random word
secret_word = random.choice(words)
guessed_letters = []

max_attempts = 6
incorrect_guesses = 0

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses available.\\n")

while incorrect_guesses < max_attempts:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    if all(letter in guessed_letters for letter in secret_word):
        print("\\nCongratulations! You guessed the word:", secret_word)
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.\\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try another.\\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!\\n")
    else:
        incorrect_guesses += 1
        print("Wrong guess!\\n")
else:
    print("Game over! The word was:", secret_word)
