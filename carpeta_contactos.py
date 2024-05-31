import os.path

from hablar_voz import Voz_asistente
asis = Voz_asistente()
from os import system
from pathlib import Path

contactos = {

}
ruta_carpeta = Path("C:/Users/bryan.nava/PycharmProjects/pythonProjects")
class contacto:

    contactos = {}

    @staticmethod
    def agregar_contacto():
        existe = False

        while not existe:
            global ruta_carpeta
            asis.hablar("Vamos a agregar un contacto")
            asis.hablar("¿Cual sera el nombre del contacto?")
            nombre = asis.transfromar_audio_en_texto()
            asis.hablar("¿Cual es el numero del contacto?")
            numero = asis.transfromar_audio_en_texto()

            ruta_nueva = Path(ruta_carpeta, "Contactos.txt")

            contactos[nombre] = numero
            contacto_nuevo = contactos[nombre]

            if not os.path.exists(ruta_nueva):
                Path.write_text(ruta_nueva, contacto_nuevo)
                existe = True
            else:
                asis.hablar("Este contacto ya existe")

    @staticmethod
    def eliminar_contacto():
        asis.hablar("Procederemos, ¿Cual es el nombre del contacto que deseas borrar?")
        nombre = asis.transfromar_audio_en_texto()

        if nombre in contactos:
            asis.hablar("Contacto encontrado ¿Estas seguro de eliminar?")
            confirmacion = asis.transfromar_audio_en_texto()
            if confirmacion == "si":
                contactos.pop(confirmacion)
                asis.hablar("Contacto Eliminado")
                asis.confirmacion()
            else:
                asis.hablar("Operacion cancelada")
                asis.confirmacion()

    @staticmethod
    def mostrar_contactos():
        if not contactos:
            asis.hablar("Lista de contactos vacia")
        else:
            asis.hablar("Estos son tus contactos")
            for elementos in contactos:
                print(elementos)


