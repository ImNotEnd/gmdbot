from googletrans import Translator
import json

translator = Translator()

def translateXXX(text, dest, src):
    if src == "":
        if dest == "":
            translated1 = translator.translate(text)
        else:
            translated1 = translator.translate(text, "", dest)
    else:
        translated1 = translator.translate(text, src, dest)

    return translated1.text

