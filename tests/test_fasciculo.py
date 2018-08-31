# coding: utf-8
from datetime import datetime
from biblat_schema.models import Fasciculo, Revista, Pais
from biblat_schema.catalogs import Disciplina
from .base import BaseTestCase


class TestFascicleModel(BaseTestCase):
    model_class_to_delete = [Fasciculo, Revista]

    def _crea_pais(self):
        _id = self.generate_uuid_32_string()

        pais_data = {
            '_id': _id,
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
        _id = self.generate_uuid_32_string()
        pais = self._crea_pais()
        disciplina = self._crea_disciplina()
        revista_data = {
            '_id': _id,
            'base_datos': 'PER01',
            'titulo': u'Estudios de cultura náhuatl',
            'issn': '2007-0705',
            'pais': pais,
            'disciplina': disciplina,
            'fecha_creacion': datetime.now(),
            'fecha_actualizacion': datetime.now(),
        }
        return Revista(**revista_data)

    def _crea_disciplina(self):
        _id = self.generate_uuid_32_string()
        disciplina_data = {
            '_id': _id,
            'nombre': {
                'es': 'Biologia',
                'en': 'Biology'
            }
        }
        return Disciplina(**disciplina_data)

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

        # Desglose revista
        self.assertEqual(fasciculo_data['revista'], fasciculo_doc.revista)
        self.assertEqual(fasciculo_data['revista']._id, fasciculo_doc.revista[
            '_id'])
        self.assertEqual(fasciculo_data['revista'].base_datos,
                         fasciculo_doc.revista['base_datos'])
        self.assertEqual(fasciculo_data['revista'].titulo,
                         fasciculo_doc.revista['titulo'])
        self.assertEqual(fasciculo_data['revista'].issn,
                         fasciculo_doc.revista['issn'])

        # Desglose pais
        self.assertEqual(fasciculo_data['revista'].pais,
                         fasciculo_doc.revista['pais'])
        self.assertEqual(fasciculo_data['revista'].pais._id,
                         fasciculo_doc.revista['pais']._id)
        self.assertEqual(fasciculo_data['revista'].pais.nombre,
                         fasciculo_doc.revista['pais'].nombre)
        self.assertEqual(fasciculo_data['revista'].pais.alpha2,
                         fasciculo_doc.revista['pais'].alpha2)
        self.assertEqual(fasciculo_data['revista'].pais.alpha3,
                         fasciculo_doc.revista['pais'].alpha3)
        self.assertEqual(fasciculo_data['revista'].pais.codigo_pais,
                         fasciculo_doc.revista['pais'].codigo_pais)
        self.assertEqual(fasciculo_data['revista'].pais.iso_3166_2,
                         fasciculo_doc.revista['pais'].iso_3166_2)
        self.assertEqual(fasciculo_data['revista'].pais.region,
                         fasciculo_doc.revista['pais'].region)
        self.assertEqual(fasciculo_data['revista'].pais.sub_region,
                         fasciculo_doc.revista['pais'].sub_region)
        self.assertEqual(fasciculo_data['revista'].pais.intermediate_region,
                         fasciculo_doc.revista['pais'].intermediate_region)
        self.assertEqual(fasciculo_data['revista'].pais.codigo_region,
                         fasciculo_doc.revista['pais'].codigo_region)
        self.assertEqual(fasciculo_data['revista'].pais.codigo_sub_region,
                         fasciculo_doc.revista['pais'].codigo_sub_region)
        self.assertEqual(fasciculo_data['revista'].pais.region_intermedia,
                         fasciculo_doc.revista['pais'].region_intermedia)
        # Desglose disciplina
        self.assertEqual(fasciculo_data['revista'].disciplina._id,
                         fasciculo_doc.revista['disciplina']._id)
        self.assertEqual(fasciculo_data['revista'].disciplina.nombre,
                         fasciculo_doc.revista['disciplina'].nombre)

        self.assertEqual(fasciculo_data['revista'].fecha_creacion,
                         fasciculo_doc.revista['fecha_creacion'])
        self.assertEqual(fasciculo_data['revista'].fecha_actualizacion,
                         fasciculo_doc.revista['fecha_actualizacion'])

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
