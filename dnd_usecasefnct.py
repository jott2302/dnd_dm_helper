def create_participant_list(chosen_names, creature_type):
    """Determines the list to store the creatures (p - Spieler, m - Monster or a- Verbündeter)
    and returns the list."""
    decided_number = (decide_creature_count(creature_type))
    generate_creatures(creature_type, decided_number, chosen_names)
    return chosen_names


def decide_creature_count(creature_type):
    """Determines the amount of times a creature is added to a list by an input."""
    creation_question_formats = {
        "p": "Anzahl an Spielern: ",
        "m": "Anzahl der angreifenden Monster: ",
        "a": "Wie viele verbündete NPC beteiligen sich an dem Kampf (0 - keine): "
    }

    while True:
        try:
            decided_number = int(input(creation_question_formats[creature_type]))
            if decided_number == 0:
                print("Es wurden keine Kreaturen erstellt.")
                return False
            else:
                return decided_number
        except (AssertionError, ValueError):
            print("Der Wert muss eine positive Zahl sein.")


def generate_creatures(creature_type, decided_number, chosen_names):
    """Adds creatures (p - Spieler, m - Monster or a- Verbündeter) in ascending numbering to a list.
    If the creature is p- Spieler the creature name is defined by an input."""
    creature_formats = {
        "p": "Wie heißt Spieler {}: ",
        "m": "Monster {}",
        "a": "Verbündeter {}"
    }

    for participant in range(decided_number):
        if creature_type == "p":
            player = input(creature_formats[creature_type].format(participant + 1))
            chosen_names.append(player)
        else:
            creature = creature_formats[creature_type].format(participant + 1)
            chosen_names.append(creature)
