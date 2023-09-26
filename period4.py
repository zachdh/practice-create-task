import random

inventory = ["BOW", "SWORD", "WAND", "BOMB"]

enemy_items = {
    "Gibby the Goblin": "SWORD",
    "Wanda the Witch": "WAND",
    "Killor the Knight": "BOW",
    "Gregory the Giant": "BOMB"
}

def adventurer_simulator():
    Player_name = input("WELCOME TO ADVENTURE SIMULATOR! WHAT IS YOUR NAME TRAVELER? ")
    
    print("AS YOU ARE TRAVELING YOU COME ACROSS MERLIN THE GREAT, HE APPROACHES YOU WITH A QUEST TO DEFEAT THE FOUR GREAT CREATURES WHO HAVE BEEN TERRIFYING THE LANDS. WILL YOU BE THE FIRST TO COME BACK ALIVE? ")

    while True:

        if not enemy_items: 
             
             print("Congratulations, you have defeated all the enemies and saved all the villagers' lives!")

             break
        
        enemy = random.choice(list(enemy_items.keys()))
        
        print(enemy, "stands in your path!")

        print("Here is your inventory ", inventory)
        
        player_choice = input("Choose a weapon from your inventory to defeat " + enemy + "! ")
        
        if player_choice in inventory:
            
            if player_choice == enemy_items[enemy]:
                 
                print("Congratulations", Player_name, ", you have defeated", enemy, ". Prepare for the next enemy.")
                
                del enemy_items[enemy]
                
            else: 
                
                print("Your", player_choice, "was no match for ", enemy, ". You died a horrible death.")
                
                print("Game over.")

                break
        else:
            print("Invalid item. Please choose from your inventory.")
    

adventurer_simulator()


