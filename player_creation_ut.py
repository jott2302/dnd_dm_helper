import unittest
from unittest.mock import patch
from player_creation import decide_player_count


class TestDecidePlayerCount(unittest.TestCase):
    @patch("builtins.input", side_effect=["3"])
    def test_valid_input(self, mock_input):
        result = decide_player_count()
        self.assertEqual(result, 3)

    @patch("builtins.input", side_effect=["-1", "0", "5"])
    def test_invalid_then_valid_input(self, mock_input):
        result = decide_player_count()
        self.assertEqual(result, 5)

    @patch("builtins.input", side_effect=["abc", "xyz", True, "10"])
    def test_non_integer_then_valid_input(self, mock_input):
        result = decide_player_count()
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main()