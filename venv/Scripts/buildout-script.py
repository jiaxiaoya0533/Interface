#!F:\zidonghua\interface\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'zc.buildout==2.13.2','console_scripts','buildout'
__requires__ = 'zc.buildout==2.13.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('zc.buildout==2.13.2', 'console_scripts', 'buildout')()
    )
