# coding: utf-8
from datetime import datetime
from biblat_schema.models import Fasciculo, Revista
from .base import BaseTestCase


class TestFascicleModel(BaseTestCase):
    model_class_to_delete = [Fasciculo, Revista]

    def _crea_revista(self):
        _id = self.generate_uuid_32_string()
        revista_data = {
            '_id': _id,
            'base_datos': 'PER01',
            'titulo': u'Perturbation Method and Laplace-Padé Approximation '
                      u'as a Novel Tool to Find Approximate Solutions for '
                      u'Troeschs Problem',
            'issn': '2007-0705',
            'pais': 'MX',
            'disciplina': u'Multidisciplinaria',
            'fecha_creacion': datetime.now(),
            'fecha_actualizacion': datetime.now(),
        }
        return Revista(**revista_data)

    def test_solo_campos_requeridos(self):
        # Guardamos
        revista_doc = self._crea_revista()
        # Datos
        _id = self.generate_uuid_32_string()
        fasciculo_data = {
            '_id': _id,
            'revista': revista_doc,
            'volumen': 7,
            'numero': 14,
            'anio': 2015,
            'mes_inicial': 2,
            'mes_final': 2,
            'parte': 'P57-73',
            'fecha_creacion': datetime.now(),
            'fecha_actualizacion': datetime.now()
        }

        # Guardamos
        fasciculo_doc = Fasciculo(**fasciculo_data)
        fasciculo_doc.save()

        # Comprobamos
        self.assertEqual(_id, fasciculo_doc._id)
        self.assertEqual(fasciculo_data['revista'], fasciculo_doc.revista)
        self.assertEqual(fasciculo_data['volumen'], fasciculo_doc.volumen)
        self.assertEqual(fasciculo_data['numero'], fasciculo_doc.numero)
        self.assertEqual(fasciculo_data['anio'], fasciculo_doc.anio)
        self.assertEqual(fasciculo_data['mes_inicial'],
                         fasciculo_doc.mes_inicial)
        self.assertEqual(fasciculo_data['mes_final'],
                         fasciculo_doc.mes_final)
        self.assertEqual(fasciculo_data['parte'], fasciculo_doc.parte)
        self.assertEqual(fasciculo_data['fecha_creacion'],
                         fasciculo_doc.fecha_creacion)
        self.assertEqual(fasciculo_data['fecha_actualizacion'],
                         fasciculo_doc.fecha_actualizacion)
        self.assertEqual(1, Fasciculo.objects.all().count())
