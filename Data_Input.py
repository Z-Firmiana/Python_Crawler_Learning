import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd
from DataLoad import Excel_Load_to_Array



def test(address, url):
    Data_Array = Excel_Load_to_Array(address)
    driver = webdriver.Chrome() # chromedriver所在路径
    driver.get(url)
    # driver.find_element(By.ID, "kw").send_keys("cnblogs") # 输入cnblogs
    # driver.find_element(By.ID, "su").click() # 点击“百度一下”搜索
    time.sleep(15) # 等待30秒钟，让页面加载完成

    # driver.switch_to.frame("printCasLogout")
    # time.sleep(1)
    for index in range(len(Data_Array[:, 0])):
        driver.find_element(By.CSS_SELECTOR, f"#pageBox > div:nth-child(5) > div > table > tbody > tr:nth-child({index + 3}) > td:nth-child(2) > div > div.dplugin-box.required.dplugin-box-1 > div > span > span > div.el-popover__reference > input[type=text]").send_keys(Data_Array[index][0])
        driver.find_element(By.CSS_SELECTOR, f"#pageBox > div:nth-child(5) > div > table > tbody > tr:nth-child({index + 3}) > td:nth-child(3) > div > div.dplugin-box.required.dplugin-box-1 > div > span > span > div.el-popover__reference > input[type=text]").send_keys(Data_Array[index][1])
        driver.find_element(By.CSS_SELECTOR, f"#pageBox > div:nth-child(5) > div > table > tbody > tr:nth-child({index + 3}) > td:nth-child(4) > div > div.dplugin-box.required.dplugin-box-1 > div.dplugin-pc.dplugin-doneplugin.dplugin-radio > label:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, f"#pageBox > div:nth-child(5) > div > table > tbody > tr:nth-child({index + 3}) > td:nth-child(5) > div > div.dplugin-box.required.dplugin-box-1 > div > span > span > div.el-popover__reference > input[type=text]").send_keys(Data_Array[index][2])
        driver.find_element(By.CSS_SELECTOR, f"#pageBox > div:nth-child(5) > div > table > tbody > tr:nth-child({index + 3}) > td:nth-child(7) > span.rtps.plus > i").click()
        time.sleep(1)
    # time.sleep(1)
    # # 保存草稿
    # driver.find_element(By.CSS_SELECTOR, "#saveDraft").click()

    time.sleep(20)
    driver.quit() # 关闭浏览器

if __name__ == "__main__":
    test()
#pageBox > div:nth-child(5) > div > table > tbody > tr.tablerow > td:nth-child(2) > div > div.dplugin-box.required.dplugin-box-1 > div > span > span > div.el-popover__reference > input[type=text]
#pageBox > div:nth-child(5) > div > table > tbody > tr:nth-child(4) > td:nth-child(2) > div > div.dplugin-box.required.dplugin-box-1 > div > span > span > div.el-popover__reference > input[type=text]
#pageBox > div:nth-child(5) > div > table > tbody > tr:nth-child(5) > td:nth-child(2) > div > div.dplugin-box.required.dplugin-box-1 > div > span > span > div.el-popover__reference > input[type=text]
#pageBox > div:nth-child(5) > div > table > tbody > tr:nth-child(6) > td:nth-child(2) > div > div.dplugin-box.required.dplugin-box-1 > div > span > span > div.el-popover__reference > input[type=text]

#pageBox > div:nth-child(5) > div > table > tbody > tr:nth-child(4) > td:nth-child(5) > div > div.dplugin-box.required.dplugin-box-1 > div > span > span > div.el-popover__reference > input[type=text]

#pageBox > div:nth-child(5) > div > table > tbody > tr:nth-child(6) > td:nth-child(7) > span.rtps.plus > i
#pageBox > div:nth-child(5) > div > table > tbody > tr:nth-child(7) > td:nth-child(7) > span.rtps.plus > i

#pageBox > div:nth-child(5) > div > table > tbody > tr.tablerow > td:nth-child(2) > div > div.dplugin-box.required.dplugin-box-1 > div > span > span > div.el-popover__reference > input[type=text]
#pageBox > div:nth-child(5) > div > table > tbody > tr.tablerow > td:nth-child(7) > span.rtps.plus > i