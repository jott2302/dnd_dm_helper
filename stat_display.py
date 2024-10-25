from ast import literal_eval

def get_info_creature(data):
    while True:
        try:
            wanted_creature = input(str("Von welcher Kreatur sollen die Statuswerte wiedergegeben werden?: ")).lower()
            print(f"\nInfos zu {wanted_creature}:")
            print(data[wanted_creature]["Stats"])
            print(data[wanted_creature]["Infos"])
            print("\n")
            return True
        except KeyError:
            print("Entweder ist die Kreatur nicht in dem Verzeichnis oder du musst auf die genaue Schreibweise achten.")

def get_info_player(data):
    while True:
        try:
            wanted_player = input(str("Von welchem Spieler sollen die Statuswerte wiedergegeben werden?: ")).lower()
            print(f"\nInfos zu {wanted_player}:")
            print(data[wanted_player])
            print("\n")
            return True
        except KeyError:
            print("Entweder ist der Spieler nicht in dem Verzeichnis oder du musst auf die genaue Schreibweise achten.")

def get_info_all_players(data):
    print("\n")
    for k, v in data.items():
        print(v)
    print("\n")


def display_stats(monster_data, player_data):
    while True:
        try:
            stat_type = input("""
Creature - Kreaturen Stats ausgeben lassen
Player - Spieler Stats ausgeben lassen
All Players - Alle Spieler Stats ausgeben lassen

Welche Statuswerte willst du angezeigt bekommen?: """).lower()
            if stat_type == "creature":
                get_info_creature(monster_data)
                return monster_data
            elif stat_type == "player":
                get_info_player(player_data)
                return player_data
            elif stat_type == "all players":
                get_info_all_players(player_data)
                return player_data
        except ValueError:
            print("Eingabe muss eines der vorgeschlagenen Commands sein")



