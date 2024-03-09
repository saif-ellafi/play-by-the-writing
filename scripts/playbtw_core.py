# Author: JeansenVaars
# Consider inviting me a Coffee, this took quite some work! -> https://ko-fi.com/JeansenVaars
# Check out my Blog -> https://jvhouse.xyz/
# Use at your OWN RISK

import argparse
from playbtw_common import *

parser = argparse.ArgumentParser(description='Play by the Writing - Oracle for Espanso')
parser.add_argument('action', type=str, help='|action|description|table|wtable|roll_dice|roll_fudge|shuffle|draw|load_utable|save_utable|aisetup|update')
parser.add_argument('--mods', type=int, default=0, help='Modifier, Numeric, various use cases')
parser.add_argument('--mode', type=str, default=None, help='Roll mode, supports normal|adv|dis')
parser.add_argument('--table', type=str, help='Random Table Key')
parser.add_argument('--formula', type=str, help='Dice formula')
parser.add_argument('--contains', type=str, default='', help='Contains sub expressions and content')
parser.add_argument('--quantity', type=int, help='Simple Roll dice quantity')
parser.add_argument('--size', type=int, help='Simple Roll dice size')

parser.add_argument('--gen_a', type=int, help='Genesys dice ability')
parser.add_argument('--gen_p', type=int, help='Genesys dice proficiency')
parser.add_argument('--gen_b', type=int, help='Genesys dice boost')
parser.add_argument('--gen_d', type=int, help='Genesys dice difficulty')
parser.add_argument('--gen_c', type=int, help='Genesys dice challenge')
parser.add_argument('--gen_s', type=int, help='Genesys dice setback')

args = vars(parser.parse_args())

TREV = 1003

# Record trev in hidden file.
trev_path = pbwdir_path('.pbtwtrev')
if not os.path.exists(trev_path):
    with open(trev_path, mode='w', encoding='utf-8') as trevlocal:
        trevlocal.write(str(TREV))

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
elif action == 'aisetup':
    setup_ai(args['formula'])
    print("Done")
elif action == 'update':
    print(download_master())
elif action == 'roll_dice':
    print(roll_advanced(args['formula']))
elif action == 'roll_fudge':
    fudges = []
    bonus = args['mods']
    def map_fudge(value):
        if value in [1, 2]:
            return '(-)'
        elif value in [3, 4]:
            return '( )'
        else:
            return '(+)'
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
else:
    raise Exception("Wrong Function argument!")
