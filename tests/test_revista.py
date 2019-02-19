# coding: utf-8
from datetime import datetime

from biblat_schema.models import Revista, Pais
from biblat_schema.catalogs import DisciplinaRevista
from biblat_schema.choices import FREQUENCY
from .base import BaseTestCase


class TestJournalModel(BaseTestCase):
    model_class_to_delete = [Revista, DisciplinaRevista, Pais]

    def _crear_disciplina_revista_prueba(self):
        disciplina_id = self.generate_uuid_32_string()
        disciplina_data = {
            '_id': disciplina_id,
            'nombre': {
                'es': u'Multidisciplinaria',
                'en': 'Multidisciplinary'
            }
        }
        disciplina_doc = DisciplinaRevista(**disciplina_data)
        return disciplina_doc

    def test_solo_campos_requeridos(self):
        """Pruebas unitarias de campos requeridos del modelo Revista"""
        # Disciplina revista
        disciplina_doc = self._crear_disciplina_revista_prueba()

        # País
        pais_doc = Pais(**{
            '_id': 'MX',
            'nombre': {
                'es': u'México',
                'en': 'Mexico'
            },
            'alpha2': 'MX',
            'alpha3': 'MEX',
            'codigo_pais': '484',
            'iso_3166_2': 'ISO 3166-2:MX',
            'region': {
                'es': 'América',
                'en': 'Americas'
            },
            'sub_region': {
                'es': 'América Latina y el Caribe',
                'en': 'Latin America and the Caribbean'
            },
            'intermediate_region': {
                'es': 'Centroamérica',
                'en': 'Central America'
            },
            'codigo_region': '019',
            'codigo_sub_region': '419',
            'region_intermedia': '013'
        })

        # Datos
        revista_id = self.generate_uuid_32_string()
        periodicidad = FREQUENCY[0][0]

        revista_data = {
            '_id': revista_id,
            'base_datos': 'PER01',
            'titulo': u'Estudios de cultura náhuatl',
            'issn': '2007-0705',
            'pais': pais_doc,
            'disciplina': disciplina_doc,
            'fecha_creacion': datetime.now(),
            'fecha_actualizacion': datetime.now(),
            'periodicidad': periodicidad
        }

        # Guardamos
        revista_doc = Revista(**revista_data)
        revista_doc.save()

        # Comprobamos
        self.assertEqual(
            revista_id,
            revista_doc.id
        )
        self.assertEqual(
            revista_data['base_datos'],
            revista_doc.base_datos
        )
        self.assertEqual(
            revista_data['titulo'],
            revista_doc.titulo
        )
        self.assertEqual(
            revista_data['issn'],
            revista_doc.issn
        )
        self.assertEqual(
            pais_doc,
            revista_doc.pais
        )
        self.assertEqual(
            disciplina_doc,
            revista_doc.disciplina
        )
        self.assertEqual(
            periodicidad,
            revista_doc.periodicidad
        )
        self.assertEqual(
            1,
            Revista.objects.all().count()
        )
