from linkedin import linkedin
import pprint

USER_TOKEN = '0cf4b73d-ed4c-474f-b62c-620404f94546'
USER_TOKEN_SECRET = '7dc3d37b-a45c-44f6-9e04-fa2e645cade9'

DEV_KEY = '75l485e9k29snc'
DEV_SECRET = 'iw7fONMpJZcY5HOb'

RETURN_URL = 'BULLSHIT'

auth = linkedin.LinkedInDeveloperAuthentication(DEV_KEY, DEV_SECRET, USER_TOKEN, USER_TOKEN_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values)

app = linkedin.LinkedInApplication(auth)

GROUP_ID = 1917190

posts = app.get_posts(GROUP_ID, selectors=['title', 'summary', 'creation-timestamp', 'attachment', 'site-group-post-url',], params={'count':10})
print type(posts)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(posts)
