import random

# List of words to choose from
word_list = ["python", "java", "javascript", "ruby", "html", "css", "swift", "kotlin", "django", "flask"]

def choose_word():
    # Randomly choose a word from the list
    return random.choice(word_list)

def scramble_word(word):
    # Scramble the word by converting it into a list of characters, then shuffling
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def play_game():
    # Choose the word for the game
    word_to_guess = choose_word()
    scrambled_word = scramble_word(word_to_guess)  # Scramble the chosen word
    
    print("Welcome to the Word Scramble Game!")
    print(f"The scrambled word is: {scrambled_word}")
    
    # Give the player a certain number of attempts
    attempts = 3  # You can increase this if you want more chances
    
    while attempts > 0:
        guess = input("Guess the original word: ").lower()
        
        # Check if the player's guess is correct
        if guess == word_to_guess:
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Oops! Incorrect guess. You have {attempts} attempts left.")
            else:
                print(f"Game Over! The correct word was: {word_to_guess}")
        print("\n")
                
if __name__ == "__main__":
    play_game()
