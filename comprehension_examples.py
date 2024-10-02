"""
Comprehensions dienen dazu Objekte wie Listen oder Dictionaries durch einen Loop direkt zu erstellen.
Sie sind effizienter und lesbarer als das Befüllen eines Objektes wie einer liste durch einen normalen Loop.
Deshalb verwenden Python Entwickler Comprehensions wo es möglich ist.
"""
def get_player_name() -> str:
    """Funktion, welche die eingabe eines Spielernamens ermöglicht

    :return: Eingegebener Spielername
    """
    return input('Spielername Eingeben:\n')

def get_initiative() -> int:
    """Funktion, die es Ermöglicht eine Initiative einzugeben.
    Die Abfrage wird so lange wiederholt, bis eine gültige Zahl eingegeben wird.

    :return: Eingegebene ganzzahlige Initiative
    """
    while 1:
        try:
            return int(input('Initiative eingeben:\n'))
        except ValueError:
            print('Eine Initiative kann nur eine Zahl sein, bitte versuche es noch einmal.')

# Der Ansatz, den du kennst (in dem fall hier erstellst du eine liste mit {number_of_players} spielern)

#number_of_players = 2
#player_list = []
#for _ in range(number_of_players):
#    player_list.append(get_player_name())
#print(player_list)

# Die 'bessere' Art eine Liste mit Spielern zu erstellen (je weniger code die Lösung eines Problems benötigt, desto besser)

number_of_players = 2
player_list = [get_player_name() for _ in range(number_of_players)] # Dieser Code macht exakt, was der Code obendrüber auch macht
print(player_list)
# Funktioniert auch für dictionaries

# Normaler Loop Ansatz:

#number_of_players = 2
#initiative_dictionary = {}
#for _ in range(number_of_players):
#    initiative_dictionary[get_player_name()] = get_initiative()
#print(initiative_dictionary)

# Comprehension (macht exakt, was der normale loop Ansatz macht)

#number_of_players = 2
#initiative_dictionary = {get_player_name(): get_initiative() for _ in range(number_of_players)}
#print(initiative_dictionary)