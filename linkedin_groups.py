from linkedin import linkedin

import pprint

from django.conf import settings
settings.configure(
    DATABASE_ENGINE = 'django.db.backends.sqlite3',
    DATABASE_NAME = 'db.sqlite3',
    DATABASE_USER = 'danthemanvsqz',
    DATABASE_PASSWORD = 'Aa1234',
    #DATABASE_HOST = 'localhost',
    #DATABASE_PORT = '5432',
    #TIME_ZONE = 'America/New_York',
)

from mep_django.linkedin.models import GroupPost


USER_TOKEN = '0cf4b73d-ed4c-474f-b62c-620404f94546'
USER_TOKEN_SECRET = '7dc3d37b-a45c-44f6-9e04-fa2e645cade9'

DEV_KEY = '75l485e9k29snc'
DEV_SECRET = 'iw7fONMpJZcY5HOb'

RETURN_URL = 'BULLSHIT'

auth = linkedin.LinkedInDeveloperAuthentication(DEV_KEY, DEV_SECRET, USER_TOKEN, USER_TOKEN_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values)

app = linkedin.LinkedInApplication(auth)

#GROUP_ID = 1917190
GROUP_ID = 6683349

posts = app.get_posts(GROUP_ID, selectors=['title', 'summary', 'creation-timestamp', 'site-group-post-url',], params={'count':10})
print type(posts)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(posts)
