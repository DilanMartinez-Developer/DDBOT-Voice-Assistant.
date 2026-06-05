from utilidades.hablar import hablar
from UtilidadesConIA.herramientas import TOOLS

def ejecutarIA(respuesta):

    tipo = respuesta.get(
        "tipo"
    )

    if tipo == "respuesta":

        hablar(
            respuesta.get(
                "contenido",
                "no tengo respuesta"
            )
        )
        print("la respuesta fue",respuesta)
        return

    if tipo == "acciones":

        acciones = respuesta.get(
            "acciones",
            []
        )
        print("json : ",acciones)
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
                "Ejecutando:", accion, "| Parametro:", parametro
            )

            if accion in TOOLS:
                
                try:
                    if accion == "activar_ventana":

                        ok = TOOLS[
                            accion
                        ](
                            parametro
                        )

                        if not ok and parametro in TOOLS:
                            TOOLS["abrir_aplicacion"](parametro)

                    else:

                        TOOLS[
                            accion
                        ](
                            parametro
                        )
                        
                except Exception as e:
                    print(f"Error crítico en la herramienta '{accion}': {e}")
                    hablar("Ups, algo falló al ejecutar esa acción")

            else:

                hablar(
                    "accion desconocida"
                )

                print(
                    "No mapeado:", accion
                )