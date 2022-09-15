# Author: JeansenVaars
# Consider inviting me a Coffee, this took quite some work! -> https://ko-fi.com/JeansenVaars
# Check out my Blog -> https://jvhouse.xyz/
# Use at your OWN RISK

import argparse
import openai
import pyperclip

from playbtw_common import *


parser = argparse.ArgumentParser(description='Play by the Writing - for Espanso - AI Mode')
parser.add_argument('action', type=str, help='ai_complete')


args = vars(parser.parse_args())
action = args['action']

with open(os.path.join(os.environ['CONFIG'], 'config', 'openai.txt'), encoding='utf-8') as file:
    openai.api_key = file.read().strip()


if action == 'ai_complete':
    context = pyperclip.paste()
    if not context.strip():
        print("ERROR: Nothing found in clipboard. Copy some text for context")
    else:
        response = openai.Completion().create(model='text-davinci-002', prompt=context, max_tokens=64, top_p=1, n=1)
        print(response['choices'][0]['text'].strip())
else:
    raise Exception("Wrong Function argument!")
