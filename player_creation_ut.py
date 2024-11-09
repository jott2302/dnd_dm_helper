import unittest
from unittest.mock import patch
from player_creation import decide_player_count, generate_players, remove_participant


class TestDecidePlayerCount(unittest.TestCase):
    @patch("builtins.input", side_effect=["3"])
    def test_valid_input(self, mock_input):
        result = decide_player_count()
        self.assertEqual(result, 3)

    @patch("builtins.input", side_effect=["-1", "0", "5"])
    def test_invalid_then_valid_input(self, mock_input):
        result = decide_player_count()
        self.assertEqual(result, 5)

    @patch("builtins.input", side_effect=["abc", "xyz", "10"])
    def test_non_integer_then_valid_input(self, mock_input):
        result = decide_player_count()
        self.assertEqual(result, 10)


class TestGeneratePlayers(unittest.TestCase):
    @patch("builtins.input", side_effect=["Julian", "Max", "Leon", "Gullo"])
    def test_valid_names(self, mock_input):
        chosen_names = []
        decided_number = 4
        generate_players(decided_number, chosen_names)
        self.assertEqual(chosen_names, ["Julian", "Max", "Leon", "Gullo"])

    @patch("builtins.input", side_effect=["123", "456", "789"])
    def test_numeric_names(self, mock_input):
        chosen_names = []
        decided_number = 3
        generate_players(decided_number, chosen_names)
        self.assertEqual(chosen_names, ["123", "456", "789"])

    @patch("builtins.input", side_effect=["", "", "", "Julian", ""])
    def test_empty_string_name(self, mock_input):
        chosen_names = []
        decided_number = 5
        generate_players(decided_number, chosen_names)
        self.assertEqual(chosen_names, ["Spieler 1", "Spieler 2", "Spieler 3", "Julian", "Spieler 5"])

    @patch("builtins.input", side_effect=["   ", "", "Jott", "     "])
    def test_spacebar_input(self, mock_input):
        chosen_names= []
        decided_number=4
        generate_players(decided_number,chosen_names)
        self.assertEqual(chosen_names, ["Spieler 1", "Spieler 2", "Jott", "Spieler 4"])

    @patch("builtins.input", side_effect=["Julian", "Julian", "Julian ", "Max", "Julian"])
    def test_reacurring_name(self, mock_input):#
        chosen_names = []
        decided_number = 5
        generate_players(decided_number, chosen_names)
        self.assertEqual(chosen_names, ["Julian", "Julian 2", "Julian 3", "Max", "Julian 4"])

class TestRemoveParticipant(unittest.TestCase):
    @patch("builtins.input", side_effect=["MONSTER 1"])
    def test_valid_removal_input(self,mock_input):
        temporary_dict_save = {"monster 1" : 2, "monster 2" : 2, "julian": 2}
        remove_participant(temporary_dict_save)
        self.assertEqual(temporary_dict_save, {"monster 2" : 2, "julian": 2})

if __name__ == "__main__":
    unittest.main()
