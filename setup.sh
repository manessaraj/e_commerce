#!/bin/bash
PYTHONVERSION=3.12
ENV="e_commerce"
pyenv virtualenv $PYTHONVERSION $ENV
pyenv activate $ENV
pip install -r requirements.txt
pre-commit install
