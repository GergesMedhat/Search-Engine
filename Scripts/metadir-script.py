#!C:\Users\Bavly\PycharmProjects\Search_Engine\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'metadir==0.0.2','console_scripts','metadir'
__requires__ = 'metadir==0.0.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('metadir==0.0.2', 'console_scripts', 'metadir')()
    )
