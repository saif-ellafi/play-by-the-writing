# Author: JeansenVaars
# Consider inviting me a Coffee, this took quite some work! -> https://ko-fi.com/JeansenVaars
# Check out my Blog -> https://jvhouse.xyz/
# Use at your OWN RISK

import argparse
import sys
from playbtw_common import *

sys.stdout.reconfigure(encoding="utf-8")

parser = argparse.ArgumentParser(description='Play by the Writing - Oracle for Espanso')
parser.add_argument('action', type=str, help='|action|description|table|wtable|roll_dice|roll_advanced|roll_fudge|shuffle|draw|list|wlist|')
parser.add_argument('--mods', type=int, default=0, help='Modifier, Numeric, various use cases')
parser.add_argument('--table', type=str, help='Random Table Key')
parser.add_argument('--formula', type=str, help='Dice formula')
parser.add_argument('--quantity', type=int, help='Simple Roll dice quantity')
parser.add_argument('--size', type=int, help='Simple Roll dice size')


args = vars(parser.parse_args())
action = args['action']

if action == 'table':
    tables = filter(lambda x: x, map(str.strip, args['table'].split(',')))
    result = []
    for t in tables:
        result.append(choice_table(t.strip()))
    print(' '.join(result))
elif action == 'wtable':
    tables = map(str.strip, args['table'].split(','))
    result = []
    for t in tables:
        result.append(choice_wtable(t.strip()))
    print(' '.join(result))
elif action == 'roll_dice':
    result = roll_dice(args['quantity'], args['size'])
    print(str(args['quantity']) + 'd' + str(args['size']) + ': ' + str(result))
elif action == 'roll_advanced':
    result = roll_advanced(args['formula'])
    if type(result) == dice.elements.Roll:
        print(args['formula'] + ': ' + str(result) + ' = ' + str(sum(result)))
    else:
        print(args['formula'] + ': ' + str(result))
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
        fudges.append(map_fudge(roll))
    total = fudges.count('(+)') - fudges.count('(-)') + bonus
    print((' '.join(fudges) + ' + (' + str(bonus) + ') = ') + str(total))
elif action == 'shuffle':
    shuffle_deck('deck_poker')
    print('Shuffled!')
elif action == 'draw':
    print(draw_card('deck_poker')
          .replace('Spades', '♠')
          .replace('Hearts', '♥')
          .replace('Diamonds', '♦')
          .replace('Clubs', '♣')
          .replace('Joker', '🃏')
          )
elif action == 'list':
    print(list_tables('.txt'))
elif action == 'wlist':
    print(list_tables('.psv'))
else:
    raise Exception("Wrong Function argument!")
