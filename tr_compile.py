#!flask/bin/python
import os
import sys
if sys.platform == 'win32':
    # pybabel = 'flask\\Scripts\\pybabel'
    pybabel = 'pybabel'
else:
    # pybabel = 'flask/bin/pybabel'
    pybabel = 'pybabel'
os.system(pybabel + ' compile -d app/translations')

