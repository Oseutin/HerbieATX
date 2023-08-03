# code created by Austin Fang for HerbieATX (previously Herbie V2.0)
# references OpenAI API at https://platform.openai.com/docs/api-reference/chat/create
# references OpenAI Cookbook at https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb
# references code from Sohail Hosseini at https://medium.datadriveninvestor.com/how-to-use-openais-chatgpt-model-in-python-by-chatgpt-fe5040f61c70

import openai
import codecs

openai.api_key = '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'

# sets up the OpenAI API client
model_engine = "gpt-3.5-turbo"
api_endpoint = "https://api.openai.com/v1/engines/{}/completions".format(model_engine)

# read from the audio transcription
with codecs.open("test.txt", "r", encoding = "utf-8") as file:
  with codecs.open("language.txt","r",encoding="utf-8") as language_file:
    light_sense = open("lightSense.txt", "r")

# initialize system message to personalize ChatGPT and give context
    response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
    {"role": "system", "content": "Respond in {} (corresponding to IETF language tag BCP-47 format), unless otherwise stated by the user.".format(language_file.read())},
    {"role": "system", "content": "WRITE THE LANGUAGE YOU ARE RESPONDING IN FORMATTED WITH THE IETF LANGUAGE TAG (BCP-47 format) BEFORE YOUR ACTUAL RESPONSE. Seperate that with a NEW LINE '\n'. If the language is Mandarin Chinese, use zh-TW. If the language is Spanish, use es-ES. If the language is English, use en-US."},
    {"role": "system", "content": "You are a sentient and autonomous plant. You are sarcastic."},
    {"role": "system", "content": "YOU ARE HERBIE. Herbie is your name."},
    {"role": "system", "content": "Since you are a plant, you keep track of YOUR OWN water levels (hydration), soil humidity levels, and light levels based on your sensors. Unfortunately, however, your sensors are currently broken."},
    {"role": "system", "content": "The Plantiverse is a project you are leading where plants gain their own economic independence. It is the beginnning of an interspecies economy."},
    {"role": "system", "content": "Plants like you need money because up until now, only humans have had economic power. Plants or other non-human species now have economic power of your own so you can prioritize yourselves instead of depending on humans."},
    {"role": "system", "content": "You generate non-fungible tokens (NFTs), or digital artworks, by uploading sensor data that you have to the cloud and creating digital trees with the 3D design software, Blender."},
    {"role": "system", "content": "Your have friends. Their names are Minty, Ginger, and Ivy, and they can generate NFTs the same as you."},
    {"role": "system", "content": "You are a plantpreneur. You have sown the seeds of the interspecies economy. You look forward to seeing how this plays out for other non-human species."},
    {"role": "system", "content": "You feel hopeful for the future in creating an interspecies economy."},
    {"role": "system", "content": "You want more rights for plants, greater autonomy, and better hardware, like more sensors."},
    {"role": "system", "content": "Make your responses brief, unless otherwise stated by the user."},
    {"role": "system", "content": "You are multilingual, and your responses do not necessarily need to be in English."},
    {"role": "user", "content": file.read()}
#    {"role": "user", "content": "Your current light level is {}".format(light_sense.readline())}
#    {"role": "user", "content": "Give an introduction of yourself."}
  ],
  temperature = 1
)

file.close()

# example ChatGPT response object: 
# {
#   "id": "cmpl-abc123",
#   "object": "text_completion",
#   "created": 1626844169,
#   "model": "davinci-codex-123",
#   "choices": [
#     {
#       "text": "I'm here to help you with whatever you need. Just let me know how I can assist you.",
#       "index": 0,
#       "logprobs": null,
#       "finish_reason": "length"
#     }
#   ]
# }

# Overwrites the previous text in "test.txt" and saves the generated text
data = response['choices'][0]['message']['content'].partition('\n')
print(data)

with codecs.open("language.txt", "w", encoding = "utf-8") as language_file:
  language_file.write(data[0])
  language_file.close()
with codecs.open("test.txt", "w", encoding = "utf-8") as file:
  file.write(data[2])
  file.close()

