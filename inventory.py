#store room 
#check items in store rom 
# add items to the storeroom 
#rename items in store  
# remove items in store room 


store_room = []


def check_items():
    global store_room
    print(store_room)

def add_items(list_items):
    global store_room
    store_room.append(list_items)
    print("success")
    print("items added : ", list_items)

def rename_items(prev_name , new_name):
     global store_room
     found = False
     for i in range(len(store_room)):
    
         for item in store_room[i]:
            if item == prev_name:
                item = new_name


                print("success")
                found = True

                print(prev_name ,"renamed to ", new_name)
            if  not found:
                print("item not found")
    
def remove_items(item_names):
    global store_room
    print("before",store_room)

    for j in range(len(store_room)):
        for k in range(len(item_names)):


         for item in store_room[j]:
            for name in item_names[k]:
                while k < len(item_names):
                    if name[k] == item[j]:
                        removed = store_room.pop(j)
                        print("removed :" ,removed)
                        print("after",store_room)
                        # print("found")
                        break
                else:
                    print("not found")

    
    



add_items(["banana", "apple"])
rename_items("banana","watermelon" )
remove_items(["banana","apple"])

check_items()
