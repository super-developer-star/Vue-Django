""" Production Settings """

import os
import dj_database_url
from .dev import *

############
# DATABASE #
############
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('postgresql-trapezoidal-13475')
    )
}


############
# SECURITY #
############

DEBUG = False
# Set to your Domain here (eg. 'onyx.herokuapp.com')
ALLOWED_HOSTS = ['*']
