#!/bin/bash -e

pyinstaller playbtw_core.spec --clean --distpath dist_core/scripts;

pyinstaller playbtw_mythic.spec --clean --distpath dist_mythic/scripts;

pyinstaller playbtw_pum.spec --clean --distpath dist_pum/scripts;

pyinstaller playbtw_gum.spec --clean --distpath dist_gum/scripts;

pyinstaller playbtw_opse.spec --clean --distpath dist_opse/match;

pyinstaller playbtw_ai.spec --clean --distpath dist_ai/scripts;

pyinstaller playbtw_all.spec --clean --distpath dist_all/scripts;

pyinstaller playbtw_all_ai.spec --clean --distpath dist_all_ai/scripts;

exit 0;