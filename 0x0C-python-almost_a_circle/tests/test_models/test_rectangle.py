#!/usr/bin/python3
"""Moduel containing unit tests for the Rectangle class"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Tests all of the atributes and methods of the Rectangle class"""

    # setUp & tearDown

    @classmethod
    def setUpClass(cls):
        """Funcion executes before the testing begins"""
        cls.r1 = Rectangle(10, 2)
        print(cls.r1.__dict__)
        print("--")
        cls.r2 = Rectangle(2, 10)
        print(cls.r2.__str__)
        print("--")
        cls.r3 = Rectangle(15, 10, 5)
        print()
        print("--")
        cls.r4 = Rectangle(10, 2, 3, 5, 12)
        print(cls.r4)
        print("--")

    @classmethod
    def tearDownClass(cls):
        """Function executes when the testing has ended"""
        del cls.r1
        del cls.r2
        del cls.r3

    # Method tests

    # Magic method tests

    def test_init(self):
        # Tests for the __init__ method of Rectangle
        self.assertEqual(self.r1.__dict__, {'_Rectangle__width': 10,
                        '_Rectangle__height': 2, 'id': 1, '_Rectangle__x': 0,
                        '_Rectangle__y': 0})
        self.assertEqual(Rectangle.__str__(self.r2),
                         "[Rectangle] (2) 0/0 - 2/10")
        #self.assertEqual(self.r3.__str__, "[Rectangle] (3) 5/0 - 10/15")
        #self.assertEqual(self.r4.__str__, "[Rectangle] (10) 3/5 - 10/2")
        #self.assertEqual(self.r1._Base__nb_objects, 3)

    """# Static method tests

    def test_to_json_string(self):
        # Tests of the to_json_string method of Base
        list_input = [{'id': 789}, {'id': 6}, {'id': None}, {'id': -16}]
        self.assertEqual(Rectangle.to_json_string(list_input),
                         '[{"id": 789}, {"id": 6}, {"id": null}, {"id": -16}]')

    def test_from_json_string(self):
        # Tests of the from_json_string method of Base
        str_input = '[{"id": 789}, {"id": 6}, {"id": null}, {"id": -16}]'
        self.assertEqual(Rectangle.from_json_string(str_input),
                         [{'id': 789}, {'id': 6}, {'id': None}, {'id': -16}])

    #Class methods

    def test_save_to_file(self):
        # Tests for the save_to_file method of Base
        pass

    def test_create(self):
        # Tests for the create method of Base
        self.dict_1 =
        self.dict_2 =
        print(self.dict_1)
        print(type(self.dict_1))
        print(self.dict_2)
        print(type(self.dict_1))
        self.r# = Rectangle.create(**self.dict_1)
        self.r# = Rectangle.create(**self.dict_2)
        self.assertEqual(self.  .__dict__, dict_1)
        self.assertEqual(self.  .__dict__, dict_2)
        self.assertEqual(Base.__nb_objects, #)

    def test_load_from_file(self):
        # Tests for the laod_from_file method of Base
        pass """
