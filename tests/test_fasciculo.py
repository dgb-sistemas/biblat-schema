# coding: utf-8
from datetime import datetime

from biblat_schema.models import Fasciculo, Revista, Pais
from biblat_schema.catalogs import Disciplina
from biblat_schema.choices import FREQUENCY
from .base import BaseTestCase


class TestFascicleModel(BaseTestCase):
    model_class_to_delete = [Fasciculo, Revista]

    def _crea_pais(self):
        pais_data = {
            "nombre": {
                "es": "",
                "en": "Mexico"
            },
            "alpha2": "MX",
            "alpha3": "MEX",
            "codigo_pais": "484",
            "iso_3166_2": "ISO 3166-2:MX",
            "region": {
                "es": "",
                "en": "Americas"
            },
            "sub_region": {
                "es": "",
                "en": "Latin America and the Caribbean"
            },
            "intermediate_region": {
                "es": "Centroamérica",
                "en": "Central America"
            },
            "codigo_region": "019",
            "codigo_sub_region": "419",
            "region_intermedia": "013"
        }

        return Pais(**pais_data)

    def _crea_revista(self):
        pais = self._crea_pais()
        disciplina = self._crea_disciplina()
        periodicidad = FREQUENCY[0][0]
        revista_data = {
            'base_datos': 'PER01',
            'titulo': u'Estudios de cultura náhuatl',
            'issn': '2007-0705',
            'pais': pais,
            'disciplina': disciplina,
            'fecha_creacion': datetime.now(),
            'fecha_actualizacion': datetime.now(),
            'periodicidad': periodicidad
        }
        return Revista(**revista_data)

    def _crea_disciplina(self):
        disciplina_data = {
            'nombre': {
                'es': 'Biologia',
                'en': 'Biology'
            }
        }
        return Disciplina(**disciplina_data)

    def test_solo_campos_requeridos(self):
        """Pruebas unitarias de campos requeridos del modelo Fasciculo"""
        # Guardamos
        revista_doc = self._crea_revista()

        # Datos
        fasciculo_data = {
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
        # Desglose revista
        self.assertEqual(
            revista_doc,
            fasciculo_doc.revista
        )
        self.assertEqual(
            revista_doc.id,
            fasciculo_doc.revista['_id']
        )
        self.assertEqual(
            revista_doc.base_datos,
            fasciculo_doc.revista['base_datos']
        )
        self.assertEqual(
            revista_doc.titulo,
            fasciculo_doc.revista['titulo']
        )
        self.assertEqual(
            revista_doc.issn,
            fasciculo_doc.revista['issn']
        )

        # Desglose pais
        self.assertEqual(
            revista_doc.pais,
            fasciculo_doc.revista['pais']
        )
        self.assertEqual(
            revista_doc.pais.id,
            fasciculo_doc.revista['pais'].id
        )
        self.assertEqual(
            revista_doc.pais.nombre,
            fasciculo_doc.revista['pais'].nombre
        )
        self.assertEqual(
            revista_doc.pais.alpha2,
            fasciculo_doc.revista['pais'].alpha2
        )
        self.assertEqual(
            revista_doc.pais.alpha3,
            fasciculo_doc.revista['pais'].alpha3
        )
        self.assertEqual(
            revista_doc.pais.codigo_pais,
            fasciculo_doc.revista['pais'].codigo_pais
        )
        self.assertEqual(
            revista_doc.pais.iso_3166_2,
            fasciculo_doc.revista['pais'].iso_3166_2
        )
        self.assertEqual(
            revista_doc.pais.region,
            fasciculo_doc.revista['pais'].region
        )
        self.assertEqual(
            revista_doc.pais.sub_region,
            fasciculo_doc.revista['pais'].sub_region
        )
        self.assertEqual(
            revista_doc.pais.intermediate_region,
            fasciculo_doc.revista['pais'].intermediate_region
        )
        self.assertEqual(
            revista_doc.pais.codigo_region,
            fasciculo_doc.revista['pais'].codigo_region
        )
        self.assertEqual(
            revista_doc.pais.codigo_sub_region,
            fasciculo_doc.revista['pais'].codigo_sub_region
        )
        self.assertEqual(
            revista_doc.pais.region_intermedia,
            fasciculo_doc.revista['pais'].region_intermedia
        )
        # Desglose disciplina
        self.assertEqual(
            revista_doc.disciplina.id,
            fasciculo_doc.revista['disciplina'].id
        )
        self.assertEqual(
            revista_doc.disciplina.nombre,
            fasciculo_doc.revista['disciplina'].nombre
        )

        self.assertEqual(
            revista_doc.fecha_creacion,
            fasciculo_doc.revista['fecha_creacion']
        )
        self.assertEqual(
            revista_doc.fecha_actualizacion,
            fasciculo_doc.revista['fecha_actualizacion']
        )
        self.assertEqual(
            revista_doc.periodicidad,
            fasciculo_doc.revista['periodicidad']
        )

        self.assertEqual(
            fasciculo_data['volumen'],
            fasciculo_doc.volumen
        )
        self.assertEqual(
            fasciculo_data['numero'],
            fasciculo_doc.numero
        )
        self.assertEqual(
            fasciculo_data['anio'],
            fasciculo_doc.anio
        )
        self.assertEqual(
            fasciculo_data['mes_inicial'],
            fasciculo_doc.mes_inicial
        )
        self.assertEqual(
            fasciculo_data['mes_final'],
            fasciculo_doc.mes_final
        )
        self.assertEqual(
            fasciculo_data['parte'],
            fasciculo_doc.parte
        )
        self.assertEqual(
            fasciculo_data['fecha_creacion'],
            fasciculo_doc.fecha_creacion
        )
        self.assertEqual(
            fasciculo_data['fecha_actualizacion'],
            fasciculo_doc.fecha_actualizacion
        )
        self.assertEqual(
            1,
            Fasciculo.objects.all().count()
        )
