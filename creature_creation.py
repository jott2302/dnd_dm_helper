def generate_creatures(creature_type, creature_list):
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
                return True
        except (UnboundLocalError, ValueError):
            print("Der Wert muss eine Zahl über 0 sein!")
