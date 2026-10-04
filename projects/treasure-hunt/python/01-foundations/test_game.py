"""Maintainer checks. Run: python3 -m unittest discover -s projects/treasure-hunt/python/01-foundations -p 'test_*.py'"""
import contextlib
import importlib.util
import io
from pathlib import Path
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("treasure_game", Path(__file__).with_name("game.py"))
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)


class GameTests(unittest.TestCase):
    def run_session(self, commands):
        output = io.StringIO()
        with patch("builtins.input", side_effect=commands), patch.object(game.random, "randint", return_value=3), contextlib.redirect_stdout(output):
            game.main()
        return output.getvalue()

    def test_win_all_difficulties(self):
        for difficulty in ("1", "2", "3"):
            with self.subTest(difficulty=difficulty):
                text = self.run_session([difficulty, "north", "take", "east", "take", "south", "take", "west", "no"])
                self.assertIn("You win!", text)
                self.assertIn("Treasure progress: 100.0% | Bonus coins: 9", text)
                self.assertIn("3. Treasure from river", text)

    def test_validation_and_duplicate_collection(self):
        text = self.run_session(["hello", "1.5", "0", "4", "2", "status", "banana", "take", " NORTH ", "take", "take", "status", "quit", "maybe", "no"])
        self.assertIn("Please enter a whole number.", text)
        self.assertIn("Choose 1, 2, or 3.", text)
        self.assertIn("Your inventory is empty.", text)
        self.assertIn("not available", text)
        self.assertEqual(text.count("Treasure collected!"), 1)
        self.assertIn("Treasure progress: 33.3% | Bonus coins: 3", text)
        self.assertIn("Please type yes or no.", text)

    def test_history_and_unique_visits(self):
        text = self.run_session(["2", "north", "south", "north", "status", "quit", "no"])
        self.assertIn("Unique rooms visited: 2/4", text)
        self.assertIn("Recent route: forest -> camp -> forest", text)

    def test_loss_and_replay_reset(self):
        text = self.run_session(["3", "north", "take", "east", "west", "east", "yes", "2", "status", "north", "take", "quit", "no"])
        self.assertIn("Game over!", text)
        self.assertIn("Treasure progress: 0.0% | Bonus coins: 0", text)
        self.assertIn("Unique rooms visited: 1/4", text)
        self.assertEqual(text.count("Treasure collected!"), 2)

    def test_helpers_and_fresh_maps(self):
        self.assertEqual(game.apply_damage(7, 2), 5)
        self.assertEqual(game.apply_damage(3, 5), 0)
        self.assertEqual(game.apply_damage(7, 0), 7)
        rooms = game.create_rooms()
        self.assertIsNone(game.find_treasure(rooms["camp"], "camp"))
        self.assertEqual(game.find_treasure(rooms["forest"], "forest"), "forest")
        rooms["forest"]["treasure"] = False
        self.assertTrue(game.create_rooms()["forest"]["treasure"])

    def test_terminal_interruptions(self):
        for error in (EOFError, KeyboardInterrupt):
            text = self.run_session([error()])
            self.assertIn("Adventure closed.", text)


if __name__ == "__main__":
    unittest.main()
