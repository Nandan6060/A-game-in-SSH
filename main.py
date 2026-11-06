from utils import slow_print

import lvl1
import lvl2
import lvl3
import lvl4
import lvl5
import lvl6
import lvl7

inventory = []

try:
  slow_print("=== THE MARK ===")
  slow_print("Chapter One: The House That Waited")
  print()
  input("Press enter to begin...")
  print()

  lvl1.play(inventory)
  lvl2.play(inventory)
  lvl3.play(inventory)
  lvl4.play(inventory)
  lvl5.play(inventory)
  lvl6.play(inventory)
  lvl7.play(inventory)

  print()
  slow_print("Thank you for playing Chapter One Of The Mark! Stay tuned for Chapter Two!")
except (KeyboardInterrupt, EOFError):
  print("\nThanks for playing!")