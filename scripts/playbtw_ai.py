# Author: JeansenVaars
# Consider inviting me a Coffee, this took quite some work! -> https://ko-fi.com/JeansenVaars
# Check out my Blog -> https://jvhouse.xyz/
# Use at your OWN RISK

import argparse

import openai
import pickle

from playbtw_common import *


parser = argparse.ArgumentParser(description='Play by the Writing - for Espanso - AI Mode')
parser.add_argument('action', type=str, help='Open AI GPT')
parser.add_argument('--prompt', type=str, default=0, help='Text to prompt the AI')
parser.add_argument('--model', type=str, default=None, help='Model to use in OpenAI')
parser.add_argument('--temperature', type=float, help='Determines randomness levels, where 1 is full risk and 0 certain')
parser.add_argument('--tokens', type=int, help='Max tokens in the response')
parser.add_argument('--remember', type=str, help='Whether to keep the answer in AI memory')
parser.add_argument('--forget', type=str, help='Whether to forget all AI memories and start clean')
parser.add_argument('--memories', type=str, help='Whether to use memories stored so far')
parser.add_argument('--img_format', type=str, default='markdown', help='Dall-E response format. url, markdown or b64_json')
parser.add_argument('--img_size', type=str, default='1024x1024', help='Image size for dall-e request')
parser.add_argument('--img_quality', type=str, default='standard', help='Image quality for dall-e response. standard or hd')
parser.add_argument('--img_style', type=str, default='vivid', help='Image style for dall-e response. vivid or natural')


args = vars(parser.parse_args())
action = args['action']

ai_memory_file = os.path.join(tempfile.gettempdir(), 'playbtw_ai_memory.txt')
ai_history_file = os.path.join(tempfile.gettempdir(), 'playbtw_ai_chat.txt')

with open(os.path.join(os.environ['CONFIG'], 'config', 'openai.txt'), encoding='utf-8') as file:
    api_key = file.read().strip()
    if api_key == '<Replace entire line with OpenAI API Key>':
        print('OpenAI API KEY NOT Replaced. Paste your OpenAI API KEY in openai.txt file (and make a backup of the file)')
        exit(0)
    openai.api_key = api_key


def memory_erase():
    if os.path.exists(ai_memory_file):
        os.remove(ai_memory_file)


def memory_save(ai_prompt, ai_answer, mode):
    with open(ai_memory_file, mode) as mem:
        mem.write(ai_prompt)
        mem.write('\n')
        mem.write(ai_answer)
        mem.write('\n\n')


def memory_read():
    if os.path.exists(ai_memory_file):
        with open(ai_memory_file, 'r') as mem:
            return mem.read()
    else:
        return ''


def chat_save(msg):
    with open(ai_history_file, 'wb') as handle:
        pickle.dump({"messages": msg}, handle)


def chat_load():
    with open(ai_history_file, 'rb') as handle:
        return pickle.load(handle)['messages']


if action == 'ai_chat_init':
    prompt = args['prompt'].strip()
    if not prompt:
        print('PBTW-ERROR: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        response = openai.ChatCompletion.create(
            messages=messages,
            model=model,
            temperature=temperature,
            max_tokens=tokens
        )
        answer = response['choices'][0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        memory_save(prompt, answer, 'w')
        chat_save(messages)
        print(prompt + '\n' + answer)
elif action == 'ai_chat':
    prompt = args['prompt'].strip()
    if not prompt:
        print('PBTW-ERROR: No prompt given')
    elif not os.path.exists(ai_history_file):
        print('PBTW-ERROR: Call `:aistart` to begin a chat first.')
    else:
        messages = chat_load()
        messages.append({
            "role": "user",
            "content": prompt
        })
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        response = openai.ChatCompletion.create(
            messages=messages,
            model=model,
            temperature=temperature,
            max_tokens=tokens
        )
        answer = response['choices'][0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        memory_save(prompt, answer, 'a')
        chat_save(messages)
        print(prompt + '\n' + answer)
elif action == 'ai_chat_isolate':
    prompt = args['prompt'].strip()
    if not prompt:
        print('PBTW-ERROR: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        response = openai.ChatCompletion.create(
            messages=messages,
            model=model,
            temperature=temperature,
            max_tokens=tokens
        )
        answer = response['choices'][0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(prompt + '\n' + answer)
elif action == 'ai_image':
    prompt = args['prompt'].strip()
    img_size = args['img_size']
    img_format = args['img_format']
    img_quality = args['img_quality']
    img_style = args['img_style']
    response = openai.Image().create(
        prompt=prompt,
        size=img_size,
        quality=img_quality,
        style=img_style,
        response_format='url' if img_format=='markdown' else img_format,
        n=1,
        model='dall-e-3'
    )
    answer = response['data'][0]['url'].strip()
    if img_format == 'markdown':
        print('%s\n![%s](%s)' % (prompt, prompt, answer))
    else:
        print(answer)
elif action == 'ai_knowledge':
    print(memory_read())
elif action == 'ai_forget':
    memory_erase()
    print("PlayBTW AI Memory erased.")
else:
    raise Exception("PBTW-ERROR: Wrong Function argument!")
