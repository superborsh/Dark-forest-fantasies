import random
import time
import os

# Color codes
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

# Game variables
player_name = ""
player_gender = ""
player_health = 100
player_max_health = 100
player_coins = 50
player_inventory = []
player_weapon = "fists"
player_attack = 10

# Shop items
shop_items = {
    "health_potion": {"name": "Health Potion", "price": 20, "effect": 30},
    "better_sword": {"name": "Iron Sword", "price": 100, "attack": 20},
    "strong_armor": {"name": "Leather Armor", "price": 80, "health": 30},
    "magic_staff": {"name": "Magic Staff", "price": 150, "attack": 25},
    "golden_key": {"name": "Golden Key", "price": 200, "special": "opens secret doors"}
}

# Game events and enemies
enemies = ["Dark Elf", "Goblin", "Wolf", "Shadow Creature", "Forest Troll"]
events = ["find_coins", "find_item", "fight", "mystery", "shop", "rest", "dialogue"]
dialogue_characters = ["Old Wizard", "Mysterious Merchant", "Lost Spirit", "Talking Tree"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(text, color):
    print(color + text + colors.END)

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_stats():
    global player_name, player_gender, player_health, player_max_health, player_coins, player_inventory, player_weapon, player_attack
    
    print_colored("\n" + "="*50, colors.CYAN)
    print_colored(f"Traveler: {player_name} ({player_gender})", colors.BOLD)
    print_colored(f"Health: {player_health}/{player_max_health}", colors.GREEN)
    print_colored(f"Coins: {player_coins}", colors.YELLOW)
    print_colored(f"Weapon: {player_weapon} (Attack: {player_attack})", colors.RED)
    print("Inventory:", ", ".join(player_inventory) if player_inventory else "Empty")
    print_colored("="*50, colors.CYAN)

def game_intro():
    global player_name, player_gender
    
    clear_screen()
    print_colored("DARK FOREST FANTASIES", colors.PURPLE + colors.BOLD)
    print_colored("~ An Infinite Adventure ~\n", colors.BLUE)
    
    slow_print("You wake up in a strange, dark forest...")
    slow_print("The trees whisper secrets in a language you almost understand.")
    slow_print("You don't remember how you got here, but you know you need to survive.\n")
    
    player_name = input("What is your name, traveler? ")
    
    while True:
        gender = input("Are you a man or a woman? (m/w): ").lower()
        if gender == 'm':
            player_gender = "man"
            break
        elif gender == 'w':
            player_gender = "woman"
            break
        else:
            print("Please enter 'm' or 'w'")
    
    print_colored(f"\nWelcome, {player_name}!", colors.GREEN)
    slow_print(f"As a {player_gender}, you must navigate through these dark fantasies...")
    slow_print("Your journey begins now!\n")
    input("Press Enter to continue...")

def rest_event():
    global player_health, player_max_health
    
    clear_screen()
    print_colored("A Peaceful Clearing", colors.GREEN)
    print("\nYou find a quiet spot to rest.")
    
    heal_amount = random.randint(15, 30)
    player_health = min(player_max_health, player_health + heal_amount)
    
    print_colored(f"\nYou rest and recover {heal_amount} health!", colors.GREEN)
    print_colored(f"Current health: {player_health}/{player_max_health}", colors.GREEN)
    input("\nPress Enter to continue...")

def find_coins_event():
    global player_coins
    
    clear_screen()
    print_colored("Shiny Discovery!", colors.YELLOW)
    
    coins_found = random.randint(5, 50)
    player_coins += coins_found
    
    print(f"\nYou found {coins_found} coins on the ground!")
    print_colored(f"Total coins: {player_coins}", colors.YELLOW)
    input("\nPress Enter to continue...")

def find_item_event():
    global player_inventory
    
    clear_screen()
    print_colored("Mysterious Item Found!", colors.CYAN)
    
    items = ["Herbs", "Strange Feather", "Old Map", "Shiny Stone", "Mysterious Potion"]
    found_item = random.choice(items)
    
    if found_item not in player_inventory:
        player_inventory.append(found_item)
        print(f"\nYou found: {found_item}!")
        print("It has been added to your inventory.")
    else:
        print(f"\nYou found another {found_item}, but you already have one.")
    
    input("\nPress Enter to continue...")

def fight_event():
    global player_health, player_coins, player_inventory, player_max_health, player_attack
    
    clear_screen()
    
    enemy = random.choice(enemies)
    enemy_health = random.randint(30, 80)
    enemy_attack = random.randint(8, 20)
    
    print_colored(f"ENCOUNTER: {enemy}!", colors.RED + colors.BOLD)
    print(f"Enemy Health: {enemy_health}")
    print(f"Enemy Attack: {enemy_attack}")
    
    while enemy_health > 0 and player_health > 0:
        print("\n" + "="*30)
        print("1. Attack")
        print("2. Try to run")
        print("3. Use item from inventory")
        
        choice = input("\nWhat will you do? (1-3): ")
        
        if choice == "1":
            damage = random.randint(player_attack - 5, player_attack + 5)
            enemy_health -= damage
            print(f"\nYou attack the {enemy} for {damage} damage!")
            
            if enemy_health > 0:
                enemy_damage = random.randint(enemy_attack - 3, enemy_attack + 3)
                player_health -= enemy_damage
                print(f"The {enemy} attacks you for {enemy_damage} damage!")
        
        elif choice == "2":
            if random.random() < 0.4:
                print("\nYou successfully run away!")
                input("\nPress Enter to continue...")
                return
            else:
                print("\nYou failed to escape!")
                enemy_damage = random.randint(enemy_attack - 3, enemy_attack + 3)
                player_health -= enemy_damage
                print(f"The {enemy} attacks you for {enemy_damage} damage!")
        
        elif choice == "3":
            if player_inventory:
                print("\nYour inventory:")
                for i, item in enumerate(player_inventory, 1):
                    print(f"{i}. {item}")
                
                try:
                    item_choice = int(input("Choose item to use (number): ")) - 1
                    if 0 <= item_choice < len(player_inventory):
                        used_item = player_inventory.pop(item_choice)
                        if used_item == "Mysterious Potion":
                            heal = random.randint(20, 40)
                            player_health = min(player_max_health, player_health + heal)
                            print(f"You drink the potion and heal {heal} health!")
                        elif used_item == "Shiny Stone":
                            print("The stone shines brightly, confusing the enemy!")
                            enemy_health -= 15
                        else:
                            print(f"You use the {used_item}, but it doesn't seem to help much...")
                    else:
                        print("Invalid choice!")
                except:
                    print("Invalid input!")
            else:
                print("Your inventory is empty!")
            continue
        
        else:
            print("Invalid choice! You hesitate and lose your turn.")
        
        if enemy_health <= 0:
            coins_won = random.randint(20, 60)
            player_coins += coins_won
            print_colored(f"\nYou defeated the {enemy}!", colors.GREEN)
            print_colored(f"You found {coins_won} coins on the enemy!", colors.YELLOW)
            input("\nPress Enter to continue...")
            return
        
        if player_health <= 0:
            print_colored("\nYou have been defeated...", colors.RED)
            input("\nPress Enter to continue...")
            return
    
    input("\nPress Enter to continue...")

def mystery_event():
    global player_health, player_attack, player_coins, player_max_health
    
    clear_screen()
    print_colored("MYSTERY EVENT", colors.PURPLE + colors.BOLD)
    
    mystery_type = random.randint(1, 3)
    
    if mystery_type == 1:
        print("\nYou find a glowing mushroom. Do you eat it?")
        print("1. Yes")
        print("2. No")
        
        choice = input("\nYour choice: ")
        
        if choice == "1":
            if random.random() < 0.7:
                heal = 40
                player_health = min(player_max_health, player_health + heal)
                print_colored("\nThe mushroom gives you strange visions but heals you!", colors.GREEN)
                print_colored(f"You heal {heal} health!", colors.GREEN)
            else:
                damage = 20
                player_health -= damage
                print_colored("\nThe mushroom was poisonous!", colors.RED)
                print_colored(f"You lose {damage} health!", colors.RED)
        else:
            print("\nYou leave the mushroom alone. Probably wise.")
    
    elif mystery_type == 2:
        print("\nA fairy offers to bless your weapon for 30 coins.")
        print("1. Accept")
        print("2. Decline")
        
        choice = input("\nYour choice: ")
        
        if choice == "1":
            if player_coins >= 30:
                player_coins -= 30
                player_attack += 5
                print_colored("\nYour weapon glows with magic! Attack increased by 5!", colors.BLUE)
            else:
                print("\nNot enough coins!")
        else:
            print("\nThe fairy flies away, disappointed.")
    
    elif mystery_type == 3:
        print("\nYou find a locked chest. Try to open it?")
        print("1. Try to pick the lock")
        print("2. Leave it")
        
        choice = input("\nYour choice: ")
        
        if choice == "1":
            if random.random() < 0.3:
                coins = 100
                player_coins += coins
                print_colored(f"\nSuccess! You find {coins} coins inside!", colors.YELLOW)
            else:
                print("\nThe lock breaks your tool. You gain nothing.")
        else:
            print("\nYou decide not to risk it.")
    
    input("\nPress Enter to continue...")

def dialogue_event():
    global player_coins, player_attack, player_weapon, player_max_health, player_health, player_inventory
    
    clear_screen()
    character = random.choice(dialogue_characters)
    print_colored(f"{character} approaches you...", colors.CYAN + colors.BOLD)
    
    dialogues = {
        "Old Wizard": [
            "The forest remembers all who walk here...",
            "Beware the shadows that move without light.",
            "Magic flows through these trees like blood."
        ],
        "Mysterious Merchant": [
            "I have wares, if you have coin...",
            "Everything has a price in this forest.",
            "Buy something or move along, traveler."
        ],
        "Lost Spirit": [
            "I cannot find my way home...",
            "The trees have swallowed my memory.",
            "Help me remember who I was..."
        ],
        "Talking Tree": [
            "My roots have seen centuries pass...",
            "The forest breathes, and I am its lungs.",
            "Respect the old ways, traveler."
        ]
    }
    
    slow_print(f"\n{character}: \"{random.choice(dialogues[character])}\"")
    
    if character == "Mysterious Merchant":
        if random.random() < 0.5:
            items_list = list(shop_items.values())
            item = random.choice(items_list)
            price = item["price"] // 2
            print(f"\nThe merchant offers you {item['name']} for {price} coins (half price!)")
            
            buy = input(f"Do you want to buy it? (y/n): ").lower()
            if buy == 'y' and player_coins >= price:
                player_coins -= price
                if "attack" in item:
                    player_attack = item["attack"]
                    player_weapon = item["name"]
                    print_colored(f"You now wield {item['name']}!", colors.BLUE)
                elif "health" in item:
                    player_max_health += item["health"]
                    player_health = player_max_health
                    print_colored(f"Your maximum health increased by {item['health']}!", colors.GREEN)
                else:
                    player_inventory.append(item["name"])
                    print(f"{item['name']} added to your inventory!")
            elif buy == 'y':
                print("You don't have enough coins!")
            else:
                print("The merchant nods and disappears into the mist.")
    
    input("\nPress Enter to continue...")

def shop_event():
    global player_coins, player_attack, player_weapon, player_max_health, player_health, player_inventory
    
    clear_screen()
    print_colored("MYSTERIOUS FOREST SHOP", colors.YELLOW + colors.BOLD)
    print("="*40)
    
    while True:
        print(f"\nYour coins: {player_coins}")
        print("\nAvailable items:")
        
        items = list(shop_items.values())
        for i, item in enumerate(items, 1):
            print(f"{i}. {item['name']} - {item['price']} coins")
            if "attack" in item:
                print(f"   Attack: {item['attack']}")
            elif "health" in item:
                print(f"   +{item['health']} Max Health")
            elif "effect" in item:
                print(f"   Heals {item['effect']} health")
            elif "special" in item:
                print(f"   {item['special']}")
        
        print(f"{len(items)+1}. Leave shop")
        
        choice = input("\nWhat would you like to buy? (number): ")
        
        if choice == str(len(items)+1):
            break
        
        if choice.isdigit() and 1 <= int(choice) <= len(items):
            item_index = int(choice) - 1
            selected_item = items[item_index]
            
            if player_coins >= selected_item["price"]:
                player_coins -= selected_item["price"]
                
                if "attack" in selected_item:
                    player_attack = selected_item["attack"]
                    player_weapon = selected_item["name"]
                    print_colored(f"\nYou bought {selected_item['name']}! Your attack is now {player_attack}.", colors.BLUE)
                
                elif "health" in selected_item:
                    player_max_health += selected_item["health"]
                    player_health = player_max_health
                    print_colored(f"\nYou bought {selected_item['name']}! Your max health is now {player_max_health}.", colors.GREEN)
                
                elif "effect" in selected_item:
                    player_inventory.append(selected_item["name"])
                    print(f"\nYou bought {selected_item['name']}! It has been added to your inventory.")
                
                else:
                    player_inventory.append(selected_item["name"])
                    print(f"\nYou bought {selected_item['name']}! It has been added to your inventory.")
            else:
                print("\nYou don't have enough coins!")
        else:
            print("\nInvalid choice!")
        
        input("\nPress Enter to continue...")
        clear_screen()
        print_colored("MYSTERIOUS FOREST SHOP", colors.YELLOW + colors.BOLD)
        print("="*40)

def main_game_loop():
    global player_health, player_max_health, player_coins, player_inventory, player_attack, player_weapon
    
    day = 1
    
    while player_health > 0:
        clear_screen()
        show_stats()
        print_colored(f"\nDay {day} in the Dark Forest", colors.BOLD)
        print("="*50)
        
        print("\nWhat will you do?")
        print("1. Continue your journey")
        print("2. Check your stats")
        print("3. Use item from inventory")
        print("4. Quit game")
        
        choice = input("\nChoose an action (1-4): ")
        
        if choice == "1":
            event = random.choice(events)
            
            if event == "find_coins":
                find_coins_event()
            elif event == "find_item":
                find_item_event()
            elif event == "fight":
                fight_event()
            elif event == "mystery":
                mystery_event()
            elif event == "shop":
                shop_event()
            elif event == "rest":
                rest_event()
            elif event == "dialogue":
                dialogue_event()
            
            day += 1
            
            # Random health regeneration
            if random.random() < 0.3 and player_health < player_max_health:
                regen = random.randint(1, 5)
                player_health = min(player_max_health, player_health + regen)
                if regen > 0:
                    print_colored(f"\nYou feel slightly refreshed (+{regen} health)", colors.GREEN)
                    input("Press Enter to continue...")
        
        elif choice == "2":
            show_stats()
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            if player_inventory:
                print("\nYour inventory:")
                for i, item in enumerate(player_inventory, 1):
                    print(f"{i}. {item}")
                
                try:
                    item_choice = int(input("Choose item to use (number, 0 to cancel): ")) - 1
                    if item_choice == -1:
                        continue
                    if 0 <= item_choice < len(player_inventory):
                        used_item = player_inventory.pop(item_choice)
                        if used_item == "Health Potion":
                            heal = 30
                            player_health = min(player_max_health, player_health + heal)
                            print_colored(f"You drink the potion and heal {heal} health!", colors.GREEN)
                        elif used_item == "Mysterious Potion":
                            heal = random.randint(20, 40)
                            player_health = min(player_max_health, player_health + heal)
                            print_colored(f"You drink the potion and heal {heal} health!", colors.GREEN)
                        else:
                            print(f"You examine the {used_item}, but decide not to use it now.")
                            player_inventory.append(used_item)
                    else:
                        print("Invalid choice!")
                except:
                    print("Invalid input!")
            else:
                print("Your inventory is empty!")
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            print("\nThank you for playing Dark Forest Fantasies!")
            print(f"You survived {day-1} days in the forest.")
            break
        
        else:
            print("Invalid choice!")
            input("\nPress Enter to continue...")
    
    if player_health <= 0:
        clear_screen()
        print_colored("\n" + "="*50, colors.RED)
        print_colored("GAME OVER", colors.RED + colors.BOLD)
        print_colored("="*50, colors.RED)
        print(f"\nYou survived {day-1} days in the Dark Forest.")
        print(f"Final coins: {player_coins}")
        print(f"Final weapon: {player_weapon}")
        print("Thank you for playing!")
    
    input("\nPress Enter to exit...")

def main():
    game_intro()
    main_game_loop()

if __name__ == "__main__":
    main()