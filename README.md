# HerbieATX
 Repository for communicating with Herbie via vocal detection, OpenAI ChatGPT API integration, and neural voices as a part of the greater Plantiverse project


## How to access/run files on the Jetson
Open the LXTerminal on the Jetson, and activate the virtual environment by pasting the following line of code:  
 ```source ~/.py3venv/bin/activate```  
Change the directory to access Herbie's programs by typing `cd herbieATX`. To open a file type `gedit filename.py`. The same line can be used to create a new file with the filename of choice.  
To run a python file typ `python3.8 -m filename.py`. When you are done accessing and running code type `deactivate` to close the virtual environment before exiting the terminal.  

## Required Python modules
Before running the contents of this repository (having been tested only on Windows 11 and Linux Ubuntu 18.04 or newer), the following modules or packages are needed. To make this ReadMe more concise, links will be provided to resources (respective to the modules) that were used. Please follow the instructions provided by these linked resources. 

OpenAI ChatGPT API with Python:  
Microsoft Azure Cognitive Speech Services API with Python:  

Use the latest version of Python, `pip`, and `pandas` available to your system. A version of **at least Python 3.8 or newer** is required.  

## Communicating with HerbieATX
The files `speech_sample2.py`, `speech_synthesis.py`, `communicate.py`, and `main.py` are imperative to communicating with HerbieATX.  

To communicate with Herbie, run `main.py` in any terminal application. In the Linux Ubuntu OS on the Jetson, you may use the command `python3.8 main.py` to run the file. 
