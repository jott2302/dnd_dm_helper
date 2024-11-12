from dnd_initiative import add_initiative_bonus

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

def assign_creature_initiative(temporary_dict_save, creature_list, creature_type, data):
    """Calls a function multiple times, till it returns false. Then it calls the second function a single time."""
    while True:
        if not generate_creatures(creature_type, creature_list,data ,temporary_dict_save):
            break
