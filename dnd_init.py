from dnd_dice import throw_dice

def manual_given_initiative(affected_group, temporary_dict_save):
    for player in affected_group:
        while True:
            try:
                int_player = input(f"Welche Initiative hat {player} gewürfelt?: ")
                temporary_dict_save.setdefault(player, int(int_player))
                break
            except ValueError:
                print("Der Wert muss eine Zahl sein")


def automatic_rolled_initiative(temporary_dict_save, *affected_group):
    all_groups = sum(affected_group,[])
    for participant in all_groups:
        int_participant = throw_dice()
        temporary_dict_save.setdefault(participant, int(int_participant))


def display_initiative(temporary_dict_save):
    for stats in sorted(temporary_dict_save.items(), key=lambda item: item[1], reverse=True):   #Nachschlagen
        print(stats)