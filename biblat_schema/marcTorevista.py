# -*- coding: utf-8 -*-
from mongoengine import (
        StringField,
        EmbeddedDocument,
        EmbeddedDocumentListField,
        Document
    )

from .models import Revista
from .marc import MarcDocumentField


class marcTorevista:
    #TODO recibir el registro de aleph en formato MARC texto plano.
    #TODO crear un objeto de tipo MarcDocumentField, definido en marc.py
    marc = MarcDocumentField
    #TODO crear un objeto de tipo Revista
    revista = Revista
    #TODO tomar los campos necesarios para llenar un objeto de tipo Revista.
    #TODO ingresar el objeto Revista creado a MongoDB