# coding: utf-8
from biblat_schema.models import Institucion
from .base import BaseTestCase


class TestInstitutionModel(BaseTestCase):
    model_class_to_delete = [Institucion]

    def test_solo_campos_requeridos(self):
        # Datos

        institucion_data = {
            'institucion': 'Universidad de Chapingo ',
            'dependencia': 'Filosofia',
            'ciudad_estado': 'Acapulco Guerrero',
            'pais': 'MX',
            'referencia': 1
        }

        # Guardamos
        institucion_doc = Institucion(**institucion_data)

        # Comprobamos
        self.assertEqual(institucion_data['institucion'],
                         institucion_doc.institucion)
        self.assertEqual(institucion_data['dependencia'],
                         institucion_doc.dependencia)
        self.assertEqual(institucion_data['ciudad_estado'],
                         institucion_doc.ciudad_estado)
        self.assertEqual(institucion_data['pais'],
                         institucion_doc.pais)
        self.assertEqual(institucion_data['referencia'],
                         institucion_doc.referencia)
