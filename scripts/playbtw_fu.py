# Author: JeansenVaars
# Consider inviting me a Coffee, this took quite some work! -> https://ko-fi.com/JeansenVaars
# Check out my Blog -> https://jvhouse.xyz/
# Use at your OWN RISK

from playbtw_common import *

import argparse

parser = argparse.ArgumentParser(description='Oracle for Espanso')
parser.add_argument('action', type=str, help='fu_oracle|fu_quality')
parser.add_argument('--fuadv', type=str, help='FU advantage. Either n,a,d')

args = vars(parser.parse_args())
action = args['action']


if action == 'fu_oracle':
    result = rolls_advanced('1d6')
    if args['fuadv'].strip() == 'a':
        result = max(result, rolls_advanced('1d6'))
    elif args['fuadv'].strip() == 'd':
        result = min(result, rolls_advanced('1d6'))
    if result == 1:
        print('No, and...')
    elif result == 3:
        print('No...')
    elif result == 5:
        print('No, but...')
    elif result == 2:
        print('Yes, but...')
    elif result == 4:
        print('Yes')
    elif result == 6:
        print('Yes, and...')
    else:
        raise Exception("Bad FU Oracle")
elif action == 'fu_quality':
    result = rolls_advanced('1d6')
    if args['fuadv'].strip() == 'a':
        result = max(result, rolls_advanced('1d6'))
    elif args['fuadv'].strip() == 'd':
        result = min(result, rolls_advanced('1d6'))
    if result == 1:
        print('Epic failure, and then some...')
    elif result == 3:
        print('Complete failure')
    elif result == 5:
        print('Fail by the smalles margin')
    elif result == 2:
        print('Only just succeed')
    elif result == 4:
        print('Complete success')
    elif result == 6:
        print('Legendary success')
    else:
        raise Exception("Bad FU Oracle")
else:
    raise Exception("Wrong Function argument!")
