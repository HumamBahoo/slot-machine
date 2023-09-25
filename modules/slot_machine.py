import random


class SlotMachine:
    def __init__(self) -> None:
        self.title: str = "Basic Slot Machine"
        self.symbols_weight: dict = {"A": 5, "B": 10, "C": 15, "D": 30, "E": 40}
        self.payout_table: dict = {"A": 50, "B": 25, "C": 20, "D": 15, "E": 10}
        self.rows_count: int = 3
        self.min_rows_count: int = 1
        self.max_rows_count: int = 5
        self.reels_count: int = 3
        self.bet_amount: float = 1
        self.min_bet_amount: float = 1
        self.max_bet_amount: float = 100
        self.selected_lines_count: int = 1
        self.balance: float = 0
        self.player_credit: str = 1000.00
        self.reels: list = []
        self.total_winnings: float = 0

    def prompt_for_rows_count(self) -> None:
        """
        Prompts user to select number of rows the slot machine has within the allowed range (1 to 5)
        """

        while True:
            try:
                count = int(input(f"How many rows would you like to have ({self.min_rows_count} to {self.max_rows_count})? "))

                if self.min_rows_count <= count <= self.max_rows_count:
                    self.rows_count = count
                    break
                else:
                    print(f"Please enter a number between {self.min_rows_count} and {self.max_rows_count}")

            except ValueError:
                print("Invalid input. Please enter valid a number.")

    def prompt_for_bet_amount(self) -> None:
        """
        Prompts user to set the bet amount the would like to place per line within the allowed range ($1 to $100).
        It will validate if there is enough balance to successfully set the desired bet amount.
        """

        if self.balance > 0:
            while True:
                try:
                    amount = float(input(f"How much bet would you like to make (${self.min_bet_amount}-${self.max_bet_amount})? $"))

                    if self.min_bet_amount <= amount <= self.max_bet_amount:
                        if amount > self.balance:
                            print(f"There is only ${self.balance} in your balance. Please try again.")
                        else:
                            self.bet_amount = amount
                            break
                    else:
                        print(f"Please enter a number between ${self.min_bet_amount} and ${self.max_bet_amount}")

                except ValueError:
                    print("Invalid input. Please enter a valid number")
        else:
            print("Your balance is $0. Add more funds and try again later.")

    def prompt_for_selected_lines_count(self) -> None:
        """
        Prompts user to select the number of lines they want to play.
        """

        while True:
            try:
                count = int(input(f"How many lines would you like to select (1-{self.rows_count})? "))

                if 1 <= count <= self.rows_count:
                    self.selected_lines_count = count
                    break
                else:
                    print(f"Please enter a number between 1 and {self.rows_count}.")

            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def add_to_balance(self) -> None:
        """
        Prompts user to select the amount of funds they would like to deposit into the slot machine from their credit.
        """

        while True:
            try:
                amount = float(input(f"How much would you like to deposit ($1-${self.player_credit})? $"))

                if 1 <= amount <= self.player_credit:
                    self.balance += amount
                    self.player_credit -= amount
                    print(f"Funds added. Your current balance is ${self.balance} and you have ${self.player_credit}.")
                    break
                else:
                    if amount < 1:
                        print("The minimum amount to deposit is $1. Please try again.")
                    else:
                        print(f"You only have ${self.player_credit}. Please try again.")

            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def spin(self) -> None:
        """
        Simulates spinning of slot machine reels.
        """

        # reset reels
        self.reels = []

        # build pool
        pool = []
        for symbol, weight in self.symbols_weight.items():
            pool += symbol * weight

        # randomly fill out each reel with symbols from the pool
        for _ in range(self.reels_count):
            current_reel_symbols = []

            for _ in range(self.rows_count):
                picked_symbol = random.choice(pool)
                pool.remove(picked_symbol)

                # append to the current reel
                current_reel_symbols.append(picked_symbol)

            # append the current reel to the list of reels
            self.reels.append(current_reel_symbols)

    def get_winning_lines(self) -> dict:
        winning_lines = {}

        for i in range(self.selected_lines_count):
            line_symbols_list = []

            for reel in self.reels:
                line_symbols_list.append(reel[i])

            # find if all symbols match based on the first one
            if all(symbol == line_symbols_list[0] for symbol in line_symbols_list):
                winning_lines[i] = line_symbols_list[0]

        return winning_lines

    def calculate_winning(self, winning_lines: dict) -> float:
        """
        Returns negative number representing the amount lost, and a positive number representing the total amount won.
        """

        calculated_value = 0

        if len(winning_lines) == 0:
            calculated_value = -(self.bet_amount * self.selected_lines_count)
        else:
            for _, line_symbol in winning_lines.items():
                payout = self.payout_table[line_symbol] * self.bet_amount
                calculated_value += payout

        return calculated_value

    def update_balance(self, amount: float) -> None:
        self.balance += amount

    def update_total_winnings(self, amount: float) -> None:
        self.total_winnings += amount

    def display_reels(self, winning_lines: dict = {}) -> None:
        """
        Displays the current state of slot machine reels and the current winning lines if provided
        """

        # iterate through each line to the number of lines
        for i in range(self.rows_count):
            # get all line symbols by iterating through each reel and extract the symbol at the current line.
            line_symbols = []
            for reel in self.reels:
                line_symbols.append(reel[i])

            # create lines symbols string
            line_symbols_string = " | ".join(line_symbols)

            # set line status string based on how many lines has been selected
            line_status_string = "[selected]" if i < self.selected_lines_count else f"{' ' * len('[selected]')}"

            # set win amount string if there is a win.
            # winning_lines key holds the value of the winning line number
            # winning_lines value holds the winning line symbol
            winning_amount_string = ""

            if i in winning_lines:
                winning_amount_string = f" => Win: ${self.payout_table[winning_lines[i]] * self.bet_amount}"

            # print the result
            print(f"Line {i+1} {line_status_string}: {line_symbols_string} {winning_amount_string}")
