from dnd_dice import throw_dice
import pandas as pd


def manual_given_initiative(affected_group, temporary_dict_save):
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
            print("Der Wert muss eine Zahl über 0 sein!")


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


# nach erstellung der modified participants weiter loopen in automatic_rolled_initiative für den rest
# differenzieren zwischen modified monster und verbündeter


def display_initiative(temporary_dict_save):
    """Converts a dictionary in a two-column-dataframe/ table.
    The columns display a creature with it's associated initiative value in descending numbering."""
    table = pd.DataFrame({"Kreatur": temporary_dict_save.keys(), "Initiative": temporary_dict_save.values()})
    table = table.sort_values(by="Initiative", ascending=False)
    print(f"\n{table.to_string(index=False)}\n")


def remove_participant(temporary_dict_save):
    """Removes a single participant by name."""
    while True:
        participant = input(
            "Welcher Mitspieler/ NPC soll aus dem Kampf entfernt werden (Eingabe 0 - Cancel): ").lower()
        if participant == "0":
            print("Es wurde kein Teilnehmer entfernt.")
            display_initiative(temporary_dict_save)
            return False
        elif participant in temporary_dict_save:
            temporary_dict_save.pop(participant)
            print(f"{participant} wurde entfernt.")
            display_initiative(temporary_dict_save)
            return True
        else:
            print(
                "Teilnehmer nicht gefunden. Bitte gebe den korrekten Namen des Spielers/ NPC, entsprechend der Auflistung, wieder!")


def multi_remove_participant(temporary_dict_save):
    """Removes multiple participants based on user input."""
    while True:
        removal_number = input("Wie viele Kreaturen sollen aus dem Kampf entfernt werden? (Eingabe 0 -Cancel): ")
        if removal_number == "0":
            print("Es wurden keine Teilnehmer entfernt.")
            display_initiative(temporary_dict_save)
            return False
        try:
            removal_number = int(removal_number)
            remove_any_participant = False
            for _ in range(removal_number):
                removed = remove_participant(temporary_dict_save)
                if removed is False:
                    print("Vorgang abgebrochen.")
                    return False
                elif removed is True:
                    remove_any_participant = True
            return remove_any_participant
        except ValueError:
            print("Der Wert muss eine Zahl sein!")
