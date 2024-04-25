#!/bin/bash -e

pyinstaller playbtw_build_default.spec --clean --noconfirm --distpath dist_playbtw/scripts;
pyinstaller playbtw_dist.spec --clean --noconfirm --distpath dist_playbtw/scripts;

exit 0;