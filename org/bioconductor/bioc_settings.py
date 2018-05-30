# Load up all known settings
from biostar.settings.base import *

# Override settings as needed

# List all extra template paths here.
EXTRA_PATHS = [
    abspath(HOME_DIR, 'org', 'bioconductor', 'templates')
]

# Activate the new PATHS
TEMPLATE_DIRS = EXTRA_PATHS + list(TEMPLATE_DIRS)

print(TEMPLATE_DIRS)
