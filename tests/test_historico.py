# coding: utf-8
from datetime import datetime

from biblat_schema.models import Historico
from .base import BaseTestCase


class TestHistoricalModel(BaseTestCase):

    model_class_to_delete = [Historico]

    def test_solo_campos_requeridos(self):
        """Pruebas unitarias de campos requeridos del modelo Historico"""
        # Datos
        historico_data = {
            'catalogador': 'Juan Perez Perez',
            'nivel': 10,
            'fecha_hora': datetime.now()
        }

        # Guardamos
        historico_doc = Historico(**historico_data)
        historico_doc.validate()
        # Comprobamos
        self.assertEqual(historico_data['catalogador'], historico_doc
                         .catalogador)
        self.assertEqual(historico_data['nivel'], historico_doc.nivel)
        self.assertEqual(historico_data['fecha_hora'], historico_doc
                         .fecha_hora)
