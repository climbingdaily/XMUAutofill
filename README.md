# Xiamen University automatic daily health check in 
 

## 声明
1. 本程序完全模拟鼠标点击，只是用一次点击代替打开网页、登录、点击打卡等操作。
2. 程序仅简化打卡步骤，打卡人仍需对自身健康状况负责，若状态变更仍需登录网页自行修改。
3. 本程序并不会将密码上传至其他其他平台。请妥善保管保存在本地的账号密码。
4. 网页内容变更时，本程序可能失效。若有问题请及时联系。

## 其他

- users文件中可添加多个账号密码，打卡结果会记录在log.txt中
- fill.py中4-8行需要修改为你本机文件的地址

## Windwos 运行方法，无需代码基础
---

1. 安装 [python 3.6](https://www.python.org/downloads/release/python-3614/)

```
# 安装后，使用win+R打开CMD窗口
# 在CMD窗口运行下面指令安装依赖库
python -m pip install selenium --user 
```

1. 安装 [chrome（点我下载）](https://www.google.cn/chrome/)
2. 下载 [chromedriver（点我下载）](http://npm.taobao.org/mirrors/chromedriver/)  *下载对应chrome的版本，若版本号最后的数字无法对应，下载最接近的即可。* <br>

```
# 查找chrome版本号，在chrome浏览器地址栏中输入
chrome://version

# 可将chromedriver放在chrome的安装位置，例如
c:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe
```
- **执行打卡程序** 
```
# 在cmd窗口运行
python fill.py
```
- **脚本 (可选，点击该文件即可运行)**
```
#将Checkin.bat中的python.exe的路径和fill.py的路径替换成你本机的路径即可
``` 

- [脚本自动运行的方法](https://www.jb51.net/article/199541.htm)

## Linux
---
1. 安装 python 3.6+
```
# 安装依赖库
pip install selenium
```
2. 安装 chrome 
3. 下载 [chromedriver（点我下载）](http://npm.taobao.org/mirrors/chromedriver/)  *下载对应chrome的版本，若版本号最后的数字无法对应，下载最接近的即可。* <br>
```
# 查找chrome版本，在命令行中输入
google-chrome -version

# 将chromedriver拷贝至
# /usr/bin/chromedriver
/usr/local/bin/chromedriver
```

* 执行程序
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

## TO DO
- [x] 打印日志 <br>
- [ ] 自动发送结果到指定邮箱 <br>
- [ ] 与微信结合<br>
- [x] Windows脚本<br>
- [ ] Mac版<br>

<br>
## License

This project is released under the [GNU GPL v3.0](LICENSE).
