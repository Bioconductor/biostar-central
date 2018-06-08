# Load up all known settings
from biostar.settings.base import *

# Override settings as needed

# List all extra template paths here.
EXTRA_PATHS = [
    abspath(HOME_DIR, 'org', 'bioconductor', 'templates')
]

# Activate the new PATHS
TEMPLATE_DIRS = EXTRA_PATHS + list(TEMPLATE_DIRS)

# This is to show you what the template loading order is:

print("*** Template loading order")
for path in TEMPLATE_DIRS:
    print(path)

START_CATEGORIES = [
    "Latest"
]

NAVBAR_TAGS = []

END_CATEGORIES = [
    "News", "Jobs", "Tutorials"
]

CATEGORIES = START_CATEGORIES + NAVBAR_TAGS + END_CATEGORIES
