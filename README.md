# Xiamen University automatic daily health check in 
每日自动健康打卡<br>
最好在服务器等永不关机的环境下运行，否则失去了自动的意义。<br>
users文件中可添加多个账号密码，打卡结果会记录在log.txt中

## Environment
* Linux/windows <br>
* chrome <br>
* chromedriver <br>
* python 3.6+ <br>

## Python lib
selenium

## Linux
* 直接运行
```
Xvfb :99 -ac -screen 0 1280x1024x24 & 
# 若服务器没有实体屏幕，则需启动虚拟屏幕。仅需启动一次，之后运行无需重复启动，否则会报错。
export DISPLAY=:99
python fill.py
```

* 脚本运行
```
bash fill.sh 
```

* 编辑定时脚本
```
crontab -l //查看系统中已有的定时任务
crontab -e //编辑定时任务
```

* 定时脚本样例
```
crontab -e
4 9 * * * bash /your/path/to/fill.sh #每天9点4分自动执行任
0 11 * * * bash /your/path/to/fill.sh #每天11点0分自动执行任务
```

## Windwos
```
python fill.py
```
## TO DO
- [x] 打印日志 <br>
- [ ] 自动发送结果到指定邮箱 <br>
- [ ] 与微信结合<br>
- [ ] Windows脚本<br>
- [ ] Mac版<br>
- [ ] 账号密码加密传输<br>

## License

This project is released under the [GNU GPL v3.0](LICENSE).
