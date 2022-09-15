# Author: JeansenVaars
# Consider inviting me a Coffee, this took quite some work! -> https://ko-fi.com/JeansenVaars
# Check out my Blog -> https://jvhouse.xyz/
# Use at your OWN RISK

from playbtw_common import *

import argparse

parser = argparse.ArgumentParser(description='Oracle for Espanso')
parser.add_argument('action', type=str, help='fate_check|focus|action|description|fu_oracle|fu_quality|mnpc|')
parser.add_argument('--odds', type=int, default=0, help='Odds towards result. From -8 to +8')
parser.add_argument('--chaos', type=int, default=4, help='Chaos Factor. From 3 to 6')
parser.add_argument('--favorable', type=int, default=1, help='Is yes a favorable answer? 0 is no. 1 is yes.')

args = vars(parser.parse_args())
action = args['action']


def fate_check(odds=0, chaos_rank=4, favorable=True):
    answer = 'Yes'
    rint1 = rolls_advanced('1d10')
    rint2 = rolls_advanced('1d10')
    core = rint1 + rint2 + odds
    chaos_roll = rolls_advanced('1d10')
    if chaos_rank == 3:
        if favorable:
            core += 2
        else:
            core -= 2
    elif chaos_rank == 6:
        if favorable:
            core -= 2
        else:
            core += 2
    if core < 11:
        answer = 'No'
    if chaos_roll <= chaos_rank:
        if rint1 % 2 == 1 and rint2 % 2 == 1:
            answer = 'Exceptional ' + answer
        elif rint1 % 2 == 0 and rint2 % 2 == 0:
            answer += ' with Random Event!'
    return answer


def scene_check(chaos=4):
    rolled = rolls_advanced('1d10')
    if rolled <= chaos:
        if rolled % 2 == 0:
            return 'Scene altered!'
        else:
            return 'Scene interrupted!'
    else:
        return 'Proceeds normally!'


if action == 'fate_check':
    print(fate_check(args['odds'], args['chaos'], args['favorable']))
elif action == 'scene_check':
    print(scene_check(args['chaos']))
else:
    raise Exception("Wrong Function argument!")
