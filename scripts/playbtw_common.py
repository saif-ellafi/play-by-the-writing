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

PBWDIR = os.path.join(os.path.expanduser('~'), 'PlayBTW')
def pbwdir_path(path, *paths):
    """
    Creates an absolute path to a subpath of the user-config directory PBWDIR.
    """
    path = os.path.join(PBWDIR, path, *paths)
    return path

# Ensure user config folder structure exists, otherwise opening files will fail due to missing directory.
empty_user_folders = ['cards_tables', 'list_tables', 'config', 'data_ai']
for folder in empty_user_folders:
    path = pbwdir_path(folder)
    os.makedirs(path, exist_ok=True)

TREV = 1000

# Record trev in hidden file.
trev_path = pbwdir_path('.pbtwtrev')
if not os.path.exists(trev_path):
    with open(trev_path, mode='w', encoding='utf-8') as trevlocal:
        trevlocal.write(str(TREV))

# If newly creating my_tables, also install example tables.
my_tables = 'my_tables'
my_tables_path = pbwdir_path(my_tables)
if not os.path.exists(my_tables_path):
    os.makedirs(my_tables_path, exist_ok=True)
    demo_tables = {
        'example.txt':
            'First result\nSecond result\nThird result',
        'example.psv':
            '25|First quarter\n50|First half\n75|Next quarter\n100|Last quarter',
        }
    for filename, contents in demo_tables.items():
        path = pbwdir_path(my_tables, filename)
        with open(path, mode='w', encoding='utf-8') as file:
            file.write(contents)

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
        with open(os.path.join(temp_dir, 'pbtw_files', 'play-by-the-writing-main', '.pbtwtrev'), encoding='utf-8') as trevpull:
            with open(os.path.join(PBWDIR, '.pbtwtrev'), encoding='utf-8') as trevlocal:
                newrev = int(trevpull.readline().strip())
                update_available = newrev > int(trevlocal.read().strip())
                update_notes = trevpull.readline().strip()
    if update_available:
        distutils.dir_util.copy_tree(os.path.join(temp_dir, 'pbtw_files', 'play-by-the-writing-main', 'tables'), os.path.join(os.environ['CONFIG'], 'tables'))
        distutils.dir_util.copy_tree(os.path.join(temp_dir, 'pbtw_files', 'play-by-the-writing-main', 'match'), os.path.join(os.environ['CONFIG'], 'match'))
        with open(os.path.join(PBWDIR, '.pbtwtrev'), mode='w', encoding='utf-8') as trevlocal:
            trevlocal.write(str(newrev))
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
    with open(os.path.join(PBWDIR, 'cards_tables', '__cards_'+table+'.txt'), 'w', encoding='utf-8') as play_deck:
        play_deck.write('\n'.join(cards))
    return cards


def draw_card(table):
    drawn = ''
    if not os.path.exists(os.path.join(PBWDIR, 'cards_tables', '__cards_'+table+'.txt')):
        shuffle_deck(table)
    with open(os.path.join(PBWDIR, 'cards_tables', '__cards_'+table+'.txt'), 'r', encoding='utf-8') as play_deck:
        cards = list(map(lambda x: x.strip(), play_deck.readlines()))
    if not cards:
        cards = shuffle_deck(table)
        drawn += '(Shuffled!) '
    drawn += cards[0].strip()
    with open(os.path.join(PBWDIR, 'cards_tables', '__cards_'+table+'.txt'), 'w', encoding='utf-8') as play_deck:
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
