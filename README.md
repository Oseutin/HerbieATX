# HerbieATX
 Repository for communicating with Herbie via vocal detection, OpenAI ChatGPT API integration, and neural voices as a part of the greater Plantiverse project


## How to access/run files on the Jetson
Open the LXTerminal on the Jetson, and activate the virtual environment by pasting the following line of code:  
 ```source ~/.py3venv/bin/activate```  
Change the directory to access Herbie's programs by typing `cd herbieATX`. To open a file type `gedit filename.py`. The same line can be used to create a new file with the filename of choice. To run a python file typ `python3.8 filename.py`. When you are done accessing and running code type `deactivate` to close the virtual environment before exiting the terminal.  

## Required Python modules
Before running the contents of this repository (having been tested only on Windows 11 and Linux Ubuntu 18.04 or newer), the following modules or packages are needed. If you are using the original Jetson Nano developed by the UT team for HerbieATX, you do not need to worry about this section, as all modules have already been installed. To make this ReadMe more concise, links will be provided to resources (respective to the modules) that were used by the team. Please follow the instructions provided by these linked resources, as they provide excellent step-by-step directions. 

OpenAI ChatGPT API with Python:  
https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb  
https://platform.openai.com/docs/api-reference/chat/create  
  
Microsoft Azure Cognitive Speech Services API with Python:  
https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/quickstart/python/from-microphone  
(Optional) The following is a sample repository for your viewing that was used and later highly modified in HerbieATX: 
https://github.com/Azure-Samples/cognitive-services-speech-sdk  
  
Use the latest version of Python, `pip`, and `pandas` available to your system. A version of **at least Python 3.8 or newer** is required. In the case that your Python version is lower on the Jetson Nano, look to this resource:  
https://jetsonhacks.com/2023/06/12/upgrade-python-on-jetson-nano-tutorial/  

## Communicating with HerbieATX
The files `speech_sample2.py`, `speech_synthesis.py`, `communicate.py`, and `main.py` are imperative to communicating with HerbieATX.  

To communicate with Herbie, run `main.py` in any terminal application. In the Linux Ubuntu OS on the Jetson, you may use the command `python3.8 main.py` to run the file. It is not recommended to run the "modular" files separately, as they are dependent on one another for transferring information through text files such as `language.txt` or `test.txt`.

## Customization and future development
We recommend using the Visual Studio Code IDE on a separate Windows device, and not the built-in editor of the Linux Ubuntu OS on the Jetson Nano to avoid disarraying indentations of the code.  

The following webpage includes all of the supported language options for text-to-speech. To change the voice used by HerbieATX, modify the key-value pair dictionary in the `speech_synthesis.py` file so that the key is the IETF language tag, and the value is the respective speech_synthesis_voice_name as determined by the voice options linked below:  
https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts  

As for speech detection, the language options that are available are unfortunately more limited. You may view the available options here:  
https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=stt  
Please note that languages with speech-to-text support will be indicated with the word "Audio" under the column of "Custom Speech support." To change the languages recognized by HerbieATX, modify the entries of the list in `speech_sample2.py` in the argument of `speechsdk.languageconfig.AutoDetectSourceLanguageConfig` on line 43. Please note that **only four entries** may be added a time due to limitations with language recognition. By default, American English `en-US`, Taiwanese Mandarin Chinese `zh-TW`, Castilian Spanish `es-ES`, and Catalan/Valencian `ca-ES` are the languages that can be recognized by HerbieATX.  

HerbieATX is able to respond in a language different from the one it has detected (e.g. "Herbie, introduce yourself in Telugu." or "Herbie, preséntate en coreano."), as long as a new entry is added for that language to the key-value pair dictionary in `speech_synthesis.py`. It does not require a new entry in `speech_sample2.py`. 
  
Currently, HerbieATX only responds to one keyword, "Herbie," adapted to the American English (`en-US`) language. To add more keyword options, like "Hello Herbie," or expand on the keyword table so that speech detection is more accurate, refer to this resource:  
https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-keyword-basics?pivots=programming-language-python

There are some files already available for implementing light sensor data via the serial monitor of the ESP-32 to the Jetson Nano. However, due to current hardware limitations placed on the battery and low-power mode of the microcontroller, we have left these files unused. If these limitations are circumvented in the future, the light sensor data may easily be implemented in `main.py` and `communicate.py` be uncommenting the respective lines of code. Further debugging may be required to completely integrate Arduino devices with the Linux-based Jetson Nano. 
