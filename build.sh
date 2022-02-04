#!/bin/bash
pandoc --standalone --template template.html doc.md > README.HTML
python setup.py sdist
