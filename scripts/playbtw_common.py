# Author: JeansenVaars
# Consider inviting me a Coffee, this took quite some work! -> https://ko-fi.com/JeansenVaars
# Check out my Blog -> https://jvhouse.xyz/
# Use at your OWN RISK

import os
import tempfile
import random
import csv
import dice

import regex as re

if 'CONFIG' not in os.environ:
    raise Exception("PBTW Error: CONFIG key not found. Espanso is not installed?")


# List TXT tables
def list_tables(tp, contains=''):
    files = os.listdir(os.path.join(os.environ['CONFIG'], 'tables'))
    names = []
    for file in files:
        split = os.path.splitext(file)
        if split[1] == tp and split[0].__contains__(contains):
            names.append(split[0])
    names.sort()
    return '\n'.join(names)


# Reads CSV table with exactly one column.
def read_table(table, override_dir=None):
    path = os.path.join(override_dir, table+'.txt') if override_dir else os.path.join(os.environ['CONFIG'], 'tables', table+'.txt')
    if not os.path.exists(path):
        return [f'User defined list not setup: (%s) ' % table.replace('_', ' ')]
    with open(path, encoding='utf-8') as file:
        lines = file.readlines()
    return list(map(lambda x: x.strip(), lines))


# Reads CSV table with exactly two columns. First column must be the max value in such range. Second column the value.
def read_wtable(table, override_dir=None):
    rows = []
    path = os.path.join(override_dir, table+'.psv') if override_dir else os.path.join(os.environ['CONFIG'], 'tables', table+'.psv')
    if not os.path.exists(path):
        return ['Weighted table not found']
    with open(path, encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|', quotechar='"')
        for row in spamreader:
            rows.append(row)
    return rows


def unwrap(result):
    nested = re.sub("u{{(\\w+)}}", lambda x: choice_table(x[1], override_dir=os.path.join(tempfile.gettempdir())), result)
    nested = re.sub("w{{(\\w+)}}", lambda x: choice_wtable(x[1]), nested)
    nested = re.sub("{{(\\w+)}}", lambda x: choice_table(x[1]), nested)
    return nested


# Rolls random from a table once
def choice_table(table, mode=None, override_dir=None):
    values = read_table(table, override_dir=override_dir)
    rolled = random.randint(0, len(values)-1)
    if mode == 'adv':
        rolled = max(rolled, random.randint(0, len(values)-1))
    elif mode == 'dis':
        rolled = min(rolled, random.randint(0, len(values)-1))
    result = unwrap(values[rolled])
    return result


# Rolls random from a weighted table once, based on the max values provided on first column
def choice_wtable(table, mode=None, override_dir=None):
    values = read_wtable(table, override_dir=override_dir)
    max_value = int(values[-1][0])
    rolled = random.randint(1, max_value)
    if mode == 'adv':
        rolled = max(rolled, random.randint(1, max_value))
    elif mode == 'dis':
        rolled = min(rolled, random.randint(1, max_value))
    for e in values:
        if rolled <= int(e[0]):
            return unwrap(e[1])


def roll_dice(q, s):
    total = 0
    values = []
    for i in range(0, q):
        res = random.randint(1, s)
        values.append(str(res))
        total += res
    return {'values': values, 'total': total}


def roll_advanced(formula):
    return dice.roll(formula)


def rolls_advanced(formula):
    return sum(dice.roll(formula))


def shuffle_deck(table):
    cards = read_table(table)
    random.shuffle(cards)
    with open(os.path.join(tempfile.gettempdir(), '__cards_'+table+'.txt'), 'w', encoding='utf-8') as play_deck:
        play_deck.write('\n'.join(cards))
    return cards


def draw_card(table):
    drawn = ''
    if not os.path.exists(os.path.join(tempfile.gettempdir(), '__cards_'+table+'.txt')):
        shuffle_deck(table)
    with open(os.path.join(tempfile.gettempdir(), '__cards_'+table+'.txt'), 'r', encoding='utf-8') as play_deck:
        cards = list(map(lambda x: x.strip(), play_deck.readlines()))
    if not cards:
        cards = shuffle_deck(table)
        drawn += '(Shuffled!) '
    drawn += cards[0].strip()
    with open(os.path.join(tempfile.gettempdir(), '__cards_'+table+'.txt'), 'w', encoding='utf-8') as play_deck:
        play_deck.write('\n'.join(cards[1:]))
    return drawn

# Open user defined table
def load_user_table(name, default=''):
    path = os.path.join(tempfile.gettempdir(), name+'.txt')
    if os.path.exists(path):
        with open(path, 'r') as mem:
            content = mem.read()
            return content if content else default
    else:
        return default
    
# Open user defined wtable
def load_user_wtable(name, default=''):
    path = os.path.join(tempfile.gettempdir(), name+'.psv')
    if os.path.exists(path):
        with open(path, 'r') as mem:
            content = mem.read()
            return content if content else default
    else:
        return default
    
# Save user defined table
def save_user_table(name, content):
    path = os.path.join(tempfile.gettempdir(), name+'.txt')
    with open(path, 'w') as f:
        f.write(content)
    return 'List updated:\n'+content

# Save user defined wtable
def save_user_wtable(name, content):
    path = os.path.join(tempfile.gettempdir(), name+'.psv')
    with open(path, 'w') as f:
        f.write(content)
    return 'List updated:\n'+content
    
# Roll user defined table
def roll_user_table(name):
    override_dir = os.path.join(tempfile.gettempdir())
    return choice_table(name, override_dir=override_dir)

# Roll user defined wtable
def roll_user_wtable(name):
    override_dir = os.path.join(tempfile.gettempdir())
    return choice_wtable(name, override_dir=override_dir)
