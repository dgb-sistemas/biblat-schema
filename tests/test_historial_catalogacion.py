# coding: utf-8

from datetime import datetime

from biblat_schema.catalogs import (
    I18NField,
    Idioma,
    Pais,
    TipoDocumento,
    EnfoqueDocumento,
    Disciplina
)
from biblat_schema.marc import MarcDocumentField
from biblat_schema.choices import FREQUENCY
from biblat_schema.models import (
    HistorialCatalogacion,
    Historico, Revista,
    Fasciculo,
    PalabraClave,
    Documento
)
from .base import BaseTestCase


class TestCatalogationHistoricalModel(BaseTestCase):

    model_class_to_delete = [HistorialCatalogacion, Historico]

    def _crea_idioma(self):
        nombre = I18NField(** {
            'es': 'Español',
            'en': 'Spanish'
        })
        idioma_data = {
            'iso_639_1': 'es',
            'iso_639_3': 'spa',
            'nombre': nombre
        }
        return Idioma(**idioma_data)

    def _crea_pais(self):
        pais_data = {
            "nombre": {
                "es": "",
                "en": "Mexico"
            },
            "alpha2": "MX",
            "alpha3": "MEX",
            "codigo_pais": "484",
            "iso_3166_2": "ISO 3166-2:MX",
            "region": {
                "es": "",
                "en": "Americas"
            },
            "sub_region": {
                "es": "",
                "en": "Latin America and the Caribbean"
            },
            "region_intermedia": {
                "es": "Centroamérica",
                "en": "Central America"
            },
            "codigo_region": "019",
            "codigo_sub_region": "419",
            "codigo_region_intermedia": "013"
        }

        return Pais(**pais_data)

    def _crea_tipo_documento(self):
        tipo_documento_data = {
            'nombre': {
                'es': 'Biologia',
                'en': 'Biology'
            },
            'descripcion': {
                'es': 'Estados Unidos de Norteamerica',
                'en': 'United States of America'
            }
        }
        return TipoDocumento(**tipo_documento_data)

    def _crea_enfoque_documento(self):
        enfoque_documento_data = {
            'nombre': {
                'es': 'Biologia',
                'en': 'Biology'
            },
            'descripcion': {
                'es': 'Estados Unidos de Norteamerica',
                'en': 'United States of America'
            }
        }
        return EnfoqueDocumento(**enfoque_documento_data)

    def _crea_disciplina(self):
        disciplina_data = {
            'nombre': {
                'es': 'Biologia',
                'en': 'Biology'
            }
        }
        return Disciplina(**disciplina_data)

    def _crea_marc_document_field(self):
        marc_document_data = {
        }
        return MarcDocumentField(**marc_document_data)

    def _crea_revista(self):
        pais = self._crea_pais()
        pais.save()
        disciplina = self._crea_disciplina()
        periodicidad = FREQUENCY[0][0]
        revista_data = {
            'base_datos': 'CLA01',
            'titulo': u'Estudios de cultura náhuatl',
            'issn': '0071-1675',
            'pais': pais,
            'disciplina': disciplina,
            'fecha_creacion': datetime.now(),
            'fecha_actualizacion': datetime.now(),
            'periodicidad': periodicidad
        }
        return Revista(**revista_data)

    def _crea_fasciculo(self):
        revista_doc = self._crea_revista()
        fasciculo_data = {
            'revista': revista_doc,
            'volumen': 1,
            'numero': 2,
            'anio': 2009,
            'mes_inicial': 2,
            'mes_final': 2,
            'parte': 'parte',
            'fecha_creacion': datetime.now(),
            'fecha_actualizacion': datetime.now()
        }
        return Fasciculo(**fasciculo_data)

    def _crea_documento(self):
        """Pruebas unitarias de campos requeridos del modelo Documento"""
        # Datos

        fasciculo = self._crea_fasciculo()
        revista = fasciculo.revista
        idioma = self._crea_idioma()

        palabra_clave = PalabraClave(**{
            'idioma': idioma,
            'palabra_clave': 'Matemáticas'
        })
        marc21 = self._crea_marc_document_field()
        tipo_documento = self._crea_tipo_documento()
        enfoque_documento = self._crea_enfoque_documento()
        disciplina = revista.disciplina

        documento_data = {
            'revista': revista,
            'fasciculo': fasciculo,
            'numero_sistema': '000463924',
            'titulo_documento': 'Filling gaps in the distribution of the '
                                'white-winged vampire bat, Diaemus youngii ('
                                'Phyllostomidae, Desmodontinae): new records '
                                'for southern Amazonia',

            'palabra_clave': [palabra_clave],
            'tipo_documento': tipo_documento,
            'enfoque_documento': enfoque_documento,
            'disciplina': [disciplina],

            'marc21': marc21,
            'fecha_creacion': datetime.now(),
            'fecha_actualizacion': datetime.now()
        }

        return Documento(**documento_data)

    def _crea_historico(self):
        historico_data = {
            'catalogador': 'Juan Perez Perez',
            'nivel': 10,
            'fecha_hora': datetime.now()
        }

        historico = Historico(**historico_data)
        return historico

    def _crea_historico2(self):
        historico_data = {
            'catalogador': 'Carlos Alberto Suárez',
            'nivel': 2,
            'fecha_hora': datetime.now()
        }

        historico = Historico(**historico_data)
        return historico

    def test_solo_campos_requeridos(self):
        """Pruebas unitarias de campos requeridos del modelo Historial
        Catalogacion"""
        # Datos
        historico = self._crea_historico()
        historico2 = self._crea_historico2()
        documento = self._crea_documento()
        historial_catalogacion_data = {
            'documento': documento,
            'catalogacion': [historico]
        }

        # Guardamos
        historial_catalogacion_doc = HistorialCatalogacion(
            **historial_catalogacion_data)
        historial_catalogacion_doc.save()

        historial_catalogacion_data.get('catalogacion').append(historico2)

        historial_catalogacion_doc = HistorialCatalogacion(
            **historial_catalogacion_data
        )
        historial_catalogacion_doc.save()
        # Comprobamos
        self.assertEqual(
            documento,
            historial_catalogacion_doc.documento
        )
        self.assertEqual(
            documento.id,
            historial_catalogacion_doc.documento.id
        )

        self.assertEqual(
            documento.revista.id,
            historial_catalogacion_doc.documento.revista.id
        )
        self.assertEqual(
            documento.revista.base_datos,
            historial_catalogacion_doc.documento.revista.base_datos
        )
        self.assertEqual(
            documento.revista.titulo,
            historial_catalogacion_doc.documento.revista.titulo
        )
        self.assertEqual(
            documento.revista.issn,
            historial_catalogacion_doc.documento.revista.issn
        )
        self.assertEqual(
            documento.revista.disciplina,
            historial_catalogacion_doc.documento.revista.disciplina
        )
        self.assertEqual(
            documento.revista.fecha_creacion,
            historial_catalogacion_doc.documento.revista.fecha_creacion
        )
        self.assertEqual(
            documento.revista.fecha_actualizacion,
            historial_catalogacion_doc.documento.revista.fecha_actualizacion
        )

        self.assertEqual(
            documento.fasciculo.id,
            historial_catalogacion_doc.documento.fasciculo.id
        )
        self.assertEqual(
            documento.fasciculo.revista,
            historial_catalogacion_doc.documento.fasciculo.revista
        )

        self.assertEqual(
            documento.fasciculo.revista.id,
            historial_catalogacion_doc.documento.fasciculo.revista.id
        )
        self.assertEqual(
            documento.fasciculo.revista.base_datos,
            historial_catalogacion_doc.documento.fasciculo.revista.base_datos
        )
        self.assertEqual(
            documento.fasciculo.revista.titulo,
            historial_catalogacion_doc.documento.fasciculo.revista.titulo
        )
        self.assertEqual(
            documento.fasciculo.revista.issn,
            historial_catalogacion_doc.documento.fasciculo.revista.issn
        )
        self.assertEqual(
            documento.fasciculo.revista.disciplina,
            historial_catalogacion_doc.documento.fasciculo.revista.disciplina
        )
        self.assertEqual(
            documento.fasciculo.revista.fecha_creacion,
            historial_catalogacion_doc.documento.fasciculo.revista.fecha_creacion
        )
        self.assertEqual(
            documento.fasciculo.revista.fecha_actualizacion,
            historial_catalogacion_doc.documento.fasciculo.revista.fecha_actualizacion
        )
        self.assertEqual(
            documento.fasciculo.revista.periodicidad,
            historial_catalogacion_doc.documento.fasciculo.revista.periodicidad
        )

        self.assertEqual(
            documento.fasciculo.anio,
            historial_catalogacion_doc.documento.fasciculo.anio
        )
        self.assertEqual(
            documento.fasciculo.mes_inicial,
            historial_catalogacion_doc.documento.fasciculo.mes_inicial
        )
        self.assertEqual(
            documento.fasciculo.mes_final,
            historial_catalogacion_doc.documento.fasciculo.mes_final
        )
        self.assertEqual(
            documento.fasciculo.fecha_creacion,
            historial_catalogacion_doc.documento.fasciculo.fecha_creacion
        )
        self.assertEqual(
            documento.fasciculo.fecha_actualizacion,
            historial_catalogacion_doc.documento.fasciculo.fecha_actualizacion
        )
        self.assertEqual(
            documento.numero_sistema,
            historial_catalogacion_doc.documento.numero_sistema
        )
        self.assertEqual(
            documento.titulo_documento,
            historial_catalogacion_doc.documento.titulo_documento
        )
        self.assertEqual(
            documento.palabra_clave,
            historial_catalogacion_doc.documento.palabra_clave
        )
        self.assertEqual(
            documento.palabra_clave[0],
            historial_catalogacion_doc.documento.palabra_clave[0]
        )
        self.assertEqual(
            documento.palabra_clave[0]['idioma'],
            historial_catalogacion_doc.documento.palabra_clave[0]['idioma']
        )
        self.assertEqual(
            documento.palabra_clave[0]['palabra_clave'],
            historial_catalogacion_doc.documento.palabra_clave[0]['palabra_clave']
        )
        self.assertEqual(
            documento.tipo_documento,
            historial_catalogacion_doc.documento.tipo_documento
        )
        self.assertEqual(
            documento.tipo_documento,
            historial_catalogacion_doc.documento.tipo_documento
        )
        self.assertEqual(
            documento.tipo_documento.id,
            historial_catalogacion_doc.documento.tipo_documento.id
        )
        self.assertEqual(
            documento.tipo_documento.nombre,
            historial_catalogacion_doc.documento.tipo_documento.nombre
        )
        self.assertEqual(
            documento.tipo_documento.descripcion,
            historial_catalogacion_doc.documento.tipo_documento.descripcion
        )
        self.assertEqual(
            documento.enfoque_documento,
            historial_catalogacion_doc.documento.enfoque_documento
        )
        self.assertEqual(
            documento.enfoque_documento.id,
            historial_catalogacion_doc.documento.enfoque_documento.id
        )
        self.assertEqual(
            documento.enfoque_documento.nombre,
            historial_catalogacion_doc.documento.enfoque_documento.nombre
        )
        self.assertEqual(
            documento.enfoque_documento.descripcion,
            historial_catalogacion_doc.documento.enfoque_documento.descripcion
        )
        self.assertEqual(
            documento.disciplina,
            historial_catalogacion_doc.documento.disciplina
        )
        self.assertEqual(
            documento.disciplina[0].id,
            historial_catalogacion_doc.documento.disciplina[0].id
        )
        self.assertEqual(
            documento.disciplina[0].nombre,
            historial_catalogacion_doc.documento.disciplina[0].nombre
        )
        self.assertEqual(
            documento.marc21,
            historial_catalogacion_doc.documento.marc21
        )
        self.assertEqual(
            documento.marc21,
            historial_catalogacion_doc.documento.marc21
        )
        self.assertEqual(
            documento.fecha_creacion,
            historial_catalogacion_doc.documento.fecha_creacion
        )
        self.assertEqual(
            documento.fecha_actualizacion,
            historial_catalogacion_doc.documento.fecha_actualizacion
        )
        self.assertEqual(
            historial_catalogacion_data['catalogacion'],
            historial_catalogacion_doc.catalogacion
        )
        self.assertEqual(
            historial_catalogacion_data['catalogacion'][0].catalogador,
            historial_catalogacion_doc.catalogacion[0].catalogador
        )
        self.assertEqual(
            historial_catalogacion_data['catalogacion'][0].nivel,
            historial_catalogacion_doc.catalogacion[0].nivel
        )
        self.assertEqual(
            historial_catalogacion_data['catalogacion'][0].fecha_hora,
            historial_catalogacion_doc.catalogacion[0].fecha_hora
        )
        self.assertEqual(
            historial_catalogacion_data['catalogacion'][1].catalogador,
            historial_catalogacion_doc.catalogacion[1].catalogador
        )
        self.assertEqual(
            historial_catalogacion_data['catalogacion'][1].nivel,
            historial_catalogacion_doc.catalogacion[1].nivel
        )
        self.assertEqual(
            historial_catalogacion_data['catalogacion'][1].fecha_hora,
            historial_catalogacion_doc.catalogacion[1].fecha_hora
        )
        self.assertEqual(
            2,
            HistorialCatalogacion.objects.all().count()
        )
