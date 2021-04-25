from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://vermont.force.com/events/s/login/")
driver.implicitly_wait(2)
email = driver.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div/div[2]/c-okcp_okdoh-login-page/div/div/div[2]/div/div/div[2]/div/input')
email.send_keys(input("Enter email: "))
password = driver.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div/div[2]/c-okcp_okdoh-login-page/div/div/div[2]/div/div/div[3]/div/input')
password.send_keys(input("Enter password: "))

#Possibilities
#//*[@id="main-content"]/div/div[2]/div/div[2]/c-okcp_okdoh-login-page/div/div/div[2]/div/div/div[4]/lightning-button
#//*[@id="main-content"]/div/div[2]/div/div[2]/c-okcp_okdoh-login-page/div/div/div[2]/div/div/div[4]/lightning-button/button
#//*[@id="main-content"]/div/div[2]/div/div[2]/c-okcp_okdoh-login-page/div/div/div[2]/div/div/div[4]/lightning-button

#THIS DID NOT WORK
#login = driver.find_element_by_xpath('//button[@type = "button"]')
#driver.execute_script("arguments[0]", login)

#THIS ALSO WORKED
driver.find_element_by_xpath('//button[@type = "button"]').click()

"""
#THIS ALSO WORKED
login = driver.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div/div[2]/c-okcp_okdoh-login-page/div/div/div[2]/div/div/div[4]/lightning-button')
login.click()
"""

#THIS WORKED
#login = driver.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div/div[2]/c-okcp_okdoh-login-page/div/div/div[2]/div/div/div[4]/lightning-button/button')
#login.click()

while (1 ==1):
#vaccine_appt = driver.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div/div/c-okcp-registration-form/div/c-okcp-dashboard/div/section/div/lightning-button[1]/button')
    try:
        vaccine_appt = driver.find_elements_by_xpath('//*[@id="main-content"]/div/div[2]/div/div/c-okcp-registration-form/div/c-okcp-dashboard/div/section/div/lightning-button[*]')
        driver.execute_script("arguments[0].click()",vaccine_appt[0])
        break
    except:
        pass

#//*[@id="main-content"]/div/div[2]/div/div/c-okcp-registration-form/div/c-okcp-dashboard/c-okpc-patient-select-modal-to-schedule-appointment/section/div/div/div/lightning-combobox/div[1]/lightning-base-combobox/div/div[1]
#//*[@id="input-28"]
# while (1==1):
#     try:
#         dependent = driver.find_element_by_xpath("//*[@id='main-content']/div/div[2]/div/div/c-okcp-registration-form/div/c-okcp-dashboard/c-okpc-patient-select-modal-to-schedule-appointment/section/div/div/div/lightning-combobox/div[1]/lightning-base-combobox/div")
#         driver.execute_script("arguments[0].click()", dependent)
#         break
#     except:
#         pass

#dependent = driver.find_element_by_xpath('//*[@id="input-18"]')
#driver.execute_script("arguments[0].click()",dependent)
dependent = driver.find_element_by_xpath("//*[@id='main-content']/div/div[2]/div/div/c-okcp-registration-form/div/c-okcp-dashboard/c-okpc-patient-select-modal-to-schedule-appointment/section/div/div/div/lightning-combobox/div[1]/lightning-base-combobox/div")
dependent.click()
dependent.send_keys(Keys.DOWN)
dependent.send_keys(Keys.ENTER)

#//*[@id="modal-content-id-1-30"]/c-vtpc-site-map/div/lightning-layout/slot/c-vt_event_scheduler_filters/div[2]/div/lightning-button[1]/button
#//*[@id="modal-content-id-1-30"]/c-vtpc-site-map/div/lightning-layout/slot/c-vt_event_scheduler_filters/div[2]/div/lightning-button[1]
#//*[@id="modal-content-id-1-30"]/c-vtpc-site-map/div/lightning-layout/slot/c-vt_event_scheduler_filters/div[2]/div/lightning-button[1]

#didnt work
#//*[@id="main-content"]/div/div[2]/div/div/c-okcp-registration-form/div/c-okcp-dashboard/c-okpc-patient-select-modal-to-schedule-appointment/section/div/footer/button[2]
#next = driver.find_element_by_xpath('//*[@id="modal-content-id-1-30"]/c-vtpc-site-map/div/lightning-layout/slot/c-vt_event_scheduler_filters/div[2]/div/lightning-button[1]/button')
#driver.execute_script("arguments[0].click()",next)

#THIS WORKED
next = driver.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div/div/c-okcp-registration-form/div/c-okcp-dashboard/c-okpc-patient-select-modal-to-schedule-appointment/section/div/footer/button[2]')
driver.execute_script("arguments[0].click()",next)
#//*[@id="input-302"]
#//*[@id="modal-content-id-1-294"]/c-vtpc-site-map/div/lightning-layout/slot/c-vt_event_scheduler_filters/div[1]/div[1]/lightning-combobox/div[1]/lightning-base-combobox/div/div[1]

#THIS USED TO WORK
#location = driver.find_element_by_xpath('//*[@id="input-40"]')

#//*[@id="modal-content-id-1-32"]/c-vtpc-site-map/div/lightning-layout/slot/c-vt_event_scheduler_filters/div[1]/div[1]/lightning-combobox/div[1]/lightning-base-combobox/div
location = driver.find_element_by_xpath("//*[matches(@id='modal-content-id-1-[1-100])']/c-vtpc-site-map/div/lightning-layout/slot/c-vt_event_scheduler_filters/div[1]/div[1]/lightning-combobox/div[1]/lightning-base-combobox/div")
driver.execute_script("arguments[0].click()",location)

county_list = ["addison", "bennington", "caledonia","chittenden","essex","franklin","grand isle","lamoille","orange","orleans","rutland","washington","windham","windsor"]

for i in range(county_list.index((input("Enter county name: ")).lower())):
    location.send_keys(Keys.DOWN)
location.send_keys(Keys.ENTER)

time_button = driver.find_element_by_xpath('//*[@id="modal-content-id-1-32"]/c-vtpc-site-map/div/lightning-layout/slot/c-vt_event_scheduler_filters/div[2]/div/lightning-button[1]/button')
time_button = driver.execute_script("arguments[0].click()",time_button)

time_list = driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div/div[2]/div/div/c-okcp-registration-form/div/div/div/div/div[2]/c-okcp-preference-component-new/c-okpc-location-map/section/div/div/c-vtpc-site-map/div/div/div/lightning-layout/slot/lightning-layout-item[2]/slot/div/c-okpc-event-list-item[*]/div/lightning-layout/slot/lightning-layout-item[*]')
for element in time_list:
    print(element.text)