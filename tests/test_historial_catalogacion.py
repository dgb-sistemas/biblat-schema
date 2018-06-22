# coding: utf-8
from datetime import datetime
from biblat_schema.models import HistorialCatalogacion, Historico
from .base import BaseTestCase


class TestCatalogationHistoricalModel(BaseTestCase):

    model_class_to_delete = [HistorialCatalogacion, Historico]

    def _crea_historico(self):
        historico_data = {
            'catalogador': 'Juan Perez Perez',
            'nivel': 10,
            'fecha_hora': datetime.now()
        }

        historico = Historico(**historico_data)
        return historico

    def test_solo_campos_requeridos(self):
        # Datos
        historico = self._crea_historico()

        historial_catalogacion_data = {
            'documento': 'documento',
            'catalogacion': [historico]
        }

        # Guardamos
        historial_catalogacion_doc = HistorialCatalogacion(
            **historial_catalogacion_data)
        historial_catalogacion_doc.save()

        # Comprobamos
        self.assertEqual(historial_catalogacion_data['documento'],
                         historial_catalogacion_doc.documento)
        self.assertEqual(historial_catalogacion_data['catalogacion'],
                         historial_catalogacion_doc.catalogacion)
