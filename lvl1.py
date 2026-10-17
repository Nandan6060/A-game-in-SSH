import time
from utils import slow_print


def play(inventory):
  journal_opened = False
  drawer_opened = False
  chair_searched = False
  door_hint_found = False
  matchbox_taken = False
  window_solved = False

  slow_print("You wake up in a dark locked room.  " \
  "You need to find a way out.")
  slow_print("The air is damp and you can hear the faint " \
  "sound of dripping water.")
  slow_print("You notice a small window high up on the wall," \
  " but it's too far to reach.")
  slow_print("There is a door in front of you, but it's locked.")
  slow_print("You look around")
  slow_print("There's a small table in the corner, a chair, and " \
  "a bookshelf of dusty old books.")
  slow_print("A strange painting on the wall catches your eye. " \
  "It depicts a serene landscape, but something about it feels off.")

  while True:
    action = input("What do you want to do? \n 1. look at painting, \n 2. look at bookshelf, " \
    "\n 3. look at the table,\n 4. look at the door,\n 5. look at the chair, " \
    "\n 6. look at the window \n 7. Check Inventory: ")

    if action == "1":
      slow_print("You approach the painting and notice that the colors seem to shift as you look at it." \
      "You feel a strange sensation, as if the painting is alive.")
      slow_print("Upon closer inspection, you see a small keyhole hidden in the corner of the frame.")
      if "silver key" in inventory:
        slow_print("You try the silver key. The keyhole seems to push away. The key won't go in.")
      else:
        slow_print("You have nothing which fits in the keyhole.")
      if journal_opened:
        slow_print("Wait... the sun in the painting is in the wrong corner")
        slow_print("Scratched into the paint right at the sun is a number: 7314. (You make a mental note of it.)")

    elif action == "2":
      slow_print("You walk over to the bookshelf and see that it's filled with dusty old books. Most of them are too worn to read, but one book catches your eye. It's a leather-bound journal with a lock on it.")
      if journal_opened:
        slow_print("You already opened the journal. The page says: 'The sun is never where it should be. Look where the light lies.'")
      elif "brass key" not in inventory:
        slow_print("You try to open it, but it's locked tight.")
      elif not journal_opened:
        slow_print("The brass key fits perfectly into the lock.")
        slow_print("You open the journal and find a series of cryptic notes and drawings. One page has a strange symbol that matches the one on the piece of paper you found on the table.")
        slow_print("A small silver key falls out of the journal. You pick it up and put it in your pocket.")
        slow_print("A page says: 'The sun is never where it should be. Look where the light lies.'")
        inventory.remove("brass key")
        inventory.append("silver key")
        journal_opened = True
      

    elif action == "3":
      slow_print("The table is small and covered in dust. You notice a few items on it: a candle, a matchbox, and a small piece of paper with a strange symbol drawn on it.")

      if not matchbox_taken:
        slow_print("You pick up the matchbox. It might come in handy.")
        inventory.append("matchbox")
        matchbox_taken = True
      if drawer_opened:
        slow_print("You already opened the hidden drawer. It's empty now.")
      elif "silver key" in inventory:
        slow_print("Wait... the same symbol is carved into the side of the table, right above a tiny hidden drawer.")
        slow_print("You slide the silver key into the lock. It fits perfectly. The drawer opens!")
        slow_print("Inside is a folded note: 'Numbers lie. Trust what you can see.'")
        drawer_opened = True

    elif action == "4":
      slow_print("The door is solid metal. There's no keyhole or handle, just a small keypad. It seems you'll need a code to unlock it.")
      code = input("Enter 4 digit code: (or press enter to cancel): ")
      if code == "":
        slow_print("You step back from the door.")
      elif code == "7314":
        if door_hint_found:
          slow_print("The keypad beeps happily again... but the door stays shut. You already know its lying")
        else:
          slow_print("The keypad beeps happily, But the door doesnt move.")
          slow_print("Something slides out from under the door. It's a piece of paper")
          slow_print("'Did you really think it would be that easy to escape the room? The door was never the way out, The real way out is where the light comes from")
          door_hint_found = True
      elif code == "2580":
        slow_print("The keypad glows green. The door creaks open.")
        slow_print("Light floods in. You step through... ")
        time.sleep(2)
        slow_print("...")
        slow_print("The door slams shut behind you.")
        time.sleep(1)      
        return

      else:
        slow_print("The keypad buzzes. Wrong code.")

    elif action == "5":
      if chair_searched:
        slow_print("You already searched the chair. There's nothing else to find.")
      else:
        slow_print("The chair is old and rickety. As you sit down, you notice a small drawer underneath the seat. You open it and find a small key inside. (+1 brass key)")  
        inventory.append("brass key")
        slow_print("Brass key added to inventory.")
        chair_searched = True


    elif action == "6":
      if not door_hint_found:
        slow_print("The window is too high to reach. You dont see a reason to try")
      elif window_solved:
        slow_print("You already saw the number on the sill 2580")
      elif "matchbox" not in inventory:
        slow_print("You drag the chair under the window and climb up")
        slow_print("It's pitch dark. You can't see anything. You need some light")
      else:
        slow_print("You drag the chair under the window and climb up.")
        slow_print("You strike a match. In the flickering light you see numbers scratched into the sill: 2580")
        slow_print("'Numbers lie. Trust what you can see.' ...maybe this one is true.")
        inventory.remove("matchbox")
        window_solved = True

    elif action == "7":
      if len(inventory) == 0:
        slow_print("Your inventory is empty.")
      else:
        slow_print("You are carrying:")
        for item in inventory:
          slow_print("- " + item)


    else:
      slow_print("Thats not an option")

                 