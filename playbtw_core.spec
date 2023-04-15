# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['scripts/playbtw_core.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='playbtw_core',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

from md2pdf.core import md2pdf

import shutil
import os
import glob

os.makedirs('{0}/../match'.format(DISTPATH), exist_ok=True)

md2pdf('README.pdf', md_file_path='README.md', css_file_path='pdf.css', base_url='./')

shutil.copy('README.pdf', '{0}/../README.pdf'.format(DISTPATH))
shutil.copy('match/playbtw_core.yml', '{0}/../match/'.format(DISTPATH))

shutil.make_archive('PlayBTW_v1_32_core', 'zip', 'dist_core')
