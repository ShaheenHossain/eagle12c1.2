# WSGI Handler sample configuration file.
#
# Change the appropriate settings below, in order to provide the parameters
# that would normally be passed in the command-line.
# (at least conf['addons_path'])
#
# For generic wsgi handlers a global application is defined.
# For uwsgi this should work:
#   $ uwsgi_python --http :9090 --pythonpath . --wsgi-file openerp-wsgi.py
#
# For gunicorn additional globals need to be defined in the Gunicorn section.
# Then the following command should run:
#   $ gunicorn eagle:service.wsgi_server.application -c openerp-wsgi.py

import eagle

#----------------------------------------------------------
# Common
#----------------------------------------------------------
eagle.multi_process = True # Nah!

# Equivalent of --load command-line option
eagle.conf.server_wide_modules = ['base', 'web']
conf = eagle.tools.config

# Path to the EagleERP Addons repository (comma-separated for
# multiple locations)

conf['addons_path'] = '../../addons/trunk,../../web/trunk/addons'

# Optional database config if not using local socket
#conf['db_name'] = 'mycompany'
#conf['db_host'] = 'localhost'
#conf['db_user'] = 'foo'
#conf['db_port'] = 5432
#conf['db_password'] = 'secret'

#----------------------------------------------------------
# Generic WSGI handlers application
#----------------------------------------------------------
application = eagle.service.wsgi_server.application

eagle.service.server.load_server_wide_modules()

#----------------------------------------------------------
# Gunicorn
#----------------------------------------------------------
# Standard EagleERP XML-RPC port is 8069
bind = '127.0.0.1:8069'
pidfile = '.gunicorn.pid'
workers = 4
timeout = 240
max_requests = 2000
