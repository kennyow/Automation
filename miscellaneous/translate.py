#pip install googletrans
#pip install --upgrade googletrans==4.0.0-rc1

from googletrans import Translator


translator = Translator()

translation= translator.translate(text='Eu quero comer ovo de Páscoa', dest = 'en').text

print(translation)