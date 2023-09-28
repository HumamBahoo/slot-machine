# Slot Machine

## Introduction

This is a simple text-based slot machine game in the terminal, written in python for learning purposes and following Object-Oriented Programming principles.

## The User Experience

I aimed for a clean and simple user experience, where the terminal clears up after every action so there will be no distraction from old messages or information.

## Game Settings

Game settings can be set from the game settings menu

[Game-Menu-Pic]

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

If a user has made a bet of $5 per line and have selected 2 lines (the total bet is $10). After spinning, only one line matched with a "B", the prize would be **$250** because `$10 * 25 = $250`.

> The `Jackpot` functionality has not been implement.
