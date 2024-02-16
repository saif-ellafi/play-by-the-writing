# Author: JeansenVaars
# Consider inviting me a Coffee, this took quite some work! -> https://ko-fi.com/JeansenVaars
# Check out my Blog -> https://jvhouse.xyz/
# Use at your OWN RISK

import os
import sys
import tempfile
import random
import csv
import dice

import regex as re

from playbtw_genesys import GenesysDiceRoller

sys.stdout.reconfigure(encoding="utf-8")

if 'CONFIG' not in os.environ:
    raise Exception("PBTW Error: CONFIG key not found. Espanso is not installed?")

if not os.path.exists(os.path.join(os.environ['CONFIG'], 'user_tables')):
    os.mkdir(os.path.join(os.environ['CONFIG'], 'user_tables'))
    with open(os.path.join(os.environ['CONFIG'], 'user_tables', 'example.txt'), mode='w', encoding='utf-8') as file:
        file.write('First result\nSecond result\nThird result')
    with open(os.path.join(os.environ['CONFIG'], 'user_tables', 'example.psv'), mode='w', encoding='utf-8') as file:
        file.write('25|First quarter\n50|First half\n75|Next quarter\n100|Last quarter')

PBWDIR = os.path.join(os.path.expanduser('~'), 'PlayBTW')

TREV = 1000

if not os.path.exists(PBWDIR):
    os.mkdir(PBWDIR)

if not os.path.exists(os.path.join(PBWDIR, 'config')):
    os.mkdir(os.path.join(PBWDIR, 'config'))

if not os.path.exists(os.path.join(PBWDIR, 'ai')):
    os.mkdir(os.path.join(PBWDIR, 'ai'))

# Download the master repo zip file and extract it in CONFIG dir using urllib
def download_master():
    import urllib.request
    import zipfile
    import shutil
    import distutils.dir_util

    url = 'https://codeload.github.com/saif-ellafi/play-by-the-writing/zip/refs/heads/main'
    temp_dir = tempfile.gettempdir()
    temp_file = temp_dir+'/master.zip'
    urllib.request.urlretrieve(url, temp_file)
    with zipfile.ZipFile(temp_file, 'r') as zip_ref:
        zip_ref.extractall(os.path.join(temp_dir, 'pbtw_files'))    
    # copy folders 'tables' and 'match' to CONFIG dir, merge files if already exist
        with open(os.path.join(temp_dir, '.playbtw_trev'), encoding='utf-8') as trev:
            update_available = int(trev.readline().strip()) > TREV
            update_notes = trev.readline().strip()
    if update_available:
        distutils.dir_util.copy_tree(os.path.join(temp_dir, 'pbtw_files', 'play-by-the-writing-main', 'tables'), os.path.join(os.environ['CONFIG'], 'tables'))
        distutils.dir_util.copy_tree(os.path.join(temp_dir, 'pbtw_files', 'play-by-the-writing-main', 'match'), os.path.join(os.environ['CONFIG'], 'match'))
        text = 'Updated: ' + update_notes
    else:
        text = 'Already up to date'
    # delete the remaining downloaded files
    shutil.rmtree(os.path.join(temp_dir, 'pbtw_files'))
    os.remove(temp_file)
    return text


def setup_ai(key):
    path = os.path.join(PBWDIR, 'config', 'openai.txt')
    with open(path, mode='w', encoding='utf-8') as file:
        file.write(key)


# Reads CSV table with exactly one column.
def read_table(table, override_dir=None, default=None):
    path = os.path.join(override_dir, table+'.txt') if override_dir else os.path.join(os.environ['CONFIG'], 'tables', table+'.txt')
    # check otherwise in the user folder
    if not os.path.exists(path):
        path = os.path.join(PBWDIR, 'user_tables', table+'.txt')
    if not os.path.exists(path):
        if default:
            with open(path, 'w') as f:
                f.write(default)
        else:
            return [f'List not found: (%s) ' % table]
    with open(path, encoding='utf-8') as file:
        lines = file.readlines()
    return list(map(lambda x: x.strip(), lines))


# Reads CSV table with exactly two columns. First column must be the max value in such range. Second column the value.
def read_wtable(table, override_dir=None, default=None):
    rows = []
    path = os.path.join(override_dir, table+'.psv') if override_dir else os.path.join(os.environ['CONFIG'], 'tables', table+'.psv')
    # check otherwise in the user folder
    if not os.path.exists(path):
        path = os.path.join(PBWDIR, 'user_tables', table+'.psv')
    if not os.path.exists(path):
        if default:
            with open(path, 'w') as f:
                f.write(default)
        else:
            return [f'Weighted list not found: (%s) ' % table]
    with open(path, encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|', quotechar='"')
        for row in spamreader:
            rows.append(row)
    return rows


def unwrap(result):
    nested = re.sub("u{{(\\w+)}}", lambda x: choice_table(x[1], override_dir=PBWDIR), result)
    nested = re.sub("w{{(\\w+)}}", lambda x: choice_wtable(x[1]), nested)
    nested = re.sub("{{(\\w+)}}", lambda x: choice_table(x[1]), nested)
    return nested


# Rolls random from a table once
def choice_table(table, mode=None, override_dir=None, default=None):
    values = read_table(table, override_dir=override_dir, default=default)
    rolled = random.randint(0, len(values)-1)
    if mode == 'adv':
        rolled = max(rolled, random.randint(0, len(values)-1))
    elif mode == 'dis':
        rolled = min(rolled, random.randint(0, len(values)-1))
    result = unwrap(values[rolled])
    return result


# Rolls random from a weighted table once, based on the max values provided on first column
def choice_wtable(table, mode=None, override_dir=None, default=None):
    values = read_wtable(table, override_dir=override_dir, default=default)
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
    roll = dice.roll(formula, raw=True)
    # triggers evaluate and includes member 'result'
    details = dice.utilities.verbose_print(roll)
    # apply regex to select the last piece of text that looks like [3, 2] or [5, 1, 2]
    parts = re.findall(r'(\[(\d+,\s)*\d+\])', details)
    # return the longest string among components
    longest_part = max(parts, key=lambda x: len(x[0]))[0]
    # result member is only available after evaluation
    result = roll.result
    if type(result) == dice.elements.Integer:
        return formula + ': ' + longest_part + ' = ' + str(result)
    else:
        return formula + ': ' + longest_part + ' = ' + str(sum(result))


def rolls_advanced(formula):
    roll = dice.roll(formula)
    if type(roll) == dice.elements.Integer:
        return int(roll)
    else:
        return sum(roll)


# Roll Genesys dice
def roll_genesys(dice_array):
    GenesysDiceRoller(dice_array).displayResults()


def shuffle_deck(table):
    cards = read_table(table)
    random.shuffle(cards)
    with open(os.path.join(PBWDIR, '__cards_'+table+'.txt'), 'w', encoding='utf-8') as play_deck:
        play_deck.write('\n'.join(cards))
    return cards


def draw_card(table):
    drawn = ''
    if not os.path.exists(os.path.join(PBWDIR, '__cards_'+table+'.txt')):
        shuffle_deck(table)
    with open(os.path.join(PBWDIR, '__cards_'+table+'.txt'), 'r', encoding='utf-8') as play_deck:
        cards = list(map(lambda x: x.strip(), play_deck.readlines()))
    if not cards:
        cards = shuffle_deck(table)
        drawn += '(Shuffled!) '
    drawn += cards[0].strip()
    with open(os.path.join(PBWDIR, '__cards_'+table+'.txt'), 'w', encoding='utf-8') as play_deck:
        play_deck.write('\n'.join(cards[1:]))
    return drawn


# Open user defined table
def load_user_table(name, default=''):
    path = os.path.join(PBWDIR, name+'.txt')
    if os.path.exists(path):
        with open(path, 'r') as mem:
            content = mem.read()
            return content if content else default
    else:
        return default


# Open user defined wtable
def load_user_wtable(name, default=''):
    path = os.path.join(PBWDIR, name+'.psv')
    if os.path.exists(path):
        with open(path, 'r') as mem:
            content = mem.read()
            return content if content else default
    else:
        return default


# Save user defined table
def save_user_table(name, content):
    path = os.path.join(PBWDIR, name+'.txt')
    with open(path, 'w') as f:
        f.write(content)
    return content


# Save user defined wtable
def save_user_wtable(name, content):
    path = os.path.join(PBWDIR, name+'.psv')
    with open(path, 'w') as f:
        f.write(content)
    return content


# Roll user defined table
def roll_user_table(name, default=None):
    return choice_table(name, override_dir=PBWDIR, default=default)


# Roll user defined wtable
def roll_user_wtable(name, default=None):
    return choice_wtable(name, override_dir=PBWDIR, default=default)
