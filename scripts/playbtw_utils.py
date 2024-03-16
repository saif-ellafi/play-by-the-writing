import os
import tempfile
import urllib.request
import zipfile
import shutil
import distutils.dir_util


PBWDIR = os.path.join(os.path.expanduser('~'), 'PlayBTW')
TREV = 1003


# Download the master repo zip file and extract it in CONFIG dir using urllib
def download_master():
    # Record trev in hidden file.
    trev_path = os.path.join(PBWDIR, '.pbtwtrev')
    if not os.path.exists(trev_path):
        with open(trev_path, mode='w', encoding='utf-8') as trevlocal:
            trevlocal.write(str(TREV))
    url = 'https://codeload.github.com/saif-ellafi/play-by-the-writing/zip/refs/heads/main'
    temp_dir = tempfile.gettempdir()
    temp_file = temp_dir+'/master.zip'
    urllib.request.urlretrieve(url, temp_file)
    with zipfile.ZipFile(temp_file, 'r') as zip_ref:
        zip_ref.extractall(os.path.join(temp_dir, 'pbtw_files'))
    # copy folders 'tables' and 'match' to CONFIG dir, merge files if already exist
        with open(os.path.join(temp_dir, 'pbtw_files', 'play-by-the-writing-main', '.pbtwtrev'), encoding='utf-8') as trevpull:
            with open(os.path.join(PBWDIR, '.pbtwtrev'), encoding='utf-8') as trevlocal:
                newrev = int(trevpull.readline().strip())
                update_available = newrev > int(trevlocal.read().strip())
                update_notes = trevpull.readline().strip()
    if update_available:
        distutils.dir_util.copy_tree(os.path.join(temp_dir, 'pbtw_files', 'play-by-the-writing-main', 'tables'), os.path.join(os.environ['CONFIG'], 'tables'))
        distutils.dir_util.copy_tree(os.path.join(temp_dir, 'pbtw_files', 'play-by-the-writing-main', 'match'), os.path.join(os.environ['CONFIG'], 'match'))
        with open(os.path.join(PBWDIR, '.pbtwtrev'), mode='w', encoding='utf-8') as trevlocal:
            trevlocal.write(str(newrev))
        text = 'Updated: ' + update_notes
    else:
        text = 'Already up to date'
    # delete the remaining downloaded files
    shutil.rmtree(os.path.join(temp_dir, 'pbtw_files'))
    os.remove(temp_file)
    return text
