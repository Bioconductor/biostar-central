#
# Django settings for support.bioconductor project.
#   for defaults see  
#   support.bioconductor.org/biostar/settings/base.py
#   this script overrides default settings
#


#
# Load up all known settings
#
from biostar.settings.base import *

#
# Override settings as needed
#


# Define Categories in top banner
START_CATEGORIES = [
    "Latest", "News", "Jobs", "Tutorials"
]

NAVBAR_TAGS = []

END_CATEGORIES = []

# These are the tags that always show up in the tag recommendation dropdown.
POST_TAG_LIST = NAVBAR_TAGS + ["software error"]

# This will form the navbar
CATEGORIES = START_CATEGORIES + NAVBAR_TAGS + END_CATEGORIES

# This will appear as a top banner.
# It should point to a template that will be included.

TOP_BANNER = ""
#TOP_BANNER = "test-banner.html"

# List all extra static paths here.
EXTRA_STATIC = [
    abspath(HOME_DIR, 'org', 'bioconductor', 'static')
]

# Activate the new static path
STATICFILES_DIRS = EXTRA_STATIC + list(STATICFILES_DIRS)


# List all extra template paths here.
EXTRA_TEMPDIR = [
    abspath(HOME_DIR, 'org', 'bioconductor', 'templates')
]

# Activate the new template path
TEMPLATE_DIRS = EXTRA_TEMPDIR + list(TEMPLATE_DIRS)

# Debugging
# This is to show you what the template loading order is:
print("*** Template loading order")
for path in TEMPLATE_DIRS:
    print(path)

# The site logo image on top navigation bar
SITE_LOGO = "bioconductor_logo_rgb_small.jpg"

# How many recent objects to show in the sidebar.
RECENT_VOTE_COUNT = 5
RECENT_USER_COUNT = 5
RECENT_POST_COUNT = 5
