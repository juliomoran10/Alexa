import pyttsx3 as voz
import speech_recognition as sr
import subprocess as sub
from datetime import datetime
from datetime import date


# Configuracion de voz
voice=voz.init()
voices=voice.getProperty('voices')
voice.setProperty('voice',voices[0].id)
voice.setProperty('rate',140)

def say (text):
    voice.say(text)
    voice.runAndWait()

while True:
    recognizer=sr.Recognizer()
#Activar microfono
    with sr.Microphone() as source:
        print('Escuchando...')
        audio=recognizer.listen(source, phrase_time_limit=3)

    try:
        comando=recognizer.recognize_google(audio, language='es-ES')
        print(f'Creo que dijiste "{comando}"')

        comando=comando.lower()
        comando=comando.split(' ')

        if 'alexa' in comando:
             
             if 'abre' in comando or 'abrir' in comando:
                 
                 sites={
                     'google':'google.com',
                     'youtube':'youtube.com',
                     'tiktok':'tiktok.com',
                     'twitch':'twitch.com',
                     'educa':'uru.insiemp.com',
                     'netflix':'netflix.com',
                     'whatsapp':'web.whatsapp.com'
                 }

                 for i in list(sites.keys()):
                     if i in comando:
                         sub.call(f'start chrome.exe {sites[i]}', shell=True)
                         say(f'Abriendo {i}')

        elif 'hora' in comando:
            time=datetime.now().strftime('%H:%M')
            say(f'Son las {time}')

        elif 'dia' in comando:
            day=datetime.today().ctime('Dia: %d , Mes: %m, Año: %Y')
            say(f'hoy es {day}')

        for i in ['cómo estas', 'como estas']:
            if i  in comando:
                say('Estoy bien gracias')

        for i in ['Adios']:
            if i  in comando:
                say('Sesion finalizada')
                break
    except:#Sino entiende esta sera la respuesta
        print('No entendi, vuelve a intentarlo')







  

            
