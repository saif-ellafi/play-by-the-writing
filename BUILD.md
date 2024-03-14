NSIS Nullsoft Scriptable -> $APPDATA\Espanso\

`pyinstaller playbtw_core.spec --clean --distpath dist_core/scripts`

`pyinstaller playbtw_example.spec --clean --distpath dist_example/scripts`

`pyinstaller playbtw_utils.spec --clean --distpath dist_utils/scripts`

`pyinstaller playbtw_mythic.spec --clean --distpath dist_mythic/scripts`

`pyinstaller playbtw_pum.spec --clean --distpath dist_pum/scripts`

`pyinstaller playbtw_gum2.spec --clean --distpath dist_gum2/scripts`

`pyinstaller playbtw_prompty.spec --clean --distpath dist_prompty/match`

`pyinstaller playbtw_mune.spec --clean --distpath dist_mune/match`

`pyinstaller playbtw_opse.spec --clean --distpath dist_opse/match`

`pyinstaller playbtw_crge.spec --clean --distpath dist_crge/match`

`pyinstaller playbtw_ai.spec --clean --distpath dist_ai/scripts`

`pyinstaller playbtw_all.spec --clean --distpath dist_all/scripts`

`pyinstaller playbtw_all_ai.spec --clean --distpath dist_all_ai/scripts`

# Windows

```cmd
pyinstaller playbtw_core.spec --clean --distpath dist_core/scripts && pyinstaller playbtw_utils.spec --clean --distpath dist_utils/scripts && pyinstaller playbtw_mythic.spec --clean --distpath dist_mythic/scripts && pyinstaller playbtw_pum.spec --clean --distpath dist_pum/scripts && pyinstaller playbtw_gum2.spec --clean --distpath dist_gum2/scripts && pyinstaller playbtw_mune.spec --clean --distpath dist_mune/scripts && pyinstaller playbtw_prompty.spec --clean --distpath dist_prompty/scripts && pyinstaller playbtw_opse.spec --clean --distpath dist_opse/match && pyinstaller playbtw_crge.spec --clean --distpath dist_crge/match && pyinstaller playbtw_ai.spec --clean --distpath dist_ai/scripts && pyinstaller playbtw_all.spec --clean --distpath dist_all/scripts && pyinstaller playbtw_all_ai.spec --clean --distpath dist_all_ai/scripts
```