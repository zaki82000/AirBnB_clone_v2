#!/usr/bin/python3
"""test module for db storage"""
import unittest
from os import getenv
from models import storage
from models.state import State
from models.city import City
from sqlalchemy.orm import Session


@unittest.skipIf(
    getenv('HBNB_TYPE_STORAGE') != 'db',
    'Not a file storage'
)
class test_DBStorage(unittest.TestCase):
    """Test cases for db storage"""
    def setUp(self):
        """setup method"""
        self.session = storage._DBStorage__session
        texas = State()
        texas.name = 'Texas'
        austin = City()
        austin.name = 'Austin'
        austin.state_id = texas.id
        dallas = City()
        dallas.name = 'Dallas'
        dallas.state_id = texas.id
        self.objs = {'states': [texas], 'cities': [austin, dallas]}

        for obj in self.objs['states'] + self.objs['cities']:
            self.session.add(obj)
        self.session.commit()

    def tearDown(self):
        """tearDown method"""
        for obj in self.objs['states'] + self.objs['cities']:
            self.session.delete(obj)
        self.session.commit()

    def test_all(self):
        """Test all"""
        objs_from_db = storage.all()
        self.assertIsInstance(objs_from_db, dict)
        self.assertEqual(
            sorted(list(map(
                lambda obj: obj.id, self.objs['states'] + self.objs['cities']
            ))),
            sorted(list(map(lambda obj: obj.id, objs_from_db.values())))
        )

    def test_filtered_all(self):
        """Test filtered all"""
        cities = storage.all(City)
        self.assertEqual(
            sorted(list(map(
                lambda obj: obj.id, self.objs['cities']
            ))),
            sorted(list(map(lambda obj: obj.id, cities.values())))
        )

    def test_new(self):
        """Test new"""
        city = City()
        city.name = 'Houston'
        city.state_id = self.objs['states'][0].id
        self.objs['cities'].append(city)
        storage.new(city)
        self.session.commit()
        cities = self.session.query(City)
        self.assertEqual(
            sorted(list(map(
                lambda obj: obj.id, self.objs['cities']
            ))),
            sorted(list(map(lambda obj: obj.id, cities)))
        )

    def test_save(self):
        """Test save"""
        self.session.delete(self.objs['cities'].pop())
        storage.save()
        cities = self.session.query(City)
        self.assertEqual(
            sorted(list(map(
                lambda obj: obj.id, self.objs['cities']
            ))),
            sorted(list(map(lambda obj: obj.id, cities)))
        )

    def test_delete(self):
        """Test delete"""
        storage.delete(self.objs['cities'].pop())
        self.session.commit()
        cities = self.session.query(City)
        self.assertEqual(
            sorted(list(map(
                lambda obj: obj.id, self.objs['cities']
            ))),
            sorted(list(map(lambda obj: obj.id, cities)))
        )

    def test_reload(self):
        """Test reload"""
        storage.reload()
        self.assertIsInstance(storage._DBStorage__session, Session)
        self.assertNotEqual(self.session, storage._DBStorage__session)
        storage._DBStorage__session.close()
        storage._DBStorage__session = self.session
