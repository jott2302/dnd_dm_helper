from dnd_dice import throw_multiple_dice
from player_creation import create_player_list, remove_participant, remove_multiple_participant
from dnd_initiative import assign_player_initiative, display_initiative, assign_creature_initiative
from external_data_implement import display_stats
from ast import literal_eval

filepath_monster = "monster_data/monsters_raw.txt"

with open(filepath_monster, "r", encoding="UTF-8") as file:
    monster_data = literal_eval(file.read())

filepath_player = "C://Users//julia//Desktop//dnd_player_stats.txt"

with open(filepath_player, "r", encoding="UTF-8") as player_file:
    player_data = literal_eval(player_file.read())


player_names = []
monster_listing = []
ally_listing = []
initiative_dict = {}


print("Gib zuerst die Spieleranzahl in das Programm ein und benenne diese Anschließend.")
create_player_list(player_names)

panel_running = True

while panel_running:

    dm_command = input("Welche Aktion willst du ausführen? : ").lower()
    if dm_command == "fight":
        assign_creature_initiative(initiative_dict, monster_listing,"m", monster_data)
        assign_creature_initiative(initiative_dict,ally_listing, "a", monster_data)
        assign_player_initiative(player_names, initiative_dict)
        display_initiative(initiative_dict)
        fight_running = True
        while fight_running:
            try:
                fight_command = input(
                    "Mit dem Command Kill/ Multikill eine oder mehrere Kreatur(en) töten oder mit Stop den Kampf beenden: ").lower()
                if fight_command == "kill":
                    remove_participant(initiative_dict)
                elif fight_command == "stop":
                    print("\n Der Kampf wurde erfolgreich beendet. \n")
                    monster_listing.clear()
                    ally_listing.clear()
                    initiative_dict.clear()
                    fight_running = False
                elif fight_command == "multikill":
                    remove_multiple_participant(initiative_dict)
                elif fight_command == "stats":
                    display_stats(monster_data, player_data)
                    display_initiative(initiative_dict)
            except ValueError:
                print("Du kannst nur Mutlikill/ Kill oder Stop verwenden")

    elif dm_command == "dice":
        throw_multiple_dice()

    elif dm_command == "end":
        print("\nProgramm wurde beendet")
        panel_running = False

    elif dm_command == "stats":
        display_stats(monster_data,player_data)

    elif dm_command == "help":
        print(
            """
            Eingabe: Fight - Kampf starten
            Eingabe im Kampf: Kill - Kreatur wird getötet
            Eingabe im Kampf: Multikill - mehrere Kreaturen werden getötet
            Eingabe im Kampf: Stop - Kampf wird beendet
            Eingabe immer: Stats - Stats von Kreaturen oder Spielern anzeigen lassen
            Eingabe: Dice - wirft eine gewünschte Anzahl an beliebigen Würfeln
            Eingabe: End - Programm Ende
            """)

    else:
        print("Deine Eingabe muss ein passendes Command sein. Schlage die Commands über die Eingabe Help nach.")
        print("\n")


#formatieren in der ausgabe
#unit Testing anschauen KANN MAN MACHEN
#assertion Error überarbeiten KANN MAN MACHEN
# GUI



