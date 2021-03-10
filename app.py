from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import datetime
import schedule


def tool():
    # ブラウザを開く。
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # Googleの検索TOP画面を開く。
    driver.get("https://www.instagram.com/")
    time.sleep(4)

    # ログインIDを入力する
    id_box = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    id_box.send_keys('ys_shiro19')

    #パスワードを入力する
    id_pass = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    id_pass.send_keys('toukoudai2')

    #ログインボタンを押す
    lg_box = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
    lg_box.click()

    time.sleep(5)
    #後でのボタンを押す

    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/main/div/div/div/div/button'))).click()

    later = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div[3]/button[2]')))
    later.click()

    time.sleep(3)
    word = ['いいねした人で気になった人フォロー','いいね返しは絶対','21歳','美男美女と繋がりたい','渋谷スカイ','インスタ映え']
    x = random.choice(word)

    time.sleep(1)
    #ハッシュタグ検索を行う
    srech = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div')
    srech.click()
    enter = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    enter.send_keys(x)
    time.sleep(5)
    push = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
    push.click()


    time.sleep(3)

    #最新の投稿をクリックする
    touko = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]')))

    touko.click()

    time.sleep(3)

    iine = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')

    iine.click()

    time.sleep(2)

    next = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]')

    next.click()


    for i in range(150):
        time.sleep(1)
        try:
            element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')))
            element.click()

        except:
            pass
        finally:
            next2 = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]')
            next2.click()



    print('終了しました')
    time.sleep(2)
    driver.close()

schedule.every().day.at("14:00").do(tool)
schedule.every().day.at("14:30").do(tool)
schedule.every().day.at("15:00").do(tool)
schedule.every().day.at("16:00").do(tool)
schedule.every().day.at("19:00").do(tool)
schedule.every().day.at("19:30").do(tool)
schedule.every().day.at("20:00").do(tool)


while True:
  schedule.run_pending()
  time.sleep(60)
