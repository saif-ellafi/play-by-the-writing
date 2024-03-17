NSIS Nullsoft Scriptable -> $APPDATA\Espanso\

`pyinstaller playbtw_build.spec --clean --noconfirm --distpath dist_playbtw/scripts`

`pyinstaller playbtw_dist.spec --clean --noconfirm --distpath dist_playbtw/scripts`

# Windows

```cmd
pyinstaller playbtw_build.spec --clean --noconfirm --distpath dist_playbtw/scripts && pyinstaller playbtw_dist.spec --clean --noconfirm --distpath dist_playbtw/scripts
```

# Windows No-AI

```cmd
pyinstaller playbtw_build_noai.spec --clean --noconfirm --distpath dist_playbtw/scripts && pyinstaller playbtw_dist_noai.spec --clean --noconfirm --distpath dist_playbtw/scripts
```
