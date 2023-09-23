class SlotMachine:
    def __init__(self) -> None:
        self.title: str = "Basic Slot Machine"
        self.symbols_weight = {"A": 5, "B": 10, "C": 15, "D": 30, "E": 40}
        self.payout_table = {"A": 50, "B": 25, "C": 20, "D": 15, "E": 10}
        self.lines_count: int = 3
        self.min_lines_count = 1
        self.max_lines_count = 5
        self.reels_count: int = 3
        self.bet_amount: float = 1
        self.min_bet_amount: float = 1
        self.max_bet_amount: float = 100
        self.selected_lines_count: int = 1
        self.balance = 0
        self.reels = []

    def set_lines_count(self) -> None:
        """
        Prompts user to select slot machine lines count within the allowed range (1 to 5)
        """

        while True:
            try:
                count = int(input(f"How many lines would you like to have ({self.min_lines_count} to {self.max_lines_count})? "))

                if self.min_lines_count <= count <= self.max_lines_count:
                    self.rows_count = count
                    break
                else:
                    print(f"Please enter a number between {self.min_lines_count} and {self.max_lines_count}")

            except ValueError:
                print("Invalid input. Please enter valid a number.")

    def set_bet_amount(self) -> None:
        """
        Prompts user to set the bet amount within the allowed range ($1 to $100).
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

    def set_selected_lines_count(self) -> None:
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
