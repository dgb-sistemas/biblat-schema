# coding: utf-8
from biblat_schema.models import PalabraClave
from biblat_schema.catalogs import I18NField, Idioma
from .base import BaseTestCase


class TestKeyWordModel(BaseTestCase):
    model_class_to_delete = [PalabraClave, I18NField, Idioma]


    def _crea_idioma(self):
        _id = self.generate_uuid_32_string()
        nombre = I18NField(** {
            'es': 'Español',
            'en': 'Spanish'
        })
        idioma_data = {
            '_id': _id,
            'iso_639_1': 'es',
            'iso_639_2': 'spa',
            'nombre': nombre
        }
        return Idioma(**idioma_data)

    def test_solo_campos_requeridos(self):
        # Datos
        idioma = self._crea_idioma()
        palabra_clave_data = {
            'idioma': idioma,
            'palabra_clave': 'estudio'
        }

        # Guardamos
        palabra_clave_doc = PalabraClave(**palabra_clave_data)

        # Comprobamos
        self.assertEqual(palabra_clave_data['idioma'],
                         palabra_clave_doc.idioma)
        self.assertEqual(palabra_clave_data['palabra_clave'],
                         palabra_clave_doc.palabra_clave)
