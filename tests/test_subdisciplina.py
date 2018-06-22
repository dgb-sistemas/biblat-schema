# coding: utf-8
from biblat_schema.models import Subdisciplina
from .base import BaseTestCase


class TestSubdisciplineModel(BaseTestCase):
    model_class_to_delete = [Subdisciplina]

    def test_solo_campos_requeridos(self):
        # Datos

        subdisciplina_data = {
            'idioma': 'ES',
            'descripcion': 'Estudios de cultura náhuatl'
        }

        # Guardamos
        subdisciplina_doc = Subdisciplina(**subdisciplina_data)

        # Comprobamos
        self.assertEqual(subdisciplina_data['idioma'],
                         subdisciplina_doc.idioma)
        self.assertEqual(subdisciplina_data['descripcion'],
                         subdisciplina_doc.descripcion)
