# Save this as "hacker_warz.py"

import random
import os
import json
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

class HackerWarz:
    def __init__(self):
        # Define global variables
        self.balance = 1000  # Starting balance
        self.days = 1
        self.hacks = 0
        self.firewall_level = 1
        self.virus_detected = False
        self.location_multiplier = {"DarkWeb": 1.2, "Corporate": 0.8, "Government": 0.7, "Offshore Account": 0.5}
        self.data_types = ["Credit Card Info", "Sensitive Documents", "Government Secrets", "Corporate Data"]
        self.hack_types = {
            "DarkWeb": {
                "Phishing": (100, 400),
                "DDoS": (200, 600),
                "Malware Injection": (250, 700),
                "Bitcoin Mining": (300, 800),
                "Identity Theft": (350, 900),
                "Cryptocurrency Scam": (400, 1000)
            },
            "Corporate": {
                "Data Breach": (300, 800),
                "Ransomware": (400, 1000),
                "Insider Trading": (350, 900),
                "Corporate Espionage": (450, 1100),
                "Social Engineering": (400, 1000),
                "Intellectual Property Theft": (500, 1200)
            },
            "Government": {
                "Espionage": (500, 1200),
                "Zero-Day Exploit": (600, 1500),
                "Cyber Warfare": (700, 1700),
                "Election Manipulation": (800, 2000),
                "Covert Surveillance": (600, 1500),
                "Critical Infrastructure Attack": (900, 2200)
            },
            "Offshore Account": {
                "Deposit": None,
                "Withdraw": None
            }
        }
        self.upgrades = {
            "Powerful CPU": {"Cost": 300, "Hack Power Increase": 50, "Firewall Level Increase": 0},
            "Encrypted VPN": {"Cost": 500, "Hack Power Increase": 0, "Firewall Level Increase": 1},
            "Advanced Malware": {"Cost": 800, "Hack Power Increase": 0, "Virus Detection Decrease": 2, "Firewall Level Increase": 0},
            "Bribe the Feds": {"Cost": 1000, "Hack Power Increase": 0, "Police Bust Chance Decrease": 2, "Firewall Level Increase": 0}
        }


        self.items = {
            "Antivirus Software": {"Cost": 100, "Virus Detection Increase": 2},
            "Proxy Server": {"Cost": 200, "Hack Power Increase": 20},
            "Data Encryption Tool": {"Cost": 400, "Data Theft Bonus": 1.5}
        }

        # New variables to store data earned from hacks, data prices, and offshore account balance
        self.data_earned = 0
        self.data_prices = {"Credit Card Info": 5, "Sensitive Documents": 10, "Government Secrets": 15, "Corporate Data": 8}
        self.data_price_fluctuations = {"Credit Card Info": 0.2, "Sensitive Documents": 0.3, "Government Secrets": 0.4, "Corporate Data": 0.2}
        self.offshore_account_balance = 0

    def main(self):
        print(Fore.GREEN + "Welcome to Hacker Warz!" + Style.RESET_ALL)
        print("1. New Game")
        print("2. Load Game")
        print("3. Quit")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.new_game()
        elif choice == '2':
            self.load_game()
        elif choice == '3':
            print(Fore.RED + "Thanks for playing Hacker Warz!" + Style.RESET_ALL)
            return
        else:
            print(Fore.YELLOW + "Invalid choice. Try again." + Style.RESET_ALL)
            self.main()

    def new_game(self):
        self.balance = 1000
        self.days = 1
        self.hacks = 0
        self.firewall_level = 1
        self.virus_detected = False
        self.play_game()

    def load_game(self):
        try:
            with open("save_game.json", "r") as save_file:
                game_state = json.load(save_file)
                self.balance = game_state.get("balance", self.balance)
                self.offshore_account_balance = game_state.get("offshore_balance", self.offshore_account_balance)  # Load offshore account balance
                self.days = game_state.get("days", self.days)
                self.hacks = game_state.get("hacks", self.hacks)
                self.firewall_level = game_state.get("firewall_level", self.firewall_level)
                self.data_earned = game_state.get("data_earned", self.data_earned)
                self.items = game_state.get("items", self.items)  # Load items data
                self.upgrades = game_state.get("upgrades", self.upgrades)  # Load upgrades data
                # Update other game state variables as needed
                print(Fore.GREEN + "Game loaded successfully!" + Style.RESET_ALL)
                self.virus_detected = False
                self.play_game()
        except FileNotFoundError:
            print(Fore.YELLOW + "No saved game found. Starting a new game." + Style.RESET_ALL)
            self.new_game()

    def play_game(self):
        while True:
            print("\n=== Day", self.days, "===")
            print("Balance:", self.balance)
            print("Hacks:", self.hacks)
            print("Firewall Level:", self.firewall_level)
            print("Data Earned:", self.data_earned)
            print("Offshore Account Balance:", self.offshore_account_balance)
            print("\nOptions:")
            print("1. Hack a Location")
            print("2. Buy Upgrades")
            print("3. Buy Items")
            print("4. Sell Data")
            print("5. End Day")
            print("6. Save Game")
            print("7. Load Game")
            print("8. Exit Game")
            choice = input("Enter the number of your choice: ")

            if choice == '1':
                self.hack_location()
            elif choice == '2':
                self.buy_upgrades()
            elif choice == '3':
                self.buy_items()
            elif choice == '4':
                self.sell_data()
            elif choice == '5':
                self.end_day()
            elif choice == '6':
                self.save_game()
                print(Fore.GREEN + "Game saved successfully!" + Style.RESET_ALL)
            elif choice == '7':
                self.load_game()
            elif choice == '8':
                print(Fore.RED + "Thanks for playing Hacker Warz!" + Style.RESET_ALL)
                return
            else:
                print(Fore.YELLOW + "Invalid choice. Try again." + Style.RESET_ALL)
                
    def save_game(self):
        game_state = {
            "balance": self.balance,
            "offshore_balance": self.offshore_account_balance,  # Include offshore account balance
            "days": self.days,
            "hacks": self.hacks,
            "firewall_level": self.firewall_level,
            "data_earned": self.data_earned,
            "items": self.items,  # Include items data
            "upgrades": self.upgrades  # Include upgrades data
            # Add other game state data here
        }

        with open("save_game.json", "w") as save_file:
            json.dump(game_state, save_file)

    def hack_location(self):
        print("Choose a location to hack:")
        print("1. DarkWeb")
        print("2. Corporate")
        print("3. Government")
        print("4. Offshore Account")
        location_choice = input("Enter the number of your choice: ")

        if location_choice in ["1", "2", "3", "4"]:
            location = "DarkWeb" if location_choice == "1" else "Corporate" if location_choice == "2" else "Government" if location_choice == "3" else "Offshore Account"
            multiplier = self.location_multiplier[location]

            if location == "Offshore Account":
                offshore_options = ["Deposit", "Withdraw"]
                print("Choose an option for your Offshore Account:")
                for i, option in enumerate(offshore_options, start=1):
                    print(f"{i}. {option}")

                offshore_choice = input("Enter the number of your choice: ")

                if offshore_choice == '1':
                    deposit_amount = int(input("Enter the amount to deposit: "))
                    if deposit_amount > self.balance:
                        print(Fore.YELLOW + "You don't have enough balance for this deposit." + Style.RESET_ALL)
                    else:
                        self.offshore_account_balance += deposit_amount
                        self.balance -= deposit_amount
                        print(Fore.GREEN + f"${deposit_amount} deposited into your Offshore Account." + Style.RESET_ALL)
                elif offshore_choice == '2':
                    withdraw_amount = int(input("Enter the amount to withdraw: "))
                    if withdraw_amount > self.offshore_account_balance:
                        print(Fore.YELLOW + "You don't have enough balance in your Offshore Account for this withdrawal." + Style.RESET_ALL)
                    else:
                        self.offshore_account_balance -= withdraw_amount
                        self.balance += withdraw_amount
                        print(Fore.GREEN + f"${withdraw_amount} withdrawn from your Offshore Account." + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + "Invalid Offshore Account choice. Try again." + Style.RESET_ALL)
            else:
                # Chance of getting a virus with consequences
                virus_chance = random.randint(1, 100)
                if virus_chance <= 20:  # 20% chance of getting a virus
                    self.virus_detected = True
                    virus_removal_cost = 500
                    self.balance -= virus_removal_cost
                    print(Fore.RED + "Virus detected! You need to spend money to remove it." + Style.RESET_ALL)

                print("Choose a type of hack:")
                hack_options = list(self.hack_types[location].keys())
                for i, hack_option in enumerate(hack_options, start=1):
                    print(f"{i}. {hack_option}")

                hack_choice = input("Enter the number of your choice: ")

                if hack_choice.isdigit() and 1 <= int(hack_choice) <= len(hack_options):
                    hack_option = hack_options[int(hack_choice) - 1]
                    min_payment, max_payment = self.hack_types[location][hack_option]
                    payment = int(random.randint(min_payment, max_payment) * multiplier)
                    self.data_earned += 1  # Increment data earned
                    print(Fore.GREEN + f"You performed a {hack_option} and earned ${payment}!" + Style.RESET_ALL)

                    self.balance += payment
                    self.hacks += 1

                    # Higher-paying locations have a higher risk of getting busted
                    if location != "Offshore Account" and random.uniform(0, 1) < 0.4:
                        self.police_bust()
                else:
                    print(Fore.YELLOW + "Invalid hack choice. Try again." + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "Invalid location choice. Try again." + Style.RESET_ALL)

    def buy_upgrades(self):
        print("Available upgrades:")
        for upgrade, info in self.upgrades.items():
            print(f"{upgrade}: Cost ${info['Cost']}, Hack Power Increase {info['Hack Power Increase']}, Firewall Level Increase {info['Firewall Level Increase']}")

        upgrade_choice = input("Enter the name of the upgrade you want to buy (or 'cancel' to go back): ")

        if upgrade_choice in self.upgrades:
            if self.balance >= self.upgrades[upgrade_choice]["Cost"]:
                self.balance -= self.upgrades[upgrade_choice]["Cost"]
                self.firewall_level += self.upgrades[upgrade_choice]["Firewall Level Increase"]
                print(Fore.GREEN + f"{upgrade_choice} purchased!" + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + "You don't have enough balance to buy this upgrade." + Style.RESET_ALL)
        elif upgrade_choice.lower() == 'cancel':
            pass
        else:
            print(Fore.YELLOW + "Invalid upgrade choice. Try again." + Style.RESET_ALL)

    def buy_items(self):
        print("Available items:")
        for item, info in self.items.items():
            cost = info.get("Cost", "N/A")
            virus_detection_increase = info.get("Virus Detection Increase", "N/A")
            hack_power_increase = info.get("Hack Power Increase", "N/A")
            data_theft_bonus = info.get("Data Theft Bonus", "N/A")

            print(f"{item}: Cost ${cost}, Virus Detection Increase {virus_detection_increase}, Hack Power Increase {hack_power_increase}, Data Theft Bonus {data_theft_bonus}")

        while True:
            item_choice = input("Enter the name of the item you want to buy (or 'cancel' to go back): ")

            if item_choice in self.items:
                if self.balance >= self.items[item_choice]["Cost"]:
                    self.balance -= self.items[item_choice]["Cost"]
                    # Apply the effects of the item to the player's character
                    # For example, increase Virus Detection or Hack Power
                    print(Fore.GREEN + f"{item_choice} purchased! You now have new abilities." + Style.RESET_ALL)
                    break  # Exit the loop after a successful purchase
                else:
                    print(Fore.YELLOW + "You don't have enough balance to buy this item." + Style.RESET_ALL)
            elif item_choice.lower() == 'cancel':
                break  # Exit the loop if the player cancels
            else:
                print(Fore.YELLOW + "Invalid item choice. Try again." + Style.RESET_ALL)

    def sell_data(self):
        print("Choose the type of data to sell:")
        for i, data_type in enumerate(self.data_types, start=1):
            print(f"{i}. {data_type}")

        data_choice = input("Enter the number of your choice: ")

        if data_choice.isdigit() and 1 <= int(data_choice) <= len(self.data_types):
            data_type = self.data_types[int(data_choice) - 1]
            data_price = self.data_prices[data_type]
            price_fluctuation = self.data_price_fluctuations[data_type]
            fluctuation_chance = random.uniform(0, 1)

            if fluctuation_chance < 0.3:
                # Announce price fluctuation
                new_price_multiplier = random.uniform(1 - price_fluctuation, 1 + price_fluctuation)
                data_price = int(data_price * new_price_multiplier)
                print(Fore.CYAN + f"The price for {data_type} has changed. New price: ${data_price}" + Style.RESET_ALL)

            if self.data_earned > 0:
                amount_to_sell = int(input(f"Enter the amount of {data_type} to sell: "))

                if amount_to_sell > self.data_earned:
                    print(Fore.YELLOW + f"You don't have {amount_to_sell} {data_type} to sell." + Style.RESET_ALL)
                else:
                    earnings = amount_to_sell * data_price
                    self.data_earned -= amount_to_sell
                    self.balance += earnings
                    print(Fore.GREEN + f"You sold {amount_to_sell} {data_type} for ${earnings}." + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + "You don't have any data to sell." + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "Invalid data choice. Try again." + Style.RESET_ALL)

    def police_bust(self):
        print(Fore.RED + "The police have busted you!" + Style.RESET_ALL)

        # Confiscate a random percentage of cash
        confiscation_percentage = random.uniform(0.1, 0.5)
        confiscated_cash = int(self.balance * confiscation_percentage)
        self.balance -= confiscated_cash

        # Confiscate a random number of upgrades, but only if firewall level is greater than 1
        if self.firewall_level > 1:
            confiscated_upgrades = random.randint(1, self.firewall_level - 1)
            self.firewall_level -= confiscated_upgrades
            print(Fore.YELLOW + f"They confiscated ${confiscated_cash} and {confiscated_upgrades} of your upgrades." + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f"They confiscated ${confiscated_cash}, but your firewall level prevented further losses." + Style.RESET_ALL)

    def end_day(self):
        # Generate daily expenses
        daily_expenses = random.randint(50, 200)
        self.balance -= daily_expenses

        # Increase day count
        self.days += 1

        print(f"Day {self.days} ended.")
        print(f"Daily Expenses: ${daily_expenses}")
        print("Data Earned Today:", self.data_earned)
        print("Offshore Account Balance:", self.offshore_account_balance)

        # Check for game over conditions
        if self.balance <= 0:
            print("You ran out of money. Game over!")
            self.main()
        elif self.days > 30:
            print("You reached the end of the game. Congratulations!")
            self.main()
        else:
            self.play_game()

if __name__ == "__main__":
    game = HackerWarz()
    game.main()
