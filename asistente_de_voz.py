import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
from carpeta_contactos import contacto
from hablar_voz import Voz_asistente
from comandos import Comandos
from youtube import Youtube
from buscadores import Buscador

comand = Comandos()
carp = contacto()
voz = Voz_asistente()
yt = Youtube()
wiki = Buscador()


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

    voz.hablar(f'Hoy es {calendario[dia_semana]}')


# Informar la hora
def pedir_hora():
    hora = datetime.datetime.now()
    voz.hablar(f"La hora actual es {hora.hour} horas y {hora.minute} minutos con {hora.second} segundos")


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
    voz.hablar(f"{momento}, mi nombre es Ecko, tu asistente personal, ¿En que puedo ayudarte?")


def pedir_cosas():
    saludo_inicial()

    # Variable de corte
    comenzar = True

    # Loop central
    while comenzar:
        # Activar micro y guardar el pedido en un string
        pedido = voz.transfromar_audio_en_texto().lower()
        pedido_avanzado = comand.identificar_comando(pedido.split())

        # Esta funcion es para repeti
        if 'ecko' in pedido:
            r = sr.Recognizer()
            voz.hablar("Reiniciando")
            r.pause_threshold = 0.8
            saludo_inicial()
            continue

        # Abrir youtube
        if 'youtube' in pedido:
            yt.abrir_youtube(pedido)
            if comand.comandos_busqueda and 'youtube' in pedido:
                voz.hablar("Buscando")
                yt.busqueda_youtube(pedido)
            continue


        # Abrir navegador
        elif 'abrir navegador' in pedido:
            voz.hablar('Enseguida se abrira tu navegador')
            webbrowser.open('https://www.google.com')
            voz.confirmacion()
            continue

        # Dia
        elif 'qué día es hoy' in pedido:
            voz.hablar("Enseguida")
            pedir_dia()
            voz.confirmacion()
            continue

        # Hora
        elif 'qué hora es' in pedido:
            voz.hablar("Por supuesto")
            pedir_hora()
            voz.confirmacion()
            continue

        # Busqueda en wikipedia
        elif 'wikipedia' in pedido:
            wiki.busqueda_wikipedia(pedido)

        # Busqueda en internet
        elif 'google' or 'escolar' or 'ciencia mundial' in pedido:
            wiki.abrir_busqueda(pedido)
            pass

            # Busqueda en internet
        elif 'busca en internet' in pedido:
            voz.hablar("Ya mismo estoy en eso")
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            voz.hablar("He encontrado lo siguiente")
            voz.confirmacion()
            continue

        # Break en el proyecto
        elif pedido in comand.comandos_shutdown:
            voz.hablar("Un placer, hasta luego")
            break

        # Mandar mensaje de whatsapp a un contacto
        elif 'manda' and 'mensaje' and 'whatsapp' in pedido:
            voz.hablar("Indicame numero por numero el contacto a quien deseas mandarle un mensaje")
            peticion_numero = voz.transfromar_audio_en_texto()
            peticion_numero_conversion = "+52" + peticion_numero
            voz.hablar("¿Cual sera el contenido del mensaje?")
            mensaje = voz.transfromar_audio_en_texto()

            pywhatkit.sendwhatmsg_instantly(peticion_numero_conversion, mensaje)
            voz.hablar("El mensaje ha sido enviado")
            voz.confirmacion()
            continue


        # Mandar mensaje de whatsapp a un grupo
        elif 'manda' and 'mensaje' and 'grupo' in pedido:
            voz.hablar("Por supuesto, ¿Cual es el nombre dle grupo?")
            nombre_grupo = voz.transfromar_audio_en_texto()
            voz.hablar("¿Cual sera el contenido del mensaje?")
            contenido = voz.transfromar_audio_en_texto()

            pywhatkit.sendwhatmsg_to_group_instantly(nombre_grupo, contenido)
            voz.hablar("El mensaje ha sido enviado")
            voz.confirmacion()
            continue

        elif 'agregar contacto' in pedido:
            """hablar("Claro, ¿Cual sera el nombre del contacto?")
            nombre = transfromar_audio_en_texto()
            hablar("¿Cual es el numero del contacto?")
            numero = transfromar_audio_en_texto()

            carp.contactos[nombre] = numero"""
            carp.agregar_contacto()

        elif 'eliminar contacto' in pedido:
            carp.eliminar_contacto()

        elif 'mostrar contactos' in pedido:
            carp.mostrar_contactos()


pedir_cosas()
