import time
from utils import slow_print

def bad_ending():
  slow_print("You stumble out into a dark, locked room. But it isn't the room you started in. The walls are different. The air smells of ash.")
  slow_print("Behind you, a voice: 'Welcome. I've been watching you for a long time.'")
  slow_print("*** THE END ***")


def play(inventory):
  clock1_set = False
  clock2_set = False
  clock3_set = False

  slow_print("You step out of the mirror room and into the front hall of the house.")
  slow_print("The front door is right there. Moonlight spills across the floor.")
  slow_print("Three grand clocks stand along the wall. All of them are stopped.")
  time.sleep(1)
  slow_print("A woman stands in front of the door, with her back to you. She doesn't move.")

  while True:
    action = input("What do you want to do? \n 1. look at the left clock" \
    "\n 2. look at the middle clock" \
    "\n 3. look at the right clock" \
    "\n 4. look at the women" \
    "\n 5. look at the front door" \
    "\n 6. check inventory: ")

    if action == "1":
      slow_print("A tall clock with a brass plate: 'The night she left.' The hands are stopped.")
      if clock1_set:
        slow_print("The clock is ticking quietly")
      else:
        setting = input("Set the clock to (or press enter to cancel): ")

        if setting == "":
          slow_print("You step back from the clock.")
        elif setting == "9:10":
          slow_print("The hands click into place. The clock begins to tick.")
          slow_print("Somewhere in the house, a clock chimes once.")
          clock1_set = True
        else:
          ("The hands spin back to where they were.")

    elif action == "2":
      slow_print("A digital clock with the brass plate: 'The day she was born'")
      if clock2_set:
        slow_print("The clock is blinking")
      else:
        setting = input("Set the date to (or press enter to cancel): ")

        if setting == "":
          slow_print("You step back from the clock.")
        elif setting == "3/14" or setting == "314" or setting == "0314":
          slow_print("The clock begins to blink. Somewhere in the house, a clock chimes.")
          clock2_set = True
        else:
          slow_print("The clock goes back to how it was.")

    elif action == "3":
      slow_print("A tall clock with a brass plate: 'The hour she came back. The hands are stopped.'")
      if clock3_set:
        slow_print("The clock is ticking quietly.")
      else:
        setting = input("Set the time to (or press enter to cancel): ")
        if setting == "":
          slow_print("You step back from the clock.")
        elif setting == "8:20" or setting =="08:20":
          slow_print("The hands click into place. The clock begins to tick.")
          slow_print("Somewhere in the house, a clock chimes.")
          clock3_set = True
        else:
          slow_print("The clock goes back to how it was.")

    elif action == "4":
      if not (clock1_set and clock2_set and clock3_set):
        slow_print("She stands perfecty still, facing the door. Every clock in the house is silent.")
      else:
        slow_print("All three clocks are ticking The women slowly turns around.")
        slow_print("She looks at you the way someone looks at the end of a very long wait.")
        slow_print("She holds out her hand.")
        slow_print("She touches your wrist, right over the scar.")
        slow_print("It's the mark she carved into every door and every toy in this house, so she could always find you.")
        choice = input(" 1. take her hand \n 2. step away: ")
        if choice == "1" and "photograph" in inventory:
          slow_print("You take her hand. It's cold, then warm, then it isn't there at all.")
          slow_print("In the other hand, the photograph changes. The scractched-out faces are yours, smiling.")
          slow_print("'You came back,' she whispers. 'I can stop waiting now.'")
          slow_print("She fades like breath on a mirror. The clocks tick on without her.")
          slow_print("The front door swings open on a grey, ordinary morning. The house is only a house. Atleast you think it is...")
          slow_print("*** THE END ***")
          time.sleep(2)
          slow_print("...")
          slow_print("On the grey morning street, you find a key in your hand. You never picked it out.")
          slow_print("It's stamped with the symbol. Across the road, another house has the same mark on its door.")
          slow_print("Behind you, someone breathes. 'You forgot to look behind you.'")
          return
        
        elif choice == "1":
          slow_print("Your hand passes through hers. She flickers, and the lights go out.")
          bad_ending()
          return

        elif choice == "2":
          slow_print("You step back. She lowers her hand and turns away again.")
        else:
          slow_print("That's not an option")

    elif action == "5":
      if not(clock1_set and clock2_set and clock3_set):
        slow_print("The door won't move. Every clock in the house is stopped, and so is everything else.")
      else:
        slow_print("You push past the woman and throw the door open.")
        slow_print("As you pull it, the symbol on the frame burns bright, then goes dark. The mark on your wrist stings.")
        bad_ending()
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
