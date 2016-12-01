import Root
import webbrowser
import os


def main():
    comuna = Root.MenuPorConsola.obtener_numero_comuna()
    negocio = Root.LectorCSV.obtener_informacion_negocio(comuna)
    if negocio == None:
        print("Ocurrio un error, intente de nuevo")
        return
    informacion_comuna = Root.LectorCSV.obtener_multipoligono_comuna(comuna)
    Root.CreadorHTML.crear_html(negocio, informacion_comuna)
    webbrowser.open_new(os.path.join(os.path.dirname(__file__), "Files", "Temporal.html"))



run = True

while run:
    main()
    run = Root.MenuPorConsola.repetir() == 1
