import unittest
from unittest import TestCase

from project.hero import Hero


class HeroTest(TestCase):
    USERNAME = 'Username'
    LEVEL = 10
    HEALTH = 50.0
    DAMAGE = 30

    def setUp(self) -> None:
        self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

    def test_init(self):
        self.assertEqual(self.hero.username, self.USERNAME)
        self.assertEqual(self.hero.level, self.LEVEL)
        self.assertEqual(self.hero.health, self.HEALTH)
        self.assertEqual(self.hero.damage, self.DAMAGE)

    def test_battle_with_same_username_of_hero_raise(self):
        enemy_hero = self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)
        with self.assertRaises(Exception) as error:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(error.exception))

    def test_battle_with_health_lower_than_zero_raise(self):
        self.hero.health = -10
        enemy_hero = Hero('Enemy Hero', 30, 70.0, 50.0)
        with self.assertRaises(ValueError) as error:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

    def test_battle_with_health_equal_to_zero_raise(self):
        self.hero.health = 0
        enemy_hero = Hero('Enemy Hero', 30, 70.0, 50.0)
        with self.assertRaises(ValueError) as error:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

    def test_battle_with_enemy_with_health_below_zero_raise(self):
        enemy_hero = Hero('Enemy Hero', 30, -10, 50.0)
        with self.assertRaises(ValueError) as error:
            self.hero.battle(enemy_hero)
        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(error.exception))

    def test_battle_with_enemy_with_health_equal_to_zero_raise(self):
        enemy_hero = Hero('Enemy Hero', 30, 0, 50.0)
        with self.assertRaises(ValueError) as error:
            self.hero.battle(enemy_hero)
        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(error.exception))

    def test_battle_when_both_players_dies_returns_draw(self):
        enemy_hero = Hero('Enemy username', self.LEVEL, self.HEALTH, self.DAMAGE)
        expected_health = self.hero.health - (self.hero.damage * self.hero.level)
        result = self.hero.battle(enemy_hero)

        self.assertEqual('Draw', result)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_health, enemy_hero.health)

    def test_battle_when_enemy_dies_return_win(self):
        enemy_hero = Hero('Enemy username', 5, 10, 5)
        expected_hero_health = (self.hero.health - (enemy_hero.damage * enemy_hero.level)) + 5
        expected_hero_level = self.hero.level + 1
        expected_hero_damage = self.hero.damage + 5
        expected_enemy_health = enemy_hero.health - (self.hero.damage * self.hero.level)
        result = self.hero.battle(enemy_hero)

        self.assertEqual('You win', result)
        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(expected_hero_level, self.hero.level)
        self.assertEqual(expected_hero_damage, self.hero.damage)
        self.assertEqual(expected_enemy_health, enemy_hero.health)

    def test_battle_when_you_hero_dies_return_lose(self):
        enemy_hero = Hero('Enemy username', 50, 1000, 50)
        expected_enemy_health = (enemy_hero.health - (self.hero.damage * self.hero.level)) + 5
        expected_enemy_level = enemy_hero.level + 1
        expected_enemy_damage = enemy_hero.damage + 5
        expected_hero_health = self.hero.health - (enemy_hero.damage * enemy_hero.level)
        result = self.hero.battle(enemy_hero)

        self.assertEqual('You lose', result)
        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(expected_enemy_level, enemy_hero.level)
        self.assertEqual(expected_enemy_damage, enemy_hero.damage)
        self.assertEqual(expected_enemy_health, enemy_hero.health)

    def test_str_representation(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                          f"Health: {self.hero.health}\n" \
                          f"Damage: {self.hero.damage}\n"
        actual_result = self.hero.__str__()

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
