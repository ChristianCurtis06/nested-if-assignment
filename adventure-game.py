# Task 1: Code Correction
place = input("Choose a place: forest or cave? ").lower()

if place == "forest":
    action = input("Climb a tree or cross a river? ").lower()
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
# Task 2: Setting the Scene
    action = input("Light a torch or proceed in the dark? ").lower()
    if action == "light a torch":
        print("You discovered a sleeping dragon!")
    elif action == "proceed in the dark":
        print("You lost your footing and fell down a crack!")
    else:
        pass
# Task 3: Default Path
else:
    pass