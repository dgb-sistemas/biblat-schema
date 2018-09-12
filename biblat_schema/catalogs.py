# -*- coding: utf-8 -*-
from mongoengine import (
    Document,
    StringField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    ReferenceField,
    URLField
)


class I18NField(EmbeddedDocument):
    es = StringField()
    en = StringField()


class Pais(Document):
    """Esquema de catalogo pais"""
    _id = StringField(max_length=2, primary_key=True, required=True)
    nombre = EmbeddedDocumentField(I18NField)
    alpha2 = StringField(max_length=2, required=True)
    alpha3 = StringField(max_length=3, required=True)
    codigo_pais = StringField(max_length=3, required=True)
    iso_3166_2 = StringField(max_length=14, required=True)
    region = EmbeddedDocumentField(I18NField)
    sub_region = EmbeddedDocumentField(I18NField)
    intermediate_region = EmbeddedDocumentField(I18NField)
    codigo_region = StringField(max_length=3, required=True)
    codigo_sub_region = StringField(max_length=3, required=True)
    region_intermedia = StringField(max_length=3)

    meta = {
        'collection': 'paises',
        'indexes': [
            'nombre.es',
            'alpha2'
        ]
    }


class Idioma(Document):
    """Esquema de catalogo idioma"""
    _id = StringField(max_length=3, primary_key=True, required=True)
    iso_639_1 = StringField(min_length=2, max_length=2)
    iso_639_2 = StringField(min_length=3, max_length=3, required=True)
    nombre = EmbeddedDocumentField(I18NField)

    meta = {
        'collection': 'idiomas',
        'indexes': [
            'nombre.es',
            'iso_639_1',
            'iso_639_2',
        ]
    }


class TipoDocumento(Document):
    """Esquema de catalogo tipo documento"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    nombre = EmbeddedDocumentField(I18NField)
    descripcion = EmbeddedDocumentField(I18NField)

    meta = {
        'collection': 'tipo_documento',
        'indexes': [
            'nombre.es'
        ]
    }


class EnfoqueDocumento(Document):
    """Esquema de catalogo enfoque documento"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    nombre = EmbeddedDocumentField(I18NField)
    descripcion = EmbeddedDocumentField(I18NField)

    meta = {
        'collection': 'enfoque_documento',
        'indexes': [
            'nombre.es'
        ]
    }


class Disciplina(Document):
    """Esquema de catalogo disciplina"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    nombre = EmbeddedDocumentField(I18NField)

    meta = {
        'collection': 'disciplinas',
        'indexes': [
            'nombre.es'
        ]
    }


class SubDisciplina(Document):
    """Esquema de catalogo subdisciplina"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    disciplina = ReferenceField(Disciplina, required=True)
    nombre = EmbeddedDocumentField(I18NField)

    meta = {
        'collection': 'subdisciplinas',
        'indexes': [
            'nombre.es',
            'disciplina'
        ]
    }


class NombreGeografico(Document):
    """Esquema de catalogo nombre geografico"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    nombre = EmbeddedDocumentField(I18NField)
    nota = EmbeddedDocumentField(I18NField)

    meta = {
        'collection': 'nombres_geograficos',
        'indexes': [
            'nombre.es'
        ]
    }


class DisciplinaRevista(Document):
    """Esquema de catalogo disciplina revista"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    base = StringField(max_length=10, required=True)
    nombre = EmbeddedDocumentField(I18NField)

    meta = {
        'collection': 'disciplinas_revista',
        'indexes': [
            'nombre.es',
            'base'
        ]
    }


class LicenciaCC(Document):
    """Esquema de catalogo licencia"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    tipo = StringField(max_length=6, required=True)
    url = URLField(required=True)

    meta = {
        'collection': 'licencias_cc',
        'indexes': [
            'tipo'
        ]
    }


class SherpaRomeo(Document):
    """Esquema de catalogo sherpa romeo"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    color = EmbeddedDocumentField(I18NField)
    politica = EmbeddedDocumentField(I18NField)
    codigo = StringField(required=True)

    meta = {
        'collection': 'sherparomeo',
        'indexes': [
            'color.es'
        ]
    }
