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
    """Esquema de Revista
    base_datos: Nombre de la base de datos(CLA01 o PER01)
    titulo: Titulo de la revista
    titulo_abreviado:
    issn: identificador de revista
    issn_electronico: identificador de revista electronica
    pais: Nombre del pais
    disciplina: Nombre de la disciplina
    licencia_cc: Licencia Creative Commons
    sherpa_romeo: Definicion Politicas open access
    idioma: Lista de idiomas de la revista
    logo:
    portada:
    fecha_creacion: fecha en que fue creada la revista
    fecha_actualizacion: fecha en que se actualizaron los datos
    """
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
    """Esquema de fascículo
    revista:Objeto referenciado de tipo revista
    volumen: volumen del fasciculo
    numero: numero del fasciculo
    año: año del fasciculo
    mes_inicial:
    mes_final:
    parte: parte del fasciculo
    fecha_creacion:
    fecha_actualizacion:
    """
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
    """Esquema de resumen
    idioma: Objeto referenciado de idioma
    resumen:
    """
    idioma = ReferenceField(Idioma, required=True)
    resumen = StringField(required=True)


class PalabraClave(EmbeddedDocument):
    """Esquema de palabra clave
    idioma: Objedo referenciado de idioma
    palabra_clave: definicion de la palabra clave
    """
    idioma = ReferenceField(Idioma, required=True)
    palabra_clave = StringField(max_length=100, required=True)


class Autor(EmbeddedDocument):
    """Esquema de autor
    nombre: Nombre(s) del autor(es)
    correo_electronico: correo de contacto del autor
    referencia: valor entero que referencia a la institucion
    a la que pertenece el autor
    """
    nombre = StringField(max_length=100, required=True)
    correo_electronico = StringField(max_length=100)
    referencia = IntField()


class AutorCorporativo(EmbeddedDocument):
    """Esquema de autor corporativo
    institucion: nombre de la institucion a la que pertenece el autor
    dependencia: nombre de la dependencia a la que pertenece el autor
    pais: nombre del pais de la institucion a la que pertenece el autor"""
    institucion = StringField(max_length=100, required=True)
    dependencia = StringField(max_length=100)
    pais = ReferenceField(Pais)


class Institucion(EmbeddedDocument):
    """Esquema de institución
    institucion: Nombre de la institucion
    dependencia: Nombre de la dependencia
    ciudad_estado: Nombre de la ciudad o estado
    pais: Nombre del pais
    referencia: Numero entero para ser referenciado por el autor
    """
    institucion = StringField(max_length=256, required=True)
    dependencia = StringField(max_length=256)
    ciudad_estado = StringField(max_length=256)
    pais = ReferenceField(Pais, required=True)
    referencia = IntField()


class UrlTextoCompleto(EmbeddedDocument):
    """Esquema de Url de texto completo
    url: URL del recurso para texto completo
    descripcion: Descripcion del texto completo
    """
    url = URLField(required=True)
    descripcion = StringField(max_length=100, required=True)


class Documento(Document):
    """Esquema de documento
    doi: identificador de objeto digital
    """
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
    """Esquema histórico
    catalogador: Nombre del catalogador
    nivel: Numero entero que define el nivel de acceso
    """
    catalogador = StringField(max_length=100, required=True)
    nivel = IntField(required=True)
    fecha_hora = DateTimeField(required=True)


class HistorialCatalogacion(Document):
    """Esquema de historial de catalogación"""
    documento = StringField(max_length=32, required=True)
    catalogacion = EmbeddedDocumentListField(Historico, required=True)
