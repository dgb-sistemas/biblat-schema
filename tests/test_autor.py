# coding: utf-8

from biblat_schema.models import Autor
from .base import BaseTestCase


class TestAuthorModel(BaseTestCase):
    model_class_to_delete = [Autor]

    def test_solo_campos_requeridos(self):
        """Pruebas unitarias de campos requeridos del modelo Autor"""
        # Datos
        autor_data = {
            'nombre': 'Vázquez Leal, H.',
            'correo_electronico': 'hvazquez@uv.mx',
            'referencia': 1

        }

        # Guardamos
        autor_doc = Autor(**autor_data)
        autor_doc.validate()
        # Comprobamos
        self.assertEqual(
            autor_data['nombre'],
            autor_doc.nombre
        )
        self.assertEqual(
            autor_data['correo_electronico'],
            autor_doc.correo_electronico)
        self.assertEqual(
            autor_data['referencia'],
            autor_doc.referencia
        )
