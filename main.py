
import argparse
import os

import queue
import sys
import sounddevice as sd
import vosk
import json

from pyttsx3 import voice
from vosk import Model, KaldiRecognizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import app
from app import *
import funcshen
from funcshen import *
q = queue.Queue()

model = vosk.Model('model_small')

device = sd.default.device
samplerate = sd.query_devices(0)['default_samplerate']


def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def reconize (data, vectorizer, clf):
    if not trigers.intersection(data.split()):
        return
    else:
        text_vector = vectorizer.transform([data]).toarray()[0]
        ansver = clf.predict([text_vector])[0]
        func_name = ansver.split()[0]
        speaker(ansver.replace(func_name, ''))
        exec(func_name+'()')
        print(func_name)
        print(ansver)


def main():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(app.data_set.keys()))
    clf = LogisticRegression()

    clf.fit(vectors, list(app.data_set.values()))
    #del data_set
    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0],dtype="int16", channels=1, callback=callback):
        rec = KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                reconize(data, vectorizer, clf)


if __name__ == '__main__':
    main()
