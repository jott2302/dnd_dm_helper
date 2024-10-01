from dnd_dice import throw_dice
import pandas as pd

def manual_given_initiative(affected_group, temporary_dict_save):
    for player in affected_group:
        while True:
            try:
                int_player = input(f"Welche Initiative hat {player} gewürfelt?: ")
                temporary_dict_save.setdefault(player.lower(), int(int_player))
                break
            except ValueError:
                print("Der Wert muss eine Zahl sein")


def automatic_rolled_initiative(temporary_dict_save, *affected_group):
    all_groups = sum(affected_group,[])
    for participant in all_groups:
        int_participant = throw_dice()
        temporary_dict_save.setdefault(participant.lower(), int(int_participant))


# strip Kreaturen recherchieren (sauberere Tabelle)
def display_initiative(temporary_dict_save):
    table = pd.DataFrame({"Kreatur": temporary_dict_save.keys(), "Initiative": temporary_dict_save.values()})
    table.sort_values(by="Initiative",inplace=True, ascending=False)
    print(f"\n{table.to_string(index=False)}\n")


def remove_participant(temporary_dict_save):
    while True:
        try:
            participant = input(f"Welcher Mitspieler/ NPC soll aus dem Kampf entfernt werden (Eingabe 0 - Cancel): ").lower()
            if participant == "0":
                print("Es wurde kein Teilnehmer entfernt.")
                display_initiative(temporary_dict_save)
                break
            else:
                temporary_dict_save.pop(participant)
                display_initiative(temporary_dict_save)
                break

        except KeyError:
            print("Bitte gebe den korrekten Namen des Spielers/ NPC, entsprechend der Auflistung, wieder!")
