from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import os
import sys
import json
import random

desired_caps = {
    "platformName": "Android",
    "appPackage": "com.shopee.id",
    "appActivity": "com.shopee.app.ui.home.HomeActivity_ t76263",
    "deviceName": "SM-G965F",
    "udid": "224baad311027ece",
    "noReset" : "true"
}


with open('caption.json', 'r', encoding='utf-8') as json_file:
    caption = json.load(json_file)
    
with open('produk.json', 'r', encoding='utf-8') as json_file:
    produk = json.load(json_file)

# total_video = 67  # Ganti nilai sesuai kebutuhan
# starting_value = 22
total_video = int(input("total video: "))
starting_value = int(input("mulai dari video ke berapa: "))

loop_limit = 20  # Batas perulangan sebelum kembali

for i in range(starting_value, starting_value + total_video):
    rc = random.randint(0, len(caption)-1)
    rp = random.randint(0, len(produk)-1)
    # print("rc = ",rc)
    # print("rp =",rp)

    # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        #klik kembali ke home
    os.system("adb shell input tap 180 1448")
    sleep(1)
    os.system("adb shell input tap 400 1154")
    sleep(2)
    
    #swipe ke menu aplikasi
    os.system("adb shell input swipe 370 1086 368 568")
    sleep(3)

    #click shopee
    os.system("adb shell input tap 246 538")
    sleep(3)

    # click video
    # driver.find_element(by=By.XPATH, value='//android.widget.ImageView[@content-desc="tab_bar_button_video"]').click()
    os.system("adb shell input tap 438 1357")
    sleep(3)

    #click pause, dan X pop up jika ada
    # os.system("adb -s "+desired_caps['udid']+" shell input tap 339 223")
    os.system("adb shell input tap 339 223")
    sleep(1)
    os.system("adb shell input tap 339 223")
    sleep(4)

    #click video atas
    os.system("adb shell input tap 681 67")
    # driver.find_element(by=By.XPATH, value='//android.view.ViewGroup[@content-desc="click top right create icon"]/android.widget.ImageView').click()
    sleep(3)

    #cswipe up untuk pilih video
    os.system("adb shell input swipe 318 1049 219 453")
    sleep(3)

    #piij video
    # os.system("adb shell input tap 135 352")
    # sleep(1)
    if i >= 20:
        swipe_count = (i - 20) // 20 + 1
        for _ in range(swipe_count):
            os.system("adb shell input swipe 380 1069 477 200 2000")
            sleep(2)
            
            
    loop_iteration = i % loop_limit
    if loop_iteration % 4 == 0:
        x = 90
    elif loop_iteration % 4 == 1:
        x = 280
    elif loop_iteration % 4 == 2:
        x = 460
    elif loop_iteration % 4 == 3:
        x = 630

    y = 315 + (loop_iteration // 4) * 175

    os.system("adb shell input tap " + str(x) + " " + str(y))
    sleep(2)

    #next
    os.system("adb shell input tap 636 1320")
    sleep(1)

    #next
    os.system("adb shell input tap 646 1342")
    sleep(1)

    #klik textarea
    os.system("adb shell input tap 493 221")
    sleep(1)

    # ketik caption
    os.system('adb shell input text "'+ caption[rc].replace(" ", "\\ ")+ '"') 
    sleep(2)

    # klik ok
    os.system("adb shell input tap 694 91")
    sleep(2)

    # klik pilih  produk
    os.system("adb shell input tap 604 480")
    sleep(2)

    # klik search produk
    os.system("adb shell input tap 314 178")
    sleep(2)

    # search produk
    os.system('adb shell input text ' +produk[rp]['search'].replace(" ", "\\ ")+ '"') 
    sleep(2)

    # pilh produk
    os.system("adb shell input tap 637 538")
    sleep(2)
    os.system("adb shell input tap 637 538")
    sleep(3)

    # klik ketik nama produk
    os.system("adb shell input tap 354 1095")
    sleep(2)

    # search produk
    os.system('adb shell input text "'+ produk[rp]['nama'].replace(" ", "\\ ")+ '"') 
    sleep(2)

    # klik back (untuk close keyboard)
    os.system("adb shell input tap 581 1443")
    sleep(1)

    # klik selesai produk
    os.system("adb shell input tap 394 1342")
    sleep(3)

    # klik posting
    os.system("adb shell input tap 390 1342")
    sleep(40)

    #klik kembali ke home
    os.system("adb shell input tap 180 1448")
    sleep(1)
    os.system("adb shell input tap 400 1154")
    sleep(2)
    
    print("berhasil ke "+str(i)+" dari "+str(total_video))

    # #swipe menu
    # os.system("adb shell input swipe 370 1086 368 568")
    # sleep(3)

    # #click file
    # os.system("adb shell input tap 107 538")
    # sleep(3)

    # #click tahan file yg mau hapus
    # os.system("adb shell input swipe 143 358 143 358 1000")
    # sleep(1)

    # #delete file
    # os.system("adb shell input tap 654 1358")
    # sleep(1)
    # os.system("adb shell input tap 527 1302")
    # sleep(2)

    # #klik kembali ke home
    # os.system("adb shell input tap 180 1448")
    # sleep(1)
    # os.system("adb shell input tap 400 1154")
    # sleep(2)
    if i == total_video +1 :
        break
        exit("selesai")

