# -*- coding: utf-8 -*-
import uuid


def generate_uuid_32_string():
    """Genera y regresa una cadena de 32 carecteres"""
    return str(uuid.uuid4().hex)
