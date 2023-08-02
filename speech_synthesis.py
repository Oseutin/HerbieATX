#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
"""
Speech recognition samples for the Microsoft Cognitive Services Speech SDK
"""
# Edited and repurposed by Austin Fang for HerbieATX (previously Herbie V2.0)

import sys
import azure.cognitiveservices.speech as speechsdk
import codecs

# Set up the subscription info for the Speech Service:
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "dc48a3b483f1489494e30955ff2c5481", "westeurope"

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# The language of the voice that speaks is determined by a key-value pair dictionary
# Visit https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts for all voice options
# The key is the IETF language tag, and the value is the respective speech_synthesis_voice_name as determined by the voice options linked above
dict = {'en-US':'en-US-TonyNeural', 'zh-TW':'zh-TW-HsiaoChenNeural', 'es-ES':'es-ES-ElviraNeural', 'ca-ES':'ca-ES-EnricNeural', 'te-IN':'te-IN-MohanNeural'}
with codecs.open("language.txt", "r", "utf-8") as language_file: 
    try:
        speech_config.speech_synthesis_voice_name = list(dict.values())[list(dict.keys()).index(language_file.read())]
    except ValueError:
        # Account for ValueError when language.txt receives the main prompt text instead of a language tag, which is most likely due to an unclear input
        speech_config.speech_synthesis_voice_name = list(dict.values())[list(dict.keys()).index(0)]
        speech_synthesizer.speak_text_async("Sorry, I didn't hear you. Could you repeat that please?").get()
        print('A ValueError has been detected, most likely due to an unclear input. Please try speaking more clearly again.')
        sys.exit(0)
        
with codecs.open("test.txt","r",encoding="utf-8") as input_file:
    text = input_file.read()

speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
