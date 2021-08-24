import os
import collections
from posixpath import dirname

EXT_AUDIO = ['mp3', 'wav', 'wma']
EXT_VIDEO = ['mp4', 'mpg', 'wvm']
EXT_IMGS = ['png', 'jpg', 'gif', 'psd', 'svg']
EXT_DOCS = ['doc', 'docx', 'js', 'json', 'log', 'pdf', 'tex', 'txt', 'xlr', 'xls', 'xlsx']
EXT_COMPR = ['zip', 'zipx', 'rar', '7z']
EXT_INSTL = ['exe', 'jar', 'bat', 'apk', 'iso', 'msi']

dirname = os.path.dirname(__file__)
BASE_PATH = os.path.join(dirname, 'INSERT PATH HERE') # Folder to move into, use \\ per directory
DOWN_PATH = os.path.dirname('C:\\Users\\YOURNAME\\Downloads\\Downloads') # folder to look into, use \\ per directory
DEST_DIRS = ['Audio', 'Video', 'Images', 'Documents', 'Compressed', 'Installers', 'Other']

for d in DEST_DIRS:
    dir_path = os.path.join(BASE_PATH, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

DOWNLOADS_PATH = os.path.join(BASE_PATH, DOWN_PATH)
files_mapping = collections.defaultdict(list)
files_list = os.listdir(DOWNLOADS_PATH)

for file_name in files_list:
    if file_name[0] != '.':
        file_ext = file_name.split('.')[-1]
        files_mapping[file_ext].append(file_name)

for f_ext, f_list in files_mapping.items():

    if f_ext in EXT_AUDIO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Audio', file))
            print(os.path.join(DOWNLOADS_PATH, file))
            print(os.path.join(BASE_PATH, 'Audio', file))

    elif f_ext in EXT_VIDEO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Video', file))
            print(os.path.join(DOWNLOADS_PATH, file))
            print(os.path.join(BASE_PATH, 'Video', file))

    elif f_ext in EXT_IMGS:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Images', file))
            print(os.path.join(DOWNLOADS_PATH, file))
            print(os.path.join(BASE_PATH, 'Images', file))

    elif f_ext in EXT_DOCS:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Documents', file))
            print(os.path.join(DOWNLOADS_PATH, file))
            print(os.path.join(BASE_PATH, 'Documents', file))

    elif f_ext in EXT_COMPR:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Compressed', file))
            print(os.path.join(DOWNLOADS_PATH, file))
            print(os.path.join(BASE_PATH, 'Compressed', file))

    elif f_ext in EXT_INSTL:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Installers', file))
            print(os.path.join(DOWNLOADS_PATH, file))
            print(os.path.join(BASE_PATH, 'Installers', file))

    else:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Other', file))
            print(os.path.join(DOWNLOADS_PATH, file))
            print(os.path.join(BASE_PATH, 'Other', file))
