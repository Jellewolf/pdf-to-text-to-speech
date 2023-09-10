import os
import random

import PyPDF2
import pyttsx3
from gtts import gTTS


def return_text_to_speech(text_input):
    # reading the text
    speak = pyttsx3.init()
    speak.say(text_input)
    speak.runAndWait()


def open_file_path(file_input_path):
    new_path = open(file_input_path, 'rb')
    return new_path


def read_file(file_to_read: str):
    pdf_reader = PyPDF2.PdfReader(file_to_read)
    # the page with which you want to start
    from_page = pdf_reader.pages[0]
    text = from_page.extract_text()
    return text


def save_converted_file(text_to_convert):
    # determine the path where the converted file should be saved to
    save_path: str = os.path.expanduser('~') + "\\Downloads\\"
    language: str = 'en'
    random_int: int = random.randint(0, 200)
    file_name = "converted_pdf_file" + str(random_int) + ".mp3"

    # convert the file into a TTS file
    converted_file = gTTS(text=text_to_convert, lang=language, slow=False)

    # save the file in the set path with the set name
    converted_file.save(save_path + file_name)
    print("File has been saved in: " + save_path + " as: " + file_name)
