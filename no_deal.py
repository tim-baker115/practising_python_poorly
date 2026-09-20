boxes = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 10, 7: 5000, 8: 1000, 9: 20000, 10: 25000}

import random
import time


def make_offer(boxes):
    opened_boxes = {}
    values = list(boxes.values())
    random.shuffle(values)
    for box in boxes:
        boxes[box] = values.pop()
    print()
    remaining = len(boxes)
    your_box = random.choice(list(boxes))
    print("Your box is: " + str(your_box))
    deal = False
    while remaining > 1:
        for box in range(1, 11):
            if box == your_box:
                print("[ X ]", end=" ")
            elif box in opened_boxes:
                print("[ £" + str(opened_boxes[box]) + " ]", end=" ")
            else:
                print("[ " + str(box) + " ]", end=" ")
        msg, offer = banker_offer(boxes)
        print(
            "\nOooh theres "
            + str(remaining)
            + " boxes left.\n"
            + msg
            + "£"
            + str(offer)
        )

        if remaining == 2:
            for box in boxes:
                if box != your_box:
                    other_box = box
                    break

            swap = input("Do you want to swap?! ")
            old_box = your_box

            if swap.lower() == "yes":
                your_box = other_box
                print("\nYou swapped!😬")
                print("The box you left behind contained £" + str(boxes[old_box]))
            else:
                print("You kept your box!")
            break
        else:
            task = input("🤔Deal or no deal? ")
        if task.lower() == "deal":
            print("dealing!")
            deal = True
            break
        if task.lower() == "no deal":
            print()
            open_box = int(input("OK, which box do you want to open? "))
            print()
            if open_box in boxes and open_box != your_box:
                print("Opening box: " + str(open_box) + "…😬😬😬")
                time.sleep(2)
                print("£" + str(boxes[open_box]))
                # boxes.pop(open_box)
                opened_boxes[open_box] = boxes.pop(open_box)
                remaining = len(boxes)
            else:
                print("😜Already open!")
    if deal == True:
        if offer >= your_box:
            emoji = "🤑"
        else:
            emoji = "😭"
        print(emoji + "You've won £" + str(offer))
    print(emoji + "Your box contained " + "£" + (str(boxes[your_box])))


def banker_offer(boxes, percentage=None):
    remaining = len(boxes)
    total = sum(boxes.values())

    if percentage is None or percentage > 1.0 or percentage < 0.0:
        if remaining >= 10:
            percentage = 0.3
        elif remaining >= 8:
            percentage = 0.4
        elif remaining >= 6:
            percentage = 0.6
        elif remaining >= 3:
            percentage = 0.75
        else:
            percentage = 0.9
    offer = round(total / remaining * percentage)

    if percentage >= 0.5:
        msg = "🥰The generous lovely banker will offer you "
    elif percentage <= 0.4:
        msg = "😭The mean banker will offer you "
    else:
        msg = "🤔The banker will offer you "
    return msg, offer


print(make_offer(boxes))
