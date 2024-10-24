from dnd_init import creature_generation, add_initiative_bonus

def create_player_list(chosen_names):
    """Determines the list to store the creatures (p - Spieler, m - Monster or a- Verbündeter)
    and returns the list."""
    decided_number = decide_player_count()
    generate_players(decided_number, chosen_names)
    return chosen_names

def creature_creation(temporary_dict_save, creature_list, creature_type):
    while True:
        if not creature_generation(creature_type, creature_list):
            break
        add_initiative_bonus(temporary_dict_save, creature_list)


def decide_player_count():
    """Determines the amount of times a creature is added to a list by an input."""
    while True:
        try:
            decided_number = int(input("Bestimme die Anzahl an Mitspielern: "))
            return decided_number
        except (AssertionError, ValueError):
            print("Der Wert muss eine positive Zahl sein.")


def generate_players(decided_number, chosen_names):
    """Adds creatures (p - Spieler, m - Monster or a- Verbündeter) in ascending numbering to a list.
    If the creature is p- Spieler the creature name is defined by an input."""
    for participant in range(decided_number):
        player = input(f"Wie heißt Spieler {participant+1}: ")
        chosen_names.append(player)

