from comandos import Comandos
from hablar_voz import Voz_asistente
import webbrowser
import pywhatkit

voz = Voz_asistente()
com = Comandos()


class Youtube:

    @staticmethod
    def abrir_youtube(pedido):
        lista_peticion = pedido.split()
        resultado_comando, resultado_pagina = com.identificar_comando(lista_peticion)

        if resultado_comando in com.comandos_apertura:
            voz.hablar(f"Abriendo {resultado_pagina}")
            webbrowser.open(com.comandos_apertura_redes_sociales[resultado_pagina])

        elif resultado_comando in com.comandos_reproduccion:
            if resultado_pagina == "youtube" or resultado_pagina == "YouTube":
                peticion_result = com.eliminar_palabras_youtube(pedido)
                pywhatkit.playonyt(peticion_result)
                voz.hablar(f"Reproduciendo {peticion_result}")

    @staticmethod
    def busqueda_youtube(pedido):
        lista_peticion = pedido.split()
        resultado_comando, resultado_pagina = com.identificar_comando(lista_peticion)
        if resultado_comando in com.comandos_busqueda:
            if resultado_pagina == "youtube" or resultado_pagina == "YouTube":
                peticion_result = com.eliminar_palabras_youtube(pedido)
                search_url = f"https://www.youtube.com/results?search_query={peticion_result.replace(' ', '+')}"
                voz.hablar(f"Buscando en YouTube: {peticion_result}")
                webbrowser.open(search_url)
            else:
                voz.hablar("Ningun resultado coincide con tu peticion")



