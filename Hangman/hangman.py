import random

# List of words to choose from
word_list = ["python", "java", "javascript", "ruby", "html", "css", "swift", "kotlin", "django", "flask"]

def choose_word():
    # Randomly choose a word from the list
    return random.choice(word_list)

def display_word(word, guessed_letters):
    # Display the word with blanks for unguessed letters
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game():
    # Choose the word for the game
    word_to_guess = choose_word()
    guessed_letters = set()  # Set to keep track of guessed letters
    attempts = 6  # Number of incorrect attempts allowed
    correct_guesses = 0

    print("Welcome to the Guess the Word Game!")
    print("Try to guess the word one letter at a time.")
    print("You have 6 attempts to guess the word correctly.\n")
    
    # Main game loop
    while attempts > 0:
        # Display the current state of the word
        current_word = display_word(word_to_guess, guessed_letters)
        print(f"Word: {current_word}")
        print(f"Attempts remaining: {attempts}")
        
        # Get the player's guess
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue
        
        # If the letter was guessed before, skip the turn
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.add(guess)
        
        # Check if the guess is correct
        if guess in word_to_guess:
            print(f"Good guess! The letter {guess} is in the word.")
            correct_guesses += word_to_guess.count(guess)
        else:
            print(f"Oops! The letter {guess} is not in the word.")
            attempts -= 1
        
        # Check if the player has guessed all letters
        if correct_guesses == len(word_to_guess):
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            break
        print("\n")

    # If the player runs out of attempts, reveal the word
    if attempts == 0:
        print(f"Game Over! The correct word was: {word_to_guess}")

if __name__ == "__main__":
    play_game()
