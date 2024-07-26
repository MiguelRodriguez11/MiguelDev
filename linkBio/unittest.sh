#!/bin/bash
source .venv/bin/activate
cd /home/user/MiguelDev/linkBio/linkBio
pytest -v
if [ $? -ne 0 ]; then
    echo "Error: Unit tests failed"
    exit 1
fi