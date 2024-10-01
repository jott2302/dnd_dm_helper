from dnd_usecasefnct import create_participants
from dnd_init import manual_given_initiative, automatic_rolled_initiative, display_initiative, remove_participant


player_names = []
monster_listing = []
ally_listing = []
initiative_dict = {}



print("Gib zuerst die Spieleranzahl in das Programm ein und benenne diese Anschließend.")

create_participants(player_names, "p")

create_participants(monster_listing,  "m")

create_participants(ally_listing, "a")

manual_given_initiative(player_names,initiative_dict)

automatic_rolled_initiative(initiative_dict, monster_listing, ally_listing)

display_initiative(initiative_dict)

remove_participant(initiative_dict)




# Spieler Listen sollen Permanent bleiben /Monster nach Eingabe des DM gelöscht oder automatisch vor dem nächsten initiative roll
# modifier für dice rolls eingeben
# panel für dm erstellen


