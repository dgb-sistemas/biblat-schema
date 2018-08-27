# coding: utf-8
from biblat_schema.models import UrlTextoCompleto
from .base import BaseTestCase


class TestURLFullTextModel(BaseTestCase):
    model_class_to_delete = [UrlTextoCompleto]

    def test_solo_campos_requeridos(self):
        # Datos

        url_texto_completo_data = {
            'url': 'http://132.248.9.34/hevila/e-BIBLAT/PERIODICA/per7857.pdf',
            'descripcion': 'Estudios de cultura nahuatl'
        }

        # Guardamos
        url_texto_completo_doc = UrlTextoCompleto(**url_texto_completo_data)

        # Comprobamos
        self.assertEqual(url_texto_completo_data['url'],
                         url_texto_completo_doc.url)
        self.assertEqual(url_texto_completo_data['descripcion'],
                         url_texto_completo_doc.descripcion)
