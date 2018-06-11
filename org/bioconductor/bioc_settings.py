# Load up all known settings
from biostar.settings.base import *

# Override settings as needed


# List all extra template paths here.
EXTRA_TEMPDIR = [
    abspath(HOME_DIR, 'org', 'bioconductor', 'templates')
]

# Activate the new PATHS
TEMPLATE_DIRS = EXTRA_TEMPDIR + list(TEMPLATE_DIRS)

# This is to show you what the template loading order is:
print("*** Template loading order")
for path in TEMPLATE_DIRS:
    print(path)

START_CATEGORIES = [
    "Latest", "News", "Jobs", "Tutorials"
]

NAVBAR_TAGS = []

END_CATEGORIES = []

# These are the tags that always show up in the tag recommendation dropdown.
POST_TAG_LIST = NAVBAR_TAGS + ["software error"]

CATEGORIES = START_CATEGORIES + NAVBAR_TAGS + END_CATEGORIES

SITE_LOGO = "bioconductor_logo_rgb_small.jpg"

EXTRA_STATIC = [
    abspath(HOME_DIR, 'org', 'bioconductor', 'static')
]

STATICFILES_DIRS = EXTRA_STATIC + list(STATICFILES_DIRS)

# How many recent objects to show in the sidebar.
RECENT_VOTE_COUNT = 5
RECENT_USER_COUNT = 5
RECENT_POST_COUNT = 5
