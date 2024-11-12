import pandas as pd
from dnd_dice import throw_dice


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

def display_initiative(temporary_dict_save):
    """Converts a dictionary in a two-column-dataframe/ table.
    The columns display a creature with it's associated initiative value in descending numbering."""
    table = pd.DataFrame({"Kreatur": temporary_dict_save.keys(), "Initiative": temporary_dict_save.values()})
    table = table.sort_values(by="Initiative", ascending=False)
    print(f"\n{table.to_string(index=False)}\n")


def add_initiative_bonus(temporary_dict_save, creature_list, data, creature):
    """Assigns a string as a key to an integer input as value in a dcitionary. The keys are received from a list. """
    while True:
        try:
            if creature in data:
                modifier = int(data[creature]["Stats"]["DEX"].split("(")[1][:-1])
                for creature in creature_list:
                    int_creature = modifier + throw_dice()
                    temporary_dict_save.setdefault(creature.lower(), int_creature)
                return True
            else:
                modifier = int(input("Dieser Kreatur muss manuell ein Initiative Wert zugeordnet werden: "))
                for creature in creature_list:
                    int_creature = modifier + throw_dice()
                    temporary_dict_save.setdefault(creature.lower(), int_creature)
                return False
        except ValueError:
            print("Der Wert muss eine Zahl sein!")

