#!/bin/bash
source ~/miniconda3/etc/profile.d/conda.sh
conda deactivate
conda env remove -n fast-api

echo "Creating conda env fast-api"
conda env create --file fastapi_env.yml -n fast-api 
source ~/miniconda3/etc/profile.d/conda.sh
conda activate fast-api

pip install --upgrade pip
pip install -r requirements.txt
