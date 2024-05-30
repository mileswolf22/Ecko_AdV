import re

import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# Escuchar nuestro microfono y devolver el audio aparte
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
def hablar(mensaje):
    # Encender el motor de pyttsx3
    engine = pyttsx3.init()

    # Pronunciar el mensaje
    engine.say(mensaje)
    engine.runAndWait()

def confirmacion():
    r = sr.Recognizer()
    r.pause_threshold = 1
    hablar("Listo ¿En que mas puedo apoyarte?")


# Informar el dia de la semana
def pedir_dia():
    # Crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # Crear variable para el dia de la semana
    dia_semana = dia.weekday()


    # Dioccionario con nombres de dias
    calendario = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miercoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sabado',
        6: 'Domingo'
    }

    hablar(f'Hoy es {calendario[dia_semana]}')

# Informar la hora
def pedir_hora():
    hora = datetime.datetime.now()
    hablar(f"La hora actual es {hora.hour} horas y {hora.minute} minutos con {hora.second} segundos")

comandos_shutdown = [
    "sería todo",
    "apágate",
    "es todo",
    "nada mas"
]

# Saludo inicial
def saludo_inicial():

    # Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buenos dias'
    else:
        momento = 'Buenas tardes'
    # Decir saludo
    hablar(f"{momento}, mi nombre es Ecko, tu asistente personal, ¿En que puedo ayudarte?")


def pedir_cosas():
    saludo_inicial()

    # Variable de corte
    comenzar = True

    # Loop central
    while comenzar:
        # Activar micro y guardar el pedido en un string
        pedido = transfromar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Abriendo Yutub, un momento')
            webbrowser.open('https://www.youtube.com')
            confirmacion()
            continue
        elif 'abrir navegador' in pedido:
            hablar('Enseguida se abrira tu navegador')
            webbrowser.open('https://www.google.com')
            confirmacion()
            continue
        elif 'qué día es hoy' in pedido:
            hablar("Enseguida")
            pedir_dia()
            confirmacion()
            continue
        elif 'qué hora es' in pedido:
            hablar("Por supuesto")
            pedir_hora()
            confirmacion()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar("Un momento, buscare tu informacion")
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es') # Establece el lenguaje para buscar en español
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("He encontrado lo siguiente")
            hablar(resultado)
            hablar("¿Quieres que abra esta información en internet?")
            confirmar_peticion = transfromar_audio_en_texto()
            if "si" or "por favor" in confirmar_peticion:
                hablar("Enseguida")
                webbrowser.open(f"https://en.wikipedia.org/wiki/{pedido}")
            elif "no" in confirmar_peticion:
                hablar("Entendido ¿En que mas puedo ayudarte?")

            confirmacion()
        elif 'busca en internet' in pedido:
            hablar("Ya mismo estoy en eso")
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar("He encontrado lo siguiente")
            confirmacion()
            continue

        # Break en el proyecto
        elif pedido in comandos_shutdown:
            hablar("Un placer, hasta luego")
            break








pedir_cosas()






