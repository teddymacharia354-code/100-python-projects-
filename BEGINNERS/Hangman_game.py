import random

def load_word_list():
    """Return a list of words to guess from"""
    words = [
        "python", "hangman", "programming", "computer", "algorithm",
        "variable", "function", "database", "internet", "keyboard",
        "monitor", "software", "hardware", "password", "security",
        "adventure", "beautiful", "chocolate", "elephant", "fantastic",
        "galaxy", "hospital", "journalist", "kangaroo", "lighthouse"
    ]
    return words

def display_hangman(tries):
    """Display hangman stages"""
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |      
           |      
           |     
           -
        """
    ]
    return stages[tries]

def get_word():
    """Select random word from list"""
    word_list = load_word_list()
    return random.choice(word_list).upper()

def display_word(word, guessed_letters):
    """Show word with guessed letters revealed"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def play_hangman():
    """Main hangman game"""
    word = get_word()
    guessed_letters = set()
    correct_letters = set()
    tries = 6
    game_over = False
    
    print("=" * 50)
    print("HANGMAN GAME")
    print("=" * 50)
    print(f"The word has {len(word)} letters.")
    
    while not game_over:
        # Display current state
        print(display_hangman(tries))
        print(f"Word: {display_word(word, correct_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Tries left: {tries}\n")
        
        # Get player input
        guess = input("Guess a letter: ").upper()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter!")
            continue
        
        if guess in guessed_letters:
            print("❌ You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word:
            correct_letters.add(guess)
            print(f"✅ Correct! The letter '{guess}' is in the word!")
        else:
            tries -= 1
            print(f"❌ Wrong! The letter '{guess}' is not in the word!")
        
        # Check win condition
        if all(letter in correct_letters for letter in word):
            print(display_hangman(tries))
            print(f"Word: {display_word(word, correct_letters)}")
            print(f"🎉 YOU WIN! The word was: {word}")
            game_over = True
        
        # Check lose condition
        elif tries == 0:
            print(display_hangman(tries))
            print(f"💀 GAME OVER! The word was: {word}")
            game_over = True

def main():
    while True:
        play_hangman()
        again = input("Play again? (yes/no): ").lower()
        if again not in ["yes", "y"]:
            print("Thanks for playing Hangman!")
            break

if __name__ == "__main__":
    main()