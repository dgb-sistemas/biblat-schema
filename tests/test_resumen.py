# coding: utf-8
from biblat_schema.catalogs import Idioma, I18NField
from biblat_schema.models import Resumen
from .base import BaseTestCase


class TestSummaryModel(BaseTestCase):
    model_class_to_delete = [Resumen, Idioma, I18NField]

    def _crea_idioma(self):
        _id = self.generate_uuid_32_string()
        nombre = I18NField(**{
            'es': 'Español',
            'en': 'Spanish'
        })
        idioma_data = {
            '_id': _id,
            'iso_639_1': 'es',
            'iso_639_2': 'spa',
            'nombre': nombre
        }
        return Idioma(** idioma_data)

    def test_solo_campos_requeridos(self):
        idioma = self._crea_idioma()

        resumen_data = {
            'idioma': idioma,
            'resumen': 'En este artículo el Método de Perturbación (PM) es '
                       'empleado para obtener una solución aproximada para '
                       'el problema de Troesch. Además describiremos el uso '
                       'de la Transformada de Laplace y la Aproximación de '
                       'Padé para trabajar con las series truncadas '
                       'obtenidas por el Método de Perturbación, '
                       'y así obtener soluciones aproximadas compactas. '
                       'Finalmente se propone una tabla comparativa entre la '
                       'solución propuesta y otras soluciones reportadas en '
                       'la '
                       'literatura: Método de Descomposición de Adomian, '
                       'Método de Perturbación Homotópica, Método de '
                       'Análisis Homotópico y la solución numérica exacta. '
                       'Los resultados muestran que nuestra solución es la '
                       'más exacta (Error Relativo Absoluto '
                       'Promedio1.705648354x10-8).'
        }

        # Guardamos
        resumen_doc = Resumen(**resumen_data)

        self.assertEqual(resumen_data['idioma']._id, resumen_doc.idioma._id)
        self.assertEqual(resumen_data['idioma'].iso_639_1,
                         resumen_doc.idioma.iso_639_1)
        self.assertEqual(resumen_data['idioma'].iso_639_2,
                         resumen_doc.idioma.iso_639_2)
        self.assertEqual(resumen_data['idioma'].nombre,
                         resumen_doc.idioma.nombre)
        self.assertEqual(resumen_data['idioma'], resumen_doc.idioma)
        self.assertEqual(resumen_data['resumen'], resumen_doc.resumen)
