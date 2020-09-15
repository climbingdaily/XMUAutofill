from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
# driver = webdriver.PhantomJS(executable_path="D:/phantomjs-2.1.1-windows/bin/phantomjs.exe", port=2)
url = 'https://xmuxg.xmu.edu.cn/login'

while True:
    try:
        driver.get(url)
        break
    except:
        print(url, "获取失败，重试中")
    
driver.maximize_window()

# logintab = driver.find_element_by_class_name('login-tab')
login = driver.find_element_by_xpath("//*[@class='buttonBox']/button[2]")

login.click()

a = '哈哈哈'
b = '嘿嘿嘿'

c = driver.find_element_by_id('username')
d = driver.find_element_by_id('password')

c.send_keys(a)
d.send_keys(b)
driver.find_element_by_xpath("//*[@id='casLoginForm']/p[5]").click() #登录

driver.get('https://xmuxg.xmu.edu.cn/app/214')
while True:
    try:
        form = driver.find_element_by_xpath("//*[@class='gm-scroll-view']/div[2]") #我的表单
        break
    except:
        time.sleep(0.2)
        print("获取\"我的表单\"失败，重试中")
form.click()
while True:
    try:
        text = driver.find_element_by_xpath("//*[@id='select_1582538939790']/div[1]/div[1]/span[1]").text
        break
    except:
        time.sleep(0.2)
        print("查找框内文本失败，重试中")

if text == '请选择':
    while True:
        try:
            yes = driver.find_element_by_xpath("//*[@id='select_1582538939790']/div[1]/div[1]") #定位填“是”的页面
            break
        except:
            time.sleep(0.2)
            print("点击\"是\"失败，重试中")
    yes.click()
    while True:
        try:
            yes = driver.find_element_by_xpath("//*[@class='v-select-cover']/ul[1]/div[1]")
            break
        except:
            time.sleep(0.2)
            print("确认\"是\"失败，重试中")
    yes.click()
    save = driver.find_element_by_xpath("//*[@class='preview-container']/div[1]/div[1]/span[1]/span[1]")
    save.click()

    time.sleep(0.2)
    driver.switch_to_alert().accept() # 保存确定
    time.sleep(3)
    output = '打卡成功\n'
elif text == '是 Yes':
    output = '已打卡\n'
else:
    output = '打卡失败！！！\n'

driver.close()

print(output)
logfile = '/your/path/to/log.txt' #日志文件地址
cur_time = (time.strftime('%Y_%m_%d_%r', time.localtime(time.time())))
with open(logfile, 'a') as log:
    log.write(cur_time + ': ' + output)

print('End\n')
