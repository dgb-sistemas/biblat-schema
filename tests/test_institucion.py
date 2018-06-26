# coding: utf-8
from biblat_schema.models import Institucion, Pais
from biblat_schema.catalogs import I18NField
from .base import BaseTestCase


class TestInstitutionModel(BaseTestCase):
    model_class_to_delete = [Institucion, Pais, I18NField]

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

    def test_solo_campos_requeridos(self):
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

        # Comprobamos
        self.assertEqual(institucion_data['institucion'],
                         institucion_doc.institucion)
        self.assertEqual(institucion_data['dependencia'],
                         institucion_doc.dependencia)
        self.assertEqual(institucion_data['ciudad_estado'],
                         institucion_doc.ciudad_estado)
        self.assertEqual(institucion_data['pais'],
                         institucion_doc.pais)
        self.assertEqual(institucion_data['referencia'],
                         institucion_doc.referencia)
