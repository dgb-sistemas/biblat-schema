# coding: utf-8
from biblat_schema.catalogs import NombreGeografico, I18NField
from .base import BaseTestCase


class TestGeographicNameModel(BaseTestCase):
    model_class_to_delete = [NombreGeografico, I18NField]

    def _crea_I18NField_nombre(self):
        I18NField_data = {
            'es': 'Estados Unidos de Norteamerica',
            'en': 'United States of America'
        }
        return I18NField(**I18NField_data)

    def test_solo_campos_requeridos(self):
        # Datos
        _id = self.generate_uuid_32_string()
        nombre = self._crea_I18NField_nombre()
        nombre_geografico_data = {
            '_id': _id,
            'nombre': nombre

        }

        # Guardamos
        nombre_geografico_doc = NombreGeografico(
            **nombre_geografico_data)

        # Comprobamos
        self.assertEqual(nombre_geografico_data['_id'],
                         nombre_geografico_doc._id)
        self.assertEqual(nombre_geografico_data['nombre'],
                         nombre_geografico_doc.nombre)
