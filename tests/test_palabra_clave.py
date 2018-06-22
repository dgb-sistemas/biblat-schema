# coding: utf-8
from biblat_schema.models import PalabraClave
from .base import BaseTestCase


class TestKeyWordModel(BaseTestCase):
    model_class_to_delete = [PalabraClave]

    def test_solo_campos_requeridos(self):
        # Datos

        palabra_clave_data = {
            'idioma': 'es',
            'palabra_clave': 'estudio'
        }

        # Guardamos
        palabra_clave_doc = PalabraClave(**palabra_clave_data)

        # Comprobamos
        self.assertEqual(palabra_clave_data['idioma'],
                         palabra_clave_doc.idioma)
        self.assertEqual(palabra_clave_data['palabra_clave'],
                         palabra_clave_doc.palabra_clave)
