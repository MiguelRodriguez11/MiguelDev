#!/bin/bash
. venv/bin/activate
pip install --upgrade pip
reflex init
reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
deactivate