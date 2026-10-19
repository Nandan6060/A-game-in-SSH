import time
from utils import slow_print

correct_order = ["blue", "red", "green"]

knock_lines = ["Something knocks from inside the boiler. Once.",
               "The knocking comes again, louder. Whatever it is, it's trying to get out.",
               "The knocking is almost a pounding now",
]

def play(inventory):
  toolbox_opened = False
  fuse_placed = False
  valve_order = []
  valves_solved = False
  knocks = 0

  slow_print("You run through the bedroom door. It slams shut behind you.")
  slow_print("You fall down a short flight of stairs into a basement")
  slow_print("Cold water covers your ankles. The only light is a dim red bulb.")
  slow_print("A huge old boiler stands in the middle of the room, with three pipes coming out of it: blue, red, and green.")
  slow_print("On the far wall is a locked iron gate, and next to it is a fuse box with an empty slot")

  while True:
    action = input("What do you want to do? \n 1. look at the tool box" \
    "\n 2. look at the clipboard" \
    "\n 3. look at the fuse box" \
    "\n 4. turn the valves" \
    "\n 5. look at the boiler" \
    "\n 6. look at the iron gate" \
    "\n 7. check inventory: ")

    if action == "1":
      if toolbox_opened:
        slow_print("You already searched the toolbox. It's empty now.")
      else:
        slow_print("The rusty toolbox creaks open. Inside is a fuse and wrench. (+1 fuse)")
        inventory.append("fuse")
        toolbox_opened = True

    elif action == "2":
      slow_print("A maintenance note hangs from a nail, in shaky handwriting: ")
      slow_print("'Drain it before you heat it. Heat it before you cool it. Never, ever the other way.'")

    elif action == "3":
      if fuse_placed:
        slow_print("The fuse box hums quietly. The fuse sits snug in its slot.")
      elif "fuse" not in inventory:
        slow_print("The fuse box has an empty slot. You need a fuse")
      else:
        slow_print("You push the fuse into the slot. A faint electric hum fills the room")
        slow_print("A small green light blinks on above the iron gate")
        inventory.remove("fuse")
        fuse_placed = True

    elif action == "4":
      slow_print("Three valve wheels: blue, red, and green. Their paint flaking.")
      if valves_solved:
        slow_print("The boiler is running. You dont dare touch the valves again.")
      else:
        while  True:
          choice = input("Turn which valve? \n 1. red \n 2. green \n 3. blue \n (or press enter to cancel):")
          if choice == "":
            slow_print("You step back from the valves.")
          elif choice == "1" or choice == "2" or choice == "3":
            if choice == "1":
              color = "red"
              slow_print("You turn the red valve. The pipe get warmer under your hand.")
            elif choice == "2":
              color = "green"
              slow_print("You turn the green valve. A cold hiss comes from the pipe")
            else:
              color = "blue"
              slow_print("You turn the blue valve. Water gurgles somewhere")

            valve_order.append(color)

            if valve_order != correct_order[:len(valve_order)]:
              slow_print("The pipes shudder and bang. The water around your ankles rises an inch.")
              slow_print("All three valves spring back to where they started")
              valve_order = []
            elif len(valve_order) == 3:
              slow_print("The boiler roars to life. The whole room shakes")
              slow_print("The knocking inside stops all at once.")
              valves_solved = True
              break
            else:
              slow_print(knock_lines[min(knocks, len(knock_lines) - 1)])
              knocks += 1

          else:
            slow_print("That's not a valve")
            break

    elif action == "5":
      if not valves_solved:
        slow_print("The boiler is cold and silent. But you swear you heard a faint knock from inside.")
      else:
        slow_print("The boiler room is warm now. On its little round window, a handprint wipes clear from the inside.")
        slow_print("The symbol is stamped on the boiler door, the same one from the rooms above.")
        slow_print("You step back. The handprint is small, like a child's.")

    elif action == "6":
      slow_print("A heavy iron gate blocks the far wall. A small light above it is dark.")

      if not fuse_placed:
        slow_print("The gate has no power. The fuse box next to it is dead.")

      elif fuse_placed and not valves_solved:
        slow_print("The gate is powered but the lock is frozen solid. Something in the boiler might thaw it.")

      elif fuse_placed and valves_solved:
        slow_print("The gate's lock hums, then clicks. The iron bars swing open.")
        slow_print("You climb the ladder on the other side. Behind you the boiler knocks once more.")
        time.sleep(1)
        return

    elif action == "7":
      if len(inventory) == 0:
        slow_print("Your inventory is empty")
      else:
        slow_print("You are carrying:")
        for item in inventory:
          slow_print("- " + item)

    else:
      slow_print("Thats not an option")
    