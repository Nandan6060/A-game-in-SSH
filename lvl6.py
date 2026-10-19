import time
from utils import slow_print

wall_word = "EMOH"
mirror_note = "02:8"


def play(inventory):
  iron_solved = False
  handle_found = False
  note_read = False

  slow_print("You climb through the attic hatch and into a long hall.")
  slow_print("Mirrors cover both walls from floor to ceiling. There's no window. A faint grey light seems to come from the mirrors themselves.")
  slow_print("You see yourself a hundred times over.")
  slow_print("When you raise your hand, your reflection raises its hand half a second late.")

  while True:
    action = input("What do you want to do? \n 1. read the writing on the wall" \
    "\n 2. look into the mirror next to the writing " \
    "\n 3. look at the iron-framed mirror" \
    "\n 4. look at the third mirror from the left" \
    "\n 5. look at the far mirror at the end of the hall" \
    "\n 6. check inventory: ")

    if action == "1":
      slow_print("Scratched into the plaster is a single word: " + wall_word)
      slow_print("It means nothing to you. But the mirror right beside it catches your eye.")

    elif action == "2":
      slow_print("You look into the mirror. The scratches on the wall flip around, and now they read: " + wall_word[::-1])
      if handle_found and not note_read:
        slow_print("In the mirror, the backwards note beside the handle reads: " + mirror_note[::-1])
        slow_print("8:20. You whisper it under your breath so you won't forget.")
        slow_print("Somewhere in the house, a clock chimes once. Then stops.")
        note_read = True
      elif note_read:
        slow_print("The note in the mirror still reads " + mirror_note[::-1] + ".")
      else:
        slow_print("Your reflection stares back. You get the feeling there's more to see in here.")

    elif action == "3":
      slow_print("An iron-framed mirror at the end of the hall. A brass plate under it reads: 'Say what you see.'")
      if iron_solved:
        slow_print("The frame is quiet now. Your reflections have stopped copying you.")
      else:
        word = input("What do you say? (or press enter to cancel): ")
        if word == "":
          slow_print("You step back from the mirror.")
        elif word.lower() == "home":
          slow_print("The iron frame clicks.")
          slow_print("Every reflection in the hall freezes. Then, one by one, they raise an arm and point at the same mirror: the third one from the left.")
          iron_solved = True
        else:
          slow_print("Nothing happens. Your reflection tilts its head.")

    elif action == "4":
      if not iron_solved:
        slow_print("Your reflection smiles a little too widely. Nothing else happens.")
      elif handle_found:
        slow_print("The hidden handle is still there, and so is the note.")
      else:
        slow_print("In the frame of this mirror is a small hidden handle.")
        slow_print("Taped behind it is a scrap of paper. The writing is backwards: " + mirror_note)
        handle_found = True

    elif action == "5":
      slow_print("At the end of the hall, in the far mirror, a woman stands behind your reflection.")
      slow_print("She is closer than she has ever been. She doesn't move.")
      if not handle_found:
        slow_print("The glass is cold and solid. You can't get through.")
      elif not note_read:
        slow_print("You grip the handle, then stop. The backwards note still doesn't make sense. You don't feel ready to leave yet.")
      else:
        slow_print("You pull the hidden handle. The mirror swings open like a door.")
        slow_print("You step through. Behind you, a hundred reflections turn to watch you as you go.")
        time.sleep(1)
        return

    elif action == "6":
      if len(inventory) == 0:
        slow_print("Your inventory is empty.")
      else:
        slow_print("You are carrying:")
        for item in inventory:
          slow_print("- " + item)

    else:
      slow_print("That's not an option")