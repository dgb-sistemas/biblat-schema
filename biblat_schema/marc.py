# !/usr/bin/python
# -*- coding: utf-8 -*-
from mongoengine import (
        StringField,
        EmbeddedDocument,
        EmbeddedDocumentListField,
        Document
    )


class Marc008Field(EmbeddedDocument):
    """008e = País de la revista"""
    e = StringField(max_length=2000)


class Marc022Field(EmbeddedDocument):
    """022a = ISSN"""
    a = StringField(max_length=9)


class Marc024Field(EmbeddedDocument):
    """024a = DOI"""
    a = StringField(max_length=2000)


class Marc035Field(EmbeddedDocument):
    """035a = Número de sistema"""
    a = StringField(max_length=14)


class Marc036Field(EmbeddedDocument):
    """036a = Fecha de ingreso"""
    a = StringField(max_length=8)


class Marc041Field(EmbeddedDocument):
    """041a = Idioma del documento"""
    a = StringField(max_length=2000)


class Marc100Field(EmbeddedDocument):
    """
    100a = Autor personal: Nombre
    100z = Autor personal: Referencia
    1006 = Autor personal: Correo electrónico
    """
    a = StringField(max_length=2000)
    z = StringField(max_length=2000)
    _6 = StringField(max_length=2000, db_field='6')


class Marc110Field(EmbeddedDocument):
    """
    110a = Autor corporativo: Institución
    110b = Autor corporativo: Dependencia
    100c = Autor corporativo: País
    """
    a = StringField(max_length=2000)
    b = StringField(max_length=2000)
    c = StringField(max_length=2000)


class Marc120Field(EmbeddedDocument):
    """
    120z = Adscripción del autor: Referencia
    120u = Adscripción del autor: Institución
    120v = Adscripción del autor: Dependencia
    120w = Adscripción del autor: Ciudad y estado
    120x = Adscripción del autor: País
    """
    z = StringField(max_length=2000)
    u = StringField(max_length=2000)
    v = StringField(max_length=2000)
    w = StringField(max_length=2000)
    x = StringField(max_length=2000)


class Marc222Field(EmbeddedDocument):
    """222a = Título de la revista"""
    a = StringField(max_length=2000)


class Marc245Field(EmbeddedDocument):
    """245a = Título del documento"""
    a = StringField(max_length=2000)


class Marc260Field(EmbeddedDocument):
    """260c = Año de la revista"""
    c = StringField(max_length=2000)


class Marc300Field(EmbeddedDocument):
    """
    300a = Descripción bibliográfica: Volumen
    300b = Descripción bibliográfica: Número
    300c = Descripción bibliográfica: Mes
    300d = Descripción bibliográfica: Parte
    300e = Descripción bibliográfica: Paginación
    """
    a = StringField(max_length=2000)
    b = StringField(max_length=2000)
    c = StringField(max_length=2000)
    d = StringField(max_length=2000)
    e = StringField(max_length=2000)


class Marc504Field(EmbeddedDocument):
    """504a = Referencias"""
    a = StringField(max_length=2000)


class Marc520Field(EmbeddedDocument):
    """
    520a = Resumen en español
    520p = Resumen en idioma portugués
    520i = Resumen en idioma inglés
    520o = Resumen en otro idioma

    """
    a = StringField(max_length=2000)
    p = StringField(max_length=2000)
    i = StringField(max_length=2000)
    o = StringField(max_length=2000)


class Marc546Field(EmbeddedDocument):
    """546a = Idioma del resumen"""
    a = StringField(max_length=2000)


class Marc590Field(EmbeddedDocument):
    """
    590a = Tipo de documento
    590b = Enfoque del documento
    """
    a = StringField(max_length=2000)
    b = StringField(max_length=2000)


class Marc698Field(EmbeddedDocument):
    """698a = Disciplina de la revista"""
    a = StringField(max_length=2000)


class Marc650Field(EmbeddedDocument):
    """650a = Disciplina del documento"""
    a = StringField(max_length=2000)


class Marc653Field(EmbeddedDocument):
    """653a = Palabra clave"""
    a = StringField(max_length=2000)


class Marc654Field(EmbeddedDocument):
    """654a = Keyword"""
    a = StringField(max_length=2000)


class Marc852Field(EmbeddedDocument):
    """
    852u = Enlace a indicadores bibliométricos
    852y = Descripción del enlace
    """
    u = StringField(max_length=2000)
    y = StringField(max_length=2000)


class Marc856Field(EmbeddedDocument):
    """
    856u = Enlace a texto completo
    856y = Descripción del enlace
    """
    u = StringField(max_length=2000)
    y = StringField(max_length=2000)


class Marc039Field(EmbeddedDocument):
    """039a = Enlace"""
    a = StringField(max_length=2000)


class MarcFMTField(EmbeddedDocument):
    """Etiqueta de control FMT"""
    fixed = StringField(max_length=2, db_field='#', default='BK')


class MarcLDRField(EmbeddedDocument):
    """Etiqueta de control LDR"""
    fixed = StringField(max_length=24, db_field='#',
                        default='00000nab^a2200000zi^4500')


class MarcOWNField(EmbeddedDocument):
    """Etiqueta de control OWN"""
    a = StringField(max_length=2000, default='PUBLIC')


class MarcDocumentField(EmbeddedDocument):
    """Campos de documentos con etiquetas MARC"""
    _FMT = EmbeddedDocumentListField(MarcFMTField, db_field='FMT')
    _LDR = EmbeddedDocumentListField(MarcLDRField, db_field='LDR')
    _008 = EmbeddedDocumentListField(Marc008Field, db_field='008', default=None)
    _022 = EmbeddedDocumentListField(Marc022Field, db_field='022', default=None)
    _024 = EmbeddedDocumentListField(Marc024Field, db_field='024', default=None)
    _035 = EmbeddedDocumentListField(Marc035Field, db_field='035', default=None)
    _036 = EmbeddedDocumentListField(Marc036Field, db_field='036', default=None)
    _041 = EmbeddedDocumentListField(Marc041Field, db_field='041', default=None)
    _100 = EmbeddedDocumentListField(Marc100Field, db_field='100', default=None)
    _110 = EmbeddedDocumentListField(Marc110Field, db_field='110', default=None)
    _120 = EmbeddedDocumentListField(Marc120Field, db_field='120', default=None)
    _222 = EmbeddedDocumentListField(Marc222Field, db_field='222', default=None)
    _245 = EmbeddedDocumentListField(Marc245Field, db_field='245', default=None)
    _260 = EmbeddedDocumentListField(Marc260Field, db_field='260', default=None)
    _300 = EmbeddedDocumentListField(Marc300Field, db_field='300', default=None)
    _504 = EmbeddedDocumentListField(Marc504Field, db_field='504', default=None)
    _520 = EmbeddedDocumentListField(Marc520Field, db_field='520', default=None)
    _546 = EmbeddedDocumentListField(Marc546Field, db_field='546', default=None)
    _590 = EmbeddedDocumentListField(Marc590Field, db_field='590', default=None)
    _698 = EmbeddedDocumentListField(Marc698Field, db_field='698', default=None)
    _650 = EmbeddedDocumentListField(Marc650Field, db_field='650', default=None)
    _653 = EmbeddedDocumentListField(Marc653Field, db_field='653', default=None)
    _654 = EmbeddedDocumentListField(Marc654Field, db_field='654', default=None)
    _856 = EmbeddedDocumentListField(Marc856Field, db_field='856', default=None)
    _852 = EmbeddedDocumentListField(Marc852Field, db_field='852', default=None)
    _039 = EmbeddedDocumentListField(Marc039Field, db_field='039', default=None)
    _OWN = EmbeddedDocumentListField(MarcOWNField, db_field='OWN')
