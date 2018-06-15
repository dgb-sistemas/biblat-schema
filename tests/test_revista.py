# coding: utf-8
from datetime import datetime
from biblat_schema.models import Revista
from biblat_schema.catalogs import DisciplinaRevista
from .base import BaseTestCase


class TestJournalModel(BaseTestCase):
    model_class_to_delete = [Revista]

    def _crear_disciplina_revista_prueba(self):
        disciplina_id = self.generate_uuid_32_string()
        disciplina_data = {
            '_id': disciplina_id,
            'nombre': {
                'es': u'Antropología',
                'en': 'Anthropology'
            }
        }
        disciplina_doc = DisciplinaRevista(**disciplina_data)
        return disciplina_doc

    def test_solo_campos_requeridos(self):
        # Disciplina revista
        disciplina_doc = self._crear_disciplina_revista_prueba()

        # Datos
        revista_id = self.generate_uuid_32_string()
        revista_data = {
            '_id': revista_id,
            'base_datos': 'CLA01',
            'titulo': u'Estudios de cultura náhuatl',
            'issn': '0071-1675',
            'pais': 'MX',
            'disciplina': disciplina_doc,
            'fecha_creacion': datetime.now(),
            'fecha_actualizacion': datetime.now(),
        }

        # Guardamos
        revista_doc = Revista(**revista_data)
        revista_doc.save()

        # Comprobamos
        self.assertEqual(revista_id, revista_doc._id)
        self.assertEqual(revista_data['base_datos'], revista_doc.base_datos)
        self.assertEqual(revista_data['titulo'], revista_doc.titulo)
        self.assertEqual(revista_data['issn'], revista_doc.issn)
        self.assertEqual(revista_data['disciplina'], revista_doc.disciplina)
        self.assertEqual(1, Revista.objects.all().count())
