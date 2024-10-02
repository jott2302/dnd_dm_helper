import ast
import re
from unittest.mock import patch
from dnd_dice import run_game, throw_dice, throw_multiple_dice


# pip install pytest in konsole
class TestDice:

    @patch('builtins.print') # Fängt prints zum testen ab
    @patch('builtins.input', side_effect=['Alice', '4', '4', '4', '0']) # Legt inputs für input() fest
    def test_run_game(self, mock_input, mock_print):
        run_game()
        # Überprüft, dass die Aussage geprintet wurde
        mock_print.assert_any_call("Du kannst das Program jederzeit mit einer Würfeleingabe von 0 beenden!")
        # Überprüft, dass die Aussage geprintet wurde
        mock_print.assert_any_call("Würfel bitte nocheinmal, es ist etwas schief gelaufen.\n\n")

        assert mock_print.call_count == 11 # Überprüft, dass die Gesamtanzahl Anzahl der Prints stimmt

    def test_throw_dice(self):
        dice_number = 6
        throws = [throw_dice(dice_number) for _ in range(1000)] # 1000 mal würfeln, um nicht lucky den test zu bestehen
        assert all([1 <= throw <= dice_number for throw in throws]) # Überprüfen, dass alle Würfe zwischen 1 und dice_number sind

    @patch('builtins.print') # Fängt prints zum Testen ab
    @patch('builtins.input', side_effect=['6', '1011', '100', '3650', 'ABC', '3', '?','1','1']) # Legt inputs für input() fest
    def test_throw_multiple_dice(self, mock_input, mock_print):
        throw_multiple_dice()
        assert mock_print.call_args_list[1][0][0] == '\n' # Überprüft zweite ausgabe
        # Findet die gewürfelte liste im print string und wandelt diese von dem String in eine Python Liste um
        thrown_list = ast.literal_eval(re.findall(r'\[([^]]*)]', mock_print.call_args_list[0][0][0])[0])
        # Überprüft, dass alle würfe in dem geforderten bereich sind
        assert all([1 <= throw <= 6 for throw in thrown_list])
        # Überprüft, ob Wurfanzahl stimmt
        assert len(thrown_list) == 1011
        # Löscht prints wegen übersichtlichkeit
        mock_print.reset_mock()

        # Dasselbe wie obendrüber mit anderen zahlen
        throw_multiple_dice()
        thrown_list = ast.literal_eval(re.findall(r'\[([^]]*)]', mock_print.call_args_list[0][0][0])[0])
        assert mock_print.call_args_list[1][0][0] == '\n'
        assert all([1 <= throw <= 100 for throw in thrown_list])
        assert len(thrown_list) == 3650
        mock_print.reset_mock()

        # Überprüft korrektes verhalten bei Fehleingaben
        throw_multiple_dice()
        thrown_list = [ast.literal_eval(re.findall(r'\[([^]]*)]', mock_print.call_args_list[2][0][0])[0])]

        # Überprüfung der 1. und 2. Ausgabe
        assert mock_print.call_args_list[0][0][0] == "\nDie Eingaben für die Würfel müssen Zahlen sein.\n"
        assert mock_print.call_args_list[1][0][0] == "\nDie Eingaben für die Würfel müssen Zahlen sein.\n"
        # Überprüfung der geworfenen Würfe
        assert all([1 <= throw <= 1 for throw in thrown_list])
        assert len(thrown_list) == 1

