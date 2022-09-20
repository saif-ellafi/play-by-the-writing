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
    raise Exception("CONFIG key not found. Espanso is not installed?")


# List TXT tables
def list_tables(tp):
    files = os.listdir(os.path.join(os.environ['CONFIG'], 'tables'))
    names = []
    for file in files:
        split = os.path.splitext(file)
        if split[1] == tp:
            names.append(split[0])
    names.sort()
    return '\n'.join(names)


# Reads CSV table with exactly one column.
def read_table(table):
    with open(os.path.join(os.environ['CONFIG'], 'tables', table+'.txt'), encoding='utf-8') as file:
        lines = file.readlines()
    return list(map(lambda x: x.strip(), lines))


# Reads CSV table with exactly two columns. First column must be the max value in such range. Second column the value.
def read_wtable(table):
    rows = []
    with open(os.path.join(os.environ['CONFIG'], 'tables', table+'.psv'), encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|', quotechar='"')
        for row in spamreader:
            rows.append(row)
    return rows


def unwrap(result):
    nested = re.sub("w{{(\\w+)}}", lambda x: choice_wtable(x[1]), result)
    nested = re.sub("{{(\\w+)}}", lambda x: choice_table(x[1]), nested)
    return nested


# Rolls random from a table once
def choice_table(table):
    values = read_table(table)
    result = unwrap(random.choice(values))
    return result


# Rolls random from a weighted table once, based on the max values provided on first column
def choice_wtable(table):
    values = read_wtable(table)
    max_value = int(values[-1][0])
    rolled = random.randint(1, max_value)
    for e in values:
        if rolled <= int(e[0]):
            return unwrap(e[1])


def roll_dice(q, s):
    total = 0
    for i in range(0, q):
        total += random.randint(1, s)
    return total


def roll_advanced(formula):
    return dice.roll(formula)


def rolls_advanced(formula):
    return sum(dice.roll(formula))


def shuffle_deck(table):
    cards = read_table(table)
    random.shuffle(cards)
    with open(os.path.join(tempfile.gettempdir(), '__play_'+table+'.txt'), 'w', encoding='utf-8') as play_deck:
        play_deck.write('\n'.join(cards))
    return cards


def draw_card(table):
    drawn = ''
    if not os.path.exists(os.path.join(tempfile.gettempdir(), '__play_'+table+'.txt')):
        shuffle_deck(table)
    with open(os.path.join(tempfile.gettempdir(), '__play_'+table+'.txt'), 'r', encoding='utf-8') as play_deck:
        cards = list(map(lambda x: x.strip(), play_deck.readlines()))
    if not cards:
        cards = shuffle_deck(table)
        drawn += '(Shuffled!) '
    drawn += cards[0].strip()
    with open(os.path.join(tempfile.gettempdir(), '__play_'+table+'.txt'), 'w', encoding='utf-8') as play_deck:
        play_deck.write('\n'.join(cards[1:]))
    return drawn
