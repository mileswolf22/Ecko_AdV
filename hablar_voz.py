import re

import pyttsx3
import speech_recognition as sr


# Escuchar nuestro microfono y devolver el audio aparte

class Voz_asistente:

    @staticmethod
    def transfromar_audio_en_texto():
        # Almacenar el recognizer en una variable
        r = sr.Recognizer()
        # Configurar el microfono
        with sr.Microphone() as origen:
            # Tiempo de espera
            r.pause_threshold = 0.8

            # Informar que comenzo la grabacion
            print("Ya puedes hablar")

            # Guardar lo que escuche como audio
            audio = r.listen(origen)

            try:
                # Buscar en google
                pedido = r.recognize_google(audio, language="es-mx")

                # Prueba de ingreso
                print("Dijiste: " + pedido)
                return pedido

            except sr.UnknownValueError:

                print("Ups, no entendi")
                return "Sigo esperando"
            # En caso de no poder resovler el pedido
            except sr.RequestError:
                print("Ups, no hay servicio")
                return "Sigo esperando"
            # Error inesperado
            except:
                print("Ups, algo ha salido mal")
                return "Sigo esperando"

    # Funcion para qu eel asistente pueda ser escuchado
    @staticmethod
    def hablar(mensaje):
        # Encender el motor de pyttsx3h
        engine = pyttsx3.init()

        # Pronunciar el mensaje
        engine.say(mensaje)
        engine.runAndWait()

    def confirmacion(self):
        r = sr.Recognizer()
        r.pause_threshold = 1
        self.hablar("¿En que mas puedo apoyarte?")
