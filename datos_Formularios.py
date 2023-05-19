import copy

# Tratamiento de los datos para los formularios
class form0001():

    """
    server_http = es el servidor donde se visualizara el fomulario
    """
    def __init__(self, server_http):

        self.consultatmp = dict()
        self.server_http = server_http
        self.botones = list()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Generacion el retorno de la consulta
    # asignamos los valores obtenidos de la tabla de datos
    def asignacion(self, datos_list, **atributos_dict):

        # Inicializacion de estructuras
        lista_list = list()
        consulta_rtn = {'lista':lista_list}
        indice = 0
        datos_list_local = datos_list

        # Obtenemos el diccionario temporario
        # k es la clave 'lista'
        # v es la lista de diccionarios de los campos a visualizar
        for k, v in self.consultatmp.items():
            for y in v:
                dict_temp = y

        # Navegamos la lista de datos obtenidos de la consulta en la tabla
        # l es el registro de la tabla de datos obtenido
        for l in datos_list_local:

            # generamos una copy del diccionario temporario
            detalle_dict    = copy.deepcopy(dict_temp)

            # Llenamos el diccionario
            # navegamos en la relacion entre las claves de los campos a visualizar y
            # los a nombres de campo de la lista
            for kg, vg in atributos_dict.items():

                # dentro del valor value coloco el valor del campo del registro
                detalle_dict[kg]['value'] = l[vg]

            # generamos un nuevo elemento a la lista
            lista_list.append(copy.deepcopy(detalle_dict))

            # limpiamos el diccionario temporario
            detalle_dict.clear()
            indice += 1

        # retornamos la consulta con los valores incorporados de la lista de registros
        # obtenidos de la tabla
        return consulta_rtn

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Generacion del atributos dict
    def consultatmp_consulta_wrk(self, datos_list, **consulta):

        atributos_dict = {}
        self.consultatmp = consulta

        # Definicion del diccionario de atributos
        # kc es la clave = 'lista'
        # vc es la lista de diccionarios con los campos a visualizar
        for kc, vc in self.consultatmp.items():

            # elemento es cada elemento de la lista de diccionarios
            for elemento in vc:

                # recorremos el elemento que es un diccionario del campo a visualizar
                for kvc, vvc in elemento.items():

                    # verifica si la clave no es un btn
                    if kvc != 'btn':

                        # generamos el diccionario de los atributos
                        atributos_dict[kvc] = vvc['name']

        return self.asignacion(datos_list, **atributos_dict)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end Provincia-update
    def provinciaupdhlp(self):
        
        consulta = {
            'update': {
                'PROVINCIAID'   : form0001.provinciaid,
                'PROVINCIA'     : form0001.provincia,
                'DESCPROVINCIA' : form0001.descprovincia,
                },
            'btn': [{'name': 'Provincias', 'link': 'http://localhost:5000/provinciawrkhlp/'}]
        }

        # Inicializacion de estructuras
        lista_list = list()
        consulta_rtn = {'lista':lista_list}
        indice = 0

        consulta_rtn = copy.deepcopy(consulta)

        for k1, v1 in consulta_rtn.items():
            for k2, v2 in v1.items():
                for k3, v3 in v2.items():
                    if k3 == 'PROVINCIAID':
                        pass

        return consulta_rtn

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end Provincia
    def provinciawrkhlp(self, *datos_list):

        # Definicion del diccionario de devolucion a un trabajar con
        consulta = {
            'lista': [
                {
                    'PROVINCIAID': {'hidden': 'on', 'name':'provinciaid', 'value': ''},
                    'PROVINCIA': {'placeholder': 'Codigo de la Provincia', 'name': 'provincia', 'value': '' },
                    'DESCPROVINCIA': {'placeholder': 'Nombre de la Provincia', 'name': 'descprovincia', 'value': '' },
                    'btn': [
                        {'name': 'modificar', 'link': self.server_http + '/provinciaupdhlp/'},
                        {'name': 'nuevo', 'link': self.server_http + '/provinciaaddhlp/'}
                    ]
                }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta de Provincia
    def provinciaaddhlp(self):

        consulta = {
            'add': {'PROVINCIA': {'placeholder': 'Ingrese el Codigo de la Provincia',
                                  'name': 'provincia', 'type': 'integer', 'min': '1', 'max': '10',
                                  'value': '', 'error': 'Debe ingresarse un valor - El valor debe ser numerico'}
                ,
                    'DESCPROVINCIA': {'placeholder': 'Ingrese el Nombre de la Provincia',
                                      'name': 'descprovincia', 'type': 'text', 'length': '50', 'value': '',
                                      'error': 'Debe ingresarse un valor - Hasta 50 caracteres'}
                    },
            'btn': [
                {'name': 'Provincias', 'link': self.server_http + '/provinciawrkhlp/'}
            ]
        }
        return consulta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end Tipo de Cuerpo
    def tipocuerpowrkhlp(self, *datos_list):

        # Definicion del diccionario de devolucion a un trabajar con
        consulta = {
            'lista': [
                {
                    'TIPOCUERPOID'    : {'hidden':'on', 'name':'tipocuerpoid', 'value':''},
                    'TIPOCUERPO'      : {'placeholder': 'Codigo del Tipo del Cuerpo',
                        'name': 'tipocuerpo', 'value': '' },
                    'DESCTIPOCUERPO'  : {'placeholder': 'Nombre del Tipo del Cuerpo',
                        'name': 'desctipocuerpo', 'value': '' },
                    'btn':[
                        {'name':'modificar', 'link': self.server_http + '/tipocuerpoupdhlp/'},
                        {'name':'nuevo', 'link': self.server_http + '/tipocuerpoaddhlp/'}
                        ]
                }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta de Tipo de Cuerpo
    def tipocuerpoaddhlp(self):

        consulta = {
            'add': {
                'TIPOCUERPO': {'placeholder': 'Ingrese el Codigo del Tipo del Cuerpo', 'name': 'tipocuerpo',
                               'type': 'text', 'length': '2', 'value': '',
                               'error': 'Debe ingresarse un valor - Hasta 2 caracteres'},
                'DESCTIPOCUERPO': {'placeholder': 'Ingrese la descripcion del Tipo del Cuerpo',
                                   'name': 'desctipocuerpo', 'type': 'text', 'length': '50', 'value': '',
                                   'error': 'Debe ingresarse un valor - Hasta 50 caracteres'},
                'btn': [{'name': 'Tipos de Cuerpos', 'link':  self.server_http + '/tipocuerpowrkhlp/'}]
            }
        }
        return consulta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Tipo de Cuota
    def tipocuotawrkhlp(self, *datos_list):

        consulta = {
            'lista': [
                {
                    'TIPOCUOTAID': {'hidden': 'on', 'name': 'tipocuotaid', 'value': ''},
                    'TIPOCUOTA': {'placeholder': 'Codigo del Tipo de Cuota', 'name': 'tipocuota', 'value': ''},
                    'DESCTIPOCUOTA': {'placeholder': 'Nombre del Tipo del Cuota', 'name': 'desctipocuota', 'value': ''},
                    'btn': [
                        {'name': 'modificar', 'link': self.server_http + '/tipocuotaupdhlp/'},
                        {'name': 'nuevo', 'link': self.server_http + '/tipocuotaaddhlp/'}
                    ]
                }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta de Tipo de Cuota
    def tipocuotaaddhlp(self):

        consulta = {
            'add': {
                'TIPOCUOTA': {'placeholder': 'Ingrese el Tipo de Cuota', 'name': 'tipocuota', 'type': 'integer',
                              'min': '1', 'max': '10', 'value': '',
                              'error': 'Debe ingresarse un valor - El valor debe ser numerico'},
                'DESCTIPOCUOTA': {'placeholder': 'Ingrese la Descripcion del Tipo de Cuota',
                                  'name': 'desctipocuota', 'type': 'text', 'length': '50', 'value': '',
                                  'error': 'Debe ingresarse un valor - Hasta 50 caracteres'}
            },
            'btn': [{'name': 'TipoCuotas', 'link': self.server_http + '/tipocuotawrkhlp/'}]
        }

        return consulta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Tipo de Documento
    def tipodocumentowrkhlp(self, *datos_list):

        consulta = {
            'lista': [
                {
                    'TIPODOCUMENTOID'    : {'hidden':'on', 'name':'tipodocumentoid', 'value':''},
                    'TIPODOCUMENTO'      : {'placeholder': 'Codigo del Tipo de Documento', 'name': 'tipodocumento',
                        'value': '' },
                    'DESCTIPODOCUMENTO'  : {'placeholder': 'Nombre del Tipo de Documento', 'name': 'desctipodocumento',
                        'value': ''},
                    'btn':[
                        {'name':'modificar', 'link': self.server_http + '/tipodocumentoupdhlp/'},
                        {'name':'nuevo', 'link': self.server_http + '/tipodocumentoaddhlp/'}
                        ]
                }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta de Tipo de Documento
    def tipodocumentoaddhlp(self):

        consulta = {
            'add': {
                'TIPODOCUMENTO': {'placeholder': 'Ingrese el Tipo de Documento',
                                  'name': 'tipodocumento', 'type': 'integer', 'min': '1', 'max': '10', 'value': '',
                                  'error': 'Debe ingresarse un valor - El valor debe ser numerico'},
                'DESCTIPODOCUMENTO': {'placeholder': 'Ingrese la Descripcion del Tipo de Documento',
                                      'name': 'desctipodocumento', 'type': 'text', 'length': '50', 'value': '',
                                      'error': 'Debe ingresarse un valor - Hasta 50 caracteres'}
            },
            'btn': [{'name': 'TipoDocumentos', 'link': self.server_http + '/tipodocumentowrkhlp/'}]
        }

        return consulta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Tipo de Estado
    def tipoestadowrkhlp(self, *datos_list):

        consulta = {
            'lista': [
                {
                'ESTADOID'    : {'hidden':'on', 'name':'estadoid', 'value':''},
                'ESTADO'      : {'placeholder': 'Codigo del Tipo de Estado', 'name': 'tipoestado', 'value': ''},
                'DESCESTADO'  : {'placeholder': 'Nombre del Tipo de Estado', 'name': 'desctipoestado', 'value': ''},
                'btn':[
                    {'name':'modificar', 'link': self.server_http + '/tipoestadoupdhlp/'},
                    {'name':'nuevo', 'link': self.server_http + '/tipoestadoaddhlp/'}
                    ]
                }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta Tipo de Estado
    def tipoestadoaddhlp(self):

        consulta = {
            'add': {
                'ESTADO': {'placeholder': 'Ingrese el Tipo de Estado', 'name': 'estado',
                           'type': 'text', 'length': '2', 'value': '',
                           'error': 'Debe ingresarse un valor - Hasta 2 caracteres'},
                'DESCESTADO': {'placeholder': 'Ingrese la Descripcion del Tipo de Estado',
                               'name': 'descestado', 'type': 'text', 'length': '50', 'value': '',
                               'error': 'Debe ingresarse un valor - Hasta 50 caracteres'}
            },
            'btn': [{'name': 'TipoEstados', 'link': self.server_http + '/tipoestadowrkhlp/'}]
        }

        return consulta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Tipo de Moneda
    def tipomonedawrkhlp(self, *datos_list):

        consulta = {
            'lista': [
                {
                    'CODIGOMONEDAID'    : {'hidden':'on', 'name':'codigomonedaid', 'value':''},
                    'CODIGOMONEDA'      : {'placeholder': 'Codigo del Tipo de Moneda', 'name': 'codigomoneda',
                        'value': '' },
                    'DESCTIPOMONEDA'  : {'placeholder': 'Nombre del Tipo de Moneda', 'name': 'desctipomoneda',
                        'value': '' },
                    'btn':[
                        {'name':'modificar', 'link': self.server_http + '/tipomonedaupdhlp/'},
                        {'name':'nuevo', 'link': self.server_http + '/tipomonedaaddhlp/'}
                        ]
                }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta de Tipo de Moneda
    def tipomonedaaddhlp(self):

        consulta = {
            'add': {
                'CODIGOMONEDA': {'placeholder': 'Ingrese el Codigo de Moneda',
                                 'name': 'codigomoneda', 'type': 'integer', 'min': '1', 'max': '10', 'value': '',
                                 'error': 'Debe ingresarse un valor - El valor debe ser numerico'},
                'DESCTIPOMONEDA': {'placeholder': 'Ingrese la Descripcion del Tipo de Moneda',
                                   'name': 'desctipomoneda', 'type': 'text', 'length': '50', 'value': '',
                                   'error': 'Debe ingresarse un valor - Hasta 50 caracteres'}
            },
            'btn': [{'name': 'TipoMonedas', 'link':  self.server_http + '/tipomonedawrkhlp/'}]
        }

        return consulta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Tipo de Movimiento
    def tipomovimientowrkhlp(self, *datos_list):

        consulta = {
            'lista': [
                {
                    'CODIGOTIPOMOVIMIENTOID'    : {'hidden':'on', 'name':'codigotipomovimientoid', 'value':''},
                    'CODIGOTIPOMOVIMIENTO'      : { 'placeholder': 'Codigo del Tipo de Movimiento',
                        'name': 'codigotipomovimiento', 'value': '' },
                    'DESCTIPOMOVIMIENTO'  : {'placeholder': 'Nombre del Tipo de Movimiento',
                        'name': 'desctipomovimiento', 'value': '' },
                    'btn':[
                        {'name':'modificar', 'link': self.server_http + '/tipomovimientoupdhlp/'},
                        {'name':'nuevo', 'link': self.server_http + '/tipomovimientoaddhlp/'}
                        ]
                }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta de Tipo de Movimiento
    def tipomovimientoaddhlp(self):

        consulta = {
            'add': {
                'CODIGOTIPOMOVIMIENTO': {'placeholder': 'Ingrese el Tipo de Movimiento',
                                         'name': 'codigotipomovimiento', 'type': 'integer', 'min': '1', 'max': '10',
                                         'value': '',
                                         'error': 'Debe ingresarse un valor - El valor debe ser numerico'},
                'DESCTIPOMOVIMIENTO': {'placeholder': 'Ingrese la Descripcion del Tipo de Movimiento',
                                       'name': 'desctipomovimiento', 'type': 'text', 'length': '50', 'value': '',
                                       'error': 'Debe ingresarse un valor - Hasta 50 caracteres'}
            },
            'btn': [{'name': 'TipoMovimientos', 'link': self.server_http + '/tipomovimientowrkhlp/'}]
        }

        return consulta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Tipo de Origen
    def tipoorigenwrkhlp(self, *datos_list):

        consulta = {
            'lista': [
                {
                    'ORIGENID'    : {'hidden':'on', 'name':'origenid', 'value':''},
                    'TIPOORIGEN'  : {'placeholder': 'Codigo del Tipo de Origen', 'name': 'tipoorigen', 'value': ''},
                    'DESCORIGEN'  : {'placeholder': 'Nombre del Tipo de Origen', 'name': 'desctipoorigen', 'value': ''},
                    'btn':[
                        {'name':'modificar', 'link': self.server_http + '/tipoorigenupdhlp/'},
                        {'name':'nuevo', 'link': self.server_http + '/tipoorigenaddhlp/'}
                        ]
                }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta de Tipo de Origen
    def tipoorigenaddhlp(self):

        consulta = {
            'add': {
                'TIPOORIGEN': {'placeholder': 'Ingrese el Tipo de Origen', 'name': 'tipoorigen', 'type': 'text',
                               'length': '1', 'value': '',
                               'error': 'Debe ingresarse un valor - Hasta 1 caracteres'},
                'DESCORIGEN': {'placeholder': 'Ingrese la Descripcion del Tipo de Origen',
                               'name': 'desctipoorigen', 'type': 'text', 'length': '50', 'value': '',
                               'error': 'Debe ingresarse un valor - Hasta 50 caracteres'}
            },
            'btn': [{'name': 'TipoOrigen', 'link':  self.server_http + '/tipoorigenwrkhlp/'}]
        }

        return consulta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Tipo de Pago
    def tipopagowrkhlp(self, *datos_list):

        consulta = {
            'lista': [
                {
                    'CODIGOFORMAPAGOID' : {'hidden':'on', 'name':'codigoformapagoid', 'value':''},
                    'CODIGOFORMAPAGO'   : {'placeholder': 'Codigo del Tipo de Forma de Pago',
                                           'name': 'codigoformapago', 'value': ''},
                    'DESCTIPOPAGO'      : {'placeholder': 'Nombre del Tipo de Forma de Pago',
                                           'name': 'desctipoopago', 'value': ''},
                    'btn'               : [
                        {'name':'modificar', 'link': self.server_http + '/tipopagoupdhlp/'},
                        {'name':'nuevo', 'link': self.server_http + '/tipopagoaddhlp/'}
                        ]
                }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta de Tipo de Pago
    def tipopagoaddhlp(self):

        consulta = {
            'add': {
                'CODIGOFORMAPAGO'   : {'placeholder': 'Ingrese el Codigo de Forma de Pago',
                                       'name': 'codigoformapago', 'type': 'integer', 'min': '1', 'max': '10',
                                       'value': '',
                                       'error': 'Debe ingresarse un valor - El valor debe ser numerico'},
                'DESCTIPOPAGO'      : {'placeholder': 'Ingrese la Descripcion del Tipo de Pago',
                                       'name': 'desctipopago', 'type': 'text', 'length': '50', 'value': '',
                                       'error': 'Debe ingresarse un valor - Hasta 50 caracteres'}
            },
            'btn': [{'name': 'TipoPago', 'link':  self.server_http + '/tipopagowrkhlp/'}]
        }

        return consulta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Tipo de Registro
    def tiporegistrowrkhlp(self, *datos_list):

        consulta = {
            'lista': [
                {
                    'TIPOREGISTROID'    : {'hidden':'on', 'name':'tiporegistroid', 'value':''},
                    'TIPOREGISTRO'      : {'placeholder': 'Codigo del Tipo de Registro', 'name': 'tiporegistro',
                                           'value': ''},
                    'DESCTIPOREGISTRO'  : {'placeholder': 'Nombre del Tipo de Registro', 'name': 'desctipooregistro',
                                           'value': ''},
                    'btn'               : [
                        {'name':'modificar', 'link': self.server_http + '/tiporegistroupdhlp/'},
                        {'name':'nuevo', 'link': self.server_http + '/tiporegistroaddhlp/'}
                        ]
                }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta de Tipo de Registro
    def tiporegistroaddhlp(self):

        consulta = {
            'add': {
                'TIPOREGISTRO'      : {'placeholder': 'Ingrese el Tipo de Registro',
                                       'name': 'tiporegistro', 'type': 'text', 'length': '2', 'value': '',
                                       'error': 'Debe ingresarse un valor - Hasta 2 caracteres'},
                'DESCTIPOREGISTRO'  : {'placeholder': 'Ingrese la Descripcion del Tipo de Registro',
                                       'name': 'desctiporegistro', 'type': 'text', 'length': '50', 'value': '',
                                       'error': 'Debe ingresarse un valor - Hasta 50 caracteres'}
            },
            'btn': [{'name': 'TipoRegistro', 'link':  self.server_http + '/tiporegistrowrkhlp/'}]
        }

        return consulta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Tipo de Sub Registro
    def tiposubregistrowrkhlp(self, *datos_list):

        consulta = {
            'lista': [
                {
                    'TIPOSUBREGISTROID'     : {'hidden':'on', 'name':'tiposubregistroid', 'value':''},
                    'TIPOSUBREGISTRO'       : {'placeholder': 'Codigo del Tipo de Sub Registro',
                                               'name': 'tiposubregistro', 'value': ''},
                    'DESCTIPOSUBREGISTRO'   : {'placeholder': 'Nombre del Tipo de Sub Registro',
                                               'name': 'desctiposubregistro', 'value': ''},
                    'btn'                   : [
                        {'name':'modificar', 'link': self.server_http + '/tiposubregistroupdhlp/'},
                        {'name':'nuevo', 'link': self.server_http + '/tiposubregistroaddhlp/'}
                        ]
                }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta de Tipo de Sub Registro
    def tiposubregistroaddhlp(self):

        consulta = {
            'add': {
                'TIPOSUBREGISTRO'       : {'placeholder': 'Ingrese el Tipo de Registro', 'name': 'tiposubregistro',
                                           'type': 'text', 'length': '1', 'value': '',
                                           'error': 'Debe ingresarse un valor - Hasta 1 caracteres' },
                'DESCTIPOSUBREGISTRO'   : {'placeholder': 'Ingrese la Descripcion del Tipo de Sub Registro',
                                           'name': 'desctiposubregistro', 'type': 'text', 'length': '50', 'value': '',
                                           'error': 'Debe ingresarse un valor - Hasta 50 caracteres'}
            },
            'btn': [{'name': 'TipoSubRegistro', 'link':  self.server_http + '/tiposubregistrowrkhlp/'}]
        }

        return consulta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Tipo de Titular
    def tipotitularwrkhlp(self, *datos_list):

        consulta = {
            'lista': [
                {
                    'TIPOTITULARID'     : {'hidden':'on', 'name':'tipotitularid', 'value':''},
                    'TIPOTITULAR'       : {'placeholder': 'Codigo del Tipo de Titular',
                                           'name': 'tipotitular', 'value': ''},
                    'DESCTIPOTITULAR'   : {'placeholder': 'Nombre del Tipo de Titular',
                                           'name': 'desctipotitular', 'value': ''},
                    'btn'               : [
                        {'name':'modificar', 'link': self.server_http + '/tipotitularupdhlp/'},
                        {'name':'nuevo', 'link': self.server_http + '/tipotitularaddhlp/'}
                        ]
                }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta de Tipo de Titular
    def tipotitularaddhlp(self):

        consulta = {
            'add': {
                'TIPOTITULAR'       : {'placeholder': 'Ingrese el Tipo de Titular',
                                       'name': 'tipotitular', 'type': 'text', 'length': '1', 'value': '',
                                       'error': 'Debe ingresarse un valor - Hasta 1 caracteres'},
                'DESCTIPOTITULAR'   : {'placeholder': 'Ingrese la Descripcion del Tipo de Titular',
                                       'name': 'desctipotitular', 'type': 'text', 'length': '50', 'value': '',
                                       'error': 'Debe ingresarse un valor - Hasta 50 caracteres'}
            },
            'btn': [{'name': 'TipoTitular', 'link':  self.server_http + '/tipotitularwrkhlp/'}]
        }

        return consulta


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Api de Estados
    def apiestadoswrkhlp(self, *datos_list):

        consulta = {
            'lista': [
                {
                    'APIESTADOSID'          : {'hidden':'on', 'name':'apiestadosid', 'value':''},
                    'APIESTADODESCRIPCION'  : {'placeholder': 'Api Estado Descripcion',
                                               'name': 'apiestadodescripcion', 'value': ''},
                    'APIUSERCRT'            : {'placeholder': 'Usuario de Creacion del Registro',
                                               'name': 'apiusercrt', 'value': ''},
                    'TOKENUSERCRTTIMESTAMP' : {'placeholder': 'Fecha y Hora de Creacion del Registro',
                                               'name': 'tokenusercrttimestamp', 'value': ''},
                    'APIUSERDLT'            : {'placeholder': 'Usuario de Eliminacion del Registro',
                                               'name': 'apiuserdlt', 'value': ''},
                    'TOKENUSERDLTTIMESTAMP' : {'placeholder': 'Fecha y Hora de Eliminacion del Registro',
                                               'name': 'tokenuserdlttimestamp', 'value': ''},
                    'btn'                   : [
                        {'name':'modificar', 'link': self.server_http + '/apiestadosupdhlp/'},
                        {'name':'nuevo', 'link': self.server_http + '/apiestadosaddhlp/'}
                        ]
                }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta de Api de Estados
    def apiestadosaddhlp(self):

        consulta = {
            'add': {
                'APIESTADODESCRIPCION': {'placeholder': 'Ingrese la Descripcion del Api de Estado',
                                         'name': 'apiestadodescripcion', 'type': 'text', 'length': '100', 'value': '',
                                         'error': 'Debe ingresarse un valor - Hasta 100 caracteres'}
            },
            'btn': [{'name': 'ApiEstados', 'link':  self.server_http + '/apiestadowrkhlp/'}]
        }

        return consulta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Api de Tareas
    def apitareaswrkhlp(self, *datos_list):

        consulta = {
            'lista': [
                {
                    'APITAREASID'           : {'hidden':'on', 'name':'apitareasid', 'value':''},
                    'APITAREASDESCRIPCION'  : {'placeholder': 'Api Tareas Descripcion',
                                               'name': 'apitareasdescripcion', 'value': ''},
                    'APIUSERCRT'            : {'placeholder': 'Usuario de Creacion del Registro',
                                               'name': 'apiusercrt', 'value': ''},
                    'TOKENUSERCRTTIMESTAMP' : {'placeholder': 'Fecha y Hora de Creacion del Registro',
                                               'name': 'tokenusercrttimestamp', 'value': ''},
                    'APIUSERDLT'            : {'placeholder': 'Usuario de Eliminacion del Registro',
                                               'name': 'apiuserdlt', 'value': ''},
                    'TOKENUSERDLTTIMESTAMP' : {'placeholder': 'Fecha y Hora de Eliminacion del Registro',
                                               'name': 'tokenuserdlttimestamp', 'value': ''},
                    'btn'                   : [
                        {'name':'modificar', 'link': self.server_http + '/apitaresaupdhlp/'},
                        {'name':'nuevo', 'link': self.server_http + '/apitareasaddhlp/'}
                        ]
                }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta de Api de Tareas
    def apitareasaddhlp(self):

        consulta = {
            'add': {
                'APITAREASDESCRIPCION': {'placeholder': 'Ingrese la Descripcion del Api de Tarea',
                                         'name': 'apiestadodescripcion', 'type': 'text', 'length': '100', 'value': '',
                                         'error': 'Debe ingresarse un valor - Hasta 100 caracteres'}
            },
            'btn': [{'name': 'ApiTareas', 'link':  self.server_http + '/apitareawrkhlp/'}]
        }

        return consulta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Api de Registro
    def apiregistroswrkhlp(self, *datos_list):

        consulta = {
            'lista': [
                {
                    'APIREGISTROSID'            : {'hidden':'on', 'name':'apiregistroid', 'value':''},
                    'APIREGISTROSDESCRIPCION'   : {'placeholder': 'Api Registro Descripcion',
                                                   'name': 'apiregistrodescripcion', 'value': ''},
                    'APIREGISTROSNUMERO'        : {'placeholder': 'Api Registro Numero',
                                                   'name': 'apiregistronumero', 'value': ''},
                    'APIUSERCRT'                : {'placeholder': 'Usuario de Creacion del Registro',
                                                   'name': 'apiusercrt', 'value': ''},
                    'TOKENUSERCRTTIMESTAMP'     : {'placeholder': 'Fecha y Hora de Creacion del Registro',
                                                   'name': 'tokenusercrttimestamp', 'value': ''},
                    'APIUSERDLT'                : {'placeholder': 'Usuario de Eliminacion del Registro',
                                                   'name': 'apiuserdlt', 'value': ''},
                    'TOKENUSERDLTTIMESTAMP'     : {'placeholder': 'Fecha y Hora de Eliminacion del Registro',
                                                   'name': 'tokenuserdlttimestamp', 'value': ''},
                    'btn'                       : [
                        {'name':'modificar', 'link': self.server_http + '/apiregiostroupdhlp/'},
                        {'name':'nuevo', 'link': self.server_http + '/apiregostroaddhlp/'}
                        ]
                }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta de Api de Registros
    def apiregistrosaddhlp(self):

        consulta = {
            'add': {
                'APIREGISTROSDESCRIPCION'   : {'placeholder': 'Ingrese la Descripcion del Api del Registro',
                                               'name': 'apiregistrodescripcion', 'type': 'text', 'length': '100',
                                               'value': '',
                                               'error': 'Debe ingresarse un valor - Hasta 100 caracteres'},
                'APIREGISTROSNUMERO'        : {'placeholder': 'Ingrese el Numero del Registro',
                                               'name': 'apiregistronumero', 'type': 'integer', 'min': '1', 'max': '10',
                                               'value': '',
                                               'error': 'Debe ingresarse un valor - El valor debe ser numerico'}

            },
            'btn': [{'name': 'ApiRegistros', 'link':  self.server_http + '/apiregistrowrkhlp/'}]
        }

        return consulta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Api Token User
    def tokenuserwrkhlp(self, *datos_list):

        consulta = {
            'lista': [
                {
                    'APIUSERID'                 : {'hidden':'on', 'name':'apiuserid', 'value':''},
                    'APIUSERNOMBRE'             : {'placeholder': 'Nombre del Usuario',
                                                   'name': 'apiusernombre', 'value': ''},
                    'APELLIDONOMBRE'            : {'placeholder': 'Apellido y Nombre del Usuario',
                                                   'name': 'apellidonombre', 'value': ''},
                    'APIUSEREMAIL'              : {'placeholder': 'Email del Usuario',
                                                   'name': 'apiuseremail', 'value': ''},
                    'APIUSERWHATSAPP'           : {'placeholder': 'Whatsapp del Usuario',
                                                   'name': 'apiuserwhatsapp', 'value': ''},
                    'TIPODOCUMENTO'             : {'placeholder': 'Tipo de Documento',
                                                   'name': 'tipodocumento', 'value': ''},
                    'DESCTIPODOCUMENTO'         : {'placeholder': 'Tipo de Documento Descripcion',
                                                   'name': 'desctipodocumento', 'value': ''},
                    'NUMERODOCUMENTO'           : {'placeholder': 'Numero de Documento',
                                                   'name': 'numerodocumento', 'value': ''},
                    'APIREGISTROSDESCRIPCION'   : {'placeholder': 'Descripcion del Registro',
                                                   'name': 'apiregistrosdescripcion', 'value': ''},
                    'APIREGISTROSNUMERO'        : {'placeholder': 'Numero de Registro',
                                                   'name': 'apiregistrosnumero', 'value': ''},
                    #'APIESTADO'                 : {'placeholder': 'Estado del Usuario',
                    #                               'name': 'apiestadodescripcion', 'value': ''},
                    'APIUSERCRT'                : {'placeholder': 'Usuario de Creacion del Registro',
                                                   'name': 'apiusercrt', 'value': ''},
                    'TOKENUSERCRTTIMESTAMP'     : {'placeholder': 'Fecha y Hora de Creacion del Registro',
                                                   'name': 'tokenusercrttimestamp', 'value': ''},
                    'APIUSERDLT'                : {'placeholder': 'Usuario de Eliminacion del Registro',
                                                   'name': 'apiuserdlt', 'value': ''},
                    'TOKENUSERDLTTIMESTAMP'     : {'placeholder': 'Fecha y Hora de Eliminacion del Registro',
                                                   'name': 'tokenuserdlttimestamp', 'value': ''},
                    'btn'                       : [
                        {'name':'modificar',    'link': self.server_http + '/tokenuserupdhlp/'},
                        {'name':'nuevo',        'link': self.server_http + '/tokenuseraddhlp/'}
                        ]
                }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta de Api de Token User *VERIFICAR EN HELP
    def tokenuseraddhlp(self):

        consulta = {
            'add': {
                'APIUSERNOMBRE'     : {'placeholder': 'Ingrese el Nombre del Usuario',
                                       'name': 'apiusernombre', 'type': 'text', 'length': '10', 'value': '',
                                       'error': 'Debe ingresarse un valor - Hasta 10 caracteres'},
                'APIUSERPASS'       : {'placeholder': 'Ingrese la password del Usuario',
                                       'name': 'apiuserpass', 'type': 'password', 'length': '10', 'value': '',
                                       'error': 'Debe ingresarse un valor - Hasta 10 caracteres'},
                'APELLIDONOMBRE'    : {'placeholder': 'Ingrese el Apellido y Nombre',
                                       'name': 'apellidonombre', 'type': 'text', 'length': '150', 'value': '',
                                       'error': 'Debe ingresarse un valor - Hasta 150 caracteres'},

                'APIUSEREMAIL'      : {'placeholder': 'Ingrese el enail del Usuario',
                                       'name': 'apiuseremail', 'type': 'email', 'length': '256', 'value': '',
                                       'error': 'Debe ingresarse un valor - Hasta 256 caracteres'},

                'APIUSERWHATSAPP'   : {'placeholder': 'Ingrese el whatsapp del Usuario',
                                       'name': 'apiuserwhatsapp', 'type': 'tel', 'length': '20', 'value': '',
                                       'error': 'Debe ingresarse un valor - Hasta 20 caracteres'},

                'SLTTIPODOCUMENTO'     : [
                    {
                        'TIPODOCUMENTO'     : {'placeholder': 'Tipo de Documento', 'name': 'tipodocumento',
                                               'value': ''},
                        'DESCTIPODOCUMENTO' : {'placeholder': 'Tipo de Documento Descripcion',
                                               'name': 'desctipodocumento', 'value': ''},
                        'TIPODOCUMENTOID'   : {'hidden': 'on', 'name': 'tipodocumentoid', 'value': ''}
                    }
                ],
                'NUMERODOCUMENTO'   : {'placeholder': 'Ingrese el whatsapp del Usuario',
                                       'name': 'numerodocumento', 'type': 'bigint', 'min': '1', 'max': '18',
                                       'value': '',
                                       'error': 'Debe ingresarse un valor - El valor debe ser numerico'},
                'SLTAPIREGISTROS'      : [
                    {
                        'APIREGISTROSDESCRIPCION'   : {'placeholder': 'Api Registro Descripcion',
                                                       'name': 'apiregistrosdescripcion', 'value': ''},
                        'APIREGISTROSNUMERO'        : {'placeholder': 'Api Registro Numero',
                                                       'name': 'apiregistrosnumero', 'value': ''},
                        'APIREGISTROSID'            : {'hidden': 'on', 'name': 'apiregistroid', 'value': ''}
                    }
                ],
            },
            'btn': [{'name': 'TokenUser', 'link': self.server_http + '/tokenuserwrkhlp/'}]
        }
        return consulta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Api Token
    def apitokenwrkhlp(self, *datos_list):

        consulta = {
            'lista': [
                    {
                        'TOKENAPIID'                : {'hidden': 'on', 'name': 'tokenapiid', 'value': ''},
                        'APIUSERNOMBRE'             : {'placeholder': 'Nombre del Usuario',
                                                       'name': 'apiusernombre', 'value': ''},
                        'APIREGISTROSDESCRIPCION'   : {'placeholder': 'Descripcion del Registro',
                                                       'name': 'apiregistrosdescripcion', 'value': ''},
                        'APIREGISTROSNUMERO'        : {'placeholder': 'Numero del Registro',
                                                       'name': 'apiregistrosnumero', 'value': ''},
                        'TOKENCONECTAR'             : {'placeholder': 'Token utilizado al Conectar',
                                                       'name': 'tokenconectar', 'value': ''},
                        'TOKENINICIOTRANSACCION'    : {'placeholder': 'Inicio de la Transaccion',
                                                       'name': 'tokeniniciotransaccion', 'value': ''},
                        'TOKENFINTRANSACCION'       : {'placeholder': 'Finaliza la transaccion',
                                                       'name': 'tokenfintransaccion', 'value': ''},
                        'btn'                       : [
                                {'name':'modificar', 'link': self.server_http + '/apitokenupdhlp/'},
                                {'name':'nuevo', 'link': self.server_http + '/apitokenaddhlp/'}
                        ]
                    }
            ]
        }
        return self.consultatmp_consulta_wrk(datos_list, **consulta)


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devolucion de datos al front-end de Alta de Api de Token *VERIFICAR EN HELP
    def apitokenaddhlp(self):

        consulta = {
            'add': {
                'SLTAPIUSER'       :[
                    {
                        'APIUSERNOMBRE' : {'placeholder': 'Nombre del Usuario',
                                           'name': 'apiusernombre', 'value': ''},
                        'APIUSERID'     : {'hidden': 'on', 'name': 'apiuserid', 'value': ''}
                    }
                ],
                'SLTAPIREGISTROS'  :[
                    {

                        'APIREGISTROSDESCRIPCION'   : {'placeholder': 'Descripcion del Registro',
                                                       'name': 'apiregistrosdescripcion', 'value': ''},
                        'APIREGISTROSNUMERO'        : {'placeholder': 'Numero del Registro',
                                                       'name': 'apiregistrosnumero', 'value': ''},
                        'APIREGISTROID'             : {'hidden': 'on', 'name': 'apiregistroid', 'value': ''},
                    }
                ],
            },
            'btn': [{'name': 'TokenUser', 'link': self.server_http + '/apitokenwrkhlp/'}]
        }
        return jsonify(**consulta)
