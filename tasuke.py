#!/bin/python3
#
# This file is part of the tasuke project (https://github.com/nthnn/tasuke).
# Copyright (c) 2024 Nathanne Isip.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import os
import sys
import json
import time
import random
import subprocess
import speech_recognition as sr

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from gtts import gTTS
from pygame import mixer

def text_to_speech(text):
    tmp3 = "/tmp/tasuke/temp.mp3"
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(tmp3)

    mixer.init()
    mixer.music.load(tmp3)
    mixer.music.play()

    while mixer.music.get_busy():
        time.sleep(1)

def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"
    return response

def load_commands(json_path):
    with open(json_path, 'r') as f:
        return json.load(f)

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"\x1b[31mError executing command\x1b[0m: {e}")

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    commands = load_commands("/etc/tasuke/conf.d/commands.json")

    print("\x1b[32mListening\x1b[0m...")
    text_to_speech("Listening to microphone")

    while True:
        result = recognize_speech_from_mic(recognizer, microphone)
        if result["transcription"]:
            print(f"\x1b[32mTranscription\x1b[0m: {result['transcription']}")
            for phrases, replies, command in commands:
                if any(phrase in result["transcription"].lower() for phrase in phrases):
                    print(f"\x1b[34mExecuting command\x1b[0m: {command}")
                    text_to_speech(random.choice(replies))
                    execute_command(command)
                    break
        elif result["error"]:
            print(f"\x1b[31mError\x1b[0m: {result['error']}")

try:
    main()
except KeyboardInterrupt:
    exit(0)
