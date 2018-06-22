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
    ReferenceField,
    URLField
)

from .marc import MarcDocumentField
from .catalogs import (
    DisciplinaRevista,
    Pais,
    LicenciaCC,
    SherpaRomeo,
    Idioma,
    EnfoqueDocumento,
    TipoDocumento,
    Disciplina,
    SubDisciplina,
    NombreGeografico
)


class Revista(Document):
    """Esquema de Revista"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    base_datos = StringField(max_length=5, required=True)
    titulo = StringField(max_length=256, required=True)
    titulo_abreviado = StringField(max_length=256)
    issn = StringField(max_length=9, required=True)
    issn_electronico = StringField(max_length=9)
    pais = ReferenceField(Pais, required=True)
    disciplina = ReferenceField(DisciplinaRevista, required=True)
    licencia_cc = ReferenceField(LicenciaCC)
    sherpa_romeo = ReferenceField(SherpaRomeo)
    idioma = ListField(ReferenceField(Idioma))
    logo = StringField(max_length=100)
    portada = StringField(max_length=100)
    fecha_creacion = DateTimeField(required=True)
    fecha_actualizacion = DateTimeField(required=True)


class Fasciculo(Document):
    """Esquema de fascículo"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    revista = ReferenceField(Revista, required=True)
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
    idioma = ReferenceField(Idioma, required=True)
    resumen = StringField(required=True)


class PalabraClave(EmbeddedDocument):
    """Esquema de palabra clave"""
    idioma = ReferenceField(Idioma, required=True)
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
    pais = ReferenceField(Pais)


class Institucion(EmbeddedDocument):
    """Esquema de institución"""
    institucion = StringField(max_length=256, required=True)
    dependencia = StringField(max_length=256)
    ciudad_estado = StringField(max_length=256)
    pais = ReferenceField(Pais, required=True)
    referencia = IntField()


class UrlTextoCompleto(EmbeddedDocument):
    """Esquema de Url de texto completo"""
    url = URLField(required=True)
    descripcion = StringField(max_length=100, required=True)


class Documento(Document):
    """Esquema de documento"""
    _id = StringField(max_length=32, primary_key=True, required=True)
    revista = ReferenceField(Revista, required=True)
    fasciculo = ReferenceField(Fasciculo, required=True)
    titulo_documento = StringField(max_length=256, required=True)
    doi = StringField(max_length=256)
    idioma = ListField(ReferenceField(Idioma))
    paginacion = StringField(max_length=100)
    autor = EmbeddedDocumentListField(Autor)
    autor_corporativo = EmbeddedDocumentListField(AutorCorporativo)
    institucion = EmbeddedDocumentListField(Institucion)
    resumen = EmbeddedDocumentListField(Resumen)
    palabra_clave = EmbeddedDocumentListField(PalabraClave, required=True)
    tipo_documento = ReferenceField(TipoDocumento, required=True)
    enfoque_documento = ReferenceField(EnfoqueDocumento, required=True)
    disciplina = ListField(ReferenceField(Disciplina), required=True)
    subdisciplinas = ListField(ReferenceField(SubDisciplina))
    nombres_geograficos = ListField(ReferenceField(NombreGeografico))
    referencias = BooleanField()
    texto_completo = EmbeddedDocumentListField(UrlTextoCompleto)
    marc21 = EmbeddedDocumentField(MarcDocumentField, required=True)
    fecha_creacion = DateTimeField(required=True)
    fecha_actualizacion = DateTimeField(required=True)


class Historico(EmbeddedDocument):
    """Esquema histórico"""
    catalogador = StringField(max_length=100, required=True)
    nivel = IntField(required=True)
    fecha_hora = DateTimeField(required=True)


class HistorialCatalogacion(Document):
    """Esquema de historial de catalogación"""
    documento = StringField(max_length=32, required=True)
    catalogacion = EmbeddedDocumentListField(Historico, required=True)
