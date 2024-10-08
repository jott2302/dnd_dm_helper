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


def automatic_rolled_initiative(temporary_dict_save, *affected_group):
    """Adds one or multiple lists contents and associates per content a
    random generated numeric value (initative stat) in a dictionary (key - list content, value - numeric)."""
    all_groups = sum(affected_group, [])
    modifier = input("Wie vielen Monstern und Verbündeten soll ein Initiative-Modifier angerechnet werden?: ")
    if modifier == "0":
        for participant in all_groups:
            int_participant = throw_dice()
            temporary_dict_save.setdefault(participant.lower(), int(int_participant))
    else:
       for _ in range(int(modifier)):
           add_initiative_bonus(temporary_dict_save, _)

def add_initiative_bonus (temporary_dict_save, modifier):
    participant = input(f"Benenne die Kreatur {modifier+1}: ")
    bonus = int(input(f"Bestimme den Initiative-Modifier von {participant}: "))
    int_participant = bonus + throw_dice()
    temporary_dict_save.setdefault(participant.lower()+ str(modifier+1), int_participant)

# Kreaturen Namen mit , zwischen zahl und Namen ausgeben
# keine doppelten namen in der Liste
# except Error bei falscher initiativ gebung
# nach erstellung der modified participants weiter loopen in automatic_rolled_initiative für den rest


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
        removal_number = input("Wieviele Kreaturen sollen aus dem Kampf entfernt werden? (Eingabe 0 -Cancel): ")
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
