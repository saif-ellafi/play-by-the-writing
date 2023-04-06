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
parser.add_argument('--img_size', type=str, help='Image size for dall-e request')
parser.add_argument('--img_format', type=str, help='Format of dall-e image response')


args = vars(parser.parse_args())
action = args['action']

ai_memory_file = os.path.join(tempfile.gettempdir(), 'playbtw_ai_memory.txt')
ai_history_file = os.path.join(tempfile.gettempdir(), 'playbtw_ai_chat.txt')

with open(os.path.join(os.environ['CONFIG'], 'config', 'openai.txt'), encoding='utf-8') as file:
    openai.api_key = file.read().strip()


def memory_erase():
    if os.path.exists(ai_memory_file):
        os.remove(ai_memory_file)


def memory_append(ai_prompt, ai_answer):
    with open(ai_memory_file, 'a') as mem:
        mem.write(ai_prompt)
        mem.write('\n')
        mem.write(ai_answer)
        mem.write('\n')


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


if action == 'ai_complete':
    if args['forget'] == 'true':
        memory_erase()
    prompt = args['prompt'].strip()
    if not prompt:
        print('PBTW-ERROR: No prompt given')
    else:
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        memories = memory_read() if args['memories'] == 'true' else ''
        response = openai.Completion.create(
            prompt=memories + prompt,
            model=model,
            temperature=temperature,
            max_tokens=tokens
        )
        answer = response['choices'][0]['text'].strip()
        if args['remember'] == 'true':
            memory_append(prompt, answer)
        print(prompt + '\n' + answer)
elif action == 'ai_complete_knowledge':
    print(memory_read())
elif action == 'ai_complete_forget':
    memory_erase()
    print("PlayBTW AI Memory erased.")
elif action == 'ai_chat_init':
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
        chat_save(messages)
        print(prompt + '\n' + answer)
elif action == 'ai_image':
    prompt = args['prompt'].strip()
    img_size = args['img_size']
    img_format = args['img_format']
    response = openai.Image().create(
        prompt=prompt,
        size=img_size,
        n=1
    )
    answer = response['data'][0]['url'].strip()
    if img_format == 'markdown':
        print('%s\n![%s](%s)' % (prompt, prompt, answer))
    else:
        print(answer)
else:
    raise Exception("PBTW-ERROR: Wrong Function argument!")
