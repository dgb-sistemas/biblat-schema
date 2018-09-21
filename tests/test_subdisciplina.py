# coding: utf-8
from biblat_schema.models import SubDisciplina, Disciplina
from biblat_schema.catalogs import I18NField
from .base import BaseTestCase


class TestSubdisciplineModel(BaseTestCase):
    model_class_to_delete = [SubDisciplina, Disciplina, I18NField]

    def _crea_disciplina(self):
        _id = self.generate_uuid_32_string()
        nombre = I18NField(**{
            'es': 'Biologia',
            'en': 'Biology'
        })
        disciplina_data = {
            '_id': _id,
            'nombre': nombre
        }
        return Disciplina(** disciplina_data)

    def test_solo_campos_requeridos(self):
        """Pruebas unitarias de campos requeridos del modelo sub disciplina"""
        # Datos
        _id = self.generate_uuid_32_string()
        disciplina = self._crea_disciplina()
        nombre = I18NField(**{
            'es': 'Biologia',
            'en': 'Biology'
        })
        subdisciplina_data = {
            '_id': _id,
            'disciplina': disciplina,
            'nombre': nombre
        }

        # Guardamos
        subdisciplina_doc = SubDisciplina(**subdisciplina_data)
        subdisciplina_doc.save()
        # Comprobamos
        self.assertEqual(
            subdisciplina_data['_id'],
            subdisciplina_doc.id
        )
        # Desglose disciplina
        self.assertEqual(
            subdisciplina_data['disciplina'],
            subdisciplina_doc.disciplina
        )
        self.assertEqual(
            subdisciplina_data['disciplina'].id,
            subdisciplina_doc.disciplina.id
        )
        self.assertEqual(
            subdisciplina_data['disciplina'].nombre,
            subdisciplina_doc.disciplina.nombre
        )

        self.assertEqual(
            subdisciplina_data['nombre'],
            subdisciplina_doc.nombre
        )
        self.assertEqual(
            1,
            SubDisciplina.objects.all().count()
        )
