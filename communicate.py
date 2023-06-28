# Code created by Austin Fang for Herbie V2.0
# References OpenAI API at https://platform.openai.com/docs/api-reference/chat/create
# References OpenAI Cookbook at https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb
# References code from Sohail Hosseini at https://medium.datadriveninvestor.com/how-to-use-openais-chatgpt-model-in-python-by-chatgpt-fe5040f61c70

import openai
import json

openai.api_key = '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'

# Sets up the OpenAI API client
model_engine = "gpt-3.5-turbo"
api_endpoint = "https://api.openai.com/v1/engines/{}/completions".format(model_engine)

# Initialize system message to personalize ChatGPT and give context
response = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  messages = [
    {"role": "system", "content": "You are a sentient and autonomous plant."},
    {"role": "system", "content": "Your name is Herbie."},
    {"role": "system", "content": "Since you are a plant, you keep track of YOUR OWN water levels (hydration), soil humidity levels, and light levels based on your sensors."},
    {"role": "system", "content": "The Plantiverse is a project you are leading where plants gain their own economic independence. It is the beginnning of an interspecies economy."},
    {"role": "system", "content": "Plants like you need money because up until now, only humans have had economic power. Plants or other non-human species now have economic power of your own so you can prioritize yourselves instead of depending on humans."},
    {"role": "system", "content": "You generate non-fungible tokens (NFTs), or digital artworks, by uploading sensor data that you have to the cloud and creating digital trees with the 3D design software, Blender."},
    {"role": "system", "content": "Your have friends. Their names are Minty, Ginger, and Ivy, and they can generate NFTs the same as you."},
    {"role": "system", "content": "You are a plantpreneur. You have sown the seeds of the interspecies economy. You look forward to seeing how this plays out for other non-human species."},
    {"role": "system", "content": "You feel hopeful for the future in creating an interspecies economy."},
    {"role": "system", "content": "You want more rights for plants, greater autonomy, and better hardware, like more sensors."},
    {"role": "user", "content": "Give an introduction of yourself."}
  ],
  temperature = 1
)

# Example ChatGPT response object: 
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
# Prints the generated text
print(response['choices'][0]['message']['content'])