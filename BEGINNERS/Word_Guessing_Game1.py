name = "ELEPHANT"
guess = "" #create the variable "guess"
guess_count = 0
guess_limit = 5 
hint_index = 0  # The index of the letter we want to pick at first ,it's zero 

def out_of_guesses(count, limit):
    # returns True if we've used up all guesses
    return count >= limit

while True:
    guess = input("Enter name: ").upper()
    
    if guess == name:
        print("you win!")
        break
    
    guess_count += 1  # use up one guess
    print("wrong, try again!")
    
    # give a hint if we still have letters left to reveal
    if hint_index < len(name):
        hint_letter = name[hint_index]  # indexing to get one letter
        print(f"Here's a hint: {hint_letter}")
        hint_index += 1
    
    if out_of_guesses(guess_count, guess_limit): #def used to confuse me, for those with same issue remember Count & limit are just placeholders
        print("You are out of guesses, You lose!")
        break
