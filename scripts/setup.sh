#!/usr/bin/env bash
set -e
echo "Setup script: creating virtualenv and installing backend deps..."
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
echo "Done"
