import os
import random

from gtts import gTTS

import functions


def start():
    while True:
        list_of_converted_files = []
        print("List of converted files: ")
        print(*list_of_converted_files, sep="\n")
        user_file_path: str = input("Please enter path name in the following format: directory\\file_name")
        # get the path where the file is located
        file_path: str = os.path.expanduser('~') + "\\" + user_file_path

        # convert and save the file
        def save_converted_file():
            save_file_bool = input("Would you like to save the converted file?")
            if save_file_bool in ["Yes", "yes"]:
                file_to_convert = functions.open_file_path(file_path)
                text_to_convert = functions.read_file(file_to_convert)
                random_int: int = random.randint(0, 200)
                # set the file name variable
                file_name = "converted_pdf_file" + str(random_int) + ".mp3"

                # determine the path where the converted file should be saved to
                save_path: str = os.path.expanduser('~') + "\\Downloads\\"
                language: str = 'en'

                # convert the file into a TTS file
                converted_file = gTTS(text=text_to_convert, lang=language, slow=False)

                # save the file in the set path with the set name
                converted_file.save(save_path + file_name)
                print("File has been saved in: " + save_path + " as: " + file_name)
                another_file: str = input("Would you like to convert another PDF file?")
                another_file_bool = bool(another_file)
                if another_file_bool == 'yes'.lower():
                    # return the user to the start of the loop
                    list_of_converted_files.append(file_name)
                    start()
            elif save_file_bool in ["No", "no"]:
                print("Thanks for using the converter!")
            #
            # else:
            #     print("Please enter 'yes' or 'no' only!")

        try:
            path = functions.open_file_path(file_path)
        except OSError as e:
            print("open() failed", e)
            # sys.exit()
        else:
            with path:

                text_speech_value = input("Type yes if you want to hear the text in the file...")
                if text_speech_value in ["Yes", "yes"]:
                    # send text to function to read
                    text = functions.read_file(path)

                    # send text to function to speak
                    functions.return_text_to_speech(text)
                if text_speech_value in ["No", "no"]:
                    print("User made the choice to not hear the text")
        save_converted_file()


start()

# TODO: create a list of converted files and show that to the user
# TODO: implement a txt file reader next to the PDF reader
# TODO: use more dataTypes int,str,float
