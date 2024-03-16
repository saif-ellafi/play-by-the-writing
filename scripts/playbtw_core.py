# Author: JeansenVaars
# Consider inviting me a Coffee, this took quite some work! -> https://ko-fi.com/JeansenVaars
# Check out my Blog -> https://jvhouse.xyz/
# Use at your OWN RISK

import argparse
from playbtw_common import *
from playbtw_ai import *
from playbtw_utils import *

parser = argparse.ArgumentParser(description='Play by the Writing - Oracle for Espanso')
parser.add_argument('action', type=str)
parser.add_argument('--mods', type=int, default=0, help='Modifier, Numeric, various use cases')
parser.add_argument('--mode', type=str, default=None, help='Roll mode, supports normal|adv|dis')
parser.add_argument('--table', type=str, help='Random Table Key')
parser.add_argument('--formula', type=str, help='Dice formula')
parser.add_argument('--contains', type=str, default='', help='Contains sub expressions and content')
parser.add_argument('--quantity', type=int, help='Simple Roll dice quantity')
parser.add_argument('--size', type=int, help='Simple Roll dice size')

parser.add_argument('--odds', type=int, default=0, help='Odds towards result. From -8 to +8')
parser.add_argument('--chaos', type=int, default=5, help='Chaos Factor. From 3 to 6')

parser.add_argument('--gen_a', type=int, help='Genesys dice ability')
parser.add_argument('--gen_p', type=int, help='Genesys dice proficiency')
parser.add_argument('--gen_b', type=int, help='Genesys dice boost')
parser.add_argument('--gen_d', type=int, help='Genesys dice difficulty')
parser.add_argument('--gen_c', type=int, help='Genesys dice challenge')
parser.add_argument('--gen_s', type=int, help='Genesys dice setback')

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

if action == 'table':
    tables = filter(lambda x: x, map(str.strip, args['table'].split(',')))
    result = []
    for t in tables:
        result.append(choice_table(t.strip(), args['mode']))
    print(' '.join(result))
elif action == 'wtable':
    tables = map(str.strip, args['table'].split(','))
    result = []
    for t in tables:
        result.append(choice_wtable(t.strip(), args['mode']))
    print(' '.join(result))
elif action == 'roll_dice':
    formula = args['formula']
    roll = roll_advanced(formula)
    print(formula + ': ' + roll[1] + ' = ' + str(roll[0]))
elif action == 'fate_check':
    print(fate_check(args['odds'], args['chaos']))
elif action == 'scene_check':
    print(scene_check(args['chaos']))
elif action == 'random_event':
    print(random_event())
elif action == 'roll_fudge':
    def map_fudge(value):
        if value in [1, 2]:
            return '(-)'
        elif value in [3, 4]:
            return '( )'
        else:
            return '(+)'
    fudges = []
    bonus = args['mods']
    for r in range(0, 4):
        roll = roll_dice(1, 6)
        fudges.append(map_fudge(roll['total']))
    total = fudges.count('(+)') - fudges.count('(-)') + bonus
    print((' '.join(fudges) + ' + (' + str(bonus) + ') = ') + str(total))
elif action == 'roll_genesys':
    roll_genesys([args['gen_b'], args['gen_s'], args['gen_a'], args['gen_d'], args['gen_p'], args['gen_c']])
elif action == 'shuffle':
    shuffle_deck(args['table'].strip())
    print('Shuffled!')
elif action == 'draw':
    print(draw_card(args['table'].strip())
          .replace('Spades', '♠')
          .replace('Hearts', '♥')
          .replace('Diamonds', '♦')
          .replace('Clubs', '♣')
          .replace('Joker', '🃏')
          )
elif action == 'load_utable':
    print(load_user_table(args['table']))
elif action == 'load_uwtable':
    print(load_user_wtable(args['table']))
elif action == 'save_utable':
    print(save_user_table(args['table'], args['contains']))
elif action == 'save_uwtable':
    print(save_user_wtable(args['table'], args['contains']))
elif action == 'update':
    print(download_master())
elif action == 'aisetup':
    setup_ai(args['prompt'])
    print("Done")
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
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
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
    elif not os.path.exists(AI_HISTORY_FILE):
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
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
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
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
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
    client = get_client()
    response = client.images.generate(
        prompt=prompt,
        size=img_size,
        quality=img_quality,
        style=img_style,
        response_format='url' if img_format=='markdown' else img_format,
        n=1,
        model='dall-e-3'
    )
    if img_format == 'b64_json':
        answer = response.data[0].b64_json.strip()
    else:
        answer = response.data[0].url.strip()
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
    raise Exception("Wrong Function argument!")
