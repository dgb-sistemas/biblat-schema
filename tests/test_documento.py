# coding: utf-8
from datetime import datetime
from biblat_schema.models import (
    Documento,
    Revista,
    Fasciculo,
    Autor,
    AutorCorporativo,
    Institucion,
    Resumen,
    PalabraClave,
    SubDisciplina,
    NombreGeografico,
    UrlTextoCompleto,
    TipoDocumento,
    EnfoqueDocumento
)
from biblat_schema.catalogs import I18NField, Disciplina, Pais
from .base import BaseTestCase
from biblat_schema.marc import MarcDocumentField


class TestDocumentModel(BaseTestCase):
    model_class_to_delete = [Documento, Revista, Fasciculo, Autor,
                             AutorCorporativo, Institucion, Resumen,
                             PalabraClave, SubDisciplina, NombreGeografico,
                             UrlTextoCompleto, TipoDocumento,
                             EnfoqueDocumento, I18NField, Disciplina,
                             MarcDocumentField]

    def _crea_pais(self):
        _id = self.generate_uuid_32_string()

        pais_data = {
            '_id': _id,
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
            "intermediate_region": {
                "es": "Centroamérica",
                "en": "Central America"
            },
            "codigo_region": "019",
            "codigo_sub_region": "419",
            "region_intermedia": "013"
        }

        return Pais(**pais_data)

    def _crea_tipo_documento(self):
        _id = self.generate_uuid_32_string()

        tipo_documento_data = {
            '_id': _id,
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
        _id = self.generate_uuid_32_string()
        enfoque_documento_data = {
            '_id': _id,
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
        _id = self.generate_uuid_32_string()
        disciplina_data = {
            '_id': _id,
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
        _id = self.generate_uuid_32_string()
        revista_data = {
            '_id': _id,
            'base_datos': 'CLA01',
            'titulo': u'Estudios de cultura náhuatl',
            'issn': '0071-1675',
            'pais': 'MX',
            'disciplina': u'Antropología',
            'fecha_creacion': datetime.now(),
            'fecha_actualizacion': datetime.now(),
        }
        return Revista(**revista_data)

    def _crea_fasciculo(self):
        _id = self.generate_uuid_32_string()
        revista_doc = self._crea_revista()
        fasciculo_data = {
            '_id': _id,
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

    def _crea_subdisciplina(self):
        _id = self.generate_uuid_32_string()
        disciplina = self._crea_disciplina()
        subdisciplina_data = {
            '_id': _id,
            'disciplina': disciplina,
            'nombre': {
                'es': 'Biologia',
                'en': 'Biology'
            }
        }
        return SubDisciplina(**subdisciplina_data)

    def _crea_descriptor_geografico(self):
        _id = self.generate_uuid_32_string()
        # nombre = self._crea_I18NField_nombre()
        nombre_geografico_data = {
            '_id': _id,
            'nombre': {
                'es': 'México',
                'en': 'Mexico'
            }
        }
        return NombreGeografico(**nombre_geografico_data)

    def test_solo_campos_requeridos(self):
        # Datos
        revista = self._crea_revista()
        fasciculo = self._crea_fasciculo()
        pais = self._crea_pais()
        autor = Autor(**{
            'nombre': 'Vázquez Leal, H.',
            'correo_electronico': 'hvazquez@uv.mx',
            'referencia': 1

        })
        autor_corporativo = AutorCorporativo(**{
            'institucion': 'Universidad Veracruzana',
            'dependencia': 'Escuela de Instrumentación Electrónica y '
                           'Ciencias Atmosféricas',
            'pais': pais
        })
        institucion = Institucion(**{
            'institucion': 'Universidad de Chapingo ',
            'dependencia': 'Filosofia',
            'ciudad_estado': 'Acapulco Guerrero',
            'pais': 'MX',
            'referencia': 1
        })
        resumen = Resumen(**{
            'idioma': 'es',
            'resumen': 'En este artículo el Método de Perturbación (PM) es '
                       'empleado para obtener una solución aproximada para '
                       'el problema de Troesch. Además describiremos el uso '
                       'de la Transformada de Laplace y la Aproximación de '
                       'Padé para trabajar con las series truncadas '
                       'obtenidas por el Método de Perturbación, '
                       'y así obtener soluciones aproximadas compactas. '
                       'Finalmente se propone una tabla comparativa entre la '
                       'solución propuesta y otras soluciones reportadas en '
                       'la '
                       'literatura: Método de Descomposición de Adomian, '
                       'Método de Perturbación Homotópica, Método de '
                       'Análisis Homotópico y la solución numérica exacta. '
                       'Los resultados muestran que nuestra solución es la '
                       'más exacta (Error Relativo Absoluto '
                       'Promedio1.705648354x10-8).'
        })
        palabra_clave = PalabraClave(**{
            'idioma': 'es',
            'palabra_clave': 'Matemáticas'
        })

        subdisciplina = self._crea_subdisciplina()
        nombres_geograficos = self._crea_descriptor_geografico()
        url_texto_completo = UrlTextoCompleto(**{
            'url': 'http://132.248.9.34/hevila/e-BIBLAT/PERIODICA/per7857.pdf',
            'descripcion': 'Estudios de cultura nahuatl'
        })
        marc21 = self._crea_marc_document_field()
        tipo_documento = self._crea_tipo_documento()
        enfoque_documento = self._crea_enfoque_documento()
        disciplina = self._crea_disciplina()

        _id = self.generate_uuid_32_string()
        documento_data = {
            '_id': _id,
            'revista': revista,
            'fasciculo': fasciculo,
            'titulo_documento': 'Estudios de cultura náhuatl',
            'doi': '10.1145/1067268.1067287',
            'paginacion': 'paginacion',
            'autor': [autor],
            'autor_corporativo': [autor_corporativo],
            'institucion': [institucion],
            'resumen': [resumen],
            'palabra_clave': [palabra_clave],
            'tipo_documento': tipo_documento,
            'enfoque_documento': enfoque_documento,
            'disciplina': [disciplina],
            'subdisciplinas': [subdisciplina],
            'nombres_geograficos': [nombres_geograficos],
            'referencias': True,
            'texto_completo': [url_texto_completo],
            'marc21': marc21,
            'fecha_creacion': datetime.now(),
            'fecha_actualizacion': datetime.now()
        }

        # Guardamos
        documento_doc = Documento(
            **documento_data)
        documento_doc.save()

        # Comprobamos
        self.assertEqual(documento_data['_id'],
                         documento_doc._id)
        self.assertEqual(documento_data['revista'],
                         documento_doc.revista)
        self.assertEqual(documento_data['fasciculo'],
                         documento_doc.fasciculo)
        self.assertEqual(documento_data['titulo_documento'],
                         documento_doc.titulo_documento)
        self.assertEqual(documento_data['doi'],
                         documento_doc.doi)
        self.assertEqual(documento_data['paginacion'],
                         documento_doc.paginacion)
        self.assertEqual(documento_data['autor'],
                         documento_doc.autor)
        self.assertEqual(documento_data['autor_corporativo'],
                         documento_doc.autor_corporativo)
        self.assertEqual(documento_data['institucion'],
                         documento_doc.institucion)
        self.assertEqual(documento_data['resumen'],
                         documento_doc.resumen)
        self.assertEqual(documento_data['palabra_clave'],
                         documento_doc.palabra_clave)
        self.assertEqual(documento_data['tipo_documento'],
                         documento_doc.tipo_documento)
        self.assertEqual(documento_data['enfoque_documento'],
                         documento_doc.enfoque_documento)
        self.assertEqual(documento_data['disciplina'],
                         documento_doc.disciplina)
        self.assertEqual(documento_data['subdisciplinas'],
                         documento_doc.subdisciplinas)
        self.assertEqual(documento_data['nombres_geograficos'],
                         documento_doc.nombres_geograficos)
        self.assertEqual(documento_data['referencias'],
                         documento_doc.referencias)
        self.assertEqual(documento_data['texto_completo'],
                         documento_doc.texto_completo)
        self.assertEqual(documento_data['marc21'],
                         documento_doc.marc21)
        self.assertEqual(documento_data['fecha_creacion'],
                         documento_doc.fecha_creacion)
        self.assertEqual(documento_data['fecha_actualizacion'],
                         documento_doc.fecha_actualizacion)

        self.assertEqual(1, Documento.objects.all().count())
