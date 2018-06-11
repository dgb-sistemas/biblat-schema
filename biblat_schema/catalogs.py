# -*- coding: utf-8 -*-
from mongoengine import (
    Document,
    StringField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    ListField
)


class I18NField(EmbeddedDocument):
    es = StringField()
    en = StringField()


class I18DField(EmbeddedDocument):
    es = StringField()
    en = StringField()


class Pais(Document):
    """Esquema de catalogo pais"""
    _id = StringField(max_length=32, primary_key=True, required=True)
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


class Idioma(Document):
    """Esquema de catalogo idioma"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    codigo = StringField(min_length=3, max_length=3, required=True)
    nombre = EmbeddedDocumentField(I18NField)


class TipoDocumento(Document):
    """Esquema de catalogo tipo documento"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    nombre = EmbeddedDocumentField(I18NField)
    descripcion = EmbeddedDocumentField(I18DField)


class EnfoqueDocumento(Document):
    """Esquema de catalogo enfoque documento"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    nombre = EmbeddedDocumentField(I18NField)
    descripcion = EmbeddedDocumentField(I18DField)


class Disciplina(Document):
    """Esquema de catalogo disciplina"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    nombre = EmbeddedDocumentField(I18NField)


class SubDisciplina(Document):
    """Esquema de catalogo subdisciplina"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    nombre = EmbeddedDocumentField(I18NField)


class NombreGeografico(Document):
    """Esquema de catalogo nombre geografico"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    nombre = EmbeddedDocumentField(I18NField)


class DisciplinaRevista(Document):
    """Esquema de catalogo disciplina revista"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    base = StringField(max_length=10, required=True)
    nombre = EmbeddedDocumentField(I18NField)


class LicenciaCC(Document):
    """Esquema de catalogo licencia"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    tipo = StringField(max_length=6, required=True)
    descripcion = EmbeddedDocumentField(I18DField)


class SherpaRomeo(Document):
    """Esquema de catalogo sherpa romeo"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    color = StringField(max_length=10, required=True)
    politica = StringField(max_length=70, required=True)
