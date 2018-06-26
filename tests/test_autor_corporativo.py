# coding: utf-8
from biblat_schema.models import AutorCorporativo
from .base import BaseTestCase
from biblat_schema.catalogs import Pais, I18NField


class TestCorporativeAuthorModel(BaseTestCase):
    model_class_to_delete = [AutorCorporativo, I18NField, Pais]

    def _crea_I18NField(self):
        I18NField_data = {
            'es': 'México',
            'en': 'Mexico'
        }
        return I18NField(**I18NField_data)

    def _crea_I18NField_region(self):
        I18NField_data = {
            'es': 'Norte',
            'en': 'North'
        }
        return I18NField(**I18NField_data)

    def _crea_I18NField_subregion(self):
        I18NField_data = {
            'es': 'Norte',
            'en': 'North'
        }
        return I18NField(**I18NField_data)

    def _crea_I18NField_intermediateregion(self):
        I18NField_data = {
            'es': 'Norte',
            'en': 'North'
        }
        return I18NField(**I18NField_data)

    def _crea_pais(self):
        _id = self.generate_uuid_32_string()
        i18nfield_nombre = self._crea_I18NField()
        region = self._crea_I18NField_region()
        subregion = self._crea_I18NField_subregion()

        pais_data = {
            '_id': _id,
            'nombre': i18nfield_nombre,
            'alpha2': 'MX',
            'alpha3': 'MEX',
            'codigo_pais': '484',
            'iso_3166_2': 'Mexico',
            'region': region,
            'codigo_region': '123',
            'codigo_sub_region': '123',
            'region_intermedia': '123'

        }
        return Pais(**pais_data)

    def test_solo_campos_requeridos(self):
        # Datos
        pais = self._crea_pais()
        autor_corporativo_data = {
            'institucion': 'Ingeniería (México, D.F.)',
            'dependencia': 'Ingeniería (México, D.F.)',
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
