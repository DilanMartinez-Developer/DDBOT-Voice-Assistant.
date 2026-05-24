from utilidades.hablar import hablar
import utilidades.Comandos as texts
import subprocess
import webbrowser
def ejecutarIA(respuesta):

    tipo = respuesta.get("tipo")

    if tipo == "respuesta":

        hablar(
            respuesta.get(
                "contenido",
                "No tengo respuesta"
            )
        )
        return

    if tipo == "acciones":

        acciones = respuesta.get(
            "acciones",
            []
        )

        for item in acciones:

            accion = item.get(
                "accion",
                ""
            ).lower()

            parametro = str(
                item.get(
                    "parametros",
                    ""
                )
            ).lower()

            print(
                accion,
                parametro
            )

            if accion == "abrir_aplicacion":

                if parametro in texts.OPEN_ROOTS:

                    hablar(
                        "abriendo " + parametro
                    )

                    texts.OPEN_ROOTS[parametro]()

                else:

                    hablar(
                        "no conozco " + parametro
                    )
              
            elif accion == "buscar_google":
                hablar(
                    "Buscando " + parametro + " en google"
                )
                webbrowser.open("https://www.google.com/search?q=" + parametro)
            
            elif accion == "buscar_youtube":
                hablar(
                    "abriendo " + parametro +" en youtube"
                )
                webbrowser.open("https://www.youtube.com/results?search_query=" + parametro)           

            elif accion == "abrir_carpeta":
                if parametro in texts.CARPETAS_ROOTS:
                    hablar(
                        "abriendo la carpeta " + parametro
                    )

                    ruta = "C:\\Users\\galos\\" + texts.CARPETAS_ROOTS[parametro]

                    subprocess.run(["cmd", "/c", "start", "",ruta])

                else:

                    hablar(
                        "no conozco " + parametro
                    )

            elif accion == "cerrar_IA":
                exit
            else:
                hablar(
                    "No se que accion es esa"
                ) 
                print(accion)
            
    