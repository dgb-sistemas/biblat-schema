# -*- coding: utf-8 -*-
from mongoengine import (
    Document,
    StringField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    ReferenceField,
    URLField,
    ListField
)


class I18NField(EmbeddedDocument):
    es = StringField()
    en = StringField()


class Pais(Document):
    """Esquema de catalogo pais
    alpha2: codigo de pais en dos letras designado para representar la
    mayoria de los lenguajes en el mundo
    alpha: codigo de pais en tres caracteres
    codigo_pais: Codigo numerico de pais
    iso_3166-2: Codigo de 3 letras que brinda mas combinaciones, pudiendo
    cubrir mas lenguajes
    """
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


class Idioma(Document):
    """Esquema de catalogo idioma
    iso_639_1:códigos de dos letras usados para identificar los idiomas
    principales del mundo
    iso_639_2:códigos de tres letras usados para identificar los idiomas
    principales del mundo
    """
    _id = StringField(max_length=3, primary_key=True, required=True)
    iso_639_1 = StringField(min_length=2, max_length=2)
    iso_639_2 = StringField(min_length=3, max_length=3, required=True)
    nombre = EmbeddedDocumentField(I18NField)


class TipoDocumento(Document):
    """Esquema de catalogo tipo documento"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    nombre = EmbeddedDocumentField(I18NField)
    descripcion = EmbeddedDocumentField(I18NField)


class EnfoqueDocumento(Document):
    """Esquema de catalogo enfoque documento"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    nombre = EmbeddedDocumentField(I18NField)
    descripcion = EmbeddedDocumentField(I18NField)


class Disciplina(Document):
    """Esquema de catalogo disciplina"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    nombre = EmbeddedDocumentField(I18NField)


class SubDisciplina(Document):
    """Esquema de catalogo subdisciplina"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    disciplina = ReferenceField(Disciplina, required=True)
    nombre = EmbeddedDocumentField(I18NField)


class NombreGeografico(Document):
    """Esquema de catalogo nombre geografico"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    nombre = EmbeddedDocumentField(I18NField)


class DisciplinaRevista(Document):
    """Esquema de catalogo disciplina revista"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    base = ListField(StringField(max_length=10, required=True))
    nombre = EmbeddedDocumentField(I18NField)


class LicenciaCC(Document):
    """Esquema de catalogo licencia
    tipo: tipo de licencia creative commons
    url: url del legal code de la licencia
    """
    _id = StringField(max_length=32, primary_key=True, required=True)
    tipo = StringField(max_length=6, required=True)
    url = URLField(required=True)


class SherpaRomeo(Document):
    """Esquema de catalogo sherpa romeo
    politica: especificacion de la politica utilizada
    codigo: codigo hexagecimal utilizado por el color
    """
    _id = StringField(max_length=32, primary_key=True, required=True)
    color = EmbeddedDocumentField(I18NField)
    politica = EmbeddedDocumentField(I18NField)
    codigo = StringField(required=True)
