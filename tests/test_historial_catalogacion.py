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

    def _crea_historico2(self):
        historico_data = {
            'catalogador': 'Carlos Alberto Suárez',
            'nivel': 2,
            'fecha_hora': datetime.now()
        }

        historico = Historico(**historico_data)
        return historico

    def test_solo_campos_requeridos(self):
        # Datos
        historico = self._crea_historico()
        historico2 = self._crea_historico2()
        historial_catalogacion_data = {
            'documento': 'documento',
            'catalogacion': [historico]
        }

        # Guardamos
        historial_catalogacion_doc = HistorialCatalogacion(
            **historial_catalogacion_data)
        historial_catalogacion_doc.save()

        historial_catalogacion_data.get('catalogacion').append(historico2)

        historial_catalogacion_doc = HistorialCatalogacion(
            **historial_catalogacion_data
        )
        historial_catalogacion_doc.save()
        # Comprobamos
        self.assertEqual(historial_catalogacion_data['documento'],
                         historial_catalogacion_doc.documento)
        self.assertEqual(historial_catalogacion_data['catalogacion'],

                         historial_catalogacion_doc.catalogacion)

        self.assertEqual(historial_catalogacion_data['catalogacion'][
                             0].catalogador,
                         historial_catalogacion_doc.catalogacion[
                             0].catalogador)
        self.assertEqual(historial_catalogacion_data['catalogacion'][0].nivel,
                         historial_catalogacion_doc.catalogacion[0].nivel)
        self.assertEqual(historial_catalogacion_data['catalogacion'][
                             0].fecha_hora,
                         historial_catalogacion_doc.catalogacion[0].fecha_hora)

        self.assertEqual(historial_catalogacion_data['catalogacion'][
                             1].catalogador,
                         historial_catalogacion_doc.catalogacion[
                             1].catalogador)
        self.assertEqual(historial_catalogacion_data['catalogacion'][1].nivel,
                         historial_catalogacion_doc.catalogacion[1].nivel)
        self.assertEqual(historial_catalogacion_data['catalogacion'][
                             1].fecha_hora,
                         historial_catalogacion_doc.catalogacion[1].fecha_hora)
