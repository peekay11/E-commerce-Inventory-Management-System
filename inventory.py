# wave 1
# store room
# check items in store room
# add items to the storeroom
# rename items in store room
# remove items in store room
# wave 2
# use csv to check

store_room = []


def check_items():
    print("checking items ...")
    global store_room
    print(store_room)
    print("Total Inventory:", len(store_room))


def add_items(list_items):
    print("adding items ...")
    global store_room
    for item in list_items:
        store_room.append(item)
        print("success")
    print("items added:", list_items)
    print("Total Inventory:", len(store_room))


def rename_items(prev_name, new_name):
    print("renaming items ...")

    # used index to rename the item instead of its temporary value in rename items function
    global store_room
    found = False

    if prev_name in store_room:
        found_ind = store_room.index(prev_name)
        store_room[found_ind] = new_name
        print("renamed..")
        print(prev_name, ": renamed to:", new_name)
    else:
        print(prev_name, "not found")

    print("Total Inventory:", len(store_room))


def remove_items(item_names):
    print("removing items ...")
    global store_room

    for name in item_names:
        if name in store_room:
            store_room.remove(name)
            print("store room results:", store_room)
        else:
            print(name, ": not in store room")
    print("Total Inventory:", len(store_room))


# Run checks
check_items()

tech_inventory = [
    "iPhone 15", "MacBook Air", "Galaxy S23", "Pixel 8",
    "iPad Pro", "AirPods Max", "Sony Headphones",
    "Apple Watch", "Kindle", "Dell XPS"
]

add_items(tech_inventory)
remove_items(["Kindle", "Dell XPS", "banana"])
rename_items("iPhone 15", "iPhone 17")

check_items()


# add csv save and load 

