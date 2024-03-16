# Author: JeansenVaars
# Consider inviting me a Coffee, this took quite some work! -> https://ko-fi.com/JeansenVaars
# Check out my Blog -> https://jvhouse.xyz/
# Use at your OWN RISK

import os
import pickle
import sys

from openai import OpenAI
from playbtw_common import PBWDIR


AI_MEM_FILE = os.path.join(PBWDIR, 'data_ai', 'playbtw_ai_memory.obj')
AI_HISTORY_FILE = os.path.join(PBWDIR, 'data_ai', 'playbtw_ai_chat.txt')


def get_client():
    if os.path.exists(os.path.join(PBWDIR, 'config', 'openai.txt')):
        with open(os.path.join(PBWDIR, 'config', 'openai.txt'), encoding='utf-8') as file:
            api_key = file.read().strip()
    else:
        print('OpenAI API key NOT FOUND. Please type :aisetup to setup your API key.')
        sys.exit(0)
    return OpenAI(api_key=api_key)


def memory_erase():
    if os.path.exists(AI_MEM_FILE):
        os.remove(AI_MEM_FILE)
    if os.path.exists(AI_HISTORY_FILE):
        os.remove(AI_HISTORY_FILE)


def memory_save(ai_prompt, ai_answer, mode):
    with open(AI_MEM_FILE, mode, encoding="utf-8") as mem:
        mem.write(ai_prompt)
        mem.write('\n')
        mem.write(ai_answer)
        mem.write('\n\n')


def memory_read():
    if os.path.exists(AI_MEM_FILE):
        with open(AI_MEM_FILE, 'r', encoding="utf-8") as mem:
            return mem.read()
    else:
        return ''


def chat_save(msg):
    with open(AI_HISTORY_FILE, 'wb') as handle:
        pickle.dump({"messages": msg}, handle)


def chat_load():
    with open(AI_HISTORY_FILE, 'rb') as handle:
        return pickle.load(handle)['messages']


def setup_ai(key):
    path = os.path.join(PBWDIR, 'config', 'openai.txt')
    with open(path, mode='w', encoding='utf-8') as file:
        file.write(key)
