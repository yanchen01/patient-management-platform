import os

from celery import Celery
from celery.utils.log import get_task_logger

import speech_recognition as sr

logger = get_task_logger(__name__)

app = Celery('speech_to_text_tasks',
             broker='amqp://admin:mypass@rabbit:5672',
             backend='mongodb://mongodb_container:27017/speech_to_text')


@app.task()
def speech_to_text(afile):
    if os.path.exists(afile):
        recognizer = sr.Recognizer()
        audioFile = sr.AudioFile(afile)
        with audioFile as source:
            data = recognizer.record(source)
        transcript = recognizer.recognize_google(data, key=None)
        return transcript
    return ""
