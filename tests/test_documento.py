# coding: utf-8
from datetime import datetime

from biblat_schema.marc import MarcDocumentField
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
from biblat_schema.catalogs import I18NField, Disciplina, Pais, Idioma
from .base import BaseTestCase


class TestDocumentModel(BaseTestCase):
    model_class_to_delete = [Documento, Revista, Fasciculo, Autor,
                             AutorCorporativo, Institucion, Resumen,
                             PalabraClave, SubDisciplina, NombreGeografico,
                             UrlTextoCompleto, TipoDocumento,
                             EnfoqueDocumento, I18NField, Disciplina,
                             MarcDocumentField]

    def _crea_idioma(self):
        _id = self.generate_uuid_32_string()
        nombre = I18NField(** {
            'es': 'Español',
            'en': 'Spanish'
        })
        idioma_data = {
            '_id': _id,
            'iso_639_1': 'es',
            'iso_639_2': 'spa',
            'nombre': nombre
        }
        return Idioma(**idioma_data)

    def _crea_pais(self):
        _id = self.generate_uuid_32_string()

        pais_data = {
            '_id': 'MX',
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
        pais = self._crea_pais()
        pais.save()
        disciplina = self._crea_disciplina()
        revista_data = {
            '_id': _id,
            'base_datos': 'CLA01',
            'titulo': u'Estudios de cultura náhuatl',
            'issn': '0071-1675',
            'pais': pais,
            'disciplina': disciplina,
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

        nombre_geografico_data = {
            '_id': _id,
            'nombre': {
                'es': 'México',
                'en': 'Mexico'
            }
        }
        return NombreGeografico(**nombre_geografico_data)

    def test_solo_campos_requeridos(self):
        """Pruebas unitarias de campos requeridos del modelo Documento"""
        # Datos

        fasciculo = self._crea_fasciculo()
        revista = fasciculo.revista
        pais_revista = revista.pais
        pais_autor_corporativo = Pais.objects(alpha2='MX').first()
        pais_institucion = Pais.objects(alpha2='MX').first()

        idioma = self._crea_idioma()
        autor = Autor(**{
            'nombre': 'Vázquez Leal, H.',
            'correo_electronico': 'hvazquez@uv.mx',
            'referencia': 1

        })
        autor_corporativo = AutorCorporativo(**{
            'institucion': 'Universidad Veracruzana',
            'dependencia': 'Escuela de Instrumentación Electrónica y '
                           'Ciencias Atmosféricas',
            'pais': pais_autor_corporativo
        })
        institucion = Institucion(**{
            'institucion': 'Universidad de Chapingo ',
            'dependencia': 'Filosofia',
            'ciudad_estado': 'Acapulco Guerrero',
            'pais': pais_institucion,
            'referencia': 1
        })

        resumen = Resumen(**{
            'idioma': idioma,
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
            'idioma': idioma,
            'palabra_clave': 'Matemáticas'
        })

        subdisciplina = self._crea_subdisciplina()
        nombres_geograficos = self._crea_descriptor_geografico()
        url_texto_completo = UrlTextoCompleto(**{
            'url': 'http://132.248.9.34/hevila/e-BIBLAT/PERIODICA/per7857.pdf',
            'descripcion': 'Texto completo (Ver PDF)'
        })
        marc21 = self._crea_marc_document_field()
        tipo_documento = self._crea_tipo_documento()
        enfoque_documento = self._crea_enfoque_documento()
        disciplina = revista.disciplina

        _id = self.generate_uuid_32_string()

        documento_data = {
            '_id': _id,
            'revista': revista,
            'fasciculo': fasciculo,
            'numero_sistema': '000463924',
            'titulo_documento': 'Filling gaps in the distribution of the '
                                'white-winged vampire bat, Diaemus youngii ('
                                'Phyllostomidae, Desmodontinae): new records '
                                'for southern Amazonia',
            'doi': '10.1145/1067268.1067287',
            'paginacion': 'P302-309',
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
            'fecha_actualizacion': datetime.now(),
            'fecha_recepcion': '2018-02-01',
            'fecha_aceptacion': '2018-10-24'
        }

        # Guardamos
        documento_doc = Documento(
            **documento_data)
        documento_doc.save()

        # Comprobamos
        self.assertEqual(
            documento_data['_id'],
            documento_doc.id
        )
        # DEsglose revista
        self.assertEqual(
            revista,
            documento_doc.revista
        )
        self.assertEqual(
            revista._id,
            documento_doc.revista.id
        )
        self.assertEqual(
            revista.base_datos,
            documento_doc.revista.base_datos
        )
        self.assertEqual(
            revista.titulo,
            documento_doc.revista.titulo
        )
        self.assertEqual(
            revista.issn,
            documento_doc.revista.issn
        )
        self.assertEqual(
            revista.fecha_creacion,
            documento_doc.revista.fecha_creacion
        )
        self.assertEqual(
            revista.fecha_actualizacion,
            documento_doc.revista.fecha_actualizacion
        )

        # Desglose pais_revista
        self.assertEqual(
            pais_revista,
            documento_doc.revista.pais
        )
        self.assertEqual(
            pais_revista.id,
            documento_doc.revista.pais.id
        )
        self.assertEqual(
            pais_revista.nombre,
            documento_doc.revista.pais.nombre
        )
        self.assertEqual(
            pais_revista.alpha2,
            documento_doc.revista.pais.alpha2
        )
        self.assertEqual(
            pais_revista.alpha3,
            documento_doc.revista.pais.alpha3
        )
        self.assertEqual(
            pais_revista.codigo_pais,
            documento_doc.revista.pais.codigo_pais
        )
        self.assertEqual(
            pais_revista.iso_3166_2,
            documento_doc.revista.pais.iso_3166_2
        )
        self.assertEqual(
            pais_revista.region,
            documento_doc.revista.pais.region
        )
        self.assertEqual(
            pais_revista.sub_region,
            documento_doc.revista.pais.sub_region
        )
        self.assertEqual(
            pais_revista.intermediate_region,
            documento_doc.revista.pais.intermediate_region
        )
        self.assertEqual(
            pais_revista.codigo_region,
            documento_doc.revista.pais.codigo_region
        )
        self.assertEqual(
            pais_revista.codigo_sub_region,
            documento_doc.revista.pais.codigo_sub_region
        )
        self.assertEqual(
            pais_revista.region_intermedia,
            documento_doc.revista.pais.region_intermedia
        )
        # desglose disciplina
        self.assertEqual(
            disciplina,
            documento_doc.revista.disciplina
        )
        self.assertEqual(
            disciplina.id,
            documento_doc.revista.disciplina.id
        )
        self.assertEqual(
            disciplina.nombre,
            documento_doc.revista.disciplina.nombre
        )

        # Desglose fasciculo
        self.assertEqual(
            fasciculo.id,
            documento_doc.fasciculo.id
        )
        self.assertEqual(
            fasciculo.revista,
            documento_doc.fasciculo.revista
        )
        self.assertEqual(
            fasciculo.revista.id,
            documento_doc.fasciculo.revista.id
        )
        self.assertEqual(
            fasciculo.volumen,
            documento_doc.fasciculo.volumen
        )
        self.assertEqual(
            fasciculo.numero,
            documento_doc.fasciculo.numero
        )
        self.assertEqual(
            fasciculo.anio,
            documento_doc.fasciculo.anio
        )
        self.assertEqual(
            fasciculo.mes_inicial,
            documento_doc.fasciculo.mes_inicial
        )
        self.assertEqual(
            fasciculo.mes_final,
            documento_doc.fasciculo.mes_final
        )
        self.assertEqual(
            fasciculo.parte,
            documento_doc.fasciculo.parte
        )
        self.assertEqual(
            fasciculo.fecha_creacion,
            documento_doc.fasciculo.fecha_creacion
        )
        self.assertEqual(
            fasciculo.fecha_actualizacion,
            documento_doc.fasciculo.fecha_actualizacion
        )

        self.assertEqual(
            documento_data['numero_sistema'],
            documento_doc.numero_sistema
        )
        self.assertEqual(
            documento_data['titulo_documento'],
            documento_doc.titulo_documento
        )
        self.assertEqual(
            documento_data['doi'],
            documento_doc.doi
        )
        self.assertEqual(
            documento_data['paginacion'],
            documento_doc.paginacion
        )
        # Desglose autor
        self.assertEqual(
            autor,
            documento_doc.autor[0]
        )
        self.assertEqual(
            autor.nombre,
            documento_doc.autor[0].nombre
        )
        self.assertEqual(
            autor.correo_electronico,
            documento_doc.autor[0].correo_electronico
        )
        self.assertEqual(
            autor.referencia,
            documento_doc.autor[0].referencia
        )
        # Desglose autor_corporativo
        self.assertEqual(
            autor_corporativo,
            documento_doc.autor_corporativo[0]
        )
        self.assertEqual(
            autor_corporativo.institucion,
            documento_doc.autor_corporativo[0].institucion
        )
        self.assertEqual(
            autor_corporativo.dependencia,
            documento_doc.autor_corporativo[0].dependencia
        )

        self.assertEqual(
            pais_autor_corporativo,
            documento_doc.autor_corporativo[0].pais
        )
        self.assertEqual(
            pais_autor_corporativo.id,
            documento_doc.autor_corporativo[0].pais.id
        )
        self.assertEqual(
            pais_autor_corporativo.nombre,
            documento_doc.autor_corporativo[0].pais.nombre
        )
        self.assertEqual(
            pais_autor_corporativo.alpha2,
            documento_doc.autor_corporativo[0].pais.alpha2
        )
        self.assertEqual(
            pais_autor_corporativo.alpha3,
            documento_doc.revista.pais.alpha3
        )
        self.assertEqual(
            pais_autor_corporativo.codigo_pais,
            documento_doc.autor_corporativo[0].pais.codigo_pais
        )
        self.assertEqual(
            pais_autor_corporativo.iso_3166_2,
            documento_doc.autor_corporativo[0].pais.iso_3166_2
        )
        self.assertEqual(
            pais_autor_corporativo.region,
            documento_doc.autor_corporativo[0].pais.region
        )
        self.assertEqual(
            pais_autor_corporativo.sub_region,
            documento_doc.autor_corporativo[0].pais.sub_region
        )
        self.assertEqual(
            pais_autor_corporativo.intermediate_region,
            documento_doc.autor_corporativo[0].pais.intermediate_region
        )
        self.assertEqual(
            pais_autor_corporativo.codigo_region,
            documento_doc.autor_corporativo[0].pais.codigo_region
        )
        self.assertEqual(
            pais_autor_corporativo.codigo_sub_region,
            documento_doc.autor_corporativo[0].pais.codigo_sub_region
        )
        self.assertEqual(
            pais_autor_corporativo.region_intermedia,
            documento_doc.autor_corporativo[0].pais.region_intermedia
        )

        # Desglose Institucion
        self.assertEqual(
            institucion,
            documento_doc.institucion[0]
        )
        self.assertEqual(
            institucion.institucion,
            documento_doc.institucion[0].institucion
        )
        self.assertEqual(
            institucion.dependencia,
            documento_doc.institucion[0].dependencia
        )
        self.assertEqual(
            institucion.ciudad_estado,
            documento_doc.institucion[0].ciudad_estado
        )

        self.assertEqual(
            institucion.referencia,
            documento_doc.institucion[0].referencia
        )

        self.assertEqual(
            pais_institucion,
            documento_doc.institucion[0].pais
        )
        self.assertEqual(
            pais_institucion.id,
            documento_doc.institucion[0].pais.id
        )
        self.assertEqual(
            pais_institucion.nombre,
            documento_doc.institucion[0].pais.nombre
        )
        self.assertEqual(
            pais_institucion.alpha2,
            documento_doc.institucion[0].pais.alpha2
        )
        self.assertEqual(
            pais_institucion.alpha3,
            documento_doc.revista.pais.alpha3
        )
        self.assertEqual(
            pais_institucion.codigo_pais,
            documento_doc.institucion[0].pais.codigo_pais
        )
        self.assertEqual(
            pais_institucion.iso_3166_2,
            documento_doc.institucion[0].pais.iso_3166_2
        )
        self.assertEqual(
            pais_institucion.region,
            documento_doc.institucion[0].pais.region
        )
        self.assertEqual(
            pais_institucion.sub_region,
            documento_doc.institucion[0].pais.sub_region
        )
        self.assertEqual(
            pais_institucion.intermediate_region,
            documento_doc.institucion[0].pais.intermediate_region
        )
        self.assertEqual(
            pais_institucion.codigo_region,
            documento_doc.institucion[0].pais.codigo_region
        )
        self.assertEqual(
            pais_institucion.codigo_sub_region,
            documento_doc.institucion[0].pais.codigo_sub_region
        )
        self.assertEqual(
            pais_institucion.region_intermedia,
            documento_doc.institucion[0].pais.region_intermedia
        )

        # Desglose resumen
        self.assertEqual(
            resumen,
            documento_doc.resumen[0]
        )
        self.assertEqual(
            resumen.resumen,
            documento_doc.resumen[0].resumen
        )
        self.assertEqual(
            resumen.idioma,
            documento_doc.resumen[0].idioma
        )

        self.assertEqual(
            idioma.id,
            documento_doc.resumen[0].idioma.id
        )
        self.assertEqual(
            idioma.iso_639_1,
            documento_doc.resumen[0].idioma.iso_639_1
        )
        self.assertEqual(
            idioma.iso_639_2,
            documento_doc.resumen[0].idioma.iso_639_2
        )
        self.assertEqual(
            idioma.nombre,
            documento_doc.resumen[0].idioma.nombre
        )

        self.assertEqual(
            palabra_clave,
            documento_doc.palabra_clave[0]
        )
        self.assertEqual(
            palabra_clave.idioma,
            documento_doc.palabra_clave[0].idioma
        )
        self.assertEqual(
            palabra_clave.palabra_clave,
            documento_doc.palabra_clave[0].palabra_clave
        )

        self.assertEqual(
            tipo_documento,
            documento_doc.tipo_documento
        )
        self.assertEqual(
            tipo_documento.id,
            documento_doc.tipo_documento.id
        )
        self.assertEqual(
            tipo_documento.nombre,
            documento_doc.tipo_documento.nombre
        )
        self.assertEqual(
            tipo_documento.descripcion,
            documento_doc.tipo_documento.descripcion
        )

        self.assertEqual(
            enfoque_documento,
            documento_doc.enfoque_documento
        )
        self.assertEqual(
            enfoque_documento.id,
            documento_doc.enfoque_documento.id
        )
        self.assertEqual(
            enfoque_documento.nombre,
            documento_doc.enfoque_documento.nombre
        )
        self.assertEqual(
            enfoque_documento.descripcion,
            documento_doc.enfoque_documento.descripcion
        )

        self.assertEqual(
            disciplina,
            documento_doc.disciplina[0]
        )
        self.assertEqual(
            disciplina._id,
            documento_doc.disciplina[0].id
        )
        self.assertEqual(
            disciplina.nombre,
            documento_doc.disciplina[0].nombre
        )

        self.assertEqual(
            subdisciplina,
            documento_doc.subdisciplinas[0]
        )
        self.assertEqual(
            subdisciplina.id,
            documento_doc.subdisciplinas[0].id
        )
        self.assertEqual(
            subdisciplina.disciplina,
            documento_doc.subdisciplinas[0].disciplina
        )
        self.assertEqual(
            subdisciplina.nombre,
            documento_doc.subdisciplinas[0].nombre
        )
        self.assertEqual(
            nombres_geograficos,
            documento_doc.nombres_geograficos[0]
        )
        self.assertEqual(
            nombres_geograficos.id,
            documento_doc.nombres_geograficos[0].id
        )
        self.assertEqual(
            nombres_geograficos.nombre,
            documento_doc.nombres_geograficos[0].nombre
        )

        self.assertEqual(
            documento_data['referencias'],
            documento_doc.referencias
        )

        self.assertEqual(
            url_texto_completo,
            documento_doc.texto_completo[0]
        )
        self.assertEqual(
            url_texto_completo.url,
            documento_doc.texto_completo[0].url
        )
        self.assertEqual(
            url_texto_completo.descripcion,
            documento_doc.texto_completo[0].descripcion
        )

        self.assertEqual(
            marc21,
            documento_doc.marc21
        )
        self.assertEqual(
            documento_data['fecha_creacion'],
            documento_doc.fecha_creacion
        )
        self.assertEqual(
            documento_data['fecha_actualizacion'],
            documento_doc.fecha_actualizacion
        )

        self.assertEqual(
            1,
            Documento.objects.all().count()
        )
