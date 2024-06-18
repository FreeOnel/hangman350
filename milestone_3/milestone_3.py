
# not in tasks for some reason
secret = "apple"

def check_guess(guess: str):
    guess = guess.lower()
    if guess in secret:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Please guess a letter: ")
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess)



ask_for_input()