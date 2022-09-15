# Author: JeansenVaars
# Consider inviting me a Coffee, this took quite some work! -> https://ko-fi.com/JeansenVaars
# Check out my Blog -> https://jvhouse.xyz/
# Use at your OWN RISK

import argparse
from playbtw_common import *


parser = argparse.ArgumentParser(description='Play by the Writing - Oracle for Espanso')
parser.add_argument('action', type=str, help='stakes|intent|property|')


args = vars(parser.parse_args())
action = args['action']

if action == 'stakes':
    print('On Success: %s - On Failure: %s' % (choice_table('pum_ch_success'), choice_table('pum_ch_fail')))
elif action == 'intent':
    print('They %s %s.' % (choice_table('pum_inta'), choice_table('pum_intb')))
elif action == 'activity':
    print('They are %s %s.' % (choice_table('pum_acta'), choice_table('pum_actb')))
elif action == 'property':
    print('It can %s, through %s.' % (choice_table('pum_prop_can'), choice_table('pum_prop_with')))
else:
    raise Exception("Wrong Function argument!")
