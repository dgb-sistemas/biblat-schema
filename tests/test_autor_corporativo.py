# coding: utf-8
from biblat_schema.models import AutorCorporativo
from .base import BaseTestCase


class TestCorporativeAuthorModel(BaseTestCase):
    model_class_to_delete = [AutorCorporativo]

    def test_solo_campos_requeridos(self):
        # Datos

        autor_corporativo_data = {
            'institucion': 'Ingeniería (México, D.F.)',
            'dependencia': 'Ingeniería (México, D.F.)',
            'pais': 'MX'
        }

        # Guardamos
        autor_corporativo_doc = AutorCorporativo(**autor_corporativo_data)

        # Comprobamos
        self.assertEqual(autor_corporativo_data['institucion'],
                         autor_corporativo_doc.institucion)
        self.assertEqual(autor_corporativo_data['dependencia'],
                         autor_corporativo_doc.dependencia)
        self.assertEqual(autor_corporativo_data['pais'],
                         autor_corporativo_doc.pais)
