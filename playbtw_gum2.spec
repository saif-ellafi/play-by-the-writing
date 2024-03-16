# -*- mode: python ; coding: utf-8 -*-

import shutil
import os
import glob

if os.path.isdir('{0}/../match'):
    shutil.rmtree('{0}/../match'.format(DISTPATH), ignore_errors=True)
if os.path.isdir('{0}/../tables'):
    shutil.rmtree('{0}/../tables'.format(DISTPATH), ignore_errors=True)

os.makedirs('{0}/../match'.format(DISTPATH), exist_ok=True)
os.makedirs('{0}/../tables'.format(DISTPATH), exist_ok=True)

shutil.copy('match/playbtw_gum2.yml', '{0}/../match/'.format(DISTPATH))

for f in glob.glob('tables/gum*'):
    shutil.copy2(f, '{0}/../tables/'.format(DISTPATH))

shutil.make_archive('PlayBTW_v3_02_gum2', 'zip', 'dist_gum2')
