#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
"""
Speech recognition samples for the Microsoft Cognitive Services Speech SDK
"""
# Edited and repurposed by Austin Fang for HerbieATX (previously Herbie V2.0)

import time
import codecs

try:
    import azure.cognitiveservices.speech as speechsdk
except ImportError:
    print("""
    Importing the Speech SDK for Python failed.
    Refer to
    https://docs.microsoft.com/azure/cognitive-services/speech-service/quickstart-python for
    installation instructions.
    """)
    import sys
    sys.exit(1)


# Set up the subscription info for the Speech Service:
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "dc48a3b483f1489494e30955ff2c5481", "westeurope"

# <SpeechRecognitionUsingKeywordModel>
def speech_recognize_keyword_from_microphone():
    """performs keyword-triggered speech recognition with input microphone"""
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # Creates an instance of a keyword recognition model. Update this to
    # point to the location of your keyword recognition model.
    model = speechsdk.KeywordRecognitionModel("9c5af1eb-1b0a-4421-8166-ed10293ab644.table")

    # The phrase your keyword recognition model triggers on.
    keyword = "Herbie"
    auto_detect_source_language_config = \
        speechsdk.languageconfig.AutoDetectSourceLanguageConfig(languages=["zh-TW", "en-US", "es-ES", "ca-ES"])
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, auto_detect_source_language_config=auto_detect_source_language_config)
    # speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    done = False

    def stop_cb(evt: speechsdk.SessionEventArgs):
        """callback that signals to stop continuous recognition upon receiving an event `evt`"""
        print('CLOSING on {}'.format(evt))
        nonlocal done
        done = True

    def recognizing_cb(evt: speechsdk.SpeechRecognitionEventArgs):
        """callback for recognizing event"""
        if evt.result.reason == speechsdk.ResultReason.RecognizingKeyword:
            print('RECOGNIZING KEYWORD: {}'.format(evt))
        elif evt.result.reason == speechsdk.ResultReason.RecognizingSpeech:
            print('RECOGNIZING: {}'.format(evt))

    def recognized_cb(evt: speechsdk.SpeechRecognitionEventArgs):
        """callback for recognized event"""
        if evt.result.reason == speechsdk.ResultReason.RecognizedKeyword:
            print('RECOGNIZED KEYWORD: {}'.format(evt))
        elif evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
            auto_detect_source_language_result = speechsdk.AutoDetectSourceLanguageResult(evt.result)
            print("Recognized: {} in language {}".format(evt.result.text, auto_detect_source_language_result.language))
            # print('RECOGNIZED: {}'.format(evt))
            # Set up the output file for the transcript
            # output_file = open("test.txt", "w")
            # Save the speech-to-text in a separate file so that communicate.py can distinguish between system and user instructions
            with codecs.open("test.txt", "w", encoding = "utf-8") as output_file:
                output_file.write("{}".format(evt.result.text))
                output_file.close()
            # Save the identified spoken language in a separate text file so that speech_synthesis.py can access and choose the right text-to-speech voice
            with codecs.open("language.txt", "w", encoding = "utf-8") as language_file:
                language_file.write(auto_detect_source_language_result.language)
                language_file.close()
        elif evt.result.reason == speechsdk.ResultReason.NoMatch:
            print('NOMATCH: {}'.format(evt))
	
# Connect callbacks to the events fired by the speech recognizer
    speech_recognizer.recognizing.connect(recognizing_cb)
    speech_recognizer.recognized.connect(recognized_cb)
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
    # stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    # Start keyword recognition
    speech_recognizer.start_keyword_recognition(model)
    print('\nSay something starting with "{}" followed by whatever you want...'.format(keyword))
    while not done:
        time.sleep(.5)

    speech_recognizer.stop_keyword_recognition()
# </SpeechRecognitionUsingKeywordModel>

speech_recognize_keyword_from_microphone()
