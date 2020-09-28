#！/bin/bash
source /your/path/to/conda/bin/activate
Xvfb :99 -ac -screen 0 1280x1024x24 & 
export DISPLAY=:99
python /your/path/to/fill.py
