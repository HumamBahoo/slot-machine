import os
from modules.slot_machine import SlotMachine


def clear_terminal():
    clear_cmd = "cls" if os.name == "nt" else "clear"
    os.system(clear_cmd)


def main():
    clear_terminal()

    machine = SlotMachine()

    # set the title
    machine.title = "A Basic Slot Machine"

    # set the number of rows
    machine.rows_count = 5

    # add to balance
    machine.add_to_balance(1000)

    # set the bet amount
    #   validate if there is enough balance to make this bet
    machine.bet_amount = 10

    # set the selected lines count
    #   validate if there is enough balance when increasing the number of selected lines
    machine.selected_lines_count = 5

    print(f"Title: {machine.title}\n")

    print(f"Rows Count: {machine.rows_count} | Balance: ${machine.balance:.2f}")
    print(f"Bet Amount: ${machine.bet_amount:.2f} | Selected Lines: {machine.selected_lines_count}")
    print(f"Total Bet: ${machine.bet_amount * machine.selected_lines_count:.2f} | Total Winnings: ${machine.total_winnings_amount}\n\n")

    input("Press [Enter] to spin")

    while True:
        # spin
        machine.spin()

        # find if there are winning lines
        machine.update_winning_lines()

        # calculate winning amount of lost amount
        amount = machine.calculate_spin_outcome()

        # update balance and total winning based on win or loss outcome
        if machine.has_won:
            machine.add_to_balance(amount)
            machine.add_to_total_winnings_amount(amount)
        else:
            machine.subtract_from_balance(amount)
            machine.subtract_from_total_winnings_amount(amount)

        # clean screen and display updated information
        clear_terminal()
        print(f"Title: {machine.title}\n")
        print(f"Rows Count: {machine.rows_count} | Balance: ${machine.balance:.2f}")
        print(f"Bet Amount: ${machine.bet_amount:.2f} | Selected Lines: {machine.selected_lines_count}")
        print(f"Total Bet: ${machine.bet_amount * machine.selected_lines_count:.2f} | Total Winnings: ${machine.total_winnings_amount}\n\n")

        # display reels
        machine.display_reels()
        print("")

        # display results with total money won, if won
        if machine.has_won:
            print(f"You've Won! Total Prize: ${amount}\n")
        else:
            print(f"You've Lost!\n")

        input("Press [Enter] to spin again...")


if __name__ == "__main__":
    main()
