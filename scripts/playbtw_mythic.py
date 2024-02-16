# Author: JeansenVaars
# Consider inviting me a Coffee, this took quite some work! -> https://ko-fi.com/JeansenVaars
# Check out my Blog -> https://jvhouse.xyz/
# Use at your OWN RISK

from playbtw_common import *

import argparse

parser = argparse.ArgumentParser(description='Oracle for Espanso')
parser.add_argument('action', type=str, help='fate_check|scene_check|random_event')
parser.add_argument('--odds', type=int, default=0, help='Odds towards result. From -8 to +8')
parser.add_argument('--chaos', type=int, default=5, help='Chaos Factor. From 3 to 6')

args = vars(parser.parse_args())
action = args['action']
chaos_map = {
    1: -5,
    2: -4,
    3: -2,
    4: -1,
    5: 0,
    6: 1,
    7: 2,
    8: 4,
    9: 5
}


def fate_check(odds=0, chaos_rank=5):
    answer = 'Yes'
    rint1 = rolls_advanced('1d10')
    rint2 = rolls_advanced('1d10')
    chaos_mod = chaos_map[chaos_rank]
    core = rint1 + rint2 + odds + chaos_mod
    if core < 2:
        answer = 'No'
    elif core <= 4:
        answer = 'Exceptional No'
    elif core <= 10:
        answer = 'No'
    elif core >= 18 and core <= 20:
        answer = 'Exceptional Yes'
    if rint1 == rint2 and rint1 <= chaos_rank:
        answer += ', with a Random Event: ' + random_event()
    return answer


def scene_check(chaos=5):
    rolled = rolls_advanced('1d10')
    if rolled <= chaos:
        if rolled % 2 == 0:
            return 'Interrupt Scene! ' + random_event()
        else:
            return 'Altered Scene'
    else:
        return 'Expected Scene'


def random_event():
    return '%s: %s %s' % (choice_wtable('mythic_list_focus'), choice_table('mythic_action_1'), choice_table('mythic_action_2'))


if action == 'fate_check':
    print(fate_check(args['odds'], args['chaos']))
elif action == 'scene_check':
    print(scene_check(args['chaos']))
elif action == 'random_event':
    print(random_event())
else:
    raise Exception("Wrong Function argument!")
