# Slot Machine

## Introduction

This is a simple text-based slot machine game in the terminal, written in Python3 for learning purposes.

## The User Experience

I aimed for a clean and simple user experience, where the terminal clears up after every action so there will be no distraction from old messages or information.

## Game Settings

Game settings can be set from the game settings menu

![image](https://github.com/HumamBahoo/slot-machine/assets/61947862/ddf5b4cf-1894-46fb-a318-2af09b0a70c9)

### Reels and Rows/Lines Count

The slot machine has 3 reels only, and 1 row by default. The player can make changes to the number of rows up to the maximum of 5. However, to keep the experience simple, the number of reels cannot be changed.

### Selected Lines Count

The number of lines can be set from **1** line to a maximum of the current number of rows/lines the machine has.

### Bet Amount

A player can place bets between a minimum of **$1** to a maximum of **$100** per line.

> The total bet amount is calculated by multiplying the number of selected lines by the bet amount. For example, if the bet amount is $2 and there 3 lines have been selected. The total bet amount would be $6.

### Depositing Funds

A player can make deposits between a minimum of **$1** to a maximum of **$1000**.

## Game Play

### Symbols and Payouts

There are 5 symbol with the following payout rate:

- A: 50
- B: 25
- C: 15
- D: 10
- E: 5

If a user has made a bet of $5 per line, and after spinning, only one line matched with a "D". The prize would be **$50** because `$5 * 10 = $50`. However, if there is no match (loss), the total bet amount of $10 ($5 \* 2 selected lines) will be deducted from the balance.

![image](https://github.com/HumamBahoo/slot-machine/assets/61947862/67734fd2-ce75-446a-97b5-6be3cba418be)

> The `Jackpot` functionality has not been implement.

## Installation

Using `bash` or `PowerShell`, go to the directory where you want to clone the repo:

```sh
git clone https://github.com/HumamBahoo/slot-machine.git
```

Then:

```sh
python slot-machine/main.py
```

> Python3 is required.
