import time
from utils import slow_print

dollhouse_lines = [
  "The dollhouse is a tiny copy of the library. A tiny figure stands in the far corner.",
  "The tiny figure is closer to the bedroom door now.",
  "The tiny figure stands right next to the bedroom door.",
  "The tiny figure is gone from the library . You hear the door handle rattle softly.",
]

def play(inventory):
  pillow_searched = False
  music_box_open = False
  dollhouse_moved = False
  dollhouse_looks = 0
  clock_solved = False
  wardrobe_open = False

  slow_print("You run through the library door. It slams shut behind you.")
  slow_print("You're in a child's bedroom. A small bed, a wardrobe, a dresser with a music box, and a dollhouse.")
  slow_print("On the wall, a clock stopped at 11:20. The only door has a dial lock.")

  while True:
    action = input("What do you want to do? \n 1. look at the pillow" \
    "\n 2. look at the music box" \
    "\n 3. look at the dollhouse" \
    "\n 4. look at the wall clock" \
    "\n 5. look at the wardrobe" \
    "\n 6. look at the door" \
    "\n 7. check inventory: ")

    if action == "1":
      if pillow_searched:
        slow_print("You already searched the pillow. Nothing else is there.")
      else:
        slow_print("You lift the pillow and find a small brass winding key. (+1 winding key)")
        inventory.append("winding key")
        pillow_searched = True

    elif action == "2":
      slow_print("On the lid of the music box is the symbol you've seen before.")
      if music_box_open:
        slow_print("The lullaby has stopped. The diary page is still inside.")
      elif "winding key" not in inventory:
        slow_print("It won't play. There's a small keyhole on the side for winding it.")
      else:
        slow_print("You wind the music box. A slow lullaby starts to play.")
        slow_print("The lid pops open. Inside is a folded page from a child's diary.")
        slow_print("'She stopped every clock the night I left. I'll set them right when i see her again.'")
        inventory.remove("winding key")
        music_box_open = True

    elif action == "3":
      if not dollhouse_moved:
        slow_print("You push the dollhouse aside. Scratched into the floorboards behind it is the time 7:45.")
        dollhouse_moved = True
      slow_print(dollhouse_lines[min(dollhouse_looks, len(dollhouse_lines) - 1)])
      dollhouse_looks += 1

    elif action == "4":
      if clock_solved:
        slow_print("The clock is set to 7:45. The panel in its face is open and empty.")
      else:
        slow_print("The clock is stopped at 11:20. The hands look like they can be turned")
        setting = input("Set the clock to (set it like , or press enter to cancel: ")
        if setting == "":
          slow_print("You step back from the clock.")
        elif setting == "7:45":
          slow_print("The hands click into place. A panel in the clock's face slides open")
          slow_print("Inside is a small silver lever. You pull it")
          slow_print("Somewhere across the room, wood creaks.")
          clock_solved = True
        else:
          slow_print("The hands move, but nothing happens")

    elif action == "5":
      if not clock_solved:
        slow_print("The wardrobe door is stuck tight. Something inside is holding it shut.")
      elif wardrobe_open:
        slow_print("The wardrobe is open. The little coat hangs inside, with nothing else in it.")
      else:
        slow_print("The wardrobe door swigns open. Inside hangs a child's coat.")
        slow_print("In the pocket is a ticket stamped 9:10. (+1 coat ticket)")
        slow_print("9:10 You stare at the time for a moment. Something tells you it's important")
        slow_print("Pinned to the coat is a note: 'The door opens only at the time she left'")
        inventory.append("coat ticket")
        wardrobe_open = True

    elif action == "6":
      slow_print("The door has a dial lock. It wants a time.")
      code = input("Set the clock to, or press enter to cancel: ")
      if code == "":
        slow_print("You step back from the door.")
      elif code == "11:20":
        slow_print("The dial clicks, then spins back by itself. The clock lied to you")
      elif code == "9:10":
        slow_print("The dial clicks. The door unlocks")
        time.sleep(1)
        slow_print("Behind you the lullaby starts playing again, all on its own.")
        slow_print("You glance at the dollhouse. The tiny figure is gone from the library.")
        time.sleep(1)
        slow_print("You run through the door.")
        time.sleep(1)
        return
      else:
        slow_print("The dial spins. The door doesn't budge")

    elif action == "7":
      if len(inventory) == 0:
        slow_print("Your inventory is empty.")
      else:
        slow_print("You are carrying: ")
        for item in inventory:
          slow_print("- " + item)
