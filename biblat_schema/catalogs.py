# -*- coding: utf-8 -*-
from mongoengine import (
    Document,
    StringField,
    IntField,
    ReferenceField
)


class PaisRevista(Document):
    """Esquema de catalogo pais revista"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_pais = IntField(required=True)
    alpha3 = StringField(min_length=3, max_length=3, required=True)
    nombre = StringField(max_length=250, required=True)


class Idioma(Document):
    """Esquema de catalogo idioma"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_idioma = IntField(required=True)
    codigo = StringField(min_length=3, max_length=3, required=True)
    nombre = StringField(max_length=250, required=True)


class TipoDocumento(Document):
    """Esquema de catalogo tipo documento"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_tipo_documento = IntField(required=True)
    nombre = StringField(max_length=150, required=True)
    descripcion = StringField(max_length=700, required=True)


class EnfoqueDocumento(Document):
    """Esquema de catalogo enfoque documento"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_enfoque = IntField(required=True)
    nombre = StringField(max_length=150, required=True)
    descripcion = StringField(max_length=700, required=True)


class Disciplina(Document):
    """Esquema de catalogo disciplina"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_disciplina = IntField(required=True)
    nombre = StringField(max_length=150, required=True)


class SubDisciplina(Document):
    """Esquema de catalogo subdisciplina"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_disciplina = ReferenceField(Disciplina)
    nombre = StringField(max_length=150, required=True)


class NombreGeografico(Document):
    """Esquema de catalogo nombre geografico"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_nombre_geografico = IntField(required=True)
    nombre_espaniol = StringField(max_length=250, required=True)
    nombre_ingles = StringField(max_length=250, required=True)


class DisciplinaRevista(Document):
    """Esquema de catalogo disciplina revista"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_disciplina = IntField(required=True)
    base = StringField(max_length=10, required=True)
    nombre = StringField(max_length=150, required=True)


class LicenciaCC(Document):
    """Esquema de catalogo licencia"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_licencia = IntField(required=True)
    tipo = StringField(max_length=6, required=True)
    descripcion = StringField(max_length=150, required=True)


class SherpaRomeo(Document):
    """Esquema de catalogo sherpa romeo"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_sherpa_romeo = IntField(required=True)
    color = StringField(max_length=10, required=True)
    politica = StringField(max_length=70, required=True)
