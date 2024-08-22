
from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



desired_caps  = {}
desired_caps ["platformName"] = "Android"
desired_caps ["appPackage"] = "com.shopee.id"
desired_caps ["appActivity"] = "com.shopee.app.ui.home.HomeActivity_ t76263"
desired_caps ["deviceName"] = "SM-G965F"
desired_caps ["udid"] = "192.168.43.1:5555"
desired_caps ["noReset"] = "true"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps )
driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView').click()
sleep(5)
driver.find_element(By.ID, 'com.shopee.id.dfpluginshopee7:id/iv_page_close').click()

# driver.find_element(By.ID, 'com.shopee.id:id/search_icon').click()
# # Find the element first
# search_box = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText')

# # Perform the action on the found element
# search_box.click()
# search_box.send_keys('fadkhera')
# driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.ImageView').click()
# driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[1]').click()
# driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="shop_page_follow_shop_voucher_popup_close_button"]/android.widget.ImageView').click()
# sleep(10)

# driver.find_element(By.XPATH, '//android.widget.TextView[@text="Live"]').click()