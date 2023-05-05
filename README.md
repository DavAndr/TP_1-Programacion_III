# Programacion III: Trabajo practico 1

Primer trabajo practico de Programacion 3 hecho por Andrada David, Martinez Gonzalo y Tempesti Mateo.

Este trabajo aplicara y explicara el funcionamiento de las siguientes librerias:

---
>## PyPDF2
>Libreria que permite la importacion de texto desde archvos PDF.
>### **Instalación:**
>Se puede instalar PyPDF usando pip
>```console
>$ pip install PyPDF2
>```
>o se puede instalar una version que permite trabajar con cifrado AES
>```console
>$ pip install PyPDF2[crypto]
>```
>### **Uso:**
>Este seria un ejemplo del uso de PyPDF2:
>```python
>from PyPDF2 import PdfReader #Importa la libreria
>
>reader = PdfReader("example.pdf") #se abre un archivo PDF
>number_of_pages = len(reader.pages) #Se determina el numero de paginas
>page = reader.pages[0] #Se guarda los datos de la pagina 0
>text = page.extract_text() #Se extrae el texto de la pagina 0
>```
>
---
>## gTTS API
>Google Text-To-Speech (gTTS) permite implementar funciones Text-To-Speech, es decir, crear narraciones basadas en un texto.
>### **Instalación:**
>```console
>$ pip install gTTS
>```
>### **Uso desde consola:**
>Se puede utilizar gTTS desde la consola con el comando `gTTS-cli`. Un ejemplo seria:
>```console
>$ gtts-cli 'hello' --output hello.mp3
>```
>### **Uso desde python:**
>Este seria un ejemplo del uso de gTTS desde python:
>```python
> from gtts import gTTS #Importa la libreria
> tts = gTTS('hello') #Se crea una nueva narracion con un string 'hello' de base 
> tts.save('hello.mp3') #Se guarda como archivo la narracion
>```