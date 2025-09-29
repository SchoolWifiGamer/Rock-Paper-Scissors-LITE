import random
# made by gao le
choices = ["rock", "paper", "scissors"]
wins = losses = ties = 0

while True:
    player = input("Rock, paper, or scissors? ").lower()
    if player not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("Tie!")
        ties += 1
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1

    print(f"Score: {wins} wins, {losses} losses, {ties} ties")

    if input("Play again? (y/n): ").lower() != 'y':
        break
