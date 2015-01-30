import unittest
from unittest import TestCase
from gambusino import (
    Gambusino, DEFAULT_AGE, DEFAULT_HEALTH, DEFAULT_FOOD, DEFAULT_POS_X, 
    DEFAULT_POS_Y, DEFAULT_MEMORY,
)
from constants import (
    MIN_MAP_WIDTH, MIN_MAP_HEIGHT, INITIAL_FOOD_SOURCES_DENSITY,
    FOOD_SOURCE_MIN_Q, FOOD_SOURCE_MAX_Q,
)
import ia.iaTest
from world import World
from foodsource import FoodSource
import math


class GambusinoTests(TestCase):

    def create_gambusino(self):
        return Gambusino(0,0,'iaTest.py')

    def test_can_create_gambusino(self):
        self.create_gambusino()
        
    def test_new_gambusino_has_correct_values(self):
        id_num = 7
        team = 2
        ia_filename = 'iaTest.py'
        gam_ = Gambusino(id_num, team, ia_filename)
        self.assertEqual(gam_.age, DEFAULT_AGE)
        self.assertEqual(gam_.health, DEFAULT_HEALTH)
        self.assertEqual(gam_.food, DEFAULT_FOOD)
        self.assertEqual(gam_.pos_x, DEFAULT_POS_X)
        self.assertEqual(gam_.pos_y, DEFAULT_POS_Y)
        self.assertEqual(gam_.id_num, id_num)
        self.assertEqual(gam_.team, team)
        self.assertEqual(gam_.ia.NAME, ia.iaTest.NAME)
        self.assertEqual(gam_.memory, DEFAULT_MEMORY)
        
    def test_feeding_the_gambusino(self):
        gam_ = self.create_gambusino()
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
        gam_ = self.create_gambusino()
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
        
    def test_movement_changes_position(self):
        gam_ = self.create_gambusino()
        # don't move
        gam_.move(-1)
        self.assertEqual(
            (gam_.pos_x, gam_.pos_y),
            (DEFAULT_POS_X, DEFAULT_POS_Y)
        )
        # over 360º
        gam_.move(999)
        self.assertEqual(
            (gam_.pos_x, gam_.pos_y),
            (DEFAULT_POS_X, DEFAULT_POS_Y)
        )
        # up
        gam_.move(90)
        self.assertEqual(
            (gam_.pos_x, gam_.pos_y),
            (DEFAULT_POS_X, DEFAULT_POS_Y + 1)
        )
        # left
        gam_.move(180)
        self.assertEqual(
            (gam_.pos_x, gam_.pos_y),
            (DEFAULT_POS_X - 1, DEFAULT_POS_Y + 1)
        )
        
class WorldTests(TestCase):

    def approx_equal(self, x, y, tolerance=0.05):
        return abs(x-y) <= 0.5 * tolerance * (x + y)

    def test_can_create_map(self):
        world_ = World()
        
    def test_create_custom_sized_map(self):
        world_ = World(11,77)
        self.assertEqual((11,77), (world_.width, world_.height))
        with self.assertRaises(ValueError):
            world_ = World(MIN_MAP_WIDTH - 1, MIN_MAP_HEIGHT - 1)
            
    def test_map_has_gambusinos_and_food_sets_but_empty_initially(self):
        world_ = World()
        self.assertIsNotNone(world_.gambusinos)
        self.assertIsNotNone(world_.foodsources)
        self.assertEqual(len(world_.gambusinos), 0)
        self.assertEqual(len(world_.foodsources), 0)
        
    def test_generating_food_on_map(self):
        world_ = World()
        world_.generateFoodSources()
        # not empty
        self.assertTrue(len(world_.foodsources) > 0, 'not empty')
        # elements are of type FoodSource
        for e in world_.foodsources:
            self.assertTrue(isinstance(e,FoodSource), 'is food')
        # check population density
        world_area = world_.width * world_.height
        self.assertTrue(
            self.approx_equal(
                len(world_.foodsources),
                world_area * INITIAL_FOOD_SOURCES_DENSITY
            ),
            'population of initial food sources (expected %d, found %d)'\
            %(world_area*INITIAL_FOOD_SOURCES_DENSITY,len(world_.foodsources))
        )
        # check minimum distance between elements is 1m
        all_distances_ok = True
        for fs in world_.foodsources:
            for ofs in world_.foodsources:
                if(fs != ofs):
                    distance = math.sqrt(math.pow(fs.pos_x-ofs.pos_x,2) \
                        + math.pow(fs.pos_y-ofs.pos_y,2))
                    all_distances_ok = distance >= 1
                    if not all_distances_ok:
                        break
            if not all_distances_ok:
                break
        self.assertTrue(all_distances_ok, 'food distances >= 1m')
        # check quantity of food per FoodSource
        all_quantities_ok = True
        for fs in world_.foodsources:
            all_quantities_ok = fs.quantity >= FOOD_SOURCE_MIN_Q \
                and fs.quantity <= FOOD_SOURCE_MAX_Q
            if not all_quantities_ok:
                break
        self.assertTrue(all_quantities_ok, 'food quantities out of range')
        
        # check food position is inside world boundaries
        all_fs_inside = True
        for fs in world_.foodsources:
            all_fs_inside = (fs.pos_x <= world_.width) and (fs.pos_x >= 0) \
                and (fs.pos_y <= world_.height) and (fs.pos_y >= 0)
            if not all_fs_inside:
                break
        self.assertTrue(all_fs_inside, 'food position is inside world')
        
        
class GameTests(TestCase):

    def test_can_create_game(self):
        pass
        # TODO
        
    def test_there_is_a_map_with_gambusinos(self):
        pass
        # TODO
        
    def test_gambusinos_ids_are_unique(self):
        pass
        # TODO 
        
        
            
if __name__ == '__main__':
    unittest.main()
