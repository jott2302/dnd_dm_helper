from dnd_dice import throw_dice

def generate_creatures(creature_type, creature_list, data, temporary_dict_save):
    """Works with a two option string, which decides the input question. Saves strings in a list whicht will be numbered
    ascending."""
    creature_class = {
        "m": "Monster",
        "a": "Verbündete"
    }
    creature_naming_question = {
        "m": "Wie heißt das angreifende Monster?(Bei Eingabe 0 Ende der Aufzählung): ",
        "a": "Wie heißt der unterstützende Verbündete?(Bei Eingabe 0 Ende der Aufzählung): "
    }
    creature = input(creature_naming_question[creature_type])
    while True:
        try:
            if creature == "0":
                print(f"Es werden keine weiteren {creature_class[creature_type]} hinzugefügt.")
                return False
            else:
                creature_count = int(input(f"Wie viele {creature} beteiligen sich an dem kampf?: "))
                for count in range(creature_count):
                    count += 1
                    creature_list.append(creature + " " + str(count))
                print(f"Es wurden {count} {creature} hinzugefügt.")
                add_initiative_bonus(temporary_dict_save,creature_list,data,creature)
                return creature
        except (UnboundLocalError, ValueError):
            print("Der Wert muss eine Zahl über 0 sein!")


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