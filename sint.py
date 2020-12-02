import pyttsx3
import time
speak = pyttsx3.init()
while True:
    phrase = input('Entre com o texto:')
    ph = phrase.split(" ")
    ph2 = phrase.split(",")
    separador = int(input("Quantas palavras por vez? "))
    seg = float(input("Quantos segundos de espera: "))
    while True:
        frase = ph[0:separador]
        if frase != []:
            speak.runAndWait()
            speak.say(frase)
            speak.runAndWait()
            time.sleep(seg)
            try:
                for i in range(separador):
                    del(ph[0])
            except:
                break