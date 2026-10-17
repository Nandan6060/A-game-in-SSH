import time

def slow_print(text, delay=0.03):
  for letter in text:
    print(letter, end="", flush = True)
    time.sleep(delay)
  print()