# coding: utf-8
from biblat_schema.models import AutorCorporativo
from .base import BaseTestCase
from biblat_schema.catalogs import Pais, I18NField


class TestCorporativeAuthorModel(BaseTestCase):
    model_class_to_delete = [AutorCorporativo, I18NField, Pais]

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

        # Comprobamos
        self.assertEqual(autor_corporativo_data['institucion'],
                         autor_corporativo_doc.institucion)
        self.assertEqual(autor_corporativo_data['dependencia'],
                         autor_corporativo_doc.dependencia)
        self.assertEqual(autor_corporativo_data['pais'],
                         autor_corporativo_doc.pais)
