# coding: utf-8
from datetime import datetime
from biblat_schema.models import Revista
from .base import BaseTestCase


class TestJournalModel(BaseTestCase):
    model_class_to_delete = [Revista]

    def test_solo_campos_requeridos(self):
        # Datos
        _id = self.generate_uuid_32_string()
        revista_data = {
            '_id': _id,
            'base_datos': 'CLA01',
            'titulo': u'Estudios de cultura náhuatl',
            'issn': '0071-1675',
            'pais': 'MX',
            'disciplina': u'Antropología',
            'fecha_creacion': datetime.now(),
            'fecha_actualizacion': datetime.now(),
        }

        # Guardamos
        revista_doc = Revista(**revista_data)
        revista_doc.save()

        # Comprobamos
        self.assertEqual(_id, revista_doc._id)
        self.assertEqual(revista_data['base_datos'], revista_doc.base_datos)
        self.assertEqual(revista_data['titulo'], revista_doc.titulo)
        self.assertEqual(revista_data['issn'], revista_doc.issn)
        self.assertEqual(revista_data['disciplina'], revista_doc.disciplina)
        self.assertEqual(1, Revista.objects.all().count())
