import PyPDF2
import pyttsx3


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
