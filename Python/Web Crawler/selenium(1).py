
# coding: utf-8

# In[1]:

from selenium import webdriver

driver=webdriver.PhantomJS(executable_path=r"D:\phantomjs-2.1.1-windows\bin\phantomjs")
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_id("su").click()
driver.get_screenshot_as_file(r"d:\aaa.png")
#driver.quit()


# In[1]:

from selenium import webdriver

driver=webdriver.PhantomJS(executable_path=r"D:\phantomjs-2.1.1-windows\bin\phantomjs")
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
for i in range(100000000):
    pass
#currentUrl=driver.getCurrentUrl() 
#s=driver.get(currentUrl)
driver.get_screenshot_as_file(r"d:\aaa1.png")
driver.quit()





# In[ ]:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#driver=webdriver.PhantomJS()     #速度快
driver=webdriver.Firefox()
driver.get("http://translate.google.com/?hl=en")

# Input the Chinese words for translation
driver.find_element_by_id("source").send_keys("今天天气很晴朗,我们出门打篮球，\
                                              但是走到半路却下雨了")
#driver.find_element_by_id("source").send_keys("这是一个波动很大的股票")
driver.find_element_by_id("gt-submit").click()

# Translation Process involves redirection
# Apply handler to switch to the current working page
handle=driver.current_window_handle
driver.switch_to.window(handle)

#Wait until the translation process finish to get the result
signal= WebDriverWait(driver, 30, 0.5).until (
    EC.presence_of_element_located((By.CSS_SELECTOR,"span#result_box>span"))
)
elements = driver.find_elements_by_css_selector("span#result_box>span");
for element in elements:
    print(element.text)

#driver.quit()





