# -*- mode: python ; coding: utf-8 -*-

from md2pdf.core import md2pdf

import shutil
import os
import glob

if os.path.isdir('{0}/../match'):
    shutil.rmtree('{0}/../match'.format(DISTPATH), ignore_errors=True)
if os.path.isdir('{0}/../tables'):
    shutil.rmtree('{0}/../tables'.format(DISTPATH), ignore_errors=True)
if os.path.isdir('{0}/../config'):
    shutil.rmtree('{0}/../config'.format(DISTPATH), ignore_errors=True)

os.makedirs('{0}/../match'.format(DISTPATH), exist_ok=True)
os.makedirs('{0}/../tables'.format(DISTPATH), exist_ok=True)
os.makedirs('{0}/../config'.format(DISTPATH), exist_ok=True)

md2pdf('README.pdf', md_file_path='README.md', css_file_path='pdf.css', base_url='./')

shutil.move('README.pdf', '{0}/../README.pdf'.format(DISTPATH))

shutil.copy('match/playbtw_core.yml', '{0}/../match/'.format(DISTPATH))
shutil.copy('match/playbtw_mythic.yml', '{0}/../match/'.format(DISTPATH))
shutil.copy('match/playbtw_pum.yml', '{0}/../match/'.format(DISTPATH))
shutil.copy('match/playbtw_gum.yml', '{0}/../match/'.format(DISTPATH))
shutil.copy('match/playbtw_opse.yml', '{0}/../match/'.format(DISTPATH))
shutil.copy('match/playbtw_ai.yml', '{0}/../match/'.format(DISTPATH))
shutil.copy('config/openai.txt', '{0}/../config/'.format(DISTPATH))

if os.path.exists('dist_core/scripts/playbtw_core.exe'):
    shutil.copy('dist_core/scripts/playbtw_core.exe', '{0}/../scripts/'.format(DISTPATH))
    shutil.copy('dist_mythic/scripts/playbtw_mythic.exe', '{0}/../scripts/'.format(DISTPATH))
    shutil.copy('dist_ai/scripts/playbtw_ai.exe', '{0}/../scripts/'.format(DISTPATH))
else:
    shutil.copy('dist_core/scripts/playbtw_core', '{0}/../scripts/'.format(DISTPATH))
    shutil.copy('dist_mythic/scripts/playbtw_mythic', '{0}/../scripts/'.format(DISTPATH))
    shutil.copy('dist_ai/scripts/playbtw_ai', '{0}/../scripts/'.format(DISTPATH))

for f in glob.glob('tables/*'):
    shutil.copy2(f, '{0}/../tables/'.format(DISTPATH))

shutil.make_archive('PlayBTW_v1_34_base_with_ai', 'zip', 'dist_all_ai')
