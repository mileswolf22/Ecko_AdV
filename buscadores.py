from comandos import Comandos
from hablar_voz import Voz_asistente
import webbrowser
import wikipedia

voz = Voz_asistente()
com = Comandos()


class Buscador:

    @staticmethod
    def busqueda_wikipedia(pedido):
        lista_peticion = pedido.split()
        resultado_comando, resultado_pagina = com.identificar_comando(lista_peticion)

        voz.hablar("Un momento")
        if resultado_comando in com.comandos_busqueda:
            if resultado_pagina == "wikipedia" or resultado_pagina == "Wikipedia":
                peticion_result = com.eliminar_palabras(pedido, resultado_pagina)
                if peticion_result == "":
                    voz.hablar("Debes indicar cual sera tu busqueda, intenta nuevamente")
                else:
                    wikipedia.set_lang('es')  # Establece el lenguaje para buscar en español
                    resultado = wikipedia.summary(peticion_result, sentences=1)
                    voz.hablar("He encontrado lo siguiente")
                    voz.hablar(resultado)
                    voz.hablar("¿Quieres que abra esta información en internet? Responde si o no")
                    confirmar_peticion = voz.transfromar_audio_en_texto()

                    if confirmar_peticion == 'si' or confirmar_peticion == 'Si':
                        voz.hablar("Enseguida")
                        webbrowser.open(f"https://en.wikipedia.org/wiki/{peticion_result}")
                    elif confirmar_peticion == 'no' or confirmar_peticion == 'No':
                        voz.hablar("Entendido")

                voz.confirmacion()
        elif resultado_comando in com.comandos_apertura:
            if resultado_pagina == 'wikipedia' or resultado_pagina == 'Wikipedia':
                voz.hablar("Abriendo wikipedia")
                webbrowser.open(com.comandos_apertura_buscadores[resultado_pagina])
                voz.hablar("¿En que mas puedo ayudarte?")

    @staticmethod
    def abrir_busqueda(pedido):
        lista_peticion = pedido.split()
        resultado_comando, resultado_pagina = com.identificar_comando(lista_peticion)

        voz.hablar("Un momento")
        if resultado_comando in com.comandos_busqueda:
            if resultado_pagina in  com.comandos_apertura_buscadores:
                peticion_result = com.eliminar_palabras(pedido, resultado_pagina)
                if peticion_result == "":
                    voz.hablar("Debes indicar cual sera tu busqueda, intenta nuevamente")
                else:
                    if resultado_pagina == 'google':
                        webbrowser.open(f"{com.comandos_apertura_buscadores[resultado_pagina]}"+f"{peticion_result}")
                    elif resultado_pagina == 'escolar':
                        webbrowser.open(f"{com.comandos_apertura_buscadores[resultado_pagina]}"+f"{peticion_result}")
                    elif resultado_pagina == "ciencia mundial":
                        webbrowser.open(f"{com.comandos_apertura_buscadores[resultado_pagina]}" + f"{peticion_result}")
                    pass

        pass