
# coding: UTF-8

# insta_profile_analysis.py

import os
import json
import shutil
import zipfile
from openpyxl import Workbook
from pathlib import Path

user_profile = os.getlogin ()
get_path = os.getcwd ()

ZIP_NAME = 'instagram-dmt.freitas-2026-11-03-aAMPyddE.zip'
EXCEL_NAME = 'insta_profile_analysis.xlsx'

def create_python_path ():
   
    path = 'Python'
    
    os.makedirs (path, exist_ok = True)
    
    return path

def create_excel_path ():
    
    wb = Workbook ()

    ws = wb.active
    ws.title = 'Sheet1'

    ws.append([
        'PROFILE',
        'FOLLOWING',
        'FOLLOWER'
    ])
    
    wb.save (EXCEL_PATH)

PYTHON_PATH = os.path.join (get_path, create_python_path ())
ZIP_PATH = os.path.join (PYTHON_PATH, ZIP_NAME)
EXCEL_PATH = os.path.join (PYTHON_PATH, EXCEL_NAME)

while True:

    if os.path.exists (rf'C:\Users\{user_profile}\Desktop\Python') and os.path.exists (rf'{get_path}\Python'):

        try:
        
            FILE_ZIP = os.path.join (rf'{get_path}\Python', ZIP_NAME)
            FILE_EXCEL = os.path.join (rf'{get_path}\Python', EXCEL_NAME)
            
            if not os.path.exists (FILE_ZIP):
            
                JOIN_ZIP = shutil.move (ZIP_NAME, FILE_ZIP)
                
            if not os.path.exists (FILE_EXCEL):
                
                create_excel_path ()
                
                JOIN_EXCEL = shutil.move (EXCEL_NAME, FILE_EXCEL)

            break
            
        except FileNotFoundError:
            
            print (rf'FileNotFoundError: [WinError 2] O sistema não pode encontrar o arquivo especificado!')
            break
            
    elif not os.path.exists (rf'C:\Users\{user_profile}\Desktop\Python') and not os.path.exists (rf'{get_path}\Python'):
        
        create_python_path ()

def read_json_sources ():

    sources = []

    if not os.path.exists (ZIP_PATH):
        
        raise FileNotFoundError (
            f'File ZIP not found: {ZIP_PATH}'
        )

    with zipfile.ZipFile (ZIP_PATH, 'r') as filename:

        for file in filename.namelist ():

            base = os.path.basename (file).lower ()

            if (base.startswith ('following') and base.endswith ('.json')) or (base.startswith ('followers') and base.endswith ('.json')):

                data = json.loads (
                    filename.read (file).decode ('utf-8-sig')
                )

                sources.append ((file, data))

    return sources

def usernames_from_record (record, is_following):

    if not isinstance (record, dict):
        
        return []

    names = []

    title = record.get ('title')

    if is_following and isinstance (title, str) and title.strip ():
        
        names.append (title.strip ())

    entries = record.get ('string_list_data', [])

    if isinstance (entries, list):

        for entry in entries:

            if isinstance (entry, dict):

                value = entry.get ('value')

                if isinstance (value, str) and value.strip ():
                    
                    names.append (value.strip ())

    return names

def extract_usernames (data, is_following):

    if isinstance (data, dict):

        records = data.get (
            'relationships_following' if is_following
            else 'relationships_followers',
            []
        )

    elif isinstance (data, list):

        records = data

    else:

        records = []

    result = {}

    for record in records:

        for name in usernames_from_record (record, is_following):

            clean = name.strip ().lstrip ('@')

            if clean:

                result.setdefault (clean.casefold (), clean)
                break

    return result

def main ():

    sources = read_json_sources ()

    if not sources:
        
        raise ValueError(
            'No JSON file of followers or following found!'
        )

    followers = {}
    following = {}

    found_followers_file = False
    found_following_file = False

    for filename, data in sources:

        base = Path (filename).name.lower ()

        if base.startswith ('followers') and base.endswith ('.json'):

            found_followers_file = True

            followers.update (
                extract_usernames (data, is_following = False)
            )

        elif base == 'following.json':

            found_following_file = True

            following.update (
                extract_usernames(data, is_following = True)
            )

    if not found_followers_file or not found_following_file:

        raise ValueError (
            'Exportação incompleta: arquivos de seguidores!'
            'E seguindo são necessários...'
        )

    all_profiles = set(followers) | set(following)

    wb = Workbook ()

    ws = wb.active
    ws.title = 'Sheet1'

    ws.append ([
        'PROFILE',
        'FOLLOWING',
        'FOLLOWER'
    ])

    for key in sorted (
        all_profiles,
        key=lambda k: (following.get (k) or followers.get (k)).casefold ()
    ):

        profile = following.get (key) or followers.get (key)

        ws.append ([
            profile,
            'SIM' if key in following else 'NÃO',
            'SIM' if key in followers else 'NÃO'
        ])

    wb.save(EXCEL_PATH)

    not_following_back = sum (
        1 for key in following if key not in followers
    )

    follows_you_only = sum (
        1 for key in followers if key not in following
    )

    print ( '\n========== ANÁLISE CONCLUÍDA! ===========')
    print ( f'----------------------------------------- ')
    print ( f'ANALYZED PROFILES - {len(all_profiles)}   ')
    print ( f'NÃO SEGUEM DE VOLTA - {not_following_back}')
    print ( f'SEGUEM E EU NÃO SIGO - {follows_you_only} ')
    print ( f'----------------------------------------- ')
    print ( f'========================================= ')
    print ( f'========= GENERATED EXCEL FILE ========== ')

if __name__ == '__main__':
    
    main()
