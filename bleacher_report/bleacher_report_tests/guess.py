import random


def main():
    guesses = 0
    hidden = random.randrange(1, 100)
    guessing(guesses, hidden)


def guessing(guesses, hidden):
    while True:
        guess = int(raw_input("Please enter your guess between 1 and 100: "))
        guesses += 1
        if guess == hidden:
            break
        elif guess < hidden:
            print "That guess was too low"
        else:
            print "That guess was too high"
    if guess == hidden:
        play_again = raw_input("Congrats you nailed it, it took you this many guesses: " + str(guesses) +
                               "\nPlay again? (y/n): ")
        if play_again == "y":
            main()
        else:
            print("Ok Game Over")
            exit(0)


if __name__ == '__main__':
    main()
