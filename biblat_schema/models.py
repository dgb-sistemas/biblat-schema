# -*- coding: utf-8 -*-
from mongoengine import (
    Document,
    StringField,
    DateTimeField,
    ListField,
    IntField,
    EmbeddedDocument,
    BooleanField,
    EmbeddedDocumentField,
    EmbeddedDocumentListField,
    ReferenceField
)

from .marc import MarcDocumentField


class Revista(Document):
    """Esquema de Revista"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    base_datos = StringField(max_length=5, required=True)
    titulo = StringField(max_length=256, required=True)
    titulo_abreviado = StringField(max_length=256)
    issn = StringField(max_length=9, required=True)
    issn_electronico = StringField(max_length=9)
    pais = StringField(max_length=2, required=True)
    disciplina = StringField(max_length=32, required=True)
    licencia_cc = StringField(max_length=32)
    sherpa_romeo = StringField(max_length=32)
    idioma = ListField(StringField(max_length=2))
    logo = StringField(max_length=100)
    portada = StringField(max_length=100)
    fecha_creacion = DateTimeField(required=True)
    fecha_actualizacion = DateTimeField(required=True)


class Fasciculo(Document):
    """Esquema de fasciculo"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    revista = ReferenceField(Revista)
    volumen = IntField()
    numero = IntField()
    anio = IntField(required=True)
    mes_inicial = IntField(required=True)
    mes_final = IntField(required=True)
    parte = StringField(max_length=100)
    fecha_creacion = DateTimeField(required=True)
    fecha_actualizacion = DateTimeField(required=True)


class Resumen(EmbeddedDocument):
    """Esquema de resumen"""
    idioma = StringField(max_length=2, required=True)
    resumen = StringField(required=True)


class PalabraClave(EmbeddedDocument):
    """Esquema de palabra clave"""
    idioma = StringField(max_length=2, required=True)
    palabra_clave = StringField(max_length=100, required=True)


class Autor(EmbeddedDocument):
    """Esquema de autor"""
    nombre = StringField(max_length=100, required=True)
    correo_electronico = StringField(max_length=100)
    referencia = IntField()


class AutorCorporativo(EmbeddedDocument):
    """Esquema de autor corporativo"""
    institucion = StringField(max_length=100, required=True)
    dependencia = StringField(max_length=100)
    pais = StringField(max_length=2)


class Institucion(EmbeddedDocument):
    """Esquema de institucion"""
    institucion = StringField(max_length=256, required=True)
    dependencia = StringField(max_length=256)
    ciudad_estado = StringField(max_length=256)
    pais = StringField(max_length=2, required=True)
    referencia = IntField()


class UrlTextoCompleto(EmbeddedDocument):
    """Esquema de Url de texto completo"""
    url = StringField(max_length=256, required=True)
    descripcion = StringField(max_length=100, required=True)


class Subdisciplina(EmbeddedDocument):
    """Esquema de sub-disciplina"""
    idioma = StringField(max_length=2, required=True)
    descripcion = StringField(max_length=100, required=True)


class DescriptorGeografico(EmbeddedDocument):
    """Esquema de descriptor geografico"""
    idioma = StringField(max_length=2, required=True)
    descripcion = StringField(max_length=100, required=True)


class Documento(Document):
    """Esquema de documento"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    revista = ReferenceField(Revista)
    fasciculo = ReferenceField(Fasciculo)
    titulo_documento = StringField(max_length=256, required=True)
    doi = StringField(max_length=256)
    idioma = ListField(StringField(max_length=2))
    paginacion = StringField(max_length=100)
    autor = EmbeddedDocumentListField(Autor)
    autor_corporativo = EmbeddedDocumentListField(AutorCorporativo)
    institucion = EmbeddedDocumentListField(Institucion)
    resumen = EmbeddedDocumentListField(Resumen)
    palabra_clave = EmbeddedDocumentListField(PalabraClave, required=True)
    tipo_documento = StringField(max_length=100, required=True)
    enfoque_documento = StringField(max_length=100, required=True)
    disciplina = ListField(StringField(), required=True)
    subdisciplinas = EmbeddedDocumentListField(Subdisciplina)
    descriptores_geograficos = EmbeddedDocumentListField(DescriptorGeografico)
    referencias = BooleanField()
    texto_completo = EmbeddedDocumentListField(UrlTextoCompleto)
    marc21 = EmbeddedDocumentField(MarcDocumentField, required=True)
    fecha_creacion = DateTimeField(required=True)
    fecha_actualizacion = DateTimeField(required=True)


class Historico(EmbeddedDocument):
    """Esquema historico"""
    catalogador = StringField(max_length=100, required=True)
    nivel = IntField(required=True)
    fecha_hora = DateTimeField(required=True)


class HistorialCatalogacion(Document):
    """Esquema de historial de catalogacion"""
    documento = StringField(max_length=32, required=True)
    catalogacion = EmbeddedDocumentListField(Historico, required=True)
