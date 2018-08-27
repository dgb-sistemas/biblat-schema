# coding: utf-8
from datetime import datetime
from biblat_schema.models import (
    Documento,
    Revista,
    Fasciculo,
    Autor,
    AutorCorporativo,
    Institucion,
    Resumen,
    PalabraClave,
    SubDisciplina,
    NombreGeografico,
    UrlTextoCompleto,
    TipoDocumento,
    EnfoqueDocumento
)
from biblat_schema.catalogs import I18NField, Disciplina
from .base import BaseTestCase
from biblat_schema.marc import MarcDocumentField


class TestDocumentModel(BaseTestCase):
    model_class_to_delete = [Documento, Revista, Fasciculo, Autor,
                             AutorCorporativo, Institucion, Resumen,
                             PalabraClave, SubDisciplina, NombreGeografico,
                             UrlTextoCompleto, TipoDocumento,
                             EnfoqueDocumento, I18NField, Disciplina,
                             MarcDocumentField]

    def _crea_tipo_documento(self):
        _id = self.generate_uuid_32_string()
        nombre = self._crea_nombre()
        descripcion = self._crea_I18NField_nombre()
        tipo_documento_data = {
            '_id': _id,
            'nombre': nombre,
            'descripcion': descripcion
        }
        return TipoDocumento(**tipo_documento_data)

    def _crea_enfoque_documento(self):
        _id = self.generate_uuid_32_string()
        nombre = self._crea_nombre()
        descripcion = self._crea_I18NField_nombre()
        enfoque_documento_data = {
            '_id': _id,
            'nombre': nombre,
            'descripcion': descripcion
        }
        return EnfoqueDocumento(**enfoque_documento_data)

    def _crea_I18NField_nombre(self):
        I18NField_data = {
            'es': 'Estados Unidos de Norteamerica',
            'en': 'United States of America'
        }
        return I18NField(**I18NField_data)

    def _crea_lista_nombre_disciplina(self):
        nombre_disciplina_data = {
            'es': 'Clase',
            'en': 'Class'
        }
        return [I18NField(** nombre_disciplina_data)]

    def _crea_lista_disciplina(self):
        _id = self.generate_uuid_32_string()
        nombre = self._crea_lista_nombre_disciplina()
        disciplina_data = {
            '_id': _id,
            'nombre': nombre
        }
        return Disciplina(** disciplina_data)

    def _crea_nombre(self):
        sub_disciplina_data = {
            'es': 'Biologia',
            'en': 'Biology'
        }
        return I18NField(** sub_disciplina_data)

    def _crea_marc_document_field(self):

        marc_document_data = {
        }
        return MarcDocumentField(**marc_document_data)

    def _crea_revista(self):
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
        return Revista(**revista_data)

    def _crea_fasciculo(self):
        _id = self.generate_uuid_32_string()
        revista_doc = self._crea_revista()
        fasciculo_data = {
            '_id': _id,
            'revista': revista_doc,
            'volumen': 1,
            'numero': 2,
            'anio': 2009,
            'mes_inicial': 2,
            'mes_final': 2,
            'parte': 'parte',
            'fecha_creacion': datetime.now(),
            'fecha_actualizacion': datetime.now()
        }
        return Fasciculo(**fasciculo_data)

    def _crea_autor(self):
        autor_data = {
            'nombre': 'Montalvo Espinoza, J.L.',
            'correo_electronico': 'sandokan55@gmail.com ',
            'referencia': 1

        }
        return Autor(**autor_data)

    def _crea_autor_corporativo(self):
        autor_corporativo_data = {
            'institucion': 'Ingeniería (México, D.F.)',
            'dependencia': 'Ingeniería (México, D.F.)',
            'pais': 'MX'
        }

        # Guardamos
        return AutorCorporativo(**autor_corporativo_data)

    def _crea_institucion(self):
        institucion_data = {
            'institucion': 'Universidad de Chapingo ',
            'dependencia': 'Filosofia',
            'ciudad_estado': 'Acapulco Guerrero',
            'pais': 'MX',
            'referencia': 1
        }

        # Guardamos
        return Institucion(**institucion_data)

    def _crea_resumen(self):
        resumen_data = {
            'idioma': 'es',
            'resumen': 'Resumen del documento '
        }

        # Guardamos
        return Resumen(**resumen_data)

    def _crea_palabra_clave(self):
        palabra_clave_data = {
            'idioma': 'es',
            'palabra_clave': 'estudio'
        }

        # Guardamos
        return PalabraClave(**palabra_clave_data)

    def _crea_subdisciplina(self):
        _id = self.generate_uuid_32_string()
        disciplina = self._crea_lista_disciplina()
        nombre = self._crea_nombre()
        subdisciplina_data = {
            '_id': _id,
            'disciplina': disciplina,
            'nombre': nombre
        }
        return SubDisciplina(**subdisciplina_data)

    def _crea_descriptor_geografico(self):
        _id = self.generate_uuid_32_string()
        nombre = self._crea_I18NField_nombre()
        nombre_geografico_data = {
            '_id': _id,
            'nombre': nombre

        }
        return NombreGeografico(**nombre_geografico_data)

    def _crea_url_texto_completo(self):
        url_texto_completo_data = {
            'url': 'http://132.248.9.34/hevila/e-BIBLAT/PERIODICA/per7857.pdf',
            'descripcion': 'Estudios de cultura nahuatl'
        }

        # Guardamos
        return UrlTextoCompleto(**url_texto_completo_data)

    def test_solo_campos_requeridos(self):

        # Datos
        revista = self._crea_revista()
        fasciculo = self._crea_fasciculo()
        autor = self._crea_autor()
        autor_corporativo = self._crea_autor_corporativo()
        institucion = self._crea_institucion()
        resumen = self._crea_resumen()
        palabra_clave = self._crea_palabra_clave()
        subdisciplina = self._crea_subdisciplina()
        nombres_geograficos = self._crea_descriptor_geografico()
        url_texto_completo = self._crea_url_texto_completo()
        marc21 = self._crea_marc_document_field()
        tipo_documento = self._crea_tipo_documento()
        enfoque_documento = self._crea_enfoque_documento()
        disciplina = self._crea_lista_disciplina()

        _id = self.generate_uuid_32_string()
        documento_data = {
            '_id': _id,
            'revista': revista,
            'fasciculo': fasciculo,
            'titulo_documento': 'Estudios de cultura náhuatl',
            'doi': '10.1145/1067268.1067287',
            'paginacion': 'paginacion',
            'autor': [autor],
            'autor_corporativo': [autor_corporativo],
            'institucion': [institucion],
            'resumen': [resumen],
            'palabra_clave': [palabra_clave],
            'tipo_documento': tipo_documento,
            'enfoque_documento': enfoque_documento,
            'disciplina': [disciplina],
            'subdisciplinas': [subdisciplina],
            'nombres_geograficos': [nombres_geograficos],
            'referencias': True,
            'texto_completo': [url_texto_completo],
            'marc21': marc21,
            'fecha_creacion': datetime.now(),
            'fecha_actualizacion': datetime.now()
        }

        # Guardamos
        documento_doc = Documento(
            **documento_data)
        documento_doc.save()

        # Comprobamos
        self.assertEqual(documento_data['_id'],
                         documento_doc._id)
        self.assertEqual(documento_data['revista'],
                         documento_doc.revista)
        self.assertEqual(documento_data['fasciculo'],
                         documento_doc.fasciculo)
        self.assertEqual(documento_data['titulo_documento'],
                         documento_doc.titulo_documento)
        self.assertEqual(documento_data['doi'],
                         documento_doc.doi)
        self.assertEqual(documento_data['paginacion'],
                         documento_doc.paginacion)
        self.assertEqual(documento_data['autor'],
                         documento_doc.autor)
        self.assertEqual(documento_data['autor_corporativo'],
                         documento_doc.autor_corporativo)
        self.assertEqual(documento_data['institucion'],
                         documento_doc.institucion)
        self.assertEqual(documento_data['resumen'],
                         documento_doc.resumen)
        self.assertEqual(documento_data['palabra_clave'],
                         documento_doc.palabra_clave)
        self.assertEqual(documento_data['tipo_documento'],
                         documento_doc.tipo_documento)
        self.assertEqual(documento_data['enfoque_documento'],
                         documento_doc.enfoque_documento)
        self.assertEqual(documento_data['disciplina'],
                         documento_doc.disciplina)
        self.assertEqual(documento_data['subdisciplinas'],
                         documento_doc.subdisciplinas)
        self.assertEqual(documento_data['nombres_geograficos'],
                         documento_doc.nombres_geograficos)
        self.assertEqual(documento_data['referencias'],
                         documento_doc.referencias)
        self.assertEqual(documento_data['texto_completo'],
                         documento_doc.texto_completo)
        self.assertEqual(documento_data['marc21'],
                         documento_doc.marc21)
        self.assertEqual(documento_data['fecha_creacion'],
                         documento_doc.fecha_creacion)
        self.assertEqual(documento_data['fecha_actualizacion'],
                         documento_doc.fecha_actualizacion)

        self.assertEqual(1, Documento.objects.all().count())
