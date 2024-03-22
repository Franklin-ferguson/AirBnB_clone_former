#!/usr/bin/python3

"""test case for BaseModel"""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_init(self):
        current_model = BaseModel()

        self.assertIsNotNone(current_model.id)
        self.assertIsNotNone(current_model.created_at)
        self.assertIsNotNone(current_model.updated_at)

    def test_save(self):
        current_model = BaseModel()
        prev_updated_at = current_model.updated_at

        cur_updated_at = current_model.save()

        self.assertNotEqual(prev_updated_at, cur_updated_at)

    def test_to_dict(self):
        current_model = BaseModel()

        current_model_dict = current_model.to_dict()

        self.assertIsInstance(current_model_dict, dict)

        self.assertEqual(current_model_dict["__class__"], 'BaseModel')
        self.assertEqual(current_model_dict["id"], current_model.id)
        self.assertEqual(current_model_dict["created_at"], current_model.created_at.isoformat())
        self.assertEqual(current_model_dict["updated_at"], current_model.updated_at.isoformat())


    def test_str(self):
        current_model = BaseModel()

        self.assertTrue(str(current_model).startswith('BaseModel'))
        self.assertIn(current_model.id, str(current_model))
        self.assertIn(str(current_model.__dict__), str(current_model))




if __name__ =="__main__":
    unittest.main()
