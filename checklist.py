checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1

# def mark_completed(index):
#     # insert code here

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
    # create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
    # read item
    elif function_code == "R":
        item_index = user_input("Index Number?")
        read(item_index)

    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        return False
    else:
        print("Unknown Option")
    return True

def test():
    checklist.append("purple sox")
    checklist.append("red cloak")

    print(read(0))
    print(read(1))

    checklist[0] = ("purple socks")
    checklist.pop(1)

    print(read(0))

    list_all_items()

    select("C")
    list_all_items()

    select("R")
    list_all_items()

    select("P")
    list_all_items()

    user_value = user_input("Please Enter a value:")
    print(user_value)

test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit")
    select(selection)
