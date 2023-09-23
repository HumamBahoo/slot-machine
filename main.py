import os
from modules.slot_machine import SlotMachine


def clear_terminal():
    clear_cmd = "cls" if os.name == "nt" else "clear"
    os.system(clear_cmd)


def main():
    clear_terminal()

    machine = SlotMachine()

    machine.set_lines_count()
    machine.add_to_balance()
    machine.set_bet_amount()
    machine.set_selected_lines_count()

    print(f"Balance: ${machine.balance}, Bet Amount: ${machine.bet_amount}, Selected Lines: {machine.selected_lines_count}\n")
    print(f"Total Bet: ${machine.selected_lines_count * machine.bet_amount}\n")

    while True:
        clear_terminal()

        machine.spin()

        print(f"Balance: ${machine.balance}, Bet Amount: ${machine.bet_amount}, Selected Lines: {machine.selected_lines_count}\n")

        print(f"Total Bet: ${machine.selected_lines_count * machine.bet_amount}\n")

        input("Press [Enter] to spin again.\n")


if __name__ == "__main__":
    main()
