'''
跳转代码
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r"G:/自动化测试14/day01/练习的html/练习的html/跳转页面/pop.html")
driver.find_element_by_xpath("//*[@id='goo']").click()
time.sleep(3)

driver.quit()
'''
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r"G:/自动化测试14/day01/练习的html/练习的html/弹框的验证/dialogs.html")
driver.find_element_by_xpath("//*[@id='alert']").click()
time.sleep(2)
a = driver.switch_to.alert
a.accept()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='confirm']").click()
time.sleep(2)
a = driver.switch_to.alert
a.accept()#单击“确定”按钮
#a.dismiss()#单击“取消”按钮
time.sleep(2)

driver.quit()
