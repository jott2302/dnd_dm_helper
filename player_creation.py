from dnd_initiative import display_initiative

def decide_player_count():
    """Determines the amount of players added to a list by an input."""
    while True:
        try:
            decided_number = int(input("Bestimme die Anzahl an Mitspielern: "))
            if decided_number > 0:
                return decided_number
            else:
                print("Der Wert muss eine positive Zahl, größer als 0 sein.")
        except (AssertionError, ValueError):
            print("Der Wert muss eine positive Zahl sein.")

def generate_players(decided_number, chosen_names):
    """Adds players to a list, the names are decided via input."""
    for participant in range(decided_number):
        player = input(f"Wie heißt Spieler {participant+1}: ")
        if player == "":
            automatic_generated_player = "Spieler "+str(participant+1)
            chosen_names.append(automatic_generated_player)
        else:
            chosen_names.append(player)

def create_player_list(chosen_names):
    """Calls the function to decide an integer input. Then calls the function to as many strings to a list as the
    previous function integers value."""
    decided_number = decide_player_count()
    generate_players(decided_number, chosen_names)
    return chosen_names


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


def remove_multiple_participant(temporary_dict_save):
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
