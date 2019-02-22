# coding: utf-8
from biblat_schema.catalogs import NombreGeografico, I18NField
from .base import BaseTestCase


class TestGeographicNameModel(BaseTestCase):
    model_class_to_delete = [NombreGeografico, I18NField]

    def test_solo_campos_requeridos(self):
        """Pruebas unitarias de campos requeridos del catalogo Nombre
        Geografico"""
        # Datos
        nombre = I18NField(**{
            'es': 'Estados Unidos de Norteamerica',
            'en': 'United States of America'
        })
        nombre_geografico_data = {
            'nombre': nombre
        }

        # Guardamos
        nombre_geografico_doc = NombreGeografico(
            **nombre_geografico_data)
        nombre_geografico_doc.save()
        # Comprobamos
        self.assertEqual(
            nombre_geografico_data['nombre'],
            nombre_geografico_doc.nombre
        )
