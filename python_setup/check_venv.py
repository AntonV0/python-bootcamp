"""Check whether the script is running inside a virtual environment."""

import sys

if sys.prefix != sys.base_prefix:
    print("Running inside a virtual environment.")
else:
    print("Not running inside a virtual environment.")
