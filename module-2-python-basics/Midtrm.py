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

def add_pet(pets):

    name =input("Name of Pet: ")
    animal = input("What type of animal: ")
    stat = input("What is the status of the pet: ")
    space = " - "
    result = name + space + animal + space + stat

    pets.append(result)
    print(result)
   
    # ask for name, animal type, status — build the string, add to the list


def view_pets(pets):

    for i in range(len(pets)):
         print(pets[i])

    # loop through and print every pet — handle empty list
    

def count_available_adopted(pets):
    Available_pet = 0
    Adopted_pet = 0
    for b in pets:
         if "available" in b:
              Available_pet +=1
         elif "adopted" in b:
              Adopted_pet +=1
    print(f"Available_pet : {Available_pet}")
    print(f"Adopted_pet : {Adopted_pet}")


    
    # loop through, count Available vs Adopted, return both
    

def find_pet(pets):
    pname = input("what is the name of the pet: ")
        

    # ask for a name, search the list, print result or "not found"
    

# BONUS (optional)
def remove_pet(pets):
    rem = input("What name of the pet you want to remove: ")
    for b in pets:
         if rem in b:
            pets.remove(b)
      
      
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



