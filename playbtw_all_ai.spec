# -*- mode: python ; coding: utf-8 -*-

from md2pdf.core import md2pdf

import shutil
import os
import glob

if os.path.isdir('{0}/../match'):
    shutil.rmtree('{0}/../match'.format(DISTPATH), ignore_errors=True)
if os.path.isdir('{0}/../tables'):
    shutil.rmtree('{0}/../tables'.format(DISTPATH), ignore_errors=True)

os.makedirs('{0}/../match'.format(DISTPATH), exist_ok=True)
os.makedirs('{0}/../tables'.format(DISTPATH), exist_ok=True)

md2pdf('README.pdf', md_file_path='README.md', css_file_path='pdf.css', base_url='./')

shutil.move('README.pdf', '{0}/../README.pdf'.format(DISTPATH))

shutil.copy('match/playbtw_core.yml', '{0}/../match/'.format(DISTPATH))
shutil.copy('match/playbtw_utils.yml', '{0}/../match/'.format(DISTPATH))
shutil.copy('match/playbtw_mythic.yml', '{0}/../match/'.format(DISTPATH))
shutil.copy('match/playbtw_pum.yml', '{0}/../match/'.format(DISTPATH))
shutil.copy('match/playbtw_gum2.yml', '{0}/../match/'.format(DISTPATH))
shutil.copy('match/playbtw_mune.yml', '{0}/../match/'.format(DISTPATH))
shutil.copy('match/playbtw_prompty.yml', '{0}/../match/'.format(DISTPATH))
shutil.copy('match/playbtw_opse.yml', '{0}/../match/'.format(DISTPATH))
shutil.copy('match/playbtw_crge.yml', '{0}/../match/'.format(DISTPATH))
shutil.copy('match/playbtw_ai.yml', '{0}/../match/'.format(DISTPATH))

if os.path.exists('dist_core/scripts/playbtw_core.exe'):
    shutil.copy('dist_core/scripts/playbtw_core.exe', '{0}/../scripts/'.format(DISTPATH))
    shutil.copy('dist_utils/scripts/playbtw_utils.exe', '{0}/../scripts/'.format(DISTPATH))
    shutil.copy('dist_ai/scripts/playbtw_ai.exe', '{0}/../scripts/'.format(DISTPATH))
else:
    shutil.copy('dist_core/scripts/playbtw_core', '{0}/../scripts/'.format(DISTPATH))
    shutil.copy('dist_utils/scripts/playbtw_utils', '{0}/../scripts/'.format(DISTPATH))
    shutil.copy('dist_ai/scripts/playbtw_ai', '{0}/../scripts/'.format(DISTPATH))

for f in glob.glob('tables/*'):
    shutil.copy2(f, '{0}/../tables/'.format(DISTPATH))

shutil.make_archive('PlayBTW_v3_02_base_with_ai', 'zip', 'dist_all_ai')
