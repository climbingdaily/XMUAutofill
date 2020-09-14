#！/bin/bash

source /your/path/to/conda/bin/activate
# conda activate base
# Xvfb :99 -ac -screen 0 1280x1024x24 & //仅需要启动一次
export DISPLAY=:99
python /your/path/to/fill.py
