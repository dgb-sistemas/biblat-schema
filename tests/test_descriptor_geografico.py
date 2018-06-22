# coding: utf-8
from biblat_schema.models import DescriptorGeografico
from .base import BaseTestCase


class TestGeographicDescriptorModel(BaseTestCase):
    model_class_to_delete = [DescriptorGeografico]

    def test_solo_campos_requeridos(self):
        # Datos

        descriptor_geografico_data = {
            'idioma': 'ES',
            'descripcion': 'Estudios de cultura náhuatl'
        }

        # Guardamos
        descriptor_geografico_doc = DescriptorGeografico(
            **descriptor_geografico_data)

        # Comprobamos
        self.assertEqual(descriptor_geografico_data['idioma'],
                         descriptor_geografico_doc.idioma)
        self.assertEqual(descriptor_geografico_data['descripcion'],
                         descriptor_geografico_doc.descripcion)
