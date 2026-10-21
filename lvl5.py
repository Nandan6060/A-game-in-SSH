import time
from utils import slow_print

def play(inventory):
  trunk_open = False
  dress_searched = False
  floor_searched = False
  frame_searched = False
  photo_made = False

  slow_print("You climb the ladder out of the basement and into the attic.")
  slow_print("Moonlight cuts through a round window. Dust hangs in the air.")
  slow_print("There's a heavy trunk, a dress form wearing a faded gown, and an empty picture frame leaning on the wall.")
  slow_print("The whole far wall is covered in old photographs. In the ceiling above you is a small hatch")

  while True:
    action = input("What do you want to do? \n 1. look at the trunk" \
    "\n 2. look at the dress form" \
    "\n 3. look at the floorboards" \
    "\n 4. look at the empty picture frame" \
    "\n 5. look at the wall of photographs" \
    "\n 6. try to put the photo pieces together" \
    "\n 7. look at the hatch" \
    "\n 8. check inventory:")

    if action == "1":
      slow_print("A heavy trunk with a brass lock. The dial has three letters. It has the same strange symbol as the last 4 rooms.")
      if trunk_open:
        ("The trunk is open and empty now.")
      else:
        word = input("Enter the 3 letter word (or press enter to cancel): ")
        if word == "":
          slow_print("You step back from the trunk")
        elif word.lower() == "sun":
          slow_print("The lock clicks. Inside, under a child's dress, is a torn piece of a photograph. (+1 photo piece 1)")
          inventory.append("photo piece 1")
          trunk_open = True
        else:
          slow_print("The dial spins. The lock doesnt budge")

    elif action == "2":
      if dress_searched:
        slow_print("You already searched the gown. There's nothing else in it.")
      else:
        slow_print("The faded gown is cold and stiff. In its pockets you find a torn piece of a photograph. (+1 photo piece 2)")
        inventory.append("photo piece 2")
        dress_searched = True


    elif action == "3":
      if floor_searched:
        slow_print("The loose board is back in place. There's nothing else under it.")
      else:
        slow_print("One floorboard is loose. You pry it up and find a torn piece of a photograph. (+1 photo piece 3)")
        inventory.append("photo piece 3")
        floor_searched = True

    elif action == "4":
      if frame_searched:
        slow_print("The frame is empty.")
      else:
        slow_print("The frame has no picture. You pry off the backing and a torn piece of photograph slides out. (+1 photo piece 4)")
        inventory.append("photo piece 4")
        frame_searched = True

    elif action == "5":
      slow_print("Dozens of old photographs cover the wall. In every one, a woman and a girl stand together.")
      slow_print("In every photo, the girl's face has been scratched out.")
      slow_print("Pinned among them is a faded sampler, stitched in a careful thread:")
      slow_print("'Every morning she rises, every evening she goes. Three letters, warm to the touch, and bright enough to show.'")

    elif action == "6":
      if photo_made:
        slow_print("You already put the photograph together.")
      elif "photo piece 1" in inventory and "photo piece 2" in inventory and "photo piece 3" in inventory and "photo piece 4" in inventory:
        slow_print("You lay the four pieces side by side. They fit together")
        slow_print("It's a photograph of a woman and a girl, holding hands infront of a tall house.")
        slow_print("The girl has a scar on her wrist, Shaped exactly like the symbol from the journal...")
        slow_print("You look down at your own wrist. The same mark is there.")
        slow_print("On the back, in faded ink: 'For my girl's tenth birthday. 03/14.'")
        slow_print("03/14. Something tells you it's important")
        inventory.remove("photo piece 1")
        inventory.remove("photo piece 2")
        inventory.remove("photo piece 3")
        inventory.remove("photo piece 4")
        inventory.append("photograph")
        photo_made = True
      else:
        slow_print("You dont have all the pieces yet.")

    elif action == "7":
      slow_print("There's a small hatch in the ceiling. It has a 4-digit dial lock.")
      code = input("Enter 4 digit code (or press enter to cancel):")
      if code == "":
        slow_print("You step back from the hatch.")
      elif code == "0314":
        slow_print("The dial clicks. The hatch swings open and a ladder drops down.")
        slow_print("You climb up. Behind you, the photographs on the wall all rustle at once.")
        time.sleep(1)
        return
      else:
        slow_print("The dial spins. Nothing happens")

    elif action == "8":
      if len(inventory) == 0:
        slow_print("Your inventory is empty")
      else:
        slow_print("You are carrying:")
        for item in inventory:
          slow_print("- " + item)

    else:
      slow_print("That's not an option")
      