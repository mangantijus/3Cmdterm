pets = []  # starts empty — the user adds pets as the program runs

def display_menu():

        print("=== Pet Adoption Records ===")
        print("1. Add a pet")
        print("2. View all pets")
        print("3. Count available vs adopted")
        print("4. Find a pet by name")
        print("5. Remove a Pet")
        print("6. Exit")
       
        num = input("Choose a number: ")
        return num
    # print the menu, return the user's choice
pass 

def add_pet(pet_list):

    name =input("Name of Pet: ")
    animal = input("What type of animal: ")
    stat = input("What is the status of the pet: ")
    space = " - "
    result = name + space + animal + space + stat

    pets.append(result)
    print(result)
   
    # ask for name, animal type, status — build the string, add to the list
    pass

def view_pets(pet_list):

    for i in range(len(pets)):
         print(pets[i])

    # loop through and print every pet — handle empty list
    pass

def count_available_adopted(pet_list):
    Available_pet = 0
    Adopted_pet = 0

    
    # loop through, count Available vs Adopted, return both
    pass

def find_pet(pet_list):
    pname = input("what is the name of the pet: ")
        

    # ask for a name, search the list, print result or "not found"
    pass

# BONUS (optional)
def remove_pet(pet_list):
    rem = input("What name of the pet you want to remove: ")
    pets.remove(rem)
pass

def main():
    running = True
    while running:
        num = display_menu()
        if num == "1":
             add_pet(pets)
        elif num =="2":
             view_pets(pets)
        elif num =="3":
             count_available_adopted(pets)
        elif num =="4":
             find_pet(pets)
        elif num =="5":
             remove_pet(pets)
        elif num =="6":
             running = False
        else:
            print("number not found")
          
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit
main()



