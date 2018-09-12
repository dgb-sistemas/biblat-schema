# coding: utf-8

from biblat_schema.models import AutorCorporativo
from biblat_schema.catalogs import Pais
from .base import BaseTestCase


class TestCorporativeAuthorModel(BaseTestCase):
    model_class_to_delete = [AutorCorporativo, Pais]

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
        """Pruebas unitarias de campos requeridos del modelo Autor
        Corporativo"""
        # Datos
        pais = self._crea_pais()
        autor_corporativo_data = {
            'institucion': 'Universidad Veracruzana',
            'dependencia': 'Escuela de Instrumentación Electrónica y '
                           'Ciencias atmosféricas',
            'pais': pais
        }

        # Guardamos
        autor_corporativo_doc = AutorCorporativo(**autor_corporativo_data)
        autor_corporativo_doc.validate()

        # Comprobamos
        self.assertEqual(autor_corporativo_data['institucion'],
                         autor_corporativo_doc.institucion)
        self.assertEqual(autor_corporativo_data['dependencia'],
                         autor_corporativo_doc.dependencia)
        # Desglose de pais
        self.assertEqual(autor_corporativo_data['pais'], autor_corporativo_doc
                         .pais)
        self.assertEqual(autor_corporativo_data['pais'].id,
                         autor_corporativo_doc.pais['_id'])
        self.assertEqual(autor_corporativo_data['pais'].nombre,
                         autor_corporativo_doc.pais['nombre'])
        self.assertEqual(autor_corporativo_data['pais'].alpha2,
                         autor_corporativo_doc.pais['alpha2'])
        self.assertEqual(autor_corporativo_data['pais'].alpha3,
                         autor_corporativo_doc.pais['alpha3'])
        self.assertEqual(autor_corporativo_data['pais'].codigo_pais,
                         autor_corporativo_doc.pais['codigo_pais'])
        self.assertEqual(autor_corporativo_data['pais'].iso_3166_2,
                         autor_corporativo_doc.pais['iso_3166_2'])
        self.assertEqual(autor_corporativo_data['pais'].region,
                         autor_corporativo_doc.pais['region'])
        self.assertEqual(autor_corporativo_data['pais'].sub_region,
                         autor_corporativo_doc.pais['sub_region'])
        self.assertEqual(autor_corporativo_data['pais'].intermediate_region,
                         autor_corporativo_doc.pais['intermediate_region'])
        self.assertEqual(autor_corporativo_data['pais'].codigo_region,
                         autor_corporativo_doc.pais['codigo_region'])
        self.assertEqual(autor_corporativo_data['pais'].codigo_sub_region,
                         autor_corporativo_doc.pais['codigo_sub_region'])
        self.assertEqual(autor_corporativo_data['pais'].region_intermedia,
                         autor_corporativo_doc.pais['region_intermedia'])
