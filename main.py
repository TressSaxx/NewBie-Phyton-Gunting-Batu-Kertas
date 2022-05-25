import random

while True:
    choices = ["batu","kertas","gunting"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("batu, kertas, or gunting?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")

    elif player == "batu":
        if computer == "kertas":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "gunting":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "gunting":
        if computer == "batu":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "kertas":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "kertas":
        if computer == "gunting":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "batu":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")
