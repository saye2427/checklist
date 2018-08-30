# print("Hello World")
#
# checklist = list()
#
# checklist.append("Hello")
# print(checklist)
# checklist.append("World")
# print(checklist)

checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    print(checklist[index])

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        # print(str(index) + list_item)
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    print("√" + checklist[index])

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def select(function_code):
    # Create item
    if function_code == "A" or function_code == "a":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "F" or function_code == "f":
        item_index = user_input("Index Number? ")
        # Remember that item_index must actually exist or our program will crash.
        read(int(item_index))

    # Print all items
    elif function_code == "L" or function_code == "l":
        list_all_items()

    elif function_code == "Q" or function_code == "q":
        print("Goodbye.")
        return False

    elif function_code == "U" or function_code == "u":
        list_item_index = user_input("Which number item would you like to change?: ")
        new_item = user_input("What item would you like to replace it with?: ")
        update(int(list_item_index), new_item)
        print("Here's your updated list!")
        list_all_items()

    elif function_code == "E" or function_code == "e":
        erase_item = user_input("Which number item would you like to erase?")
        destroy(int(erase_item))

    # Catch all
    else:
        print("Unknown Option!")
    return True

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))

    mark_completed(0)

    list_all_items()

    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run
    select("P")
    list_all_items()

    select("S")
    list_all_items()

    user_value = user_input("Please Enter a value:")
    print(user_value)

test()

running = True
while running:
    selection = user_input("Press A to add to your list, F to fetch an item from your list, L to see your full list, U to update your existing list, E to erase an item from your list, or Q to exit.")
    running = select(selection)
