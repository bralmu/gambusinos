import unittest
from unittest import TestCase
from gambusino import (
    Gambusino, DEFAULT_AGE, DEFAULT_HEALTH, DEFAULT_FOOD, DEFAULT_POS_X, 
    DEFAULT_POS_Y, DEFAULT_MEMORY,
)
import ia.iaTest


class GambusinoTests(TestCase):
    def test_create_gambusino(self):
        gam_ = Gambusino(0,0,'iaTest.py')
        
    def test_new_gambusino_has_correct_values(self):
        id_num = 7
        team = 2
        ia_filename = 'iaTest.py'
        gam_ = Gambusino(id_num, team, ia_filename)
        self.assertEqual(gam_.age, DEFAULT_AGE)
        self.assertEqual(gam_.health, DEFAULT_HEALTH)
        self.assertEqual(gam_.food, DEFAULT_FOOD)
        self.assertEqual(gam_.posX, DEFAULT_POS_X)
        self.assertEqual(gam_.posY, DEFAULT_POS_Y)
        self.assertEqual(gam_.id_num, id_num)
        self.assertEqual(gam_.team, team)
        self.assertEqual(gam_.ia.NAME, ia.iaTest.NAME)
        self.assertEqual(gam_.memory, DEFAULT_MEMORY)
        
    def test_feeding_the_gambusino(self):
        gam_ = Gambusino(0, 0, 'iaTest.py')
        gam_.food = 50
        # Feeding
        consumed = gam_.feed(20)
        self.assertEqual(consumed, 20)
        self.assertEqual(gam_.food, 70)
        # Over-feeding
        consumed = gam_.feed(50)
        self.assertEqual(consumed, 30)
        self.assertEqual(gam_.food, 100)
        # Feeding negative values should have no effect
        previous_food = gam_.food
        consumed = gam_.feed(-11)
        self.assertEqual(consumed, 0)
        self.assertEqual(gam_.food, previous_food)
        
    def test_health_changes(self):
        gam_ = Gambusino(0, 0, 'iaTest.py')
        gam_.health = 50
        # Increase
        gam_.changeHealth(10)
        self.assertEqual(gam_.health, 60)
        # Decrease
        gam_.changeHealth(-20)
        self.assertEqual(gam_.health, 40)
        # Decrease under 0
        gam_.changeHealth(-50)
        self.assertEqual(gam_.health, 0)
        # Increase over 100
        gam_.changeHealth(9999)
        self.assertEqual(gam_.health, 100)
        
            
if __name__ == '__main__':
    unittest.main()
