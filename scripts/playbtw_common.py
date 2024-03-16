# Author: JeansenVaars
# Consider inviting me a Coffee, this took quite some work! -> https://ko-fi.com/JeansenVaars
# Check out my Blog -> https://jvhouse.xyz/
# Use at your OWN RISK

import os
import random
import csv
import rolldice

import regex as re

from playbtw_genesys import GenesysDiceRoller

if 'CONFIG' not in os.environ:
    raise Exception("PBTW Error: CONFIG key not found. Espanso is not installed?")

PBWDIR = os.path.join(os.path.expanduser('~'), 'PlayBTW')

# Ensure user config folder structure exists, otherwise opening files will fail due to missing directory.
empty_user_folders = ['cards_tables', 'my_tables', 'list_tables', 'data_ai', 'config']
for folder in empty_user_folders:
    fpath = os.path.join(PBWDIR, folder)
    if not os.path.exists(fpath):
        os.makedirs(fpath, exist_ok=True)
        if folder == 'my_tables':
            demo_tables = {
                'example.txt':
                    'First result\nSecond result\nThird result',
                'example.psv':
                    '25|First quarter\n50|First half\n75|Next quarter\n100|Last quarter',
            }
            for filename, contents in demo_tables.items():
                file_path = os.path.join(fpath, filename)
                with open(file_path, mode='w', encoding='utf-8') as efile:
                    efile.write(contents)


# Reads CSV table with exactly one column.
def read_table(table):
    path1 = os.path.join(PBWDIR, 'list_tables', table+'.txt')
    path2 = os.path.join(PBWDIR, 'my_tables', table+'.txt')
    path3 = os.path.join(os.environ['CONFIG'], 'tables', table+'.txt')
    # check otherwise in the user folder
    if os.path.exists(path1):
        path = path1
    elif os.path.exists(path2):
        path = path2
    elif os.path.exists(path3):
        path = path3
    else:
        return [f'List not found: (%s) ' % table]
    with open(path, encoding='utf-8') as file:
        lines = file.readlines()
    return list(map(lambda x: x.strip(), lines))


# Reads CSV table with exactly two columns. First column must be the max value in such range. Second column the value.
def read_wtable(table):
    rows = []
    path1 = os.path.join(PBWDIR, 'list_tables', table+'.psv')
    path2 = os.path.join(PBWDIR, 'my_tables', table+'.psv')
    path3 = os.path.join(os.environ['CONFIG'], 'tables', table+'.psv')
    # check otherwise in the user folder
    if os.path.exists(path1):
        path = path1
    elif os.path.exists(path2):
        path = path2
    elif os.path.exists(path3):
        path = path3
    else:
        return [[1, f'Weighted list not found: (%s) ' % table]]
    with open(path, encoding='utf-8') as psvfile:
        spamreader = csv.reader(psvfile, delimiter='|', quotechar='"')
        for row in spamreader:
            rows.append(row)
    return rows


def unwrap(result):
    nested = re.sub("w{{(\\w+)}}", lambda x: choice_wtable(x[1]), result)
    nested = re.sub("{{(\\w+)}}", lambda x: choice_table(x[1]), nested)
    return nested


# Rolls random from a table once
def choice_table(table, mode=None):
    values = read_table(table)
    rolled = random.randint(0, len(values)-1)
    if mode == 'adv':
        rolled = max(rolled, random.randint(0, len(values)-1))
    elif mode == 'dis':
        rolled = min(rolled, random.randint(0, len(values)-1))
    result = unwrap(values[rolled])
    return result


# Rolls random from a weighted table once, based on the max values provided on first column
def choice_wtable(table, mode=None):
    values = read_wtable(table)
    max_value = int(values[-1][0])
    rolled = random.randint(1, max_value)
    if mode == 'adv':
        rolled = max(rolled, random.randint(1, max_value))
    elif mode == 'dis':
        rolled = min(rolled, random.randint(1, max_value))
    for e in values:
        if rolled <= int(e[0]):
            return unwrap(e[1])


# Simple dice roller. No longer used but kept for internal use
def roll_dice(q, s):
    total = 0
    values = []
    for i in range(0, q):
        res = random.randint(1, s)
        values.append(str(res))
        total += res
    return {'values': values, 'total': total}


# dice library is weird... different functions have different return types based on the formula given... act with care
def roll_advanced(formula):
    # CLEANUP IF THE NEW ROLLDICE LIB WORKS WELL
    # triggers evaluate and includes member 'result'
    # details = dice.utilities.verbose_print(roll)
    # apply regex to select the last piece of text that looks like [3, 2] or [5, 1, 2]
    # parts = re.findall(r'(\[(\d+,\s)*\d+\])', details)
    # return the longest string among components
    # longest_part = max(parts, key=lambda x: len(x[0]))[0]
    # result member is only available after evaluation
    return rolldice.roll_dice(formula)


def fate_check(odds=0, chaos_rank=5):
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
    answer = 'Yes'
    rint1 = roll_advanced('1d10')[0]
    rint2 = roll_advanced('1d10')[0]
    chaos_mod = chaos_map[chaos_rank]
    core = rint1 + rint2 + odds + chaos_mod
    if core < 2:
        answer = 'No'
    elif core <= 4:
        answer = 'Exceptional No'
    elif core <= 10:
        answer = 'No'
    elif 18 <= core <= 20:
        answer = 'Exceptional Yes'
    if rint1 == rint2 and rint1 <= chaos_rank:
        answer += ', with a Random Event: ' + random_event()
    return answer


def scene_check(chaos=5):
    rolled = roll_advanced('1d10')[0]
    if rolled <= chaos:
        if rolled % 2 == 0:
            return 'Interrupt Scene! ' + random_event()
        else:
            return 'Altered Scene'
    else:
        return 'Expected Scene'


def random_event():
    return '%s: %s %s' % (choice_wtable('mythic_list_focus'), choice_table('mythic_action_1'), choice_table('mythic_action_2'))


# Roll Genesys dice
def roll_genesys(dice_array):
    GenesysDiceRoller(dice_array).display_results()


def shuffle_deck(table):
    cards = read_table(table)
    cards_path = os.path.join(PBWDIR, 'cards_tables', '__cards_'+table+'.txt')
    random.shuffle(cards)
    with open(cards_path, 'w', encoding='utf-8') as play_deck:
        play_deck.write('\n'.join(cards))
    return cards


def draw_card(table):
    cards_path = os.path.join(PBWDIR, 'cards_tables', '__cards_'+table+'.txt')
    drawn = ''
    if not os.path.exists(cards_path):
        shuffle_deck(table)
    with open(cards_path, 'r', encoding='utf-8') as play_deck:
        cards = list(map(lambda x: x.strip(), play_deck.readlines()))
    if not cards:
        cards = shuffle_deck(table)
        drawn += '(Shuffled!) '
    drawn += cards[0].strip()
    with open(cards_path, 'w', encoding='utf-8') as play_deck:
        play_deck.write('\n'.join(cards[1:]))
    return drawn


# Open user defined table
def load_user_table(name):
    path = os.path.join(PBWDIR, 'list_tables', name+'.txt')
    default_path = os.path.join(os.environ['CONFIG'], 'tables', name+'.txt')
    if os.path.exists(path):
        with open(path, 'r') as mem:
            return mem.read()
    elif os.path.exists(default_path):
        with open(default_path, 'r') as mem:
            return mem.read()
    else:
        return ''


# Open user defined wtable
def load_user_wtable(name):
    path = os.path.join(PBWDIR, 'list_tables', name+'.psv')
    default_path = os.path.join(os.environ['CONFIG'], 'tables', name+'.psv')
    if os.path.exists(path):
        with open(path, 'r') as mem:
            return mem.read()
    elif os.path.exists(default_path):
        with open(default_path, 'r') as mem:
            return mem.read()
    else:
        return ''


# Save user defined table
def save_user_table(name, content):
    path = os.path.join(PBWDIR, 'list_tables', name+'.txt')
    with open(path, 'w') as f:
        f.write(content)
    return content


# Save user defined wtable
def save_user_wtable(name, content):
    path = os.path.join(PBWDIR, 'list_tables', name+'.psv')
    with open(path, 'w') as f:
        f.write(content)
    return content
