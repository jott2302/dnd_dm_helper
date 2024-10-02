def create_participants(chosen_names, creature):

    if creature == "p":
        while True:
            try:
                decided_number = int(input("Anzahl an Spielern: "))
                break
            except ValueError:
                print("Der Wert muss eine Zahl sein")

        dm_list = list(range(decided_number))
        for i in dm_list:
            player = input(f"Wie heißt Spieler {dm_list[i]}: ")
            chosen_names.append(player)

    elif creature == "m":
        while True:
            try:
                decided_number = int(input("Anzahl der angreifenden Monster: "))
                break
            except ValueError:
                print("Der Wert muss eine Zahl sein")

        dm_list = list(range(decided_number))
        for i in dm_list:
            monster = f"monster {i}"
            chosen_names.append(monster)

    elif creature == "a":
        while True:
            try:
                decided_number = int(input("Wieviele verbündete NPC beteiligen sich an dem Kampf (0 - keine): "))
                break
            except ValueError:
                print("Der Wert muss eine Zahl sein")

        dm_list = list(range(decided_number))
        for i in dm_list:
            ally = f"Verbündeter {i}"
            chosen_names.append(ally)

    return chosen_names

# funktionen schreiben für überschneidungen
