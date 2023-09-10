import os
import sys

import functions

exit_message: str = "Thanks for using the converter!"


def start():
    while True:
        user_file_path: str = input("Please enter path name in the following format: directory\\file_name")
        # get the path where the file is located
        file_path: str = os.path.expanduser('~') + "\\" + user_file_path
        save_file_bool = input("Would you like to save the converted file?")
        if not save_file_bool == 'yes'.lower():
            print(exit_message)
            sys.exit()
        file_to_convert = functions.open_file_path(file_path)
        text_to_convert = functions.read_file(file_to_convert)
        functions.save_converted_file(text_to_convert)
        another_file: str = input("Would you like to convert another PDF file?")
        if not another_file == 'yes'.lower():
            print(exit_message)
            sys.exit()
        # return the user to the start of the loop
        start()

    # try:
    #     path = functions.open_file_path(file_path)
    # except OSError as e:
    #     print("open() failed", e)
    # else:
    #     with path:
    #
    #         text_speech_value = input("Type yes if you want to hear the text in the file...")
    #         if text_speech_value in ["Yes", "yes"]:
    #             # send text to function to read
    #             text = functions.read_file(path)
    #
    #             # send text to function to speak
    #             functions.return_text_to_speech(text)
    #         if text_speech_value in ["No", "no"]:
    #             print("User made the choice to not hear the text")
    # save_converted_filetemp()


start()

# TODO: create a list of converted files and show that to the user
# TODO: implement a txt file reader next to the PDF reader
# TODO: use more dataTypes int,str,float
