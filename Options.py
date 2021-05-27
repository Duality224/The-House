class options:
    inventory = []
    endings = []


    def endgame(choice):
        if choice == "porch":
            print("Guess the paper sent out the wrong person for the story, huh?")
            print("GAME OVER: Ending 1: Coward")
            options.endings.append("Ending 1: Coward")

    def porch():
        choice = input("Do you dare to enter the house? Y/N: ")

        if choice.lower() == 'y':
            print("\nYou grip the doorknob again and with a shaky breath, open the door...")
            options.entryway()
        elif choice.lower() == 'n':
            print("\nYou turn around and head back to your car, head lowered in")
            print("shame.")
            options.endgame("porch")
        else:
            options.try_again()
            options.porch()

    def entryway():
        print("A dimly lit entryway greets you, sunlight managing to make it in through")
        print("the caked-on grime on the large stained glass windows above the front door.")
        print("There's an expensive-looking rug running along the floor and a surprising lack")
        print("of vandalism, despite the door not being locked. There is a small table on one side")
        print("and a painting on the other. There is also one door leading further into the house.")
        options.entryway_2()
    
    def entryway_2():
        print("As far as you can tell, there are three options:\n")
        print("A. Investigate the table.")
        print("B. Investigate the painting.")
        print("C. Go through the door.")
        choice = input("\nWhat would you like to do?: ")

        if choice.lower() == "a":
            print("You investigate the table and notice it has only one drawer. You open it.")
            print("Inside, you find a single key with a decorative ellipse on it. You pocket it.")
            options.inventory.append("Attic Key")
            options.entryway_2()
            
        elif choice.lower() == "b":
            print("You investigate the painting. It is a self-portait of a very stern-looking man with")
            print("a large handlebar mustache and piercing brown eyes. There is otherwise nothing interesting")
            print("about it.")
            options.entryway_2()

        elif choice.lower() == "c":
            print("You go through the door and make your way further inside...\n")
            options.foyer()
        
        else:
            options.try_again()
            options.entryway_2()
            


    
    def foyer():
        print("On the other side of the door lies a dimly lit foyer, stairs go up on the right, to the left there is a")
        print("swinging door, to the right just before the stairs there is another door, and forward there is a dark hallway.")
        print("\nWhich area would you like to explore?")
        print("A. Go through the left door")
        print("B. Go forward into the hallway")
        print("C. Go through the right door")
        print("D. Go up the stairs")
        print("E. Go back through the door.")
        choice = input()


        if choice.lower() == "a":
            print("You have chosen to go through the left door. It creaks open...")
            options.left_door()
        elif choice.lower() == "b":
            print("You have chosen to go forward into the hallway. You step forward...")
            options.hallway()
        elif choice.lower() == "c":
            print("You have chosen to go through the right door. You turn the knob...")
            options.right_door()
        elif choice.lower() == "d":
            print("You have chosen to go up the stairs. You grip the banister and take the first step...")
            options.stairs()
        elif choice.lower() == "e":
            print("You turn around.")
            options.entryway_2()
        else:
            options.try_again()
            options.foyer()


    def left_door():
        print("The left door leads to a living room. Dust coats the antique furniture and the faint smell of old books hangs in the air.\n")
        print("There are several things about this room that intrigue you.")

    def right_door():
        print("The right door leads into a small home office. Strangely, the desk lamp is on despite the fact that the house does not have ")
        print("power connected to it. A large globe stand sits next to the desk supported by three legs. It looks like the kind to have a hidden compartment within.")
        choice = input("You could either check out the desk or the globe, which do you choose?\n A: The desk\n B: The globe stand")
        
        if choice.lower() == "a":
            print("The desk itself has several drawers, two of which are empty. The main drawer only has a single pen inside it and the bottom left drawer ")
            print("has a locked box with the emblem of a crane on it.")
            print("What do you want to do?")

            
        elif choice.lower() == "b":
            print("You were right when you guessed the globe had a hidden compartment within it.")
            print("You opened it up to find a contraption made of several gears tucked tightly inside.")
            print("There appears to be a gear missing. Nothing will move without that gear.")
      
    
    def hallway():
        pass

    def stairs():
        pass
    
    def try_again():
        print("Sorry, that is not a valid option. Please try again.")