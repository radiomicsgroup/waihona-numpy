#!/bin/bash
# First Install twine
# pip install twine
# Set Enviroment Pip Username and Password
# you can set in ~/.pypirc
# [pypi]
# username = username
# password = password

twine upload dist/* 
