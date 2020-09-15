# auto_fill_x_m_u

You know
最好在服务器等永不关机的环境下运行。

## 环境
* linux/windows
* chrome
* chromedriver
* python 3.6+

## python依赖库
selenium

## 运行方式
* 直接运行
```
Xvfb :99 -ac -screen 0 1280x1024x24 & #启动虚拟屏幕
export DISPLAY=:99
python fill.py
```
* 脚本运行
```
bash fill.sh 
```

* 定时脚本运行
```
crontab -l //查看定时任务和定时任务说明
crontab -e //编辑定时任务
```

每天九点4分自动执行任务
```
crontab -e
4 9 * * * bash /your/path/to/fill.sh 
```

## TO DO
- [ ] 打印日志 <br>
- [ ] 自动发送结果到指定邮箱 <br>
- [ ] 与微信结合<br>
