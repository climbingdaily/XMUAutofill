# Xiamen University automatic daily health check in 
自从用了这个，辅导员再也不用催我打卡了。腰也不酸了，腿也不疼了，注意力也更集中了，我感觉我又行了。<br>
最好在服务器等永不关机的环境下运行，否则失去了自动的意义<br>
users文件中可添加多个账号密码，打卡结果会记录在log.txt中<br>

## Environment
* Linux/windows <br>
* chrome <br>
* [chromedriver](http://npm.taobao.org/mirrors/chromedriver/) <br>
* python 3.6+ <br>

## Python lib
selenium <br>
```
pip3 install selenium
```
## Linux
* 直接运行
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
python3 fill.py
```
## TO DO
- [x] 打印日志 <br>
- [ ] 自动发送结果到指定邮箱 <br>
- [ ] 与微信结合<br>
- [ ] Windows脚本<br>
- [ ] Mac版<br>
- [ ] 账号密码加密传输<br>

## 更新日志
更新查找登录按钮
```
driver.find_element_by_xpath("//*[@id='casLoginForm']/p[4]").click() #登录
```
## License

This project is released under the [GNU GPL v3.0](LICENSE).
