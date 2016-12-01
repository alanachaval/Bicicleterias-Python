import os


def crear_html(negocio, informacion_comuna):
    """Devuelve la ruta del HTML creado
    crea el mapa en HTML utilizando Google Maps Embed API
    el mapa contiene la posicion, el nombre y el horario de atencion del negocio y el contorno de la comuna
    """
    texto = ""
    negocio = negocio.split(";")
    posision_negocio = "{lat:" + negocio[0][7:-1].split(" ")[1] + ", lng: " + negocio[0][7:-1].split(" ")[0] + "}"
    a_remplazar = [negocio[2], posision_negocio, posision_negocio, negocio[2], negocio[2], negocio[3], negocio[8],
                   informacion_comuna[0], negocio[13][:-1], informacion_comuna[1]]
    i = 0
    for line in open(os.getcwd() + "\Files\Mapa.html"):
        if "REPLACE" in line:
            texto += (line.replace("REPLACE", a_remplazar[i]))
            i = (i + 1)
        else:
            texto += line + "\n"
    html = open(os.path.join(os.path.dirname(__file__), "..", "Files", "Temporal.html"), "w")
    html.write(texto)
    html.close()
