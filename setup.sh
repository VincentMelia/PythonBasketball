#!/usr/bin/env bash

conda create --name deleteme python=3.6
source activate deleteme
conda update --all


pip install -r requirements.txt

