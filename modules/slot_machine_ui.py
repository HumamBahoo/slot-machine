import os
from modules.slot_machine import SlotMachine, SlotMachineError


class SlotMachineUI:
    @staticmethod
    def clear_terminal() -> None:
        cmd = "cls" if os.name == "nt" else "clear"
        os.system(cmd)

    @staticmethod
    def print_header(slot_machine: SlotMachine):
        print(slot_machine.title)
        print(f"{'-' * len(slot_machine.title)}\n")

    @staticmethod
    def print_slot_machine_details(slot_machine: SlotMachine):
        print(
            f"Balance: ${slot_machine.balance:.2f}, Bet Amount: ${slot_machine.bet_amount:.2f}, Selected Lines: {slot_machine.selected_lines_count}"
        )
        print(
            f"Total Bet: ${slot_machine.bet_amount * slot_machine.selected_lines_count:.2f}, Total Winnings: ${slot_machine.total_winnings_amount}\n"
        )

    @staticmethod
    def prompt_for_menu_selection(
        slot_machine: SlotMachine,
        options: list[str],
        prompt_message: str,
        valid_selections: list[str],
        can_press_enter: bool = False,
        clear_terminal: bool = False,
        print_header: bool = False,
        print_slot_machine_details: bool = False,
    ) -> str:
        user_selection = None

        while True:
            if clear_terminal:
                SlotMachineUI.clear_terminal()

            if print_header:
                SlotMachineUI.print_header(slot_machine)

            if print_slot_machine_details:
                SlotMachineUI.print_slot_machine_details(slot_machine)

            is_valid = False

            for option in options:
                print(option)

            print("")

            user_selection = input(f"{prompt_message}: ")

            if not user_selection:
                if can_press_enter:
                    is_valid = True
            else:
                for selection in valid_selections:
                    if user_selection.lower() == selection.lower():
                        is_valid = True

            if is_valid:
                break
            else:
                print("Invalid input. Please provide a valid selection option.")
                input("Press [Enter] to continue...")

        return user_selection

    @staticmethod
    def prompt_for_amount(slot_machine: SlotMachine, prompt_message: str, is_currency: bool, min: float, max: float) -> float:
        value = 0

        while True:
            SlotMachineUI.clear_terminal()
            SlotMachineUI.print_header(slot_machine)

            try:
                if is_currency:
                    value = float(input(f"{prompt_message} (min: ${min} - max: ${max})? $"))
                else:
                    value = int(input(f"{prompt_message} (min: {min} - max: {max})? "))

                if min <= value <= max:
                    break
                else:
                    if is_currency:
                        print(f"Invalid value. Amount must be between ${min} and ${max}.")
                    else:
                        print(f"Invalid value. Number must be between {min} and {max}.")

                    input("Press [Enter] to continue...")

            except ValueError:
                if is_currency:
                    print("Invalid input. Please enter a number.")
                else:
                    print("Invalid input. Please enter a digit.")

                input("Press [Enter] to continue...")

        return value
