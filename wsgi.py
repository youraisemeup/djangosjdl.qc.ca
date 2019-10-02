from __future__ import unicode_literals

import os
import locale
import sys
sys.stdout = sys.stderr

sys.path.append('/var/www/vhosts/sjdl.qc.ca/httpdocs/src/sjdl')
sys.path.append('/var/www/vhosts/sjdl.qc.ca/httpdocs/src/')

#addsitedir('/home/pawesome/envs/pinax072/lib/python2.6/site-packages')


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
settings_module = "%s.prod_settings" % PROJECT_ROOT.split(os.sep)[-1]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

python_home = '/var/www/vhosts/sjdl.qc.ca/httpdocs/venv/sjdl'

activate_this = python_home + '/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

os.environ['LC_ALL'] = 'fr_CA.UTF8'
locale.setlocale(locale.LC_ALL, '')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
