#！/bin/bash
sleep $(($RANDOM % 60))m #添加一个休眠的随机时间0-59分钟，避免每天都在同一时刻打卡
source /your/path/to/conda/bin/activate
Xvfb :99 -ac -screen 0 1280x1024x24 & 
export DISPLAY=:99
python3 /your/path/to/fill.py
