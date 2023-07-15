import json
import pyaudio

from vosk import Model, KaldiRecognizer


en_model = Model('vosk-model-en-us-0.22-lgraph')
uk_model = Model('vosk-model-uk-v3-lgraph')
model = uk_model
recognizer = KaldiRecognizer(model, 16000)
words = pyaudio.PyAudio()
stream = words.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def listening():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (recognizer.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(recognizer.Result())
            if answer['text']:
                yield answer['text']


for text in listening():
    if model == en_model:
        if 'hello' in text.lower():
            print('UkrBot: Hello my dear user!')
            print(f'UkrBot: your text = {text}')
        elif 'volleyball' in text.lower():
            print('UkrBot: Voleyball is my favourite sport!')
        else:
            print(f'User: {text}')
    elif model == uk_model:
        if 'як твої справи' in text.lower():
            print(f'UkrBot: У мене все добре, а у тебе як?')
        else:
            print(f'User: {text}')