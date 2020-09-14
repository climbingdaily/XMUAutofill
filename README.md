# auto_fill_x_m_u

You know

## 环境
linux
chrome
chromedriver

## 运行方式

可以在服务器上设置一个脚本定时运行
crontab -l //查看定时任务和定时任务说明
crontab -e //编辑定时任务

0 9 * * * bash /your/path/to/fill.sh #每天九点自动执行任务

## 待实现
crontab可以自动发送运行结果到指定邮箱，这样就能及时知道结果
与微信结合
