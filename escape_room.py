room = ["door", "picture"]

state = {
    "door_unlocked": False,
    "keypad_inspected": False,
    "picture_inspected": False,
    "door_inspected": False,
    "lamp_inspected": False,
    "clock_inspected": False,
}


def inspect(room):
    selection = ""

    while selection not in range(1, len(room) + 1):
        counter = 0
        # print("What do you want to inspect?")
        for element in room:
            counter += 1
            print(str(counter) + ". " + element)
        selection = int(input("What do you want to inspect? "))

        if selection not in range(1, len(room) + 1):
            print("\nInvalid selection")
            break
        else:
            print("\nYou picked the " + room[selection - 1])
            inspections[room[selection - 1]]()


def inspect_door():
    if state["keypad_inspected"] == True:
        print("Inspecting door…")
        print("The door opens!")
    else:
        print("You turn the door handle…")
        print("Its locked")


def inspect_clock():
    riddle_answer = 50
    if state["clock_inspected"] == True:
        print("You get a strange sense of deja vu…")
        print("The answer was " + str(riddle_answer))
        inspect(room)
    print("Inspecting clock…")
    print("The clock has stopped.")
    print("The hands point stubbornly to 3:15.")
    print("Take the hour.")
    print("Multiply by the minutes.")
    print("Add the number of letters in the word that brought you here.")
    answer = int(input("Answer: "))
    if answer == riddle_answer:
        print("That would make sense 🤔.")
        state["clock_inspected"] = True
        room.append("lamp")
    else:
        if answer > riddle_answer:
            difference = answer - riddle_answer
            print("So close " + str(difference) + " out!")
        elif answer < riddle_answer:
            difference = riddle_answer - answer
            print("So close " + str(difference) + " out!")
    inspect(room)


def inspect_keypad():
    attempts = 0
    allowed = 5
    answer = "523698"
    if state["keypad_inspected"] == True:
        print("You get a strange sense of deja vu…")
        print("The answer was " + str(answer))
        inspect(room)
    state["door_keypad"] = True
    print("Inspecting keypad…")
    print("5 is first.")
    print("Up until now you may have felt confident.")
    print("Right beside you sits the final puzzle.")
    print("Down the page, nothing appears unusual.")
    print("Down here, perhaps you should look again.")
    print("Left with nowhere else to go, you try the keypad.")
    print("+---+---+---+")
    print("| 1 | 2 | 3 |")
    print("+---+---+---+")
    print("| 4 | 5 | 6 |")
    print("+---+---+---+")
    print("| 7 | 8 | 9 |")
    print("+---+---+---+")
    print("|     0     |")
    print("+-----------+")
    while attempts < allowed:
        # print()
        code = input("CODE: ")
        if code != answer:
            print("INCORRECT")
            attempts += 1
            print(str(attempts) + "/" + str(allowed))
        else:
            print("That would make sense 🤔.")
            state["keypad_inspected"] = True
            # room.append("door")
            break
    inspect(room)


switches = [32, 16, 8, 4, 2, 1]
states = [False, False, False, False, False, False]


def inspect_lamp():
    target = 50
    total = 0
    if state["lamp_inspected"] == True:
        print("You get a strange sense of deja vu…")
        print("The answer was " + str(target))
        inspect(room)
    print()
    print("Inspecting lamp…")
    print("The lamp has six switches.")
    for position in range(len(switches)):
        if states[position] == True:
            print("[X]", switches[position], end=" ")
            total += switches[position]
        else:
            print("[ ]", switches[position], end=" ")
    if total == target:
        print("That would make sense 🤔.")
        state["lamp_inspected"] = True
        room.append("keypad")
        return
    print("\n")
    print("TARGET: " + str(target))
    print("REQUIRED: " + str(target - total))
    print("TOTAL: " + str(total))
    selection = int(input("Which switch? "))
    if selection > len(switches):
        print("LaMp ErR0R")
        inspect(room)
    if states[selection - 1] == True:
        states[selection - 1] = False
    else:
        states[selection - 1] = True
    inspect_lamp()


def inspect_picture():
    riddle_answer = "clock"
    if state["picture_inspected"] == True:
        print("You get a strange sense of deja vu…")
        print("The answer was " + riddle_answer)
        inspect(room)
    else:
        state["picture_inspected"] = True
        print("_" * len(riddle_answer))
        print()
        print("Inspecting picture…")
        print("I have a face but never smile,")
        print("I have hands but never clap.")
        print("I tell you something all day long,")
        print("But never speak a word.")
        answer = input("What am I? ")
        if answer.lower() == riddle_answer:
            print()
            print("That would make sense 🤔.")
            room.append(riddle_answer)
            # room.append("door")
            inspect(room)
        else:
            state["picture_inspected"] = False
            for position, letter in enumerate(riddle_answer):
                if letter in answer.lower():
                    print(letter.upper(), end=" ")
                else:
                    print("_", end=" ")
                    # print()
            # for letter in answer.lower():
            # if letter in riddle_answer:
            # for position, letter in enumerate(riddle_answer):
            # print("youve got some of the letters…")
            # print("Nope…" + answer + "lets go home")
            # else:
            # print(letter)
    print()
    inspect(room)
    # print(state)


inspections = {
    "door": inspect_door,
    "keypad": inspect_keypad,
    "lamp": inspect_lamp,
    "picture": inspect_picture,
    "clock": inspect_clock,
}


print(inspect(room))
