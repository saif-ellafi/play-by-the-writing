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

shutil.copy('match/playbtw_gum2.yml', '{0}/../match/'.format(DISTPATH))

for f in glob.glob('tables/gum*'):
    shutil.copy2(f, '{0}/../tables/'.format(DISTPATH))

shutil.make_archive('PlayBTW_v2_09_gum2', 'zip', 'dist_gum2')
