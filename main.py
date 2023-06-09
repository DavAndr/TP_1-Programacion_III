import PyPDF2
from gtts import gTTS
from playsound import playsound

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    full_text = ""
    for no_page in range(len(reader.pages)):
        info_page = reader.pages[no_page]
        extract_info = info_page.extract_text()
        full_text += extract_info + "\n"
    return full_text

def convert_text_to_speech(text):
    tts = gTTS(text, lang="es")
    output_file = "audio.mp3"
    tts.save(output_file)
    return output_file

def play_audio_file(audio_file):
    playsound(audio_file)

while True:
    print("=== Programa de Lectura de PDF ===")
    print("1. Ingresar un archivo PDF")
    print("2. Escuchar el PDF")
    print("3. Cerrar el programa")
    choice = input("Ingrese su opción: \n")

    if choice == "1":
        pdf_file = input("Ingrese el nombre del archivo PDF: ")
        try:
            extracted_text = extract_text_from_pdf(pdf_file + ".pdf")
            print("Texto extraído del PDF exitosamente.")
        except:
            print("Error al procesar el archivo PDF.")

    elif choice == "2":
        try:
            audio_file = convert_text_to_speech(extracted_text)
            play_audio_file(audio_file)
        except NameError:
            print("No se ha ingresado ningún archivo PDF o se ha extraído el texto.")

    elif choice == "3":
        print("Programa cerrado.")
        break

    else:
        print("Opción inválida. Por favor, elija una opción válida.")
