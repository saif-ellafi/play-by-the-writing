# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['scripts/playbtw_core.py'],
    pathex=[],
    binaries=[],
    datas=[('match/*', 'match'), ('tables/*', 'tables')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    name='playbtw',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity='Developer ID Application: Saif Addin Ellafi (4R2BZ2DV4D)',
    entitlements_file='entitlements.plist',
    osx_bundle_identifier='com.jeansensmachines.pbtw',
    exclude_binaries=True
)

app = BUNDLE(
    exe,
    a.binaries,
    a.datas,
    name='playbtw_macos_3_11.app',
    bundle_identifier='com.jeansensmachines.pbtw',
    version='3.11'
)
