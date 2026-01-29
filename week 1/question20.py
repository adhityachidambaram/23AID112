#creating empty list
shopping_list = []

while True:
    choice = input("What would you like to do? (add, remove, show, or quit: )")

    #add item
    if choice == "add":
        item = input("Enter item: ")
        shopping_list.append(item)
    
    #remove item
    elif choice == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("item not in list")

    #show items 
    elif choice == "show":
        print("Your shopping list:", shopping_list)

    elif choice == "quit":
        break

    else:
        print("Invalid option")
print("Final shopping list:", shopping_list)
