from mongoengine import *


class Revista(Document):
    _id = StringField(max_length=32)
    base_datos = StringField(max_length=5, required=True)
    titulo_revista = StringField(max_length=256, required=True)
    titulo_abreviado_revista = StringField(max_length=256)
    issn = StringField(max_length=9, required=True)
    issn_electronico = StringField(max_length=9)
    pais_revista = StringField(max_length=2, required=True)
    disciplina_revista = StringField(max_length=32, required=True)
    licencia_cc = StringField(max_length=32)
    sherpa_romeo = StringField(max_length=32)
    idioma = ListField(StringField(max_length=2), )
    logo = StringField(max_length=100)
    portada = StringField(max_length=100)
    fecha_creacion = DateTimeField(required=True)
    fecha_actualizacion = DateTimeField(required=True)


class Fasciculo(Document):
    revista = StringField(max_length=32, required=True)
    volumen = IntField()
    numero = IntField()
    año = IntField(required=True)
    mes_inicial = IntField(required=True)
    mes_final = IntField(required=True)
    parte = StringField(max_length=100)
    fecha_creacion = DateTimeField(required=True)
    fecha_actualizacion = DateTimeField(required=True)


class Resumen(EmbeddedDocument):
    idioma = StringField(max_length=2, required=True)
    resumen = StringField(required=True)


class PalabraClave(EmbeddedDocument):
    idioma = StringField(max_length=2, required=True)
    palabra_clave = StringField(max_length=100, required=True)


class Autor(EmbeddedDocument):
    nombre = StringField(max_length=100, required=True)
    correo_electronico = StringField(max_length=100)
    referencia = IntField()


class Autor_Corporativo(EmbeddedDocument):
    institucion = StringField(max_length=100, required=True)
    dependencia = StringField(max_length=100)
    pais = StringField(max_length=2)


class Institucion(EmbeddedDocument):
    institucion = StringField(max_length=256, required=True)
    dependencia = StringField(max_length=256)
    ciudad_estado = StringField(max_length=256)
    pais = StringField(max_length=2, required=True)
    referencia = IntField()


class UrlTextoCompleto(EmbeddedDocument):
    url = StringField(max_length=256, required=True)
    descripcion = StringField(max_length=100, required=True)


class Subdisciplina(EmbeddedDocument):
    idioma = StringField(max_length=2, required=True)
    descripcion = StringField(max_length=100, required=True)


class DescriptorGeografico(EmbeddedDocument):
    idioma = StringField(max_length=2, required=True)
    descripcion = StringField(max_length=100, required=True)


class Documento(Document):
    revista = StringField(max_length=32, required=True)
    fasciculo = StringField(max_length=32, required=True)
    titulo_documento = StringField(max_length=256, required=True)
    doi = StringField(max_length=256)
    idioma = ListField(StringField(max_length=2), )
    paginacion = StringField(max_length=100)
    autor = ListField(EmbeddedDocumentField(Autor))
    autor_corporativo = ListField(EmbeddedDocumentField(Autor_Corporativo), )
    institucion = ListField(EmbeddedDocumentField(Institucion), )
    resumen = ListField(EmbeddedDocumentField(Resumen), )
    palabra_clave = ListField(EmbeddedDocumentField(PalabraClave), required=True)
    tipo_documento = StringField(max_length=100, required=True)
    enfoque_documento = StringField(max_length=100, required=True)
    disciplina = ListField(StringField(), required=True)
    subdisciplinas = ListField(EmbeddedDocumentField(Subdisciplina), required=True)
    descriptores_geograficos = ListField(EmbeddedDocumentField(Subdisciplina))
    referencias = BooleanField()
    texto_completo = ListField(EmbeddedDocumentField(UrlTextoCompleto))
    marc21 = DictField(required=True)
    fecha_creacion = DateTimeField(required=True)
    fecha_actualizacion = DateTimeField(required=True)


class Historico(EmbeddedDocument):
    catalogador = StringField(max_length=100, required=True)
    nivel = IntField(required=True)
    fecha_hora = DateTimeField(required=True)


class HistorialCatalogacion(Document):
    documento = StringField(max_length=32, required=True)
    catalogacion = ListField(EmbeddedDocumentField(Historico), required=True)
