# Author: JeansenVaars
# Consider inviting me a Coffee, this took quite some work! -> https://ko-fi.com/JeansenVaars
# Check out my Blog -> https://jvhouse.xyz/
# Use at your OWN RISK

import argparse
import openai

from playbtw_common import *


parser = argparse.ArgumentParser(description='Play by the Writing - for Espanso - AI Mode')
parser.add_argument('action', type=str, help='ai_complete')
parser.add_argument('--prompt', type=str, default=0, help='Text to prompt the AI')
parser.add_argument('--model', type=str, default=None, help='Model to use in OpenAI')
parser.add_argument('--temperature', type=float, help='Determines randomness levels, where 1 is full risk and 0 certain')
parser.add_argument('--tokens', type=int, help='Max tokens in the response')


args = vars(parser.parse_args())
action = args['action']

with open(os.path.join(os.environ['CONFIG'], 'config', 'openai.txt'), encoding='utf-8') as file:
    openai.api_key = file.read().strip()


if action == 'ai_complete':
    prompt = args['prompt']
    model = args['model']
    temperature = args['temperature']
    tokens = args['tokens']
    response = openai.Completion().create(
        prompt=prompt,
        model=model,
        temperature=temperature,
        max_tokens=tokens
    )
    print(response['choices'][0]['text'].strip())
else:
    raise Exception("Wrong Function argument!")
