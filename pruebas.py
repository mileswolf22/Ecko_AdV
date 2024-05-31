import webbrowser

import pywhatkit

from comandos import Comandos
from hablar_voz import Voz_asistente
voz = Voz_asistente()
com = Comandos()

voz.hablar("¿Cual es tu peticion?")
peticion = voz.transfromar_audio_en_texto()
lista_peticion = peticion.split()
resultado_comando, resultado_pagina = com.identificar_comando(lista_peticion)

if resultado_comando in com.comandos_apertura:
    voz.hablar(f"Abriendo {resultado_pagina}")
    webbrowser.open(com.comandos_apertura_redes_sociales[resultado_pagina])

elif resultado_comando in com.comandos_agregar:
    voz.hablar("Comando agregar")

elif resultado_comando in com.comandos_reproduccion:
    if resultado_pagina == "youtube":
        peticion_result = com.eliminar_palabras(peticion)
        pywhatkit.playonyt(peticion_result)
