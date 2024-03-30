#把同文件夹下的coding.code文件上传至文叔叔，并打印下载网址，运行需要一定时间，视文件大小而定
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
options=Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
driver.get('https://www.wenshushu.cn/')
element=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/div[2]/div[1]/button')
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div/div/div[1]/div').click()
path=os.path.join(os.getcwd(),'coding.code')
driver.find_element(By.XPATH,'//*[@id="file_upload_input"]').send_keys(path)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/button').click()
element = WebDriverWait(driver,timeout=100).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[9]/div[2]/div/div/div/div[2]/div[1]/div[4]/div/span/span')))
print(element.text)
