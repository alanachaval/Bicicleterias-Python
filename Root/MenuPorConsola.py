from Tools.scripts.treesync import raw_input


def obtener_numero_comuna():
    """Devuelve a que número de comuna se quiere acceder"""
    comuna = None
    input_invalido = True
    while input_invalido:
        try:
            comuna = " " + raw_input("Inserte número de Comuna :\n")
            input_invalido = not (0 < int(comuna) < 16)
        except:
            pass
        finally:
            if input_invalido:
                print("Debe ingresar un numero entre: 1 y 15")
    return comuna


def obtener_numero_negocio(lista_negocios):
    """Devuelve a que posicion en la lista de Bicicleterias se quiere acceder

    recibe una lista de tuplas de bicicleterias (nombre, direccion)
    """
    if len(lista_negocios) == 0:
        print("No hay bicileterias registradas en esta comuna")
        return None
    numero_negocio = None
    input_invalido = True
    while input_invalido:
        print()
        for i in range(0, len(lista_negocios)):
            print(str(i + 1) + (3 - len(str(i + 1))) * " " + lista_negocios[i][0] + (
                40 - len(lista_negocios[i][0])) * " " + lista_negocios[i][1])
        print()
        try:
            numero_negocio = raw_input("Inserte número de bicicleteria :\n")
            input_invalido = (1 > int(numero_negocio)) or int(numero_negocio) > (len(lista_negocios))
        except:
            pass
        finally:
            if input_invalido:
                print("Ingrese un numero entre: 1 y " + str(len(lista_negocios)))
    return numero_negocio

def repetir():
    """1 para realizar otra busqueda o 2 para cerrar"""
    while True:
        try:
            respuesta = int(raw_input(" \n 1 Para realizar otra busqueda \n 2 Para salir \n"))
            if respuesta == 1 or respuesta == 2:
                return respuesta
        except:
            pass
