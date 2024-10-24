from dnd_dice import throw_dice

#################################################################################################################
def creature_generation(creature_type, creature_list):
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
            print("Der Wert muss eine Zahl größer als 0 sein!")


def add_initiative_bonus(temporary_dict_save, creature_list):
    while True:
        try:
            bonus = int(input("Welcher Initiative Modifier soll für die Kreatur verwendet werden?: "))
            for creature in creature_list:
                int_creature = bonus + throw_dice()
                temporary_dict_save.setdefault(creature.lower(), int_creature)
            return creature_list
        except ValueError:
            print("Der Wert muss eine Zahl sein!")


def participant_creation(temporary_dict_save, creature_list, creature_type):
    while True:
        if not creature_generation(creature_type, creature_list):
            break
        add_initiative_bonus(temporary_dict_save, creature_list)



#beide creature types "m" und "a" ausgeben. Danndann kompletten dictionary mit pandas ausgeben.

dict = {}
yee = []
print(yee)
participant_creation(dict, yee, "a")
print(dict)

