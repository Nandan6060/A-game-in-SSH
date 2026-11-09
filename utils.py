import os
import sys
import select
import time

try:
  import msvcrt

  def key_pressed():
    if msvcrt.kbhit():
      msvcrt.getch()
      return True
    return False

except ImportError:
  def key_pressed():
    if select.select([sys.stdin], [], [], 0)[0]:
      sys.stdin.readline()
      return True
    return False

OVER_SSH = bool(os.environ.get("SSH_CONNECTION"))


def slow_print(text, delay=0.03):
  if OVER_SSH:
    print(text, flush=True)
    time.sleep(min(0.5, len(text) * delay / 10))
    return
  current = delay
  for letter in text:
    print(letter, end="", flush=True)
    if key_pressed():
      current = delay / 8
    time.sleep(current)
  print()