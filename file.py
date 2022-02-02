# *************************************************************************
# Script Name: 
# Author: 
# Date: 
# Description: 
# *************************************************************************
#!/usr/bin/env python3
import sys

if len(sys.argv) == 2 and sys.argv[1] == "Kyndryl":
    print("Welcome to Kyndryl!!!")
elif len(sys.argv) == 1:
    print("You need type the name of company.")
else:
    print("Wrong company.")
