# -*- coding: utf-8 -*-
from mongoengine import (
    Document,
    StringField,
    IntField,
    ReferenceField
)


class PaisesRevistas(Document):
    """Esquema de catalogo paises revistas"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_pais = IntField(required=True)
    alpha3 = StringField(min_length=3, max_length=3, required=True)
    nombre = StringField(max_length=250, required=True)


class Idiomas(Document):
    """Esquema de catalogo idiomas"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_idioma = IntField(required=True)
    codigo = StringField(min_length=3, max_length=3, required=True)
    nombre = StringField(max_length=250, required=True)


class TiposDocumentos(Document):
    """Esquema de catalogo tipos documntos"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_tipo_documento = IntField(required=True)
    nombre = StringField(max_length=150, required=True)
    descripcion = StringField(max_length=700, required=True)


class EnfoquesDocumentos(Document):
    """Esquema de catalogo enfoques documentos"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_enfoque = IntField(required=True)
    nombre = StringField(max_length=150, required=True)
    descripcion = StringField(max_length=700, required=True)


class Disciplinas(Document):
    """Esquema de catalogo disciplinas"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_disciplina = IntField(required=True)
    nombre = StringField(max_length=150, required=True)


class SubDisciplinas(Document):
    """Esquema de catalogo subdisciplinas"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_disciplina = ReferenceField(Disciplinas)
    nombre = StringField(max_length=150, required=True)


class NombresGeograficos(Document):
    """Esquema de catalogo nombres geograficos"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_nombre_geografico = IntField(required=True)
    nombre_espaniol = StringField(max_length=250, required=True)
    nombre_ingles = StringField(max_length=250, required=True)


class DisciplinasRevistas(Document):
    """Esquema de catalogo disciplinas revistas"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    id_disciplina = IntField(required=True)
    base = StringField(max_length=10, required=True)
    nombre = StringField(max_length=150, required=True)


class LicenciasCC(Document):
    """Esquema de catalogo licencias"""
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
