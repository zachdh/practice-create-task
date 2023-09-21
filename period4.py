inventory = ["BOW", "SWORD", "WAND", "BOMB"]

enemy_items = {
    "Gibby the Goblin": "SWORD",
    "Wanda the Witch": "WAND",
    "Killor the Knight": "BOW",
    "Gregory the Giant": "BOMB"
}

def adventurer_simulator():
    Player_name = input("WELCOME TO ADVENTURE SIMULATOR! WHAT IS YOUR NAME TRAVELER? ")
   
    print("AS YOU ARE TRAVELING YOU COME  ACROSS MERLIN THE GREAT, HE APPROACHES YOU WITH A QUEST TO DEFEAT THE FOUR GREAT CREATURES WHO HAVE BEEN TERRIFYING THE LANDS. WILL YOU BE THE FIRST TO COME BACK ALIVE? ")
   
    print("Here is your inventory ", inventory)
   
    print("Gibby the Giant stands in your path!")
   
    correct_item = enemy_items["Gibby the Goblin"]
   
    player_choice= input("Choose a weapon from your inventory to defeat the enemy!")

if player_choice == correct_item:

    print("Congratulations", Player_name, ", you have defeated Gibby the Goblin. Prepare for the next enemy.")

else: 

    print:("Your", player_choice, "was no match for Gibby the Goblin. Gibby the Goblin sat on you and you died a horrible death.")

    break

adventurer_simulator()


