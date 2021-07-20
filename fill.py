from selenium import webdriver
import time

logfile = 'g:\\Github\\Autofill_x_m_u\\log.txt' #打印日志文件的地址，可以指定任意位置
userfile = 'g:\\Github\\Autofill_x_m_u\\users'  #存放用户名密码的文件地址，可指定任意位置
url = 'https://xmuxg.xmu.edu.cn/login'
# chromedriver = '/your/path/to/driver' #如果需要
chromedriver = 'c:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe' #设置chromedriver的位置，仅在windows下需要

def daka(a, b):
    driver = webdriver.Chrome(chromedriver)
    run = True
    now = time.time()
    while run:
        try:
            driver.get(url)
            break
        except:
            print(url, "获取失败，重试中")
            if (time.time() - now) > 10:
                run = False
                return '网页登陆失败'
     
    driver.maximize_window()
    # logintab = driver.find_element_by_class_name('login-tab')
    login = driver.find_element_by_xpath("//*[@class='buttonBox']/button[3]")
    login.click()

    time.sleep(0.2)
    c = driver.find_element_by_id('username')
    d = driver.find_element_by_id('password')
    c.send_keys(a)
    d.send_keys(b)

    #driver.find_element_by_xpath("//*[@id='casLoginForm']/p[4]").click() #登录
    driver.find_element_by_xpath("//*[@class='auth_login_btn primary full_width']").click() #登录
    driver.get('https://xmuxg.xmu.edu.cn/app/214')

    now = time.time()
    while True:
        try:
            form = driver.find_element_by_xpath("//*[@class='gm-scroll-view']/div[2]") #我的表单
            form.click()
            break
        except:
            time.sleep(0.2)
            print("获取\"我的表单\"失败，重试中")
            if (time.time() - now) > 10:
                run = False
                return '获取\"我的表单\"失败'

    now = time.time()
    while True :
        try:
            text = driver.find_element_by_xpath("//*[@id='select_1582538939790']/div[1]/div[1]/span[1]").text
            break
        except:
            time.sleep(0.2)
            print("查找框内文本失败，重试中")
            if (time.time() - now) > 10:
                run = False
                return '查找框内文本失败'
    
    if text == '请选择':
        now = time.time()
        while True:
            try:
                yes = driver.find_element_by_xpath("//*[@id='select_1582538939790']/div[1]/div[1]") #定位填“是”的页面
                yes.click()
                break
            except:
                time.sleep(0.2)
                print("点击\"是\"失败，重试中")
                if (time.time() - now) > 10:
                    run = False
                    return '点击\"是\"失败'

        now = time.time()
        while True:
            try:
                yes = driver.find_element_by_xpath("//*[@class='v-select-cover']/ul[1]/div[1]")
                yes.click()
                break
            except:
                time.sleep(0.2)
                print("确认\"是\"失败，重试中")
                if (time.time() - now) > 10:
                    return '确认\"是\"失败'
        save = driver.find_element_by_xpath("//*[@class='form-save position-absolute']")
        save.click()

        time.sleep(0.2)
        driver.switch_to.alert.accept() # 保存确定
        time.sleep(3)
        output = '打卡成功'
    elif text == '是 Yes':
        output = '已打卡'
    else:
        output = '打卡失败！！！'
    print(output)
    driver.close()
    return output

with open(userfile, 'r') as users:
    lines = users.readlines()
    for line in lines:
        line = line.strip()
        if line[0] == '#':
            continue
        a, b = line.split(' ')
        output = daka(a, b)

        cur_time = (time.strftime('%Y_%m_%d_%r', time.localtime(time.time())))
        with open(logfile, 'a') as log:
            log.write(cur_time + ' ' + a + ' ' + output + '\n')

        print('End\n')




