from character import player
import sys

class Item:
    def __init__(self, item_name, item_cost):
        self.item_name = item_name
        self.item_cost = item_cost

def baker_trade(item):
    if player.money >= item.item_cost:
        player.money -= item.item_cost
        player.inventory.append(item.item_name)
        print(f"you bought {item.item_name} for {item.item_cost}!")
        return True
    else:
        print("You don't have enough money.")
        return False


sourdough = Item("sourdough", 2)
pumpernickel = Item("pumpernickel", 3)


