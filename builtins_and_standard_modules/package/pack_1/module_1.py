"""Module 1 in package pack_1."""

# absolute import from another package
from package.pack_2.module_2 import alphabet_consonants
from . import module_3  # Relative import of module_3 within the same package

print("Consonants from module_2:", alphabet_consonants)
# ModuleNotFoundError: No module named 'package'
# Cannot do this from the terminal directly because Python won't recognise 'package' as a package

# To run this module correctly, use the -m flag from the command line:
# Navigate to directory containing 'package' folder
# C:\Users\Anton\Documents\BOOTCAMP\Python\python-basics\builtins_and_standard_modules
# Then run:
# python -m package.pack_1.module_1 # This will run module_1.py
# Output: Consonants from module_2: ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
# 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

# Alternatively, you can run it from a terminal inside an IDE like VSCode:
# cd into project root folder (builtins_and_standard_modules)
# python -m package.pack_1.module_1

alphabet_vowels = ['a', 'e', 'i', 'o', 'u']

# ------------------------------------------------------

# Relative imports (only within packages)
# In module_1.py, we can import module_3.py using relative import
# from . import module_3 (top of the file)

print(module_3.str1)
# Output: This is module 3 in package pack_1.
# Note: Relative imports work only when the module is run as part of a package
# (using the -m flag or from another module in the package).
