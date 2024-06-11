"""
Simulate betting on Roulette games.

After every win, the minimum bet is placed on one color.
After every loss, the bet is doubled.

Eventually, the strategy will fail, but it is very likely to 
win money before it does.
"""

import random


PRINT_EACH_GAME = False


def play() -> bool:
    num = random.random()
    return num <= (18/38)


def simulate_games():
    min_bet = 5
    max_bet = 5000
    balance = 500
    loss_streak = 0
    games_played = 0
    wins = 0
    losses = 0
    max_balance = 0

    while balance > 0:
        if balance > max_balance:
            max_balance = balance

        bet = min_bet * (2**loss_streak)

        if bet > max_bet or bet > balance:
            break

        win = play()
        games_played += 1

        if PRINT_EACH_GAME:
            print(f"Game #{games_played} ... bet ${bet}")
        
        if win:
            wins += 1
            loss_streak = 0
            balance += bet
            if PRINT_EACH_GAME:
                print(f"[WON] Balance: ${balance}")
        else:
            losses += 1
            loss_streak += 1
            balance -= bet
            if PRINT_EACH_GAME:
                print(f"[LOST] Balance: ${balance}")

    print(f"Strategy failed at game #{games_played}; ${balance} left; {wins} wins and {losses} losses; peaked at ${max_balance}")


for _ in range(50):
    simulate_games()
