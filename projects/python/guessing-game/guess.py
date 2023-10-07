from random import randint

affirm = ["y", "yes", "yup", "sure", "ok", "okay", "yeah", "yea", "yeahh", "ye", "yessir", "yep"]

def game():
    num = randint(1, 100)
    tries = 10
    while tries > 0:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == num:
            tries -= 1
            print(f"You win! It only took you {10-tries} tries! :)")
            break
        elif guess < num:
            print("Too low!")
        else:
            print("Too high!")
        tries -= 1
        print(f"You have {tries} tries left.")
    print(f"The number was {num}.")

def play_game():
    num = randint(1, 100)
    tries = 10
    prev = []
    while tries > 0:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == num:
            tries -= 1
            print(f"You win! It only took you {10-tries} tries! :)")
            break
        if guess in prev:
            print("You already guessed that!")
            continue
        if len(prev) == 0:
            if guess < num:
                print("Too low!")
            else:
                print("Too high!")
            prev.append(guess)
        else:
            delta = abs(guess - num)
            prev_delta = abs(prev[-1] - num)
            if delta < prev_delta:
                print("Getting warmer!")
            else:
                print("Getting colder!")
            prev.append(guess)
        tries -= 1
        print(f"You have {tries} tries left.")
    if tries == 0:
        print("You ran out of tries! :(")
    print(f"The number was {num}.")

if __name__ == "__main__":
    while True:
        gameNum = 0
        while gameNum not in [1, 2]:
            gameNum = int(input("Which guessing game do you want to play?\n1. Lower-Higher or\n2. Hot-Cold?\n"))
        if gameNum == 1: game()
        else: play_game()
        again = input("Do you want to play again? (y/n) ")
        if again.lower() not in affirm: 
            print("Thanks for playing!")
            break