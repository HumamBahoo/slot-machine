import os
from modules.slot_machine import SlotMachine


def clear_terminal():
    clear_cmd = "cls" if os.name == "nt" else "clear"
    os.system(clear_cmd)


def main():
    clear_terminal()

    machine = SlotMachine()

    machine.prompt_for_rows_count()
    machine.add_to_balance()
    machine.prompt_for_bet_amount()
    machine.prompt_for_selected_lines_count()

    clear_terminal()

    print(f"Balance: ${machine.balance}, Bet Amount: ${machine.bet_amount}, Selected Lines: {machine.selected_lines_count}\n")
    print(f"Total Bet: ${machine.selected_lines_count * machine.bet_amount}, Total Winning: ${machine.total_winnings}\n")

    input("Press [Enter] to spin")

    while True:
        machine.spin()

        winning_lines = machine.get_winning_lines()
        amount_won = machine.calculate_winning(winning_lines)

        machine.update_balance(amount_won)
        machine.update_total_winnings(amount_won)

        clear_terminal()

        print(f"Balance: ${machine.balance}, Bet Amount: ${machine.bet_amount}, Selected Lines: {machine.selected_lines_count}\n")
        print(f"Total Bet: ${machine.selected_lines_count * machine.bet_amount}, Total Winning: ${machine.total_winnings}\n")

        machine.display_reels(winning_lines)
        print("")

        if amount_won > 0:
            print(f"You've won! Total prize: ${amount_won}")
        else:
            print(f"You've lost!")

        print("")

        input("Press [Enter] to spin again.\n")


if __name__ == "__main__":
    main()
