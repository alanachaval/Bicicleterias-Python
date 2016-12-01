import os
import Root.MenuPorConsola


def obtener_informacion_negocio(comuna):
    """Devuelve la linea del negocio especificado del csv"""
    lista_negocios = []
    archivo = open(os.getcwd() + "\Files\Bicicleterias.csv", "r")
    archivo.readline()
    for line in archivo:
        line = line.split(";")
        if line[13].endswith(comuna):
            lista_negocios.append((line[2], line[3]))
    posicion = Root.MenuPorConsola.obtener_numero_negocio(lista_negocios)
    if posicion == None:
        return None
    negocio_seleccionado = lista_negocios[int(posicion) - 1]
    negocio = None
    for line in open(os.getcwd() + "\Files\Bicicleterias.csv", "r").readlines():
        if line.split(";")[2] == negocio_seleccionado[0] and line.split(";")[3] == negocio_seleccionado[1]:
            negocio = line
    return negocio


def obtener_multipoligono_comuna(comuna):
    """Devuelve el multipoligono de la comuna especificada
    devuelve cada punto en cooredenadas latitud y longitud
    Elementos {lat: XX.XXXXXXXXXXXXXX, lng: XX.XXXXXXXXXXXXXXX}
    separados por una ,
    """
    multipoligono = ""
    barrios = ""
    for line in open(os.getcwd() + "\Files\Comunas.csv", "r"):
        if line.endswith("," + comuna[1:]):
            barrios = line.split('"')[2].split(",")[1]
            multipolygon = line[17:].split(")))")[0]
            for coord in multipolygon.split(","):
                multipoligono += ("     {lat: " + coord.split(" ")[1] + ", lng: " + coord.split(" ")[0] + "},\n")
            multipoligono = multipoligono[:-2] + "\n"
    return multipoligono, barrios


def obtener_posicion_negocio(nombre_negocio, path):
    """Devuelve la posicion del negocio especificado
    Ejemplo {lat: XX.XXXXXXXXXXXXXX, lng: XX.XXXXXXXXXXXXXXX}
    """
    posicion_negocio = ""
    for line in open(path, "r"):
        line = line.split(";")
        if line[2] == nombre_negocio:
            posicion_negocio = "     {lat: " + line[0][7:-1].split(" ")[1] + ", lng: " + \
                               line[0][7:-1].split(" ")[0] + "}"
    return posicion_negocio
