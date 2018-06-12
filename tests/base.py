# coding: utf-8
import uuid
import unittest
from mongoengine import connect


class BaseTestCase(unittest.TestCase):
    connection = None
    model_class_to_delete = []

    def setUp(self):
        self.connection = connect(db='mongoenginetest',
                                  host='mongomock://localhost',
                                  is_mock=True)
        # workaroud to fix "drop database" that run only once:
        # https://github.com/mongomock/mongomock/issues/371
        if self.model_class_to_delete:
            for model_class in self.model_class_to_delete:
                try:
                    model_class.objects.all().delete()
                except Exception:
                    pass

    def tearDown(self):
        self.connection.drop_database('mongotest')

    def generate_uuid_32_string(self):
        return str(uuid.uuid4().hex)
