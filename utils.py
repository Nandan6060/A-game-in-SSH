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

CHUNK = 3 if os.environ.get("SSH_CONNECTION") else 1

def slow_print(text, delay=0.03):
  current = delay * CHUNK
  for i in range(0, len(text), CHUNK):
    print(text[i:i + CHUNK], end ="", flush = True)
    if key_pressed():
      current = delay * CHUNK/8
    time.sleep(current)
  print()