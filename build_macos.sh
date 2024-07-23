#!/bin/bash -e

pyinstaller playbtw_build_macos.spec --clean --noconfirm --distpath dist_playbtw/scripts;

exit 0;