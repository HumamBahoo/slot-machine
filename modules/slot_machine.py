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


