
import random

MAX_LINES = 4
MAX_BET = 100
MIN_BET = 1

ROWS = MAX_LINES
COLS = 3

SYMBOL_COUNT = {"A": 3, "B": 3, "C": 4, "D": 5}
SYMBOL_VALUE = {"A": 5, "B": 4, "C": 3, "D": 2}


def deposit():
    while True:
        balance = input("How much would you like to top up? $")
        if balance.isdigit():
            balance = int(balance)
            if balance > 0:
                break
            else:
                print("Please enter more than $0")
        else:
            print("Invalid Amount!")
    return balance


def get_bet_lines():
    while True:
        line = input(f"How many lines to bet (1-{MAX_LINES})? ")
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINES:
                break
            else:
                print("Please enter more than 0")
        else:
            print("Invalid Amount!")
    return line


def get_bet():
    while True:
        balance = input(f"How much bet on each line (${MIN_BET} - ${MAX_BET})? $")
        if balance.isdigit():
            balance = int(balance)
            if MIN_BET <= balance <= MAX_BET:
                break
            else:
                print("Please enter more than $0")
        else:
            print("Invalid Amount!")
    return balance


def verify_bet(balance, line):
    while True:
        bet = get_bet()
        total_bet = line * bet
        if total_bet > balance:
            insufficient_balance = total_bet - balance
            topup = input(
                f"Insufficent balance!, you need ${insufficient_balance} more. Would you like to topup (y/n)? "
            )
            if topup == "y":
                balance += deposit()
                return balance, bet, total_bet
        else:
            return balance, bet, total_bet


def get_slot_symbol(rows, cols, symbols):
    symbol_list = []
    for symbol, count in symbols.items():
        for _ in range(count):
            symbol_list.append(symbol)

    collumns = []
    for _ in range(cols):
        collumn = []
        current_symbol = symbol_list[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            collumn.append(value)

        collumns.append(collumn)
    return collumns


def print_slots(collumns):
    for row in range(len(collumns[0])):
        for i, col in enumerate(collumns):
            if i != len(collumns) - 1:
                print(col[row], "|", end="")
            else:
                print(col[row])


def check_winning(collumns, lines, bet, values):
    winning = 0
    winning_line = []
    for line in range(lines):
        symbol = collumns[0][line]
        for collumn in collumns:
            symbol_check = collumn[line]
            if symbol != symbol_check:
                break
        else:
            winning += values[symbol] * bet
            winning_line.append(line + 1)
    return winning, winning_line


def game(balance):
    while True:
        print(f"balance = ${balance}")
        line = get_bet_lines()
        balance, bet, total_bet = verify_bet(balance, line)
        balance -= total_bet
        print(
            f"balance = ${balance}\nBetting {bet}$ bet on {line} line(s)\nTotal = ${total_bet}"
        )
        slot = get_slot_symbol(ROWS, COLS, SYMBOL_COUNT)
        print_slots(slot)
        winning, winning_line = check_winning(slot, line, bet, SYMBOL_VALUE)
        print(f"You've won ${winning} on line ", *winning_line)
        balance += winning
        token = input("Do you want to play again (n for no)?")
        if token == "n":
            print(f"you left with ${balance}")
            break


def main():
    balance = deposit()
    game(balance)


main()
get_slot_symbol