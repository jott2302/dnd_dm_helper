from dnd_dice import throw_dice
import pandas as pd
from creature_creation import generate_creatures


def assign_player_initiative(affected_group, temporary_dict_save):
    """Iterates over a list associating each content with a numeric input (initiative),
    storing it in a dictionary."""
    for player in affected_group:
        while True:
            try:
                int_player = input(f"Welche Initiative hat {player} gewürfelt?: ")
                temporary_dict_save.setdefault(player.lower(), int(int_player))
                break
            except (AssertionError, ValueError):
                print("Der Wert muss eine positive Zahl oder 0 sein")


def add_initiative_bonus(temporary_dict_save, creature_list):
    """Assigns a string as a key to an integer input as value in a dcitionary. The keys are received from a list. """
    while True:
        try:
            bonus = int(input("Welcher Initiative Modifier soll für die Kreatur verwendet werden?: "))
            for creature in creature_list:
                int_creature = bonus + throw_dice()
                temporary_dict_save.setdefault(creature.lower(), int_creature)
            return creature_list
        except ValueError:
            print("Der Wert muss eine Zahl sein!")


def display_initiative(temporary_dict_save):
    """Converts a dictionary in a two-column-dataframe/ table.
    The columns display a creature with it's associated initiative value in descending numbering."""
    table = pd.DataFrame({"Kreatur": temporary_dict_save.keys(), "Initiative": temporary_dict_save.values()})
    table = table.sort_values(by="Initiative", ascending=False)
    print(f"\n{table.to_string(index=False)}\n")

def assign_creature_initiative(temporary_dict_save, creature_list, creature_type):
    """Calls a function multiple times, till it returns false. Then it calls the second function a single time."""
    while True:
        if not generate_creatures(creature_type, creature_list):
            break
        add_initiative_bonus(temporary_dict_save, creature_list)

