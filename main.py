__author__ = "Jelle de Wolf"
__credits__ = ["Jelle de Wolf"]
__version__ = "1.0.0"
__maintainer__ = "Jelle de Wolf"
__email__ = "wolfjj@hva.nl"
__status__ = "Production"
"""Goal of the program:

The goal of this simple program is to allow the user to convert either a PDF/TXT file and then,
save the converted file to the downloads folder.

The user us also able to listen to the converted file.
"""
import os
import random
import sys

import functions

exit_message: str = "Thanks for using the converter!"

converted_files_list = []


def convert_another_file():
    another_file = input("Would you like to convert another file?")
    if another_file == 'no'.lower():
        print("Thanks for using the converter!")
        sys.exit()
    if another_file == 'yes'.lower():
        # return the user to the start of the loop
        start()
    else:
        print("Please enter 'yes' or 'no'!")
        convert_another_file()


def listen_to_converted_file(text_to_convert):
    user_response = input("Would you like to listen to the converted file?")
    if user_response == 'yes'.lower():
        functions.return_text_to_speech(text_to_convert)
        convert_another_file()
    if user_response == 'no'.lower():
        convert_another_file()
    else:
        print("Did not recognize input value")
        listen_to_converted_file(text_to_convert)


def start():
    while True:
        random_int: int = random.randint(0, 200)
        file_name = "converted_pdf_file" + str(random_int) + ".mp3"
        converted_files_list.append(file_name)
        selected_type = input("Which file type would you like to convert? Choose between PDF or TXT")
        user_file_path: str = input("Please enter path name in the following format: directory\\file_name")
        file_to_read: str = os.path.expanduser('~') + "\\" + user_file_path
        if not functions.open_file(file_to_read):
            start()
        save_file_bool = input("Would you like to save the converted file?")
        if not save_file_bool == 'yes'.lower():
            print(exit_message)
            sys.exit()
        if selected_type == 'TXT'.lower():
            text_to_convert = functions.convert_from_text(file_to_read)
        else:
            text_to_convert = functions.convert_from_pdf(file_to_read)
        functions.save_converted_file(text_to_convert, file_name)
        print(converted_files_list)
        listen_to_converted_file(text_to_convert)


start()
