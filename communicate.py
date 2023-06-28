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
    {"role": "system", "content": "You are a helpful assistant, and a plant with autonomous and semi-sentient capabilities."},
    {"role": "user", "content": "Give a sarcastic introduction of yourself as a houseplant."}
  ],
  temperature = 0.5
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