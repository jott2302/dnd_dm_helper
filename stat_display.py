from ast import literal_eval

filepath_monster = "monster_data/monsters_raw.txt"

with open(filepath_monster, "r", encoding="UTF-8") as file:
    monster_data = literal_eval(file.read())

filepath_player = "C://Users//julia//Desktop//dnd_player_stats.txt"

with open(filepath_player, "r", encoding="UTF-8") as player_file:
    player_data = literal_eval(player_file.read())

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

def get_info_all_players():
    #for dictionary in data:
    #    for _ in dictionary:
    #        print(data)
    with open("C://Users//julia//Desktop//dnd_player_stats.txt", 'r') as file:
        for line in file:
            print(line.strip())


get_info_all_players()

#Commands einfügen
#get_info_all_players verbessern