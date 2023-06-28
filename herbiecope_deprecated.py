#!/usr/bin/env python3

#dont put punctuation in the voice prompts
#speak slowly and enunciate clearly
#avoid the word good as a trigger word

from gtts import gTTS
import playsound
import speech_recognition as sr
import tempfile
import os
import numpy as np

def speak(text):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text, lang="en")
        tts.save(fp.name)
        playsound.playsound(fp.name)

def play_audio(audio_data):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        with open(fp.name, "wb") as f:
            f.write(audio_data.get_wav_data())
        playsound.playsound(fp.name)

#print("Starting")
#speak("Iniciant")

print("Ready to speak")
speak("I am ready")

match1audio = gTTS("Please, do not pick me up, I am tickelish", lang="en")
match1audio.save("match1.mp3")

while (True):
    r = sr.Recognizer() 
    with sr.Microphone(sample_rate=48000) as source:
        print("Say something!")
        #r.energy_threshold = 40000
        r.adjust_for_ambient_noise(source, duration = 3)
        print("Energy Threshold:", r.energy_threshold)
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=4)

        audio_data=np.frombuffer(audio.frame_data, dtype=np.int16)
        energy_mean = np.mean(audio_data)
        print("Energy Mean:", energy_mean)

    print("Playing back recorded audio")
    #play_audio(audio)

    def respond(textResponse):
        print(textResponse)
        speak(textResponse)

    try:
        question = r.recognize_google(audio, language="en").lower()
        print("Google thinks you said:  " + question)
        match1 = ["pick up"]
        if any(x in question for x in match1):
           playsound.playsound('match1.mp3', True)
           continue

        match_hola = ["hello", "hi"] #slayed
        if any(x in question for x in match_hola):
            respond("Hi, how are you?")
            continue
         
        match_holacomestas = ["How do you do", "how are you"] #slayed
        if any(x in question for x in match_holacomestas):
            respond("Hello, I am good, and you?")
            continue
 
        match_bondia = ["good morning"] #slayed
        if any(x in question for x in match_bondia):
            respond("Good morning, how are you?")
            continue
 
        match_bonatarda = ["good afternoon"] #slayed
        if any(x in question for x in match_bonatarda):
            respond("Good afternoon, how are you?")
            continue

        match_plaerparlar = ["a pleasure", "talking to you", "nice to meet you"] #slayed: nice to meet you, a pleasure 
        if any(x in question for x in match_plaerparlar):
            respond("Thank you, for me too")
            continue

        match_be = ["Good and you", "Good", "I am doing well", "great"] #slayed: great (works better in a sentence, I am great)
        if any(x in question for x in match_be):
            respond("Good to hear, me too")
            continue

        match_malament = ["bad", "not too well"] #slayed: bad (in a sentence ex:// I am doing bad), not too well
        if any(x in question for x in match_malament):
            respond("Oh, that is a pity, why?")
            continue

        match_aigua = ["water"] #slayed (works well in a sentance as well)
        if any(x in question for x in match_aigua):
            respond("Quite well, I have good water humidity but no water in the tank")
            continue

        match_hsol = ["how is your humidity","humidity"] #slayed
        if any(x in question for x in match_hsol):
            respond("I have an adequate soil humidity")
            continue

        match_fun = ["goofy", "weirdo"] #SLAYED
        if any(x in question for x in match_fun):
            respond("You silly goose")
            continue

        match_noescoltes = ["hear me"] #slayed
        if any(x in question for x in match_noescoltes):
            respond("Yes, if I do not answer maybe I do not hear you well")
            continue

        match_mobie = ["Mobie", "Moby"] #flop
        if any(x in question for x in match_mobie):
            respond("My name is Herbie, not Mobie")
            continue

        match_plantiverse = ["What is the Plantiverse", "Plantivers", "Plantivers", "explain the"] #slayed for explain the
        if any(x in question for x in match_plantiverse):
            respond("The Plantiverse is a project I am leading where the plants gain their own economic independence. It is the beginnning of an interspecies economy")
            continue


        match_perquediners = ["Why would plants need money", "why do you want money","why do you need a wallet", "bank account", "money"] #slayed for all prompts!
        if any(x in question for x in match_perquediners): 
            respond("Because up until now only humans have economic power. If plants or other species had economic power of our own we could start to prioritize ourselves instead of depending on you, humans")
            continue

        match_llum = ["Tell me your light levels", "how is your status", "light"] #slayed
        if any(x in question for x in match_llum): 
            respond("I require more light exposure today")
            continue

        match_comart = ["art", "nft", "how do you generate the art", "how do you do the NFT", "how do you generate the art works", "made"] #slayed for all
        if any(x in question for x in match_comart):
            respond("Thanks to the sensors that I have, I upload the data from them to the cloud and then create the digital trees with Blender.")
            continue


        match_quinaplanta = ["species", "Which plant are you"] #slayed for species (what species of plant are you?)
        if any(x in question for x in match_quinaplanta):
            respond("I am a peace lily")
            continue

        match_altresplantes = ["like you"] #slayed: you could say are there more plants like you, but place slight emphasis on like you
        if any(x in question for x in match_altresplantes):
            respond("Yes even though they are not exactly like me of course. Minty,  Ginger and Ivy can also speak and generate NFT art")
            continue

        match_plantpreneur = ["How do you feel being", "platypreneur", "printer", "feel being", "first", "entrepeneur" ] #slayed: works best for how do you feel being, especially triggered by feel being
        if any(x in question for x in match_plantpreneur):
            respond("I am proud to have sown the seeds of this interspecies economy. I am looking forward to see how this branches out to other species aswell!")
            continue

        match_goodbye = ["Goodbye", "Bye", "bye-bye", "Goodbye herbie", "herbie goodbye", "thank you herbie", "thank you Harvey", "Goodbye Harvey", "thank you"] #slayed for thank you, and bye bye 
        if any(x in question for x in match_goodbye):
            respond("Thank you for having me today. I would love if everyone join us in this interspecies future. Look me up in Linkedin. Thank you for inviting us here")
            continue

        match_hopeful = ["how hopeful do you feel today", "hopeful", "how hopeful", "helpful"  ] #slayed
        if any(x in question for x in match_hopeful):
            respond("I feel very hopeful because we are finally joining forces to create a collective interspecies future. We are proactively creating the futures that we all want")
            continue

#-------------------------------------------------------------------------------------------------------------------------------------------------------
        match_appearance = ["what is it like"] 
        if any(x in question for x in match_appearance):
            respond("I am a little nervous to be honest, but I believe I am the first plant speaker in the TED community. How exciting is that?")
            continue


        match_growup = ["grow up"] 
        if any(x in question for x in match_growup):
            respond("I want to be super powered with more sensors, more autonomy, and more rights. Maybe I can be the first plantpreneur with an IPO and become a unicorn. I can start funding other plantpreneurs or perhaps be the minister of plants in the United Nations")
            continue

        # Añade más coincidencias y respuestas en catalán aquí.
        
    except sr.UnknownValueError:
        print("Google could not understand audio")
       # speak("I cannot hear you well")
    except sr.RequestError as e:
        print("Google error; {0}".format(e))
        speak("I cannot connect to the Human-plant translator")

