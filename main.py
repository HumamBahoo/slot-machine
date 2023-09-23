import os
from modules.slot_machine import SlotMachine

def clear_terminal():
    clear_cmd = "cls" if os.name == 'nt' else "clear"
    os.system(clear_cmd)

def main():
    clear_terminal()

if __name__ == '__main__':
    main()