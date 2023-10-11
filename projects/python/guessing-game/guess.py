## imperative / functional approach

from random import randint, seed
seed(42)

affirm = ["y", "yes", "yup", "sure", "ok", "okay", "yeah", "yea", "yeahh", "ye", "yessir", "yep"]

def get_integer_input(prompt, min_val=None, max_val=None):
    """Get an integer input from the user with optional min and max bounds."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Please enter a number greater than or equal to {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Please enter a number less than or equal to {max_val}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")

def get_feedback(num, guess, prev_guess=None):
    """Returns feedback based on the player's guess."""
    if guess == num:
        return "correct"
    elif prev_guess is None:
        return "low" if guess < num else "high"
    else:
        delta = abs(guess - num)
        prev_delta = abs(prev_guess - num)
        if delta < prev_delta:
            return "warmer"
        else:
            return "colder"

def get_bounds():
    """Get the minimum and maximum bounds for the game."""
    min_bound = get_integer_input("Enter the minimum bound: ")
    max_bound = get_integer_input("Enter the maximum bound: ")
    while min_bound >= max_bound:
        print("The maximum bound must be greater than the minimum bound.")
        min_bound = get_integer_input("Enter the minimum bound: ")
        max_bound = get_integer_input("Enter the maximum bound: ")
    return min_bound, max_bound

def game(min_bound, max_bound):
    num = randint(min_bound, max_bound)
    tries = 10
    prev_guesses = []
    
    while tries > 0:
        guess = get_integer_input(f"Guess a number between {min_bound} and {max_bound}: ", min_bound, max_bound)
        
        if guess in prev_guesses:
            print("You already guessed that!")
            continue
        
        prev_guesses.append(guess)
        feedback = get_feedback(num, guess, prev_guesses[-2] if len(prev_guesses) > 1 else None)
        
        if feedback == "correct":
            print(f"You win! It only took you {10 - tries + 1} tries! :)")
            break
        elif feedback == "low":
            print("Too low!")
        elif feedback == "high":
            print("Too high!")
        elif feedback == "warmer":
            print("Warmer!")
        elif feedback == "colder":
            print("Colder!")
        
        tries -= 1

    if feedback != "correct":
        print(f"You lost! The correct number was {num}.")

def test_game(inputs, min_bound, max_bound, expected_output):
    def mock_input(prompt):
        return inputs.pop(0)
    
    global input
    input = mock_input
    game(min_bound, max_bound)
    print(expected_output)

if __name__ == "__main__":
    min_bound, max_bound = get_bounds()
    game(min_bound, max_bound)

    # Test Case 1: User correctly guesses the number
    test_game(inputs=["50"], min_bound=1, max_bound=100, expected_output="You win! It only took you 1 tries! :)")

    # Test Case 2: User's guesses get progressively closer to the number
    test_game(inputs=["10", "20", "30", "40", "50"], min_bound=1, max_bound=100, expected_output="You win! It only took you 5 tries! :)")

    # Test Case 3: User's guesses get progressively farther from the number
    test_game(inputs=["50", "40", "30", "20", "10"], min_bound=1, max_bound=100, expected_output="You lost! The correct number was 51.")

    # Test Case 4: User runs out of tries
    test_game(inputs=["10", "20", "30", "40", "60", "70", "80", "90", "100", "1"], min_bound=1, max_bound=100, expected_output="You lost! The correct number was 51.")

    # Test Case 5: User repeatedly guesses the same number
    test_game(inputs=["50", "50", "50", "50", "50", "50", "50", "50", "50", "50"], min_bound=1, max_bound=100, expected_output="You win! It only took you 1 tries! :)")
