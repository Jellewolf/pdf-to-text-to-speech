import os
import sys
from gtts import gTTS

import functions

user_file_path: str = input("Please enter path name in the following format: directory\\file_name")
# get the path where the file is located
file_path = os.path.expanduser('~') + "\\" + user_file_path
try:
    path = functions.open_file_path(file_path)
except OSError as e:
    print("open() failed", e)
    sys.exit()
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

save_file_bool = input("Would you like to save the converted file?")
if save_file_bool in ["Yes", "yes"]:
    file_to_convert = functions.open_file_path(file_path)
    text = functions.read_file(file_to_convert)
    language = 'en'
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save("voice.mp3")

    # save_path: str = os.path.expanduser('~') + "\\Downloads\\"
    # random_int = str(random.randint(0, 200))
    # name_of_file: str = "convert_pdf_file" + random_int
    # file_extension: str = ".tts"
    # complete_name = os.path.join(save_path, name_of_file + file_extension)
    # file = open(complete_name, "w")

    # path = functions.open_file_path(file_path)
    # text = functions.read_file(path)
    # file.write("text")
    # file.close()
    # functions.return_text_to_speech(file)
    # print("File has been saved in: " + save_path + " as: " + name_of_file + file_extension)
