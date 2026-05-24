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

            if accion in TOOLS:

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

            else:

                hablar(
                    "accion desconocida"
                )

                print(
                    accion
                )