import random


# Custom Exception
class SlotMachineError(Exception):
    pass


class SlotMachine:
    def __init__(self) -> None:
        self._title: str = ""
        self._symbols_weight: dict[str, int] = {"A": 5, "B": 10, "C": 15, "D": 30, "E": 40}
        self._payout_table: dict[str, int] = {"A": 50, "B": 25, "C": 20, "D": 15, "E": 10}
        self._min_rows_count: int = 1
        self._max_rows_count: int = 5
        self._rows_count: int = 1
        self._reels_count: int = 3
        self._bet_amount: float = 1
        self._min_bet_amount: float = 1
        self._max_bet_amount: float = 100
        self._selected_lines_count: int = 1
        self._balance: float = 0
        self._reels: list[list[str]] = []
        self._total_winnings_amount: float = 0
        self._winning_lines: dict[int, str] = {}
        self._has_won: bool = False

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        if not title == "" or not title == None:
            self._title = title
        else:
            raise SlotMachineError("Title must not be empty")

    @property
    def symbols_weight(self) -> dict[str, int]:
        return self._symbols_weight

    @property
    def payout_table(self) -> dict[str, int]:
        return self._payout_table

    @property
    def min_rows_count(self) -> int:
        return self._min_rows_count

    @property
    def max_rows_count(self) -> int:
        return self._max_rows_count

    @property
    def rows_count(self) -> int:
        return self._rows_count

    @rows_count.setter
    def rows_count(self, count: int) -> None:
        if self.min_rows_count <= count <= self.max_rows_count:
            self._rows_count = count
        else:
            raise SlotMachineError(f"Rows count must be between {self.min_rows_count} and {self.max_rows_count}")

    @property
    def reels_count(self) -> int:
        return self._reels_count

    @property
    def min_bet_amount(self) -> float:
        return self._min_bet_amount

    @property
    def max_bet_amount(self) -> float:
        return self._max_bet_amount

    @property
    def bet_amount(self) -> float:
        return self._bet_amount

    @bet_amount.setter
    def bet_amount(self, amount: float) -> None:
        if self.min_bet_amount <= amount <= self.max_bet_amount:
            self._bet_amount = amount
        else:
            raise SlotMachineError(f"Bet amount must be between ${self.min_bet_amount} and ${self.max_bet_amount}")

    @property
    def selected_lines_count(self) -> int:
        return self._selected_lines_count

    @selected_lines_count.setter
    def selected_lines_count(self, count: int) -> None:
        if 1 <= count <= self.rows_count:
            self._selected_lines_count = count
        else:
            raise SlotMachineError(f"Selected lines count must be between 1 and the number of machine lines ({self.rows_count})")

    @property
    def balance(self) -> float:
        return self._balance

    def add_to_balance(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
        else:
            raise SlotMachineError(f"Amount must be greater than 0.")

    def subtract_from_balance(self, amount: float) -> None:
        self._balance -= amount

    @property
    def reels(self) -> list[list[str]]:
        return self._reels

    @property
    def total_winnings_amount(self) -> float:
        return self._total_winnings_amount

    def add_to_total_winnings_amount(self, amount: float) -> None:
        self._total_winnings_amount += amount

    def subtract_from_total_winnings_amount(self, amount: float) -> None:
        self._total_winnings_amount -= amount

    @property
    def winning_lines(self) -> dict[int, str]:
        return self._winning_lines

    def update_winning_lines(self) -> None:
        winning_lines: dict[int, str] = {}

        # for each line and up to the number of selected lines, retrieve
        # the line symbol and find if they all match
        for i in range(self.selected_lines_count):
            line_symbols = []
            for reel in self.reels:
                line_symbols.append(reel[i])

            # if all match, then there is a win on the current line
            if all(symbol == line_symbols[0] for symbol in line_symbols):
                winning_lines[i] = line_symbols[0]

        if len(winning_lines) > 0:
            self.has_won = True
            self._winning_lines = winning_lines
        else:
            self.has_won = False
            self._winning_lines = {}

    @property
    def has_won(self) -> bool:
        return self._has_won

    @has_won.setter
    def has_won(self, value: bool) -> None:
        self._has_won = value

    def spin(self) -> None:
        """
        Simulates spinning slot machine reels
        """

        ##
        # TODO replace algorithm with this one, which
        # will theoretically make sure there is an accurate probability:
        #
        # 1- reel init method: a method to initialize all reels
        #   - reset reels
        #   - build pool
        #   - each reel in the list of reels will have the current pool
        # 2- spin method: a method to spin all reels
        #   - redistribute each reel content randomly
        ##

        # reset reels
        self._reels = []

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

    def calculate_spin_outcome(self) -> float:
        """
        Returns the total amount of winning or loss (positive if won, and negative if lost)
        """

        total_amount = 0

        if self.has_won:
            # calculate payout and add to total amount
            for _, symbol in self.winning_lines.items():
                current_line_payout = self.payout_table[symbol] * self.bet_amount
                total_amount += current_line_payout
        else:
            total_amount = self.bet_amount * self.selected_lines_count

        return total_amount

    def display_reels(self) -> None:
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

            if i in self.winning_lines:
                winning_amount_string = f" => Win: ${self.payout_table[self.winning_lines[i]] * self.bet_amount}"

            # print the result
            print(f"Line {i+1} {line_status_string}: {line_symbols_string} {winning_amount_string}")
