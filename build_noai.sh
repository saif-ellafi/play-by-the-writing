#!/bin/bash -e

pyinstaller playbtw_build_noai.spec --clean --noconfirm --distpath dist_playbtw/scripts;
pyinstaller playbtw_dist_noai.spec --clean --noconfirm --distpath dist_playbtw/scripts;

exit 0;