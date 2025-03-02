import pywhatkit
from hablar_voz import Voz_asistente

voz = Voz_asistente()


class Comandos:
    comandos_agregar = [
        "añadir",
        "añade",
        "añadas"
        "añademe",
        "registra",
        "registrar",
        "registrame"
        "agregar",
        "agrega"
    ]

    comandos_apertura = [
        "abrir",
        "abre",
        "ejecuta",
        "ábreme",
        "muestra",
        "muéstrame",
        "abras",
    ]

    comandos_reproduccion = [
        # comandos de reproduccion para youtube
        "reproduce",
        "ponme",
        "pongas",
        "reproduzcas",
        "reproducir",
        "poner"
    ]

    comandos_busqueda = [
        "buscar",
        "busca",
        "busques",
        "búscame",
        "investiga",
        "investigues",
        "investígame",
        "revisa",
        "revisar",
        "revísame"
        "Buscar",
        "Busca",
        "Busques",
        "Búscame",
        "Investiga",
        "Investigues",
        "Investígame",
        "Revisa",
        "Revisar",
        "Revísame"
    ]

    comandos_apertura_redes_sociales = {
        "youtube": "https://www.youtube.com/",
        "YouTube": "https://www.youtube.com/",
        "x": "https://x.com/",
        "ekis": "https://x.com/",
        "equis": "https://x.com/",
        "tweeter": "https://x.com/",
        "X": "https://x.com/",
        "facebook": "https://www.facebook.com/",
        "Facebook": "https://www.facebook.com/",
    }

    comandos_apertura_buscadores = {
        "google": "https://www.google.com/",
        "wikipedia": "https://https://en.wikipedia.org/wiki/",
        "google escolar": "https://scholar.google.com/",
        "ciencia mundial": "https://worldwidescience.org/"
    }

    comandos_apertura_redes_videojuegos = {
        "vandal": "https://www.vandal.elespanol.com"
    }

    comandos_shutdown = [
        "sería todo",
        "apágate",
        "es todo",
        "nada mas"
    ]

    # Primero verificar cuales son los comandos que el usuario dijo
    def identificar_comando(self, lista):
        comando_ = ""
        pagina = ""
        # Variable para saber si encontramos un comando válido

        for elemento in lista:
            if elemento in self.comandos_apertura:
                comando_ = elemento
            elif elemento in self.comandos_reproduccion:
                comando_ = elemento
            elif elemento in self.comandos_agregar:
                comando_ = elemento
            elif elemento in self.comandos_apertura_redes_sociales:
                pagina = elemento
            elif elemento in self.comandos_busqueda:
                comando_ = elemento
            elif elemento in self.comandos_apertura_buscadores:
                pagina = elemento

        # Comandos identificados
        return comando_, pagina

    @staticmethod
    def eliminar_palabras_youtube(peticion):
        # Dividir la cadena en dos partes usando "youtube" como separador
        pedido = peticion.lower()
        partes = pedido.split("youtube", 1)

        # Verificar si "youtube" fue encontrado y reconstruir la cadena a partir de la segunda parte
        if len(partes) > 1:
            nueva_peticion = partes[1].strip()  # Eliminar espacios en blanco iniciales y finales
        else:
            nueva_peticion = peticion  # Si "youtube" no está en la cadena, no hacemos nada

        return nueva_peticion

    @staticmethod
    def eliminar_palabras(peticion, pagina):
        # Dividir la cadena en dos partes usando "youtube" como separador
        pedido = peticion.lower()
        partes = pedido.split(pagina, 1)

        # Verificar si "youtube" fue encontrado y reconstruir la cadena a partir de la segunda parte
        if len(partes) > 1:
            nueva_peticion = partes[1].strip()  # Eliminar espacios en blanco iniciales y finales
        else:
            nueva_peticion = peticion  # Si "pagina" no está en la cadena, no hacemos nada

        return nueva_peticion


""" peticion = "Te solicito que me reproduzcas en youtube army of stone de windrose"

    # Recuperar los comandos
    comandos_peticion = identificar_comando(peticion.split())

    if comandos_peticion[0] in comandos_reproduccion and comandos_peticion[1] == 'youtube':
        peticion_result = eliminar_palabras(peticion)
        pywhatkit.playonyt(peticion_result)"""
