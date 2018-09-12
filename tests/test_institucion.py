# coding: utf-8
from biblat_schema.models import Institucion, Pais
from .base import BaseTestCase


class TestInstitutionModel(BaseTestCase):
    model_class_to_delete = [Institucion, Pais]

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

    def test_solo_campos_requeridos(self):
        """Pruebas unitarias de campos requeridos del modelo Institucion"""
        # Datos
        pais = self._crea_pais()
        institucion_data = {
            'institucion': 'Universidad de Chapingo ',
            'dependencia': 'Filosofia',
            'ciudad_estado': 'Acapulco Guerrero',
            'pais': pais,
            'referencia': 1
        }

        # Guardamos
        institucion_doc = Institucion(**institucion_data)
        institucion_doc.validate()
        # Comprobamos
        self.assertEqual(institucion_data['institucion'], institucion_doc
                         .institucion)
        self.assertEqual(institucion_data['dependencia'], institucion_doc
                         .dependencia)
        self.assertEqual(institucion_data['ciudad_estado'], institucion_doc
                         .ciudad_estado)
        # Desglose pais
        self.assertEqual(pais, institucion_doc.pais)
        self.assertEqual(pais.id, institucion_doc.pais.id)
        self.assertEqual(pais.nombre, institucion_doc.pais.nombre)
        self.assertEqual(pais.alpha2, institucion_doc.pais.alpha2)
        self.assertEqual(pais.alpha3, institucion_doc.pais.alpha3)
        self.assertEqual(pais.codigo_pais, institucion_doc.pais.codigo_pais)
        self.assertEqual(pais.iso_3166_2, institucion_doc.pais.iso_3166_2)
        self.assertEqual(pais.region, institucion_doc.pais.region)
        self.assertEqual(pais.sub_region, institucion_doc.pais.sub_region)
        self.assertEqual(pais.intermediate_region, institucion_doc.pais
                         .intermediate_region)
        self.assertEqual(pais.codigo_region, institucion_doc.pais
                         .codigo_region)
        self.assertEqual(pais.codigo_sub_region, institucion_doc.pais
                         .codigo_sub_region)
        self.assertEqual(pais.region_intermedia, institucion_doc.pais
                         .region_intermedia)

        self.assertEqual(institucion_data['referencia'], institucion_doc
                         .referencia)
