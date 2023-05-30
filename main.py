from gtts import gTTS
import os

text = "hola mamamamaammamama"

lenguage = "es-us"

speech = gTTS(text = text, lang = lenguage, slow = False)

speech.save("prueba1.mp3")

os.system("start texto.mp3")