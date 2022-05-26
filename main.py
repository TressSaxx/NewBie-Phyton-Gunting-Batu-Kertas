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
        print("Seri")

    elif player == "batu":
        if computer == "kertas":
            print("computer: ", computer)
            print("player: ", player)
            print("Kamu Kalah!")
        if computer == "gunting":
            print("computer: ", computer)
            print("player: ", player)
            print("Kamu Menang!")

    elif player == "gunting":
        if computer == "batu":
            print("computer: ", computer)
            print("player: ", player)
            print("Kamu kalah!")
        if computer == "kertas":
            print("computer: ", computer)
            print("player: ", player)
            print("Kamu Menang!")

    elif player == "kertas":
        if computer == "gunting":
            print("computer: ", computer)
            print("player: ", player)
            print("Kamu Kalah!")
        if computer == "batu":
            print("computer: ", computer)
            print("player: ", player)
            print("Kamu Menang!")

    play_again = input("Main Lagi? (Iya/Tidak): ").lower()

    if play_again != "Iya":
        break

print("Bye!")
