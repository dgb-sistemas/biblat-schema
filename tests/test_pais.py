# coding: utf-8
from biblat_schema.catalogs import Pais
from .base import BaseTestCase


class TestGeographicNameModel(BaseTestCase):
    model_class_to_delete = [Pais]

    def test_solo_campos_requeridos(self):

        pais_data = {
            '_id': 'MX',
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
        pais_doc = Pais(**pais_data)
        pais_doc.save()
        # Comprobamos

        self.assertEqual(
            pais_data['_id'],
            pais_doc.id
        )

        self.assertEqual(
            pais_data['nombre']['en'],
            pais_doc.nombre['en']
        )
        self.assertEqual(
            pais_data['nombre']['es'],
            pais_doc.nombre['es']
        )
        self.assertEqual(
            pais_data['alpha2'],
            pais_doc.alpha2
        )
        self.assertEqual(
            pais_data['alpha3'],
            pais_doc.alpha3
        )
        self.assertEqual(
            pais_data['codigo_pais'],
            pais_doc.codigo_pais
        )
        self.assertEqual(
            pais_data['iso_3166_2'],
            pais_doc.iso_3166_2
        )
        self.assertEqual(
            pais_data['region']['es'],
            pais_doc.region['es']
        )
        self.assertEqual(
            pais_data['region']['en'],
            pais_doc.region['en']
        )
        self.assertEqual(
            pais_data['sub_region']['es'],
            pais_doc.sub_region['es']
        )
        self.assertEqual(
            pais_data['sub_region']['en'],
            pais_doc.sub_region['en']
        )
        self.assertEqual(
            pais_data['intermediate_region']['es'],
            pais_doc.intermediate_region['es']
        )
        self.assertEqual(
            pais_data['intermediate_region']['en'],
            pais_doc.intermediate_region['en']
        )
        self.assertEqual(
            pais_data['codigo_region'],
            pais_doc.codigo_region
        )
        self.assertEqual(
            pais_data['codigo_sub_region'],
            pais_doc.codigo_sub_region
        )
        self.assertEqual(
            pais_data['region_intermedia'],
            pais_doc.region_intermedia
        )
        self.assertEqual(
            1,
            Pais.objects.all().count()
        )
