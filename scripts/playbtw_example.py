# Author: JeansenVaars
# Consider inviting me a Coffee, this took quite some work! -> https://ko-fi.com/JeansenVaars
# Check out my Blog -> https://jvhouse.xyz/
# Use at your OWN RISK

import argparse


parser = argparse.ArgumentParser(description='Play by the Writing - Oracle for Espanso')
parser.add_argument('action', type=str, help='|example|')

args = vars(parser.parse_args())
action = args['action']

if action == 'example':
    print('[' + 'Play by the Writing works fine!' + ']')
else:
    raise Exception("Wrong Function argument!")
