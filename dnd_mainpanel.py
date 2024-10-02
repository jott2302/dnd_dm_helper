from dnd_dice import throw_multiple_dice
from dnd_usecasefnct import create_participants
from dnd_init import manual_given_initiative, automatic_rolled_initiative, display_initiative, remove_participant, \
    multi_remove_participant

player_names = []
monster_listing = []
ally_listing = []
initiative_dict = {}

print("Gib zuerst die Spieleranzahl in das Programm ein und benenne diese Anschließend.")
create_participants(player_names, "p")

panel_running = True

while panel_running:

    dm_command = input("Welche Aktion willst du ausführen? : ").lower()
    if dm_command == "fight":
        create_participants(monster_listing, "m")
        create_participants(ally_listing, "a")
        manual_given_initiative(player_names, initiative_dict)
        automatic_rolled_initiative(initiative_dict, monster_listing, ally_listing)
        display_initiative(initiative_dict)
        fight_running = True
        while fight_running:
            try:
                fight_command = input("Mit dem Command Kill/ Multikill eine oder mehrere Kreatur(en) töten oder mit Kampf beenden den Kampf beenden: ").lower()
                if fight_command == "kill":
                    remove_participant(initiative_dict)
                    display_initiative(initiative_dict)
                elif fight_command == "stop":
                    print("\n Der Kampf wurde erfolgreich beendet. \n")
                    monster_listing.clear()
                    ally_listing.clear()
                    initiative_dict.clear()
                    fight_running = False
                elif fight_command == "multikill":
                    multi_remove_participant(initiative_dict)
            except ValueError:
                print("Du kannst nur kill oder kampf beenden verwenden")

    elif dm_command == "dice":
        throw_multiple_dice()

    elif dm_command == "end":
        print("\nProgramm wurde beendet")
        panel_running = False

    elif dm_command == "help":
        print(
            """
            Eingabe: Kampf - fight starten
            Eingabe im Kampf: Kill - Kreatur wird getötet
            Eingabe im Kampf: Multikill - mehrere Kreaturen werden getötet
            Eingabe im Kampf: Stop - Kampf wird beendet
            Eingabe: Dice - wirft eine gewünschte Anzahl an beliebigen Würfeln
            Eingabe: End - Programm Ende
            """)

    else:
        print("Deine Eingabe muss ein passendes Command sein. Schlage die Commands über die Eingabe Help nach")
        print("\n")


# modifier für dice rolls eingeben



