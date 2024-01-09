from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine-tuning.
include_files = ['.\img\icon.ico']
build_options = {'packages': [], 'excludes': [], 'include_files': include_files}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('dcm-get.py', base=base, target_name='PACS_del_req_wip')
]

setup(name='Deletion Request',
      version='1.3',
      description='Sends an image deletion request to google sheets',
      options={'build_exe': build_options},
      executables=executables)
