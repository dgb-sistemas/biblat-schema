# coding: utf-8
from biblat_schema.catalogs import Idioma, I18NField
from biblat_schema.models import Resumen
from .base import BaseTestCase


class TestSummaryModel(BaseTestCase):
    model_class_to_delete = [Resumen, Idioma, I18NField]

    def _crea_nombre(self):
        nombre_data = {
            'es': 'Español',
            'en': 'Spanish'
        }
        return I18NField(** nombre_data)

    def _crea_idioma(self):
        _id = self.generate_uuid_32_string()
        nombre = self._crea_nombre()
        idioma_data = {
            '_id': _id,
            'iso_639_1': 'es',
            'iso_639_2': 'spa',
            'nombre': nombre
        }
        return Idioma(** idioma_data)

    def test_solo_campos_requeridos(self):
        idioma = self._crea_idioma()

        resumen_data = {
            'idioma': idioma,
            'resumen': 'Resumen del documento '
        }

        # Guardamos
        resumen_doc = Resumen(**resumen_data)

        self.assertEqual(resumen_data['idioma'], resumen_doc.idioma)
        self.assertEqual(resumen_data['resumen'], resumen_doc.resumen)
