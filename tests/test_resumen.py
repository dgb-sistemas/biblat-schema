# coding: utf-8
from datetime import datetime
from biblat_schema.models import Resumen
from .base import BaseTestCase


class TestSummaryModel(BaseTestCase):
    model_class_to_delete = [Resumen]

    def test_solo_campos_requeridos(self):

        resumen_data = {
            'idioma': 'es',
            'resumen': 'Resumen del documento '
        }

        # Guardamos
        resumen_doc = Resumen(**resumen_data)

        self.assertEqual(resumen_data['idioma'], resumen_doc.idioma)
        self.assertEqual(resumen_data['resumen'], resumen_doc.resumen)
