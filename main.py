from modules.slot_machine_ui import SlotMachineUI
from modules.slot_machine import SlotMachine


def play_game(slot_machine: SlotMachine):
    # spin
    slot_machine.spin()

    # find if there are winning lines
    slot_machine.update_winning_lines()

    # calculate winning amount of lost amount
    amount = slot_machine.calculate_spin_outcome()

    # update balance and total winning based on win or loss outcome
    if slot_machine.has_won:
        slot_machine.add_to_balance(amount)
        slot_machine.add_to_total_winnings_amount(amount)

    else:
        slot_machine.subtract_from_balance(amount)
        slot_machine.subtract_from_total_winnings_amount(amount)

    # clean screen and display updated information
    SlotMachineUI.clear_terminal()
    SlotMachineUI.print_header(slot_machine)
    SlotMachineUI.print_slot_machine_details(slot_machine)

    # display reels
    slot_machine.display_reels()
    print("")

    # display results with total money won, if won
    if slot_machine.has_won:
        print(f"You've Won! Total Prize: ${amount}\n")
    else:
        print(f"You've Lost!\n")


def main():
    slot_machine = SlotMachine()
    slot_machine.title = "A Basic Slot Machine"

    while True:
        # main menu
        options = [
            "1- New Game",
            "2- Exit",
        ]
        prompt_message = "Please make a selection"
        valid_selections = ["1", "2"]
        main_menu_selection = SlotMachineUI.prompt_for_menu_selection(
            slot_machine, options, prompt_message, valid_selections, False, True, True, False
        )

        if main_menu_selection == "1":
            slot_machine.reset_slot_machine()

            while True:
                # game menu
                options = [
                    "1- Update Rows Count",
                    "2- Update Selected Lines Count",
                    "3- Update bet Amount",
                    "4- Deposit Funds",
                    "5- Exit to Main Menu",
                ]
                prompt_message = "Please select an option or press [Enter] to start playing"
                valid_selections = ["1", "2", "3", "4", "5"]

                game_menu_selection = SlotMachineUI.prompt_for_menu_selection(
                    slot_machine,
                    options,
                    prompt_message,
                    valid_selections,
                    True,
                    True,
                    True,
                    True,
                )

                if game_menu_selection == "1":
                    prompt_message = "How many lines/rows you want the slot machine to have"
                    min = slot_machine.min_rows_count
                    max = slot_machine.max_rows_count

                    rows_count = SlotMachineUI.prompt_for_amount(slot_machine, prompt_message, False, min, max)

                    try:
                        slot_machine.rows_count = rows_count
                        print(f"Rows count has been successfully set to {rows_count}.")
                        input(f"Press [Enter] to continue...")
                    except:
                        print("There was an error in setting the rows count.")

                elif game_menu_selection == "2":
                    prompt_message = "How many lines would you like to make a bet on"
                    min = 1
                    max = slot_machine.rows_count

                    selected_lines_count = SlotMachineUI.prompt_for_amount(slot_machine, prompt_message, False, min, max)

                    try:
                        slot_machine.selected_lines_count = selected_lines_count
                        print(f"Selected lines count has been successfully set to {selected_lines_count}.")
                        input(f"Press [Enter] to continue...")
                    except:
                        print("There was an error in setting the selected lines count.")

                elif game_menu_selection == "3":
                    prompt_message = "How much bet would you like to make"
                    min = slot_machine.min_bet_amount
                    max = slot_machine.max_bet_amount

                    bet_amount = SlotMachineUI.prompt_for_amount(slot_machine, prompt_message, True, min, max)

                    try:
                        slot_machine.bet_amount = bet_amount
                        print(f"Bet amount has been successfully set to ${bet_amount}.")
                        input(f"Press [Enter] to continue...")
                    except:
                        print("There was an error in setting the bet amount.")

                elif game_menu_selection == "4":
                    prompt_message = "How much money would you like to deposit"
                    min = 1
                    max = 1000

                    deposit_amount = SlotMachineUI.prompt_for_amount(slot_machine, prompt_message, True, min, max)

                    try:
                        slot_machine.add_to_balance(deposit_amount)
                        print(f"The amount ${deposit_amount} has been add successfully.")
                        input(f"Press [Enter] to continue...")
                    except:
                        print("There was an error in adding to balance.")

                elif game_menu_selection == "5":
                    break

                else:
                    while True:
                        play_game(slot_machine)

                        # after spin selection
                        options = []
                        prompt_message = "Press [Enter] to spin again, or enter [B] to go back to previous menu"
                        valid_selections = ["b"]

                        after_spin_selection = SlotMachineUI.prompt_for_menu_selection(
                            slot_machine,
                            options,
                            prompt_message,
                            valid_selections,
                            True,
                            False,
                            False,
                            False,
                        )

                        if after_spin_selection.lower() == "b":
                            break

        else:
            SlotMachineUI.clear_terminal()
            SlotMachineUI.print_header(slot_machine)

            print("Goodbye!")

            break


if __name__ == "__main__":
    main()
