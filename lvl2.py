import time
from utils import slow_print
import random

creepy_lines = [
  "Somewhere behind you, a book slides back into place.",
  "Footsteps cross the ceiling above you, then stop.",
  "The bulb flickers. For a second, a shadow moves between the shelves",
  "You hear a quiet whisper, but you cant make out the words",
  "A page turns by itself on the desk.",
]

figure_lines = [
  "The painting is an empty field. Far away, a tiny figure stands in the grass.",
  "The figure in the painting is closer now. You're sure it wasnt there before.",
  "The figure is halfway across the field. It seems to be facing you.",
  "The figure is almost at the edge of the frame. You can see its arms hanging at its sides.",
  "The field is empty. The figure is gone from the painting.",
]

def play(inventory):
  light_on = False
  chain_found = False
  painting_opened = False
  painting_looks = 0
  catalogue_read = False
  almanac_read = False
  whisper_turn = 0
  whisper_heard = False
  drawer_opened = False
  turns = 0

  slow_print("You step through the door. It slams shut behind you.")
  slow_print("It's pitch black you can't see your own hands")

  while not light_on:
    if not chain_found:
      choice = input ("1. feel around: ")
    else:
      choice = input("1. feel around:  \n2. pull the chain: ")

    if choice == "1":
      if not chain_found:
        slow_print("You wave your hand in the dark. Something thin and cold brushes your fingers. It's chain hanging from the ceiling.")
        chain_found = True
      else:
        slow_print("You feel the cold chain hanging infront of you. Nothing else")
    elif choice == "2" and chain_found:
      slow_print("You pull the chain.")
      time.sleep(1)
      slow_print("Click.")
      light_on = True 
    else:
      slow_print("That's not an option")
  slow_print("A bare bulb flickers on and swings slowly above you.")
  slow_print("You're in an old library. Tall shelves lean over you, There's a reading desk, a rolling ladder, and a heavy door at the back.")
  slow_print("On the wall hangs a painting you recognize: the same landscape from the room you just left.")
  time.sleep(1)
  slow_print("Somewhere behind you, a book slides into place. You turn around. Nothing.")

  while True:
    turns += 1
    action = input("What do you want to do ? \n 1. look at the painting \n 2. look at the desk " \
    "\n 3. climb the ladder \n 4. look at the shelves \n 5. look at the back door" \
    "\n 6. check inventory: ")

    creep_ok = True

    if action == "1":
      slow_print("You walk up to the painting. In the corner of the frame is the same small keyhole")
      if painting_opened:
        slow_print("The painting hangs open. The hollow behind it is empty now.")
      elif "silver key" in inventory:
        slow_print("You try the silver key. It slides in smoothly")
        slow_print("The painting swings open like a cupboard door. Inside the hollow is a torn reading log.")
        slow_print("It reads: 'The Fire - March 3rd. The Sea - March 1st. The Moon - March 2nd.'")
        inventory.remove("silver key")
        inventory.append("reading log")
        painting_opened = True
      else:
        slow_print("You have nothing that fits the keyhole")
      slow_print(figure_lines[min(painting_looks, len(figure_lines)-1)])
      painting_looks += 1
    elif action == "2":
      slow_print("The desk is covered in dust. A dead lamp sits on it, and a library catalogue lies open.")
      slow_print("One entry is circled in red pen: 'The Watcher's Almanac. Top shelf, far left.'")
      catalogue_read = True
      if drawer_opened:
        slow_print("The little drawer is already open and empty")
      else:
        slow_print("There's a small drawer with a 4-digit dial lock.")
        code = input("Enter 4 digit code (or press enter to cancel): ")
        if code == "":
          slow_print("You step back from the desk.")
        elif code == "6145":
          slow_print("The dial clicks. The drawer slides open.")
          slow_print("Inside is a heavy iron key. (+1 iron key)")
          inventory.append("iron key")
          drawer_opened = True
        else:
          slow_print("The dial spins, but nothing happens.")

    elif action == "3":
      if not catalogue_read:
        slow_print("You climb the ladder. There are a lot of books up here. You dont know what to look for.")
      elif almanac_read:
        slow_print("You already read the Almanac. The riddle is still on its first page")
      else:
        slow_print("You roll the ladder to the far left and climb to the top shelf.")
        slow_print("The Watcher's Almanac is right where the catalogue said. You open it.")
        slow_print("On the first page, in faded ink: 'What happens to ink, and to memory, if you wait long enough?'")
        almanac_read = True
        whisper_turn = turns + 1

    elif action == "4":
      slow_print("Among the dusty spines, three books stand out. Each has a number stamped on it:")
      slow_print("The Sea (7), The Moon (2), The Fire (5).")
      if "reading log" in inventory:
        slow_print("You check the reading log: The Sea came first, then the Moon, then the Fire.")

    elif action == "5":
      slow_print("The back door is heavy and old. It has an iron keyhole and a 3 digit dial.")
      slow_print("Carved around the keyhole is a symbol. You've seen it before: it's the same one from the table and journal.")
      if "iron key" not in inventory:
        slow_print("It's locked tight. You need a key.")
      else:
        slow_print("The iron key has the same symbol stamped on its handle")
        code = input("You put the iron key in the lock. Enter the 3 digit code (or press enter to cancel): ")
        if code == "":
          slow_print("You step back from the door.")
        elif code == "725":
          slow_print("The dial clicks into place. The key turns.")
          time.sleep(1)
          slow_print("Behind you the bulb dies.")
          time.sleep(1)
          slow_print("In the dark, someone breathes right behind your ear.")
          slow_print("'You forgot to look behind you'")
          time.sleep(1)
          slow_print("You throw the door open and run through. The library closes behind you.")
          inventory.remove("iron key")
          return
        else:
          slow_print("The dial spins. Nothing happens")

    elif action == "6":
      if len(inventory) == 0:
        slow_print("Your inventory is empty.")
      else:
        slow_print("You are carrying: ")
        for item in inventory:
          slow_print("- " + item)

    else:
      slow_print("That's not an option.")
      creep_ok = False

    if almanac_read and not whisper_heard and turns >= whisper_turn:
      time.sleep(1)
      slow_print("The bulb flickers. A voice whispers from between the shelves: ")
      slow_print("'The dead are filed in order. A is the first and the rest follow.'")
      whisper_heard = True
    elif creep_ok and random.randint(1, 4) == 1:
      if whisper_heard and random.randint(1, 3) == 1:
        slow_print("'The dead are filed in order. A is the first and the rest follow.'")
      else:
        slow_print(random.choice(creepy_lines))


